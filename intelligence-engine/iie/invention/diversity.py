"""Conceptual diversity: detect overlap, cosmetic variants, and form solution families.

Heuristic, documented thresholds (TF-IDF cosine over principle + mechanism text):
  cosmetic_variant : nearly all differing words are colour/size/finish/style/name words
  same_solution    : text similarity >= 0.50, or >= 0.30 with the same principle class AND business model
  related          : text similarity >= 0.22, or 4+ of 5 axes shared
  distinct         : otherwise
These numbers group concepts; they are not quality scores.
"""
from __future__ import annotations

from ..text import TfIdf, cosmetic_only_difference
from .methods import AXES

SAME_T = 0.50
SAME_WITH_AXES_T = 0.30
RELATED_T = 0.22


def concept_text(c: dict) -> str:
    d = c.get("detail") or {}
    return " ".join(str(x) for x in (c.get("principle"), d.get("how_it_works"), d.get("assumption_challenged")) if x)


def full_text(c: dict) -> str:
    d = c.get("detail") or {}
    return " ".join(str(x) for x in (c.get("title"), c.get("principle"), d.get("how_it_works"), c.get("user_value"),
                                      c.get("business_model"), " ".join(d.get("materials") or [])) if x)


def compare(concepts: list[dict]) -> list[dict]:
    if len(concepts) < 2:
        return []
    tf = TfIdf([concept_text(c) for c in concepts])
    out = []
    for i in range(len(concepts)):
        for j in range(i + 1, len(concepts)):
            a, b = concepts[i], concepts[j]
            sim = round(tf.sim(i, j), 3)
            ax_a, ax_b = a.get("axes") or {}, b.get("axes") or {}
            shared = [k for k in AXES if ax_a.get(k) and ax_a.get(k) == ax_b.get(k)]
            cosmetic, subst = cosmetic_only_difference(full_text(a), full_text(b))
            same_core = "principle_class" in shared and "business_model_class" in shared
            if cosmetic:
                verdict, reason = "cosmetic_variant", "differs only in cosmetic terms"
            elif sim >= SAME_T or (sim >= SAME_WITH_AXES_T and same_core):
                verdict = "same_solution"
                reason = f"principle text similarity {sim}" + (", same principle class and business model" if same_core else "")
            elif sim >= RELATED_T or len(shared) >= 4:
                verdict, reason = "related", f"similarity {sim}; shared axes: {', '.join(shared) or 'none'}"
            else:
                verdict, reason = "distinct", f"similarity {sim}; shared axes: {', '.join(shared) or 'none'}"
            out.append({"a_id": a["id"], "b_id": b["id"], "text_similarity": sim, "shared_axes": shared,
                        "verdict": verdict, "reason": reason, "substantive_differences": subst[:10]})
    return out


def families(concepts: list[dict], pairs: list[dict]) -> dict[str, list[str]]:
    parent = {c["id"]: c["id"] for c in concepts}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for p in pairs:
        if p["verdict"] in ("same_solution", "cosmetic_variant"):
            ra, rb = find(p["a_id"]), find(p["b_id"])
            if ra != rb:
                parent[rb] = ra
    groups: dict[str, list[str]] = {}
    for c in concepts:
        groups.setdefault(find(c["id"]), []).append(c["id"])
    return groups


def diversity_report(concepts: list[dict], min_families: int = 3) -> dict:
    pairs = compare(concepts)
    fams = families(concepts, pairs)
    reps = [ids[0] for ids in fams.values()]
    by_id = {c["id"]: c for c in concepts}
    principle_classes = {(by_id[r].get("axes") or {}).get("principle_class") for r in reps}
    models = {(by_id[r].get("axes") or {}).get("business_model_class") for r in reps}
    ok = len(fams) >= min_families
    return {
        "pairs": pairs,
        "families": fams,
        "representatives": reps,
        "family_count": len(fams),
        "distinct_principle_classes": sorted(x for x in principle_classes if x),
        "distinct_business_models": sorted(x for x in models if x),
        "meets_requirement": ok,
        "explanation": (f"{len(fams)} solution families from {len(concepts)} concepts; "
                        f"{sum(1 for p in pairs if p['verdict'] in ('same_solution', 'cosmetic_variant'))} overlapping pairs merged."),
    }
