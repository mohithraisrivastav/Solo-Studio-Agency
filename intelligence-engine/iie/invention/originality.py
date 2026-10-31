"""Originality investigation: search for existing products, patents, and papers before any novelty claim.

Verdicts (never "novel"):
  not_checked                         no source could be searched
  close_match_found                   a source closely matches the concept (similarity >= 0.30)
  related_work_found                  related sources exist (>= 0.18)
  no_close_match_in_searched_sources  nothing close in what was searched; this is not proof of novelty
"""
from __future__ import annotations

from ..context import Ctx, source_block
from ..evidence import QuoteRef, add_claim
from ..llm import GenTask
from ..schema import BOOL, STR, arr, obj
from ..text import TfIdf
from .diversity import full_text

CLOSE_T = 0.30
RELATED_T = 0.18

JUDGE_SCHEMA = obj(
    ["closest_source_id", "overlap", "meaningful_difference", "difference"],
    closest_source_id=STR, overlap=STR, meaningful_difference=BOOL, difference=STR, quote=STR,
)


def queries_for(concept: dict) -> list[tuple[str, str]]:
    d = concept.get("detail") or {}
    principle = concept.get("principle") or ""
    words = " ".join(principle.split()[:12])
    return [
        (f"{concept['title']}", "competitor"),
        (words, "prior_art"),
        (f"{d.get('target_buyer', '')} {concept['title']}".strip(), "competitor"),
    ]


def assess(ctx: Ctx, concept: dict, candidate_sources: list[dict], searched: list[str],
           unavailable: dict) -> dict:
    db = ctx.db
    if not candidate_sources:
        verdict = "not_checked" if not searched else "no_close_match_in_searched_sources"
        note = ("No source could be searched; originality is unknown." if not searched else
                "Searched sources returned nothing relevant. This is not proof of novelty.")
        with db.tx():
            db.insert("originality_checks", {"project_id": ctx.project_id, "concept_id": concept["id"],
                                             "searched": searched, "unavailable": unavailable,
                                             "verdict": verdict, "note": note})
        return {"verdict": verdict, "max_similarity": 0.0, "matches": []}

    ctext = full_text(concept)
    docs = [ctext] + [f"{s.get('title')} {s.get('content') or ''}"[:4000] for s in candidate_sources]
    tf = TfIdf(docs)
    sims = sorted(((round(tf.sim(0, i + 1), 3), s) for i, s in enumerate(candidate_sources)),
                  key=lambda x: -x[0])
    top = sims[:5]
    max_sim = top[0][0] if top else 0.0
    if max_sim >= CLOSE_T:
        verdict = "close_match_found"
    elif max_sim >= RELATED_T:
        verdict = "related_work_found"
    else:
        verdict = "no_close_match_in_searched_sources"
    with db.tx():
        for sim, s in top:
            db.insert("prior_art", {"project_id": ctx.project_id, "concept_id": concept["id"], "source_id": s["id"],
                                    "similarity": sim, "verdict": "close" if sim >= CLOSE_T else
                                    ("related" if sim >= RELATED_T else "weak"),
                                    "note": "text similarity of concept to source", "created_by": "originality_investigator"})

    judged = None
    relevant = [s for sim, s in top if sim >= RELATED_T][:3]
    if relevant:
        prompt = ("CONCEPT:\n" + ctext + "\n\nEXISTING WORK FOUND:\n" + "\n\n".join(source_block(s, 1500) for s in relevant)
                  + "\n\nWhich source is closest? Describe the overlap. Is the concept's difference meaningful to a "
                    "buyer (function, cost, experience), or only cosmetic? Give one exact quote from the closest source.")
        res = ctx.generate([GenTask(role="originality_investigator", purpose=f"originality:{concept['id']}",
                                    system="You are the Originality Investigator. You look for reasons the concept "
                                           "already exists.", prompt=prompt, schema=JUDGE_SCHEMA, temperature=0.1)])
        if res:
            judged = res[0]
            if judged.get("quote") and judged.get("closest_source_id") in {s["id"] for s in relevant}:
                add_claim(db, ctx.project_id, f"Existing work related to '{concept['title']}': {judged['overlap']}",
                          "competitor", "originality_investigator",
                          [QuoteRef(judged["closest_source_id"], judged["quote"])], subject_type="concept",
                          subject_id=concept["id"])
            if verdict != "close_match_found" and judged.get("meaningful_difference") is False:
                verdict = "close_match_found"
    note = f"max similarity {max_sim} across {len(candidate_sources)} sources"
    if judged:
        note += f"; judgement: {judged.get('overlap')} | difference: {judged.get('difference')}"
    with db.tx():
        db.insert("originality_checks", {"project_id": ctx.project_id, "concept_id": concept["id"],
                                         "searched": searched, "unavailable": unavailable, "verdict": verdict,
                                         "note": note})
    return {"verdict": verdict, "max_similarity": max_sim, "matches": [(sim, s["id"]) for sim, s in top],
            "judgement": judged}
