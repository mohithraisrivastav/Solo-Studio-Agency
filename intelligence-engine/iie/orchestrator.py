"""Orchestrator: runs workflows stage by stage with persistent jobs, recovery, and revisits.

Job states: pending, running, done, incomplete (ran but failed its completion
check), failed, waiting_operator, waiting_approval, interrupted.
A process crash leaves jobs 'running'; recover() marks them 'interrupted' and the
next run resumes them from their checkpoints.
"""
from __future__ import annotations

import threading
import traceback
from pathlib import Path

import httpx

from .approvals import ApprovalRequired
from .config import Settings, load_settings
from .context import Ctx
from .db import DB, open_db
from .guard import SafeFS
from .llm import OperatorPending, Provider, get_provider
from .research.connectors import build_connectors
from .research.http import Fetcher
from .stages import STAGES, WORKFLOWS
from .tools import ToolRunner
from .util import now_iso

MAX_ATTEMPTS = 2
_locks: dict[str, threading.Lock] = {}


class Engine:
    def __init__(self, settings: Settings | None = None, provider: Provider | None = None,
                 transport: httpx.BaseTransport | None = None, offline: bool = False):
        self.settings = settings or load_settings()
        self.settings.ensure_dirs()
        self.db: DB = open_db(self.settings.db_path)
        self.fs = SafeFS(self.settings.home)
        self.fetcher = Fetcher(self.settings, transport=transport, offline=offline or not self.settings.research_enabled)
        self.connectors = build_connectors(self.fetcher, self.settings)
        self.tools = ToolRunner(self.db, self.fs, self.settings)
        self.provider = provider or get_provider(self.settings, self.db)

    # projects -------------------------------------------------------------
    def create_project(self, question: str, workflow: str = "full", mode: str = "fresh", title: str | None = None,
                       budget_inr: float | None = None, settings: dict | None = None) -> str:
        if workflow not in WORKFLOWS:
            raise ValueError(f"Unknown workflow {workflow}; choose from {list(WORKFLOWS)}")
        if mode not in ("fresh", "evidence"):
            raise ValueError("mode must be 'fresh' or 'evidence'")
        with self.db.tx():
            pid = self.db.insert("projects", {"title": title or question[:80], "question": question,
                                              "workflow": workflow, "mode": mode, "status": "new",
                                              "budget_inr": budget_inr, "settings": settings or {}})
            self.db.log(pid, None, "user", "project_created", f"{workflow} ({mode}): {question[:200]}")
        return pid

    def update_project_settings(self, pid: str, **changes) -> None:
        p = self.db.get("projects", pid)
        st = dict(p.get("settings") or {})
        st.update(changes)
        self.db.update("projects", pid, {"settings": st})

    # recovery -------------------------------------------------------------
    def recover(self) -> list[str]:
        rows = self.db.query("jobs", "status='running'")
        with self.db.tx():
            for j in rows:
                self.db.execute("UPDATE jobs SET status='interrupted', error=? WHERE id=?",
                                ("process stopped while running; will resume from checkpoint", j["id"]))
                self.db.execute("UPDATE projects SET status='interrupted' WHERE id=?", (j["project_id"],))
                self.db.log(j["project_id"], j["id"], "system", "job_interrupted", f"{j['stage']} was interrupted")
        return [j["id"] for j in rows]

    # running --------------------------------------------------------------
    def _job(self, pid: str, stage: str, cycle: int) -> dict | None:
        return self.db.one("jobs", "project_id=? AND stage=? AND cycle=? ORDER BY created_at DESC", (pid, stage, cycle))

    def run(self, pid: str, stop_after: str | None = None) -> dict:
        lock = _locks.setdefault(pid, threading.Lock())
        if not lock.acquire(blocking=False):
            return {"status": "already_running"}
        try:
            return self._run(pid, stop_after)
        finally:
            lock.release()

    def _run(self, pid: str, stop_after: str | None) -> dict:
        project = self.db.get("projects", pid)
        if project is None:
            raise KeyError(pid)
        stages = WORKFLOWS[project["workflow"]]
        st = project.get("settings") or {}
        cycle = int(st.get("cycle", 0))
        i = int(st.get("cycle_start", 0))
        self._set_project(pid, "running")
        while i < len(stages):
            key = stages[i]
            stage = STAGES[key]
            job = self._job(pid, key, cycle)
            if job and job["status"] == "superseded":
                job = None
            if job and job["status"] in ("done", "incomplete"):
                if stop_after == key:
                    break
                i += 1
                continue
            if job is None:
                with self.db.tx():
                    jid = self.db.insert("jobs", {"project_id": pid, "stage": key, "cycle": cycle, "status": "pending",
                                                  "attempt": 0})
                job = self.db.get("jobs", jid)
            attempt = (job["attempt"] or 0) + 1
            self.db.execute("UPDATE jobs SET status='running', attempt=?, started_at=?, heartbeat_at=?, error=NULL "
                            "WHERE id=?", (attempt, now_iso(), now_iso(), job["id"]))
            job = self.db.get("jobs", job["id"])
            project = self.db.get("projects", pid)
            ctx = Ctx(self.db, self.settings, self.provider, self.fetcher, self.connectors, self.fs, self.tools,
                      project, job)
            self.db.log(pid, job["id"], stage.roles[0], "stage_start", f"{stage.title} (cycle {cycle}, attempt {attempt})")
            try:
                out = stage.run(ctx)
                ok, reason = stage.check(ctx, out)
            except OperatorPending as e:
                self._finish(job["id"], "waiting_operator", error=str(e))
                self._set_project(pid, "waiting_operator")
                self.db.log(pid, job["id"], "system", "waiting_operator", str(e), detail={"tasks": e.task_ids})
                return {"status": "waiting_operator", "stage": key, "tasks": e.task_ids}
            except ApprovalRequired as e:
                self._finish(job["id"], "waiting_approval", error=str(e))
                self._set_project(pid, "waiting_approval")
                return {"status": "waiting_approval", "stage": key, "approval": e.approval_id}
            except Exception as e:  # noqa: BLE001
                tb = traceback.format_exc()
                self.db.log(pid, job["id"], "system", "stage_error", f"{key}: {type(e).__name__}: {e}",
                            detail={"trace": tb[-3000:]})
                if attempt < MAX_ATTEMPTS:
                    self.db.execute("UPDATE jobs SET status='pending', error=? WHERE id=?", (f"{type(e).__name__}: {e}", job["id"]))
                    continue
                self._finish(job["id"], "failed", error=f"{type(e).__name__}: {e}")
                self._set_project(pid, "failed")
                return {"status": "failed", "stage": key, "error": f"{type(e).__name__}: {e}"}
            status = "done" if ok else "incomplete"
            self._finish(job["id"], status, output={**out, "_check": reason})
            self.db.log(pid, job["id"], stage.roles[0], "stage_end", f"{stage.title}: {status} ({reason})")
            if key == "decision" and out.get("revisit"):
                target = out["revisit"]
                cycle += 1
                i = stages.index(target)
                new_st = dict((self.db.get("projects", pid) or {}).get("settings") or {})
                new_st.update({"cycle": cycle, "cycle_start": i})
                self.db.update("projects", pid, {"settings": new_st})
                self.db.log(pid, None, "decision_director", "revisit", f"returning to {target} (cycle {cycle})")
                continue
            if stop_after == key:
                break
            i += 1
        done = i >= len(stages)
        self._set_project(pid, "complete" if done else "paused")
        return {"status": "complete" if done else "paused", "cycle": cycle}

    def _finish(self, jid: str, status: str, output: dict | None = None, error: str | None = None) -> None:
        import json
        self.db.execute("UPDATE jobs SET status=?, output=?, error=?, finished_at=? WHERE id=?",
                        (status, json.dumps(output, default=str) if output is not None else None, error, now_iso(), jid))

    def _set_project(self, pid: str, status: str) -> None:
        self.db.execute("UPDATE projects SET status=?, updated_at=? WHERE id=?", (status, now_iso(), pid))

    def rerun_from(self, pid: str, stage: str, reason: str, actor: str = "user") -> list[str]:
        """Supersede a stage and every later stage in the current cycle so they run again.

        Earlier outputs stay in the store with status 'superseded'; nothing is deleted.
        """
        p = self.db.get("projects", pid)
        stages = WORKFLOWS[p["workflow"]]
        if stage not in stages:
            raise ValueError(f"{stage} is not in workflow {p['workflow']}")
        cycle = int((p.get("settings") or {}).get("cycle", 0))
        later = stages[stages.index(stage):]
        changed = []
        with self.db.tx():
            for k in later:
                for j in self.db.query("jobs", "project_id=? AND stage=? AND cycle=? AND status!='superseded'",
                                       (pid, k, cycle)):
                    self.db.execute("UPDATE jobs SET status='superseded', error=? WHERE id=?", (reason, j["id"]))
                    self.db.execute("UPDATE operator_tasks SET status='withdrawn' WHERE job_id=? AND status='pending'",
                                    (j["id"],))
                    changed.append(j["id"])
            self.db.log(pid, None, actor, "rerun_from", f"rerun from {stage}: {reason}", detail={"jobs": changed})
        self._set_project(pid, "paused")
        return changed

    def status(self, pid: str) -> dict:
        p = self.db.get("projects", pid)
        jobs = self.db.query("jobs", "project_id=?", (pid,), "created_at")
        pending_ops = self.db.query("operator_tasks", "project_id=? AND status='pending'", (pid,))
        pending_apr = self.db.query("approvals", "project_id=? AND status='pending'", (pid,))
        return {"project": p, "jobs": [{k: j[k] for k in ("id", "stage", "cycle", "status", "attempt", "error")} for j in jobs],
                "operator_tasks_pending": [o["id"] for o in pending_ops],
                "approvals_pending": [a["id"] for a in pending_apr]}

    def describe(self) -> dict:
        return {
            "home": str(self.settings.home),
            "db": str(self.settings.db_path),
            "instance": self.db.meta("instance_id"),
            "created": self.db.meta("created_at"),
            "provider": self.provider.describe(),
            "connectors": {n: c.configured()[1] for n, c in self.connectors.items()},
        }


def engine_for(home: Path | None = None, **kw) -> Engine:
    return Engine(load_settings(home), **kw)
