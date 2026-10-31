"""Structured invention methods and the concept schema.

Each method is a distinct way of reasoning, with its own instructions. Every
concept must state its core principle and axes so the diversity checker can
compare concepts on substance (principle, value, material, business model,
interaction), not names or styling.
"""
from __future__ import annotations

from ..schema import STR, STRS, arr, obj

AXES: dict[str, list[str]] = {
    "principle_class": [
        "mechanical", "material_structural", "thermal", "optical", "acoustic", "fluidic", "chemical",
        "biological", "electronic", "software", "informational", "behavioural", "logistical", "business_model",
    ],
    "value_type": [
        "cost_saving", "time_saving", "risk_reduction", "performance", "status_meaning", "convenience",
        "access", "sustainability", "experience", "income",
    ],
    "material_class": [
        "none_digital", "wood", "metal", "ceramic_glass", "polymer", "textile", "stone", "composite",
        "bio_based", "electronic", "mixed",
    ],
    "business_model_class": [
        "product_sale", "edition_collectible", "licensing_royalty", "service", "recurring_supply",
        "b2b_institutional", "rental_access", "marketplace", "commissioned", "equipment",
        "proprietary_process", "software_subscription",
    ],
    "interaction_mode": ["passive_object", "tool", "installed_system", "service_delivered", "software", "consumable"],
}

METHODS: dict[str, dict] = {
    "first_principles": {
        "title": "First principles",
        "instructions": (
            "Break the problem into its physical, practical, economic, and human factors. List the assumptions "
            "that existing products inherit without question. Rebuild a solution from the fundamental "
            "requirements only. Name the specific requirement your concept satisfies better."
        ),
    },
    "cross_domain": {
        "title": "Cross-disciplinary transfer",
        "instructions": (
            "Find a working principle from a different field (biology, aerospace, logistics, textiles, optics, "
            "finance, agriculture, etc.) and transfer the mechanism, not the look. State the source field, the "
            "mechanism, and the concrete advantage it gives here. Surface visual resemblance does not count."
        ),
    },
    "inversion": {
        "title": "Inversion",
        "instructions": (
            "Pick an accepted approach in this category (who pays, what is sold, what material, who does the "
            "work, when value is delivered) and reverse it. Explain what the reversal makes possible and what "
            "it breaks."
        ),
    },
    "constraint_transformation": {
        "title": "Constraint transformation",
        "instructions": (
            "Change one hard constraint: material, manufacturing technique, energy need, installation method, "
            "scale, or cost ceiling. Redesign around the new constraint. Respect physical, legal, and economic "
            "limits and state them."
        ),
    },
    "unmet_need": {
        "title": "Unmet need",
        "instructions": (
            "Start from the strongest recurring frustration or costly compromise in the evidence. Identify the "
            "poorly served buyer and design for them specifically. Cite the claim ids that show the need."
        ),
    },
    "combination": {
        "title": "Original combination",
        "instructions": (
            "Combine two or more established ideas so the result delivers a different function, experience, or "
            "benefit than either alone. Explain why the combination is more than the sum of its parts."
        ),
    },
    "radical": {
        "title": "Radical alternative",
        "instructions": (
            "Propose an unconventional approach grounded in credible science, engineering, behaviour, or market "
            "evidence. Explain the grounding. Do not choose it because it sounds futuristic, and do not reject "
            "it because it is unfamiliar."
        ),
    },
}

CONCEPT_ITEM = obj(
    ["title", "core_principle", "how_it_works", "assumption_challenged", "user_value", "target_buyer",
     "business_model", "why_different", "key_risks", "axes"],
    title=STR,
    core_principle=STR,
    how_it_works=STR,
    assumption_challenged=STR,
    user_value=STR,
    target_buyer=STR,
    materials=STRS,
    process=STR,
    business_model=STR,
    why_different=STR,
    key_risks=STRS,
    evidence_claim_ids=STRS,
    source_field=STR,
    axes=obj(list(AXES), **{k: {"type": "string", "enum": v} for k, v in AXES.items()}),
)

CONCEPTS_SCHEMA = obj(["concepts"], concepts=arr(CONCEPT_ITEM, 1, 2))


def method_prompt(method: str, opportunity: dict, facts: list[str], avoid: list[str], prior_results: list[str]) -> str:
    m = METHODS[method]
    parts = [
        f"METHOD: {m['title']}\n{m['instructions']}",
        "",
        f"OPPORTUNITY: {opportunity.get('title')}",
        f"Problem: {opportunity.get('problem')}",
        f"Who: {opportunity.get('who')}",
    ]
    det = opportunity.get("detail") or {}
    for k in ("current_alternatives", "why_gap_exists", "weakest_assumption"):
        if det.get(k):
            parts.append(f"{k.replace('_', ' ').title()}: {det[k]}")
    if facts:
        parts += ["", "EVIDENCE (claim id: text):", *facts[:30]]
    if prior_results:
        parts += ["", "TESTED RESULTS FROM EARLIER WORK (evidence mode):", *prior_results[:10]]
    if avoid:
        parts += ["", "Already explored principles. Your concept must use a different underlying principle "
                  "or business model, not a restyled version of these:", *[f"- {a}" for a in avoid]]
    parts += ["", "Return 1 or 2 concepts. Fill 'axes' honestly. Keep each field short and concrete. Cite claim "
              "ids in evidence_claim_ids only if they exist above."]
    return "\n".join(parts)
