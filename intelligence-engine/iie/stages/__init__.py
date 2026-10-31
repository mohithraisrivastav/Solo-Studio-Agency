"""Stage definitions for the intelligence cycle.

Question -> Research -> Discovery -> Invention -> Comparison -> Technical -> Commercial
-> Critique -> Validation -> Decision -> Learning
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from ..context import Ctx
from ..evidence import demand_level
from ..engineering import detect_hazards
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


def concept_state(ctx: Ctx, concept: dict) -> dict:
    db = ctx.db
    lvl, why = demand_level(db, ctx.project_id, concept["id"])
    plan_row = db.one("technical_plans", "concept_id=? ORDER BY created_at DESC", (concept["id"],))
    plan = (plan_row or {}).get("plan") or {}
    hazards = (plan_row or {}).get("hazards") if plan_row else detect_hazards(full_text(concept))
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
