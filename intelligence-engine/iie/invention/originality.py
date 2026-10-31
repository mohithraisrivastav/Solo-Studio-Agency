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
    ["closest_source_id", "match_level", "overlap", "meaningful_difference", "difference"],
    closest_source_id=STR, match_level={"type": "string", "enum": ["close", "related", "unrelated"]},
    overlap=STR, meaningful_difference=BOOL, difference=STR, quote=STR,
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


def prepare(ctx: Ctx, concept: dict, candidate_sources: list[dict]) -> dict:
    """Rank candidate sources by similarity and build the judgement task (no writes)."""
    if not candidate_sources:
        return {"concept": concept, "top": [], "max_sim": 0.0, "task": None, "relevant": []}
    ctext = full_text(concept)
    docs = [ctext] + [f"{s.get('title')} {s.get('content') or ''}"[:4000] for s in candidate_sources]
    tf = TfIdf(docs)
    sims = sorted(((round(tf.sim(0, i + 1), 3), s) for i, s in enumerate(candidate_sources)), key=lambda x: -x[0])
    top = sims[:5]
    # Word overlap misses paraphrase, so a model (when present) judges the three closest sources regardless
    # of the lexical score. Without a model only the lexical thresholds apply.
    own_q = {t.strip().lower() for t, _ in queries_for(concept)}
    targeted = [s for s in candidate_sources
                if (s.get("query") or "").strip().lower() in own_q
                or ((s.get("meta") or {}).get("query") or "").strip().lower() in own_q]
    if ctx.has_model():
        relevant = (targeted + [s for _, s in top if s not in targeted])[:4]
    else:
        relevant = [s for sim, s in top if sim >= RELATED_T][:3]
    # sources retrieved for this concept's own queries count as prior-art candidates even if word overlap is low
    sim_by_id = {s["id"]: sim for sim, s in sims}
    for s in targeted:
        if s["id"] not in {x["id"] for _, x in top}:
            top.append((sim_by_id.get(s["id"], 0.0), s))
    task = None
    if relevant:
        prompt = ("CONCEPT:\n" + ctext + "\n\nEXISTING WORK FOUND:\n" + "\n\n".join(source_block(s, 1500) for s in relevant)
                  + "\n\nWhich source is closest? Rate the match: 'close' if it already delivers the same core function "
                    "to the same buyer, 'related' if it shares the principle or market but differs in a way a buyer would "
                    "notice, 'unrelated' otherwise. Is the concept's difference meaningful to a buyer (function, cost, "
                    "experience), or only cosmetic? Give one exact quote from the closest source.")
        task = GenTask(role="originality_investigator", purpose=f"originality:{concept['id']}",
                       system="You are the Originality Investigator. You look for reasons the concept already exists.",
                       prompt=prompt, schema=JUDGE_SCHEMA, temperature=0.1)
    return {"concept": concept, "top": top, "max_sim": top[0][0] if top else 0.0, "task": task, "relevant": relevant}


def finalize(ctx: Ctx, prep: dict, judged: dict | None, searched: list[str], unavailable: dict) -> dict:
    """Write prior-art rows, the optional competitor claim, and the originality verdict (idempotent)."""
    db = ctx.db
    concept, top, max_sim = prep["concept"], prep["top"], prep["max_sim"]
    if not top:
        verdict = "not_checked" if not searched else "no_close_match_in_searched_sources"
        note = ("No source could be searched; originality is unknown." if not searched else
                "Searched sources returned nothing relevant. This is not proof of novelty.")
    else:
        verdict = ("close_match_found" if max_sim >= CLOSE_T else
                   "related_work_found" if max_sim >= RELATED_T else "no_close_match_in_searched_sources")
        note = f"max similarity {max_sim} across {len(top)} top sources"
    with db.tx():
        db.execute("DELETE FROM prior_art WHERE concept_id=?", (concept["id"],))
        for sim, s in top:
            db.insert("prior_art", {"project_id": ctx.project_id, "concept_id": concept["id"], "source_id": s["id"],
                                    "similarity": sim, "verdict": "close" if sim >= CLOSE_T else
                                    ("related" if sim >= RELATED_T else "weak"),
                                    "note": "text similarity of concept to source", "created_by": "originality_investigator"})
    if judged:
        if judged.get("quote") and judged.get("closest_source_id") in {s["id"] for s in prep["relevant"]}:
            add_claim(db, ctx.project_id, f"Existing work related to '{concept['title']}': {judged['overlap']}",
                      "competitor", "originality_investigator", [QuoteRef(judged["closest_source_id"], judged["quote"])],
                      subject_type="concept", subject_id=concept["id"])
        level = judged.get("match_level")
        if level == "close" or judged.get("meaningful_difference") is False:
            verdict = "close_match_found"
        elif level == "related" and verdict == "no_close_match_in_searched_sources":
            verdict = "related_work_found"
        note += f"; judgement: {judged.get('overlap')} | difference: {judged.get('difference')}"
    with db.tx():
        db.execute("DELETE FROM originality_checks WHERE concept_id=?", (concept["id"],))
        db.insert("originality_checks", {"project_id": ctx.project_id, "concept_id": concept["id"], "searched": searched,
                                         "unavailable": unavailable, "verdict": verdict, "note": note})
    return {"verdict": verdict, "max_similarity": max_sim, "matches": [(sim, s["id"]) for sim, s in top],
            "judgement": judged}


def assess(ctx: Ctx, concept: dict, candidate_sources: list[dict], searched: list[str], unavailable: dict) -> dict:
    prep = prepare(ctx, concept, candidate_sources)
    judged = None
    if prep["task"]:
        res = ctx.generate([prep["task"]])
        judged = res[0] if res else None
    return finalize(ctx, prep, judged, searched, unavailable)
