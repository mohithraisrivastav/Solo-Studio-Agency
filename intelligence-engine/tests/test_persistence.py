"""Test 8: Interrupt active research with a hard kill, restart, and verify nothing completed is lost."""
import os
import signal
import subprocess
import sys
import textwrap
import time
from pathlib import Path

from iie import approvals
from iie.approvals import ApprovalRequired
from iie.config import Settings
from iie.orchestrator import Engine

ROOT = Path(__file__).resolve().parents[1]

CHILD = textwrap.dedent('''
    import sys, time, httpx
    sys.path.insert(0, {root!r}); sys.path.insert(0, {tests!r})
    from conftest import _handler, ScriptedProvider
    from iie.config import Settings
    from iie.orchestrator import Engine
    def slow(req):
        time.sleep(0.4)
        return _handler(req)
    s = Settings(home=__import__("pathlib").Path({home!r}))
    s.connectors = ["wikipedia", "openalex", "stackexchange", "hackernews"]
    s.saturation_window = 99
    e = Engine(s, provider=ScriptedProvider(), transport=httpx.MockTransport(slow))
    print("START", flush=True)
    e.run({pid!r})
''')


def _settings(home: Path) -> Settings:
    s = Settings(home=home)
    s.connectors = ["wikipedia", "openalex", "stackexchange", "hackernews"]
    s.saturation_window = 99
    s.ensure_dirs()
    return s


def test_kill_during_research_then_resume(tmp_path, transport, scripted):
    home = tmp_path / "home"
    s = _settings(home)
    e = Engine(s, provider=scripted, transport=transport)
    # A finished project with a decision and an approval, which must survive the crash.
    done_pid = e.create_project("earlier project", "full", budget_inr=100000,
                                settings={"industries": ["bicycles and urban mobility cycling"]})
    assert e.run(done_pid)["status"] == "complete"
    try:
        e.tools.call("webhook_post", {"url": "https://hooks.example.com/a", "payload": {}}, actor="experiment_designer")
    except ApprovalRequired as ex:
        approvals.decide(e.db, ex.approval_id, True, "user")
    decisions_before = e.db.scalar("SELECT COUNT(*) FROM decisions")
    pid = e.create_project("interrupted project", "full", budget_inr=100000,
                           settings={"industries": ["bicycles and urban mobility cycling", "home repair and maintenance home"]})
    e.db.close()

    code = CHILD.format(root=str(ROOT), tests=str(ROOT / "tests"), home=str(home), pid=pid)
    proc = subprocess.Popen([sys.executable, "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    assert proc.stdout.readline().strip() == "START"
    # wait until research has stored some sources, then kill without cleanup
    e2 = Engine(_settings(home), provider=scripted, transport=transport)
    deadline = time.time() + 30
    while time.time() < deadline:
        n = e2.db.scalar("SELECT COUNT(*) FROM sources WHERE project_id=?", (pid,)) or 0
        if n >= 2:
            break
        time.sleep(0.1)
    os.kill(proc.pid, signal.SIGKILL)
    proc.wait()
    assert n >= 2, proc.stderr.read()

    # restart
    e3 = Engine(_settings(home), provider=scripted, transport=transport)
    sources_after_kill = e3.db.scalar("SELECT COUNT(*) FROM sources WHERE project_id=?", (pid,))
    job = e3.db.one("jobs", "project_id=? AND stage='research'", (pid,))
    assert job["status"] == "running"  # stale state left by the crash
    recovered = e3.recover()
    assert job["id"] in recovered
    assert e3.db.get("jobs", job["id"])["status"] == "interrupted"
    done_queries = len((e3.db.get("jobs", job["id"])["checkpoint"] or {}).get("research", {}).get("done", []))
    assert done_queries >= 1
    # earlier work preserved
    assert e3.db.scalar("SELECT COUNT(*) FROM decisions") == decisions_before
    assert e3.db.scalar("SELECT COUNT(*) FROM approvals WHERE status='approved'") == 1
    # resume finishes and keeps the sources gathered before the crash
    assert e3.run(pid)["status"] == "complete"
    assert e3.db.scalar("SELECT COUNT(*) FROM sources WHERE project_id=?", (pid,)) >= sources_after_kill
    assert e3.db.get("jobs", job["id"])["status"] in ("done", "incomplete")
    assert e3.db.scalar("SELECT COUNT(*) FROM events WHERE kind='job_interrupted'") >= 1


def test_waiting_for_operator_survives_restart(tmp_path):
    from iie.llm import OperatorProvider, answer_operator_task
    s = _settings(tmp_path / "h")
    e = Engine(s, offline=True)
    e.provider = OperatorProvider(e.db)
    pid = e.create_project("Is a sealed chain case worth making?", "invention")
    r = e.run(pid)
    assert r["status"] == "waiting_operator"
    task_id = r["tasks"][0]
    e.db.close()
    e2 = Engine(_settings(tmp_path / "h"), offline=True)
    e2.provider = OperatorProvider(e2.db)
    assert e2.db.get("operator_tasks", task_id)["status"] == "pending"
    answer_operator_task(e2.db, task_id, {"framing": "f", "queries": [{"text": "chain case", "purpose": "competitor"}]}, "test-operator")
    r2 = e2.run(pid)
    assert r2["status"] in ("waiting_operator", "complete")
    assert e2.db.get("jobs", e2.db.one("jobs", "project_id=? AND stage='question'", (pid,))["id"])["status"] == "done"
