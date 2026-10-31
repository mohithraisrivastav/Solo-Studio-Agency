"""Memory built only from this engine's own work.

* Fresh Discovery Mode: idea generation receives no stored concept history.
  Duplication against history is checked afterwards.
* Evidence Mode: feasibility work can use stored sources, test results, and
  outcomes from earlier projects, ranked by relevance and capped per project so
  one frequent idea cannot dominate.
Stored records are information, not model training.
"""
from __future__ import annotations

from .db import DB
from .text import TfIdf
from .invention.diversity import full_text


def evidence_context(db: DB, query: str, exclude_project: str | None, limit: int = 10) -> list[str]:
    rows = db.query("learnings", "project_id != ? AND kind IN ('outcome','failed_hypothesis','lesson')",
                    (exclude_project or "",), "created_at DESC")
    if not rows:
        return []
    tf = TfIdf([query] + [r["text"] for r in rows])
    scored = sorted(((tf.sim(0, i + 1), r) for i, r in enumerate(rows)), key=lambda x: -x[0])
    out, per_project = [], {}
    for s, r in scored:
        if s <= 0.05:
            break
        n = per_project.get(r["project_id"], 0)
        if n >= 2:
            continue
        per_project[r["project_id"]] = n + 1
        out.append(f"[{r['kind']} from {r['project_id']}] {r['text'][:300]}")
        if len(out) >= limit:
            break
    return out


def history_duplicates(db: DB, concept: dict, threshold: float = 0.45) -> list[dict]:
    others = db.query("concepts", "project_id != ?", (concept["project_id"],))
    if not others:
        return []
    tf = TfIdf([full_text(concept)] + [full_text(o) for o in others])
    hits = []
    for i, o in enumerate(others):
        s = tf.sim(0, i + 1)
        if s >= threshold:
            hits.append({"concept_id": o["id"], "project_id": o["project_id"], "title": o["title"], "similarity": round(s, 3)})
    return sorted(hits, key=lambda h: -h["similarity"])


def progress_metrics(db: DB) -> dict:
    """Observable outcomes only."""
    q = lambda sql: db.scalar(sql) or 0  # noqa: E731
    return {
        "projects": q("SELECT COUNT(*) FROM projects"),
        "sources": q("SELECT COUNT(*) FROM sources"),
        "verified_claims": q("SELECT COUNT(*) FROM claims WHERE support='verified_quote'"),
        "unverified_model_quotes": q("SELECT COUNT(*) FROM claims WHERE support='source_unverified'"),
        "concepts": q("SELECT COUNT(*) FROM concepts"),
        "concepts_rejected": q("SELECT COUNT(*) FROM decisions WHERE verdict='reject'"),
        "experiments_planned": q("SELECT COUNT(*) FROM experiments"),
        "experiments_passed": q("SELECT COUNT(*) FROM experiments WHERE status='passed'"),
        "experiments_failed": q("SELECT COUNT(*) FROM experiments WHERE status='failed'"),
        "direct_evidence_records": q("SELECT COUNT(*) FROM direct_evidence"),
        "highest_demand_level": q("SELECT MAX(level) FROM direct_evidence"),
        "paid_orders": q("SELECT COUNT(*) FROM direct_evidence WHERE kind IN ('paid_order','deposit','repeat_order')"),
    }
