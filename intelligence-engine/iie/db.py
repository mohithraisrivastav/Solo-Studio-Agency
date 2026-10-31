"""Persistent store (SQLite, WAL). Every versioned record keeps its history."""
from __future__ import annotations

import sqlite3
import threading
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

from .util import dumps, loads, new_id, now_iso

SCHEMA_VERSION = 1

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);

CREATE TABLE IF NOT EXISTS projects (
  id TEXT PRIMARY KEY, title TEXT, question TEXT, workflow TEXT, mode TEXT, status TEXT,
  budget_inr REAL, settings TEXT, created_at TEXT, updated_at TEXT, version INTEGER DEFAULT 1);

CREATE TABLE IF NOT EXISTS jobs (
  id TEXT PRIMARY KEY, project_id TEXT REFERENCES projects(id), stage TEXT, cycle INTEGER DEFAULT 0,
  status TEXT, attempt INTEGER DEFAULT 0, input TEXT, output TEXT, checkpoint TEXT, error TEXT,
  created_at TEXT, started_at TEXT, finished_at TEXT, heartbeat_at TEXT);

CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY AUTOINCREMENT, project_id TEXT, job_id TEXT, ts TEXT, actor TEXT,
  kind TEXT, tool TEXT, summary TEXT, detail TEXT);

CREATE TABLE IF NOT EXISTS sources (
  id TEXT PRIMARY KEY, project_id TEXT, url TEXT, title TEXT, publisher TEXT, source_type TEXT,
  connector TEXT, query TEXT, retrieved_at TEXT, published_at TEXT, content TEXT, content_hash TEXT,
  retrieval_method TEXT, meta TEXT, created_at TEXT);
CREATE INDEX IF NOT EXISTS ix_sources_project ON sources(project_id);

CREATE TABLE IF NOT EXISTS research_gaps (
  id TEXT PRIMARY KEY, project_id TEXT, job_id TEXT, connector TEXT, query TEXT, reason TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS claims (
  id TEXT PRIMARY KEY, project_id TEXT, subject_type TEXT, subject_id TEXT, claim_type TEXT, text TEXT,
  metric TEXT, value REAL, unit TEXT, currency TEXT, support TEXT, evidence_level INTEGER,
  origin TEXT, created_by TEXT, created_at TEXT, updated_at TEXT, version INTEGER DEFAULT 1);
CREATE INDEX IF NOT EXISTS ix_claims_project ON claims(project_id);

CREATE TABLE IF NOT EXISTS claim_sources (
  claim_id TEXT, source_id TEXT, quote TEXT, stance TEXT, verified INTEGER,
  PRIMARY KEY (claim_id, source_id, stance));

CREATE TABLE IF NOT EXISTS contradictions (
  id TEXT PRIMARY KEY, project_id TEXT, metric TEXT, claim_a TEXT, claim_b TEXT, ratio REAL,
  note TEXT, status TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS direct_evidence (
  id TEXT PRIMARY KEY, project_id TEXT, concept_id TEXT, kind TEXT, level INTEGER, counterparty TEXT,
  contact_ref TEXT, occurred_on TEXT, amount REAL, currency TEXT, notes TEXT, recorded_by TEXT,
  recorded_at TEXT);

CREATE TABLE IF NOT EXISTS opportunities (
  id TEXT PRIMARY KEY, project_id TEXT, industry TEXT, title TEXT, problem TEXT, who TEXT,
  detail TEXT, claim_ids TEXT, status TEXT, created_by TEXT, created_at TEXT, updated_at TEXT,
  version INTEGER DEFAULT 1);

CREATE TABLE IF NOT EXISTS concepts (
  id TEXT PRIMARY KEY, project_id TEXT, opportunity_id TEXT, family_id TEXT, title TEXT, method TEXT,
  principle TEXT, user_value TEXT, business_model TEXT, axes TEXT, detail TEXT, status TEXT,
  merged_into TEXT, generation_mode TEXT, created_by TEXT, created_at TEXT, updated_at TEXT,
  version INTEGER DEFAULT 1);

CREATE TABLE IF NOT EXISTS concept_overlaps (
  id TEXT PRIMARY KEY, project_id TEXT, a_id TEXT, b_id TEXT, text_similarity REAL, shared_axes TEXT,
  verdict TEXT, reason TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS prior_art (
  id TEXT PRIMARY KEY, project_id TEXT, concept_id TEXT, source_id TEXT, similarity REAL, verdict TEXT,
  note TEXT, created_by TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS originality_checks (
  id TEXT PRIMARY KEY, project_id TEXT, concept_id TEXT, searched TEXT, unavailable TEXT,
  verdict TEXT, note TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS economics (
  id TEXT PRIMARY KEY, project_id TEXT, concept_id TEXT, scenario TEXT, inputs TEXT, outputs TEXT,
  findings TEXT, created_by TEXT, created_at TEXT, updated_at TEXT, version INTEGER DEFAULT 1);

CREATE TABLE IF NOT EXISTS demand_answers (
  id TEXT PRIMARY KEY, project_id TEXT, concept_id TEXT, question_key TEXT, answer TEXT,
  evidence_level INTEGER, claim_ids TEXT, created_by TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS technical_plans (
  id TEXT PRIMARY KEY, project_id TEXT, concept_id TEXT, plan TEXT, hazards TEXT, maturity TEXT,
  created_by TEXT, created_at TEXT, updated_at TEXT, version INTEGER DEFAULT 1);

CREATE TABLE IF NOT EXISTS artifacts (
  id TEXT PRIMARY KEY, project_id TEXT, concept_id TEXT, kind TEXT, path TEXT, description TEXT,
  validated INTEGER DEFAULT 0, created_at TEXT);

CREATE TABLE IF NOT EXISTS critiques (
  id TEXT PRIMARY KEY, project_id TEXT, target_type TEXT, target_id TEXT, actor TEXT, category TEXT,
  objection TEXT, severity TEXT, basis TEXT, source_ids TEXT, claim_ids TEXT, rule_id TEXT,
  status TEXT, resolution TEXT, created_at TEXT, updated_at TEXT, version INTEGER DEFAULT 1);

CREATE TABLE IF NOT EXISTS disagreements (
  id TEXT PRIMARY KEY, project_id TEXT, topic TEXT, role_a TEXT, position_a TEXT, evidence_a TEXT,
  role_b TEXT, position_b TEXT, evidence_b TEXT, status TEXT, resolution TEXT, created_at TEXT,
  updated_at TEXT, version INTEGER DEFAULT 1);

CREATE TABLE IF NOT EXISTS experiments (
  id TEXT PRIMARY KEY, project_id TEXT, concept_id TEXT, assumption TEXT, hypothesis TEXT, method TEXT,
  cost_inr REAL, duration_days REAL, success_criteria TEXT, failure_criteria TEXT,
  evidence_level_target INTEGER, gated_actions TEXT, status TEXT, result TEXT, created_by TEXT,
  created_at TEXT, updated_at TEXT, version INTEGER DEFAULT 1);

CREATE TABLE IF NOT EXISTS decisions (
  id TEXT PRIMARY KEY, project_id TEXT, concept_id TEXT, verdict TEXT, rationale TEXT, gates TEXT,
  unresolved TEXT, next_actions TEXT, decided_by TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS approvals (
  id TEXT PRIMARY KEY, project_id TEXT, kind TEXT, payload TEXT, payload_hash TEXT, status TEXT,
  requested_by TEXT, reason TEXT, created_at TEXT, decided_at TEXT, decided_by TEXT,
  consumed INTEGER DEFAULT 0);

CREATE TABLE IF NOT EXISTS operator_tasks (
  id TEXT PRIMARY KEY, project_id TEXT, job_id TEXT, role TEXT, purpose TEXT, request_key TEXT,
  prompt TEXT, schema TEXT, status TEXT, answer TEXT, answered_by TEXT, created_at TEXT,
  answered_at TEXT);
CREATE INDEX IF NOT EXISTS ix_optask_key ON operator_tasks(request_key);

CREATE TABLE IF NOT EXISTS learnings (
  id TEXT PRIMARY KEY, project_id TEXT, kind TEXT, ref_type TEXT, ref_id TEXT, text TEXT, data TEXT,
  created_by TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS benchmarks (
  id TEXT PRIMARY KEY, provider TEXT, model TEXT, tokens_per_sec REAL, latency_s REAL, json_valid INTEGER,
  correct INTEGER, hardware TEXT, error TEXT, ran_at TEXT);

CREATE TABLE IF NOT EXISTS record_versions (
  id INTEGER PRIMARY KEY AUTOINCREMENT, table_name TEXT, record_id TEXT, version INTEGER,
  data TEXT, changed_at TEXT, changed_by TEXT);
"""

PREFIX = {
    "projects": "prj", "jobs": "job", "sources": "src", "research_gaps": "gap", "claims": "clm",
    "contradictions": "con", "direct_evidence": "dev", "opportunities": "opp", "concepts": "cpt",
    "concept_overlaps": "ovl", "prior_art": "pa", "originality_checks": "orc", "economics": "eco",
    "demand_answers": "dmd", "technical_plans": "tec", "artifacts": "art", "critiques": "crt",
    "disagreements": "dis", "experiments": "exp", "decisions": "dec", "approvals": "apr",
    "operator_tasks": "opt", "learnings": "lrn", "benchmarks": "bm",
}

JSON_COLS = {
    "projects": {"settings"},
    "jobs": {"input", "output", "checkpoint"},
    "events": {"detail"},
    "sources": {"meta"},
    "opportunities": {"detail", "claim_ids"},
    "concepts": {"axes", "detail"},
    "concept_overlaps": {"shared_axes"},
    "originality_checks": {"searched", "unavailable"},
    "economics": {"inputs", "outputs", "findings"},
    "demand_answers": {"claim_ids"},
    "technical_plans": {"plan", "hazards"},
    "critiques": {"source_ids", "claim_ids"},
    "disagreements": {"evidence_a", "evidence_b"},
    "experiments": {"gated_actions", "result"},
    "decisions": {"gates", "unresolved", "next_actions"},
    "approvals": {"payload"},
    "operator_tasks": {"prompt", "schema", "answer"},
    "learnings": {"data"},
    "benchmarks": {"hardware"},
    "record_versions": {"data"},
}

VERSIONED = {
    "projects", "claims", "opportunities", "concepts", "economics", "technical_plans",
    "critiques", "disagreements", "experiments",
}


class DB:
    def __init__(self, path: Path | str):
        self.path = str(path)
        self._local = threading.local()
        self._cols: dict[str, set[str]] = {}

    # connection per thread
    @property
    def conn(self) -> sqlite3.Connection:
        c = getattr(self._local, "conn", None)
        if c is None:
            c = sqlite3.connect(self.path, timeout=30, isolation_level=None, check_same_thread=False)
            c.row_factory = sqlite3.Row
            c.execute("PRAGMA journal_mode=WAL")
            c.execute("PRAGMA foreign_keys=ON")
            c.execute("PRAGMA busy_timeout=30000")
            self._local.conn = c
            self._local.depth = 0
        return c

    def close(self) -> None:
        c = getattr(self._local, "conn", None)
        if c is not None:
            c.close()
            self._local.conn = None

    def init(self) -> None:
        self.conn.executescript(SCHEMA)
        if self.meta("schema_version") is None:
            self.set_meta("schema_version", str(SCHEMA_VERSION))
            self.set_meta("created_at", now_iso())
            self.set_meta("instance_id", new_id("iie"))
            self.set_meta("origin", "fresh database created by this engine; no imported records")

    def meta(self, key: str) -> str | None:
        row = self.conn.execute("SELECT value FROM meta WHERE key=?", (key,)).fetchone()
        return row["value"] if row else None

    def set_meta(self, key: str, value: str) -> None:
        self.conn.execute("INSERT OR REPLACE INTO meta(key, value) VALUES (?, ?)", (key, value))

    @contextmanager
    def tx(self) -> Iterator[sqlite3.Connection]:
        c = self.conn
        depth = getattr(self._local, "depth", 0)
        if depth == 0:
            c.execute("BEGIN IMMEDIATE")
        self._local.depth = depth + 1
        try:
            yield c
        except BaseException:
            self._local.depth = depth
            if depth == 0:
                c.execute("ROLLBACK")
            raise
        else:
            self._local.depth = depth
            if depth == 0:
                c.execute("COMMIT")

    def columns(self, table: str) -> set[str]:
        if table not in self._cols:
            rows = self.conn.execute(f"PRAGMA table_info({table})").fetchall()
            if not rows:
                raise KeyError(f"Unknown table {table}")
            self._cols[table] = {r["name"] for r in rows}
        return self._cols[table]

    def _encode(self, table: str, data: dict[str, Any]) -> dict[str, Any]:
        cols = self.columns(table)
        unknown = set(data) - cols
        if unknown:
            raise KeyError(f"Unknown columns for {table}: {sorted(unknown)}")
        jc = JSON_COLS.get(table, set())
        out = {}
        for k, v in data.items():
            if k in jc and v is not None and not isinstance(v, str):
                v = dumps(v)
            elif isinstance(v, bool):
                v = int(v)
            out[k] = v
        return out

    def _decode(self, table: str, row: sqlite3.Row | None) -> dict[str, Any] | None:
        if row is None:
            return None
        d = dict(row)
        for k in JSON_COLS.get(table, set()):
            if k in d and isinstance(d[k], str):
                d[k] = loads(d[k], d[k])
        return d

    def insert(self, table: str, data: dict[str, Any]) -> str:
        data = dict(data)
        cols = self.columns(table)
        if "id" in cols and not data.get("id") and table in PREFIX:
            data["id"] = new_id(PREFIX[table])
        ts = now_iso()
        if "created_at" in cols and not data.get("created_at"):
            data["created_at"] = ts
        if "updated_at" in cols and not data.get("updated_at"):
            data["updated_at"] = ts
        enc = self._encode(table, data)
        keys = ",".join(enc)
        qs = ",".join("?" for _ in enc)
        self.conn.execute(f"INSERT INTO {table} ({keys}) VALUES ({qs})", tuple(enc.values()))
        return data.get("id", "")

    def update(self, table: str, rid: str, data: dict[str, Any], actor: str = "system") -> None:
        cols = self.columns(table)
        with self.tx():
            if table in VERSIONED:
                old = self.conn.execute(f"SELECT * FROM {table} WHERE id=?", (rid,)).fetchone()
                if old is not None:
                    od = dict(old)
                    self.conn.execute(
                        "INSERT INTO record_versions(table_name, record_id, version, data, changed_at, changed_by)"
                        " VALUES (?,?,?,?,?,?)",
                        (table, rid, od.get("version") or 1, dumps(od), now_iso(), actor),
                    )
                    data = dict(data)
                    data["version"] = (od.get("version") or 1) + 1
            if "updated_at" in cols:
                data = dict(data)
                data["updated_at"] = now_iso()
            enc = self._encode(table, data)
            sets = ",".join(f"{k}=?" for k in enc)
            self.conn.execute(f"UPDATE {table} SET {sets} WHERE id=?", (*enc.values(), rid))

    def get(self, table: str, rid: str) -> dict[str, Any] | None:
        return self._decode(table, self.conn.execute(f"SELECT * FROM {table} WHERE id=?", (rid,)).fetchone())

    def query(self, table: str, where: str = "1=1", params: tuple = (), order: str = "") -> list[dict[str, Any]]:
        sql = f"SELECT * FROM {table} WHERE {where}" + (f" ORDER BY {order}" if order else "")
        return [self._decode(table, r) for r in self.conn.execute(sql, params).fetchall()]  # type: ignore[misc]

    def one(self, table: str, where: str, params: tuple = ()) -> dict[str, Any] | None:
        rows = self.query(table, where + " LIMIT 1", params)
        return rows[0] if rows else None

    def scalar(self, sql: str, params: tuple = ()) -> Any:
        row = self.conn.execute(sql, params).fetchone()
        return row[0] if row else None

    def execute(self, sql: str, params: tuple = ()) -> None:
        self.conn.execute(sql, params)

    def history(self, table: str, rid: str) -> list[dict[str, Any]]:
        return self.query("record_versions", "table_name=? AND record_id=?", (table, rid), "version")

    def log(self, project_id: str | None, job_id: str | None, actor: str, kind: str, summary: str,
            tool: str | None = None, detail: Any = None) -> None:
        self.conn.execute(
            "INSERT INTO events(project_id, job_id, ts, actor, kind, tool, summary, detail) VALUES (?,?,?,?,?,?,?,?)",
            (project_id, job_id, now_iso(), actor, kind, tool, summary, dumps(detail) if detail is not None else None),
        )


def open_db(path: Path | str) -> DB:
    db = DB(path)
    db.init()
    return db
