"""The twelve commercial questions, each answered with an evidence level computed in code."""
from __future__ import annotations

from ..context import Ctx
from ..evidence import demand_level
from ..llm import GenTask
from ..schema import STR, STRS, arr, obj

QUESTIONS: list[tuple[str, str]] = [
    ("problem", "What problem or desire exists?"),
    ("who", "Who specifically experiences it?"),
    ("frequency_intensity", "How frequently and intensely does it matter?"),
    ("alternatives", "What alternatives are currently available?"),
    ("current_spend", "What do buyers currently spend?"),
    ("why_choose", "Why would someone choose this new offering?"),
    ("switch_trigger", "What would make them switch?"),
    ("reach", "How can those buyers be reached?"),
    ("acquisition_cost", "How expensive is customer acquisition likely to be?"),
    ("delivery_cost", "What does production or delivery actually cost?"),
    ("working_capital", "How much working capital is required?"),
    ("failure_risks", "What risks could make the business fail?"),
]

ANSWERS_SCHEMA = obj(
    ["answers"],
    answers=arr(obj(["key", "answer", "claim_ids", "status"], key={"type": "string", "enum": [k for k, _ in QUESTIONS]},
                    answer=STR, claim_ids=STRS, status={"type": "string", "enum": ["evidenced", "assumption", "unknown"]}),
                min_items=1),
)


def _claim_lines(ctx: Ctx, limit: int = 60) -> list[str]:
    rows = ctx.db.query("claims", "project_id=? AND support='verified_quote'", (ctx.project_id,),
                        "evidence_level DESC, created_at")
    return [f"{r['id']} [{r['claim_type']}]: {r['text'][:220]}" for r in rows[:limit]]


def assess_demand(ctx: Ctx, concept: dict, econ_summary: str = "") -> list[dict]:
    db = ctx.db
    lvl, why = demand_level(db, ctx.project_id, concept["id"])
    claims_txt = _claim_lines(ctx)
    prompt = (
        f"CONCEPT: {concept['title']}\nPrinciple: {concept.get('principle')}\nBuyer: {(concept.get('detail') or {}).get('target_buyer')}\n"
        f"Business model: {concept.get('business_model')}\n\nDirect buyer evidence on file: {why} (level {lvl}).\n"
        + (f"\nECONOMICS SUMMARY:\n{econ_summary}\n" if econ_summary else "")
        + "\nVERIFIED CLAIMS:\n" + "\n".join(claims_txt)
        + "\n\nAnswer each of the twelve questions. Cite claim ids that support each answer. If no claim supports it, "
          "set status 'assumption' or 'unknown' and say what evidence is missing.\n"
        + "\n".join(f"- {k}: {q}" for k, q in QUESTIONS)
    )
    res = ctx.generate([GenTask(role="buyer_researcher", purpose=f"demand:{concept['id']}",
                                system="You are the Buyer Researcher working with the Commercial Analyst.",
                                prompt=prompt, schema=ANSWERS_SCHEMA, temperature=0.2, max_tokens=3000)])
    answers = {a["key"]: a for a in (res[0]["answers"] if res else [])}
    valid = {r["id"]: r for r in db.query("claims", "project_id=?", (ctx.project_id,))}
    rows = []
    with db.tx():
        db.execute("DELETE FROM demand_answers WHERE project_id=? AND concept_id=?", (ctx.project_id, concept["id"]))
        for key, q in QUESTIONS:
            a = answers.get(key)
            if a is None:
                text = "Not assessed: no model available." if res is None else "Not answered."
                cids: list[str] = []
            else:
                text = a["answer"]
                cids = [c for c in a.get("claim_ids", []) if c in valid]
            level = max([valid[c]["evidence_level"] or 0 for c in cids] or [0])
            if key in ("problem", "who", "frequency_intensity", "why_choose", "switch_trigger") and lvl >= 2:
                level = max(level, lvl)
            rows.append({"key": key, "question": q, "answer": text, "claim_ids": cids, "evidence_level": level,
                         "status": (a or {}).get("status", "unknown")})
            db.insert("demand_answers", {"project_id": ctx.project_id, "concept_id": concept["id"], "question_key": key,
                                         "answer": text, "evidence_level": level, "claim_ids": cids,
                                         "created_by": "buyer_researcher" if a else "system"})
    return rows
