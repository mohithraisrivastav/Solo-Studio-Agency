"""Stage definitions for the intelligence cycle.

Question -> Research -> Discovery -> Invention -> Comparison -> Technical -> Commercial
-> Critique -> Validation -> Decision -> Learning
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from ..context import Ctx
from ..evidence import demand_level
from ..engineering import detect_hazards, hazard_text
from ..invention.diversity import full_text


@dataclass
class Stage:
    key: str
    title: str
    roles: list[str]
    inputs: str
    outputs: str
    tools: list[str]
    evidence: str
    completion: str
    failure: str
    run: Callable[[Ctx], dict]
    check: Callable[[Ctx, dict], tuple[bool, str]]


def active_concepts(ctx: Ctx) -> list[dict]:
    return ctx.db.query("concepts", "project_id=? AND status IN ('active','shortlisted')", (ctx.project_id,), "created_at")


def shortlisted(ctx: Ctx) -> list[dict]:
    rows = ctx.db.query("concepts", "project_id=? AND status='shortlisted'", (ctx.project_id,), "created_at")
    return rows or active_concepts(ctx)[:3]


def selected_opportunity(ctx: Ctx) -> dict | None:
    sel = (ctx.project.get("settings") or {}).get("opportunity_id")
    if sel:
        return ctx.db.get("opportunities", sel)
    row = ctx.db.one("opportunities", "project_id=? AND status='selected'", (ctx.project_id,))
    if row:
        return row
    rows = ctx.db.query("opportunities", "project_id=? AND status IN ('ranked','candidate')", (ctx.project_id,),
                        "created_at")
    return rows[0] if rows else None


def latest_econ(ctx: Ctx, concept_id: str, scenario: str = "base") -> dict | None:
    return ctx.db.one("economics", "concept_id=? AND scenario=? ORDER BY created_at DESC", (concept_id, scenario))


def relevant_claims(ctx: Ctx, concept: dict | None = None, opportunity: dict | None = None,
                    types: tuple[str, ...] | None = None, limit: int = 40) -> list[dict]:
    """Verified claims ranked by relevance: cited by the concept, cited by its opportunity, same industry, rest.

    Duplicate texts are dropped so repeated extractor claims do not crowd the list.
    """
    db = ctx.db
    if opportunity is None and concept and concept.get("opportunity_id"):
        opportunity = db.get("opportunities", concept["opportunity_id"])
    rows = db.query("claims", "project_id=? AND support='verified_quote'", (ctx.project_id,), "created_at")
    if types:
        rows = [r for r in rows if r["claim_type"] in types]
    first = set(((concept or {}).get("detail") or {}).get("evidence_claim_ids") or [])
    second = set((opportunity or {}).get("claim_ids") or [])
    industry = (opportunity or {}).get("industry")
    ind_claims: set[str] = set()
    if industry:
        src_ind = {s["id"]: (s.get("meta") or {}).get("industry") for s in
                   db.query("sources", "project_id=?", (ctx.project_id,))}
        for cid, sid in db.conn.execute("SELECT claim_id, source_id FROM claim_sources WHERE verified=1").fetchall():
            if src_ind.get(sid) == industry:
                ind_claims.add(cid)

    def rank(r: dict) -> int:
        return 0 if r["id"] in first else 1 if r["id"] in second else 2 if r["id"] in ind_claims else 3

    out, seen = [], set()
    for r in sorted(rows, key=rank):
        key = r["text"].strip().lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out[:limit]


def concept_state(ctx: Ctx, concept: dict) -> dict:
    db = ctx.db
    lvl, why = demand_level(db, ctx.project_id, concept["id"])
    plan_row = db.one("technical_plans", "concept_id=? ORDER BY created_at DESC", (concept["id"],))
    plan = (plan_row or {}).get("plan") or {}
    hazards = (plan_row or {}).get("hazards") if plan_row else detect_hazards(hazard_text(concept))
    return {
        "demand_level": lvl,
        "demand_why": why,
        "originality": db.one("originality_checks", "concept_id=? ORDER BY created_at DESC", (concept["id"],)),
        "econ": latest_econ(ctx, concept["id"], "base"),
        "econ_conservative": latest_econ(ctx, concept["id"], "conservative"),
        "econ_optimistic": latest_econ(ctx, concept["id"], "optimistic"),
        "hazards": hazards or [],
        "plan": plan,
        "budget": ctx.project.get("budget_inr"),
    }


from . import evaluate, explore  # noqa: E402

STAGES: dict[str, Stage] = {s.key: s for s in explore.STAGES + evaluate.STAGES}

WORKFLOWS: dict[str, list[str]] = {
    "full": ["question", "research", "discovery", "invention", "comparison", "technical", "commercial",
             "critique", "validation", "decision", "learning"],
    "discovery": ["question", "research", "discovery", "decision", "learning"],
    "invention": ["question", "research", "invention", "comparison", "critique", "decision", "learning"],
    "evaluate": ["question", "research", "comparison", "technical", "commercial", "critique", "validation",
                 "decision", "learning"],
    "commercial": ["question", "commercial", "critique", "validation", "decision", "learning"],
}
