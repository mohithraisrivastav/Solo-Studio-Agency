"""Critical review: fixed rules plus an adversarial model review, and disagreement records."""
from __future__ import annotations

from .context import Ctx
from .evidence import freshness
from .llm import GenTask
from .schema import STR, STRS, arr, obj

CRITIC_QUESTIONS = [
    "What could make this fail?",
    "Which assumption is least reliable?",
    "Does something similar already exist?",
    "Is the difference meaningful?",
    "Would anyone pay for this?",
    "Can it be manufactured or delivered?",
    "Does the business work financially?",
    "Can customers be reached?",
    "What would competitors do?",
    "What would a critical investor or experienced buyer question?",
    "Is there a much simpler or more effective approach?",
]

CRITIC_SCHEMA = obj(
    ["objections", "strongest_point", "simpler_alternative"],
    objections=arr(obj(["question", "objection", "severity", "basis"], question=STR, objection=STR,
                       severity={"type": "string", "enum": ["fatal", "major", "minor"]},
                       basis={"type": "string", "enum": ["source", "calculation", "reasoning"]},
                       source_ids=STRS, claim_ids=STRS, disputes_role=STR)),
    strongest_point=STR,
    simpler_alternative=STR,
)


def _add(ctx: Ctx, concept_id: str, category: str, objection: str, severity: str, basis: str, rule_id: str | None,
         actor: str, source_ids: list[str] | None = None, claim_ids: list[str] | None = None) -> str:
    with ctx.db.tx():
        return ctx.db.insert("critiques", {
            "project_id": ctx.project_id, "target_type": "concept", "target_id": concept_id, "actor": actor,
            "category": category, "objection": objection, "severity": severity, "basis": basis,
            "source_ids": source_ids or [], "claim_ids": claim_ids or [], "rule_id": rule_id, "status": "open"})


def rule_critiques(ctx: Ctx, concept: dict, state: dict) -> list[str]:
    """state: demand_level, originality (row|None), econ (scenario dict|None), hazards, plan, gaps, contradictions."""
    ids = []
    cid = concept["id"]
    lvl = state.get("demand_level", 0)
    if lvl <= 1:
        ids.append(_add(ctx, cid, "demand", f"Demand is not shown beyond indirect evidence (level {lvl}). "
                        "No buyer has confirmed the problem, interest, or a price.", "major", "calculation",
                        "R_DEMAND_UNPROVEN", "critical_reviewer"))
    orc = state.get("originality")
    if not orc or orc["verdict"] == "not_checked":
        ids.append(_add(ctx, cid, "originality", "No existing-solution search could be completed, so novelty is "
                        "unknown. Do not claim the concept is new.", "major", "calculation", "R_NO_ORIGINALITY_CHECK",
                        "critical_reviewer"))
    elif orc["verdict"] == "close_match_found":
        pa = ctx.db.query("prior_art", "concept_id=? ORDER BY similarity DESC LIMIT 3", (cid,))
        ids.append(_add(ctx, cid, "originality", f"Close existing work found ({orc['note'][:300]}). The concept may "
                        "be too similar to what already exists.", "major", "source", "R_CLOSE_PRIOR_ART",
                        "critical_reviewer", [p["source_id"] for p in pa]))
    econ = state.get("econ")
    if econ:
        for f in econ["findings"]:
            if f["severity"] in ("fatal", "major"):
                ids.append(_add(ctx, cid, "economics", f"[base case] {f['message']}", f["severity"], "calculation",
                                f"R_ECON_{f['code']}", "critical_reviewer"))
    cons = state.get("econ_conservative")
    if cons and cons["verdict"] == "not_viable" and econ and econ["verdict"] != "not_viable":
        ids.append(_add(ctx, cid, "economics", "In the conservative scenario the business is not viable: "
                        + "; ".join(f["message"] for f in cons["findings"] if f["severity"] == "fatal")[:400],
                        "major", "calculation", "R_ECON_CONSERVATIVE_FAILS", "critical_reviewer"))
    for h in state.get("hazards", []):
        ids.append(_add(ctx, cid, "safety", f"Keyword scan flagged a possible {h['category']} hazard (words: "
                        f"{', '.join(h['triggers'])}). If it applies: {h['mandatory_review']}",
                        "major", "calculation", f"R_HAZARD_{h['category'].upper()}", "critical_reviewer"))
    plan = state.get("plan") or {}
    for p in plan.get("processes", []) or []:
        cost = p.get("equipment_cost_inr") or 0
        if cost >= ctx.settings.equipment_threshold_inr and lvl < 3:
            ids.append(_add(ctx, cid, "capital", f"Plan buys equipment ({p.get('equipment')}, about ₹{cost:,.0f}) "
                            f"before demand reaches level 3. Rent, outsource, or use a maker space for validation.",
                            "major", "calculation", "R_EQUIPMENT_BEFORE_DEMAND", "critical_reviewer"))
    ev_ids = (concept.get("detail") or {}).get("evidence_claim_ids") or []
    if ev_ids:
        srcs = {r["source_id"] for r in ctx.db.conn.execute(
            f"SELECT source_id FROM claim_sources WHERE claim_id IN ({','.join('?' * len(ev_ids))})", ev_ids).fetchall()}
        if len(srcs) == 1:
            ids.append(_add(ctx, cid, "evidence", "All evidence cited for this concept comes from a single source.",
                            "minor", "calculation", "R_SINGLE_SOURCE", "critical_reviewer", list(srcs)))
    stale = []
    for c in ctx.db.query("claims", "project_id=? AND claim_type IN ('price_observation','market_size','competitor')",
                          (ctx.project_id,)):
        for cs in ctx.db.conn.execute("SELECT s.published_at, s.retrieved_at, s.id FROM claim_sources x JOIN sources s "
                                      "ON s.id=x.source_id WHERE x.claim_id=?", (c["id"],)).fetchall():
            st, _ = freshness(c["claim_type"], cs[0], cs[1])
            if st == "possibly_outdated":
                stale.append(cs[2])
    if stale:
        ids.append(_add(ctx, cid, "evidence", f"{len(set(stale))} price, market, or competitor source(s) may be "
                        "outdated.", "minor", "calculation", "R_STALE_EVIDENCE", "critical_reviewer", sorted(set(stale))))
    n_contra = ctx.db.scalar("SELECT COUNT(*) FROM contradictions WHERE project_id=? AND status='open'", (ctx.project_id,))
    if n_contra:
        ids.append(_add(ctx, cid, "evidence", f"{n_contra} open contradiction(s) between sources are unresolved.",
                        "major", "calculation", "R_OPEN_CONTRADICTIONS", "critical_reviewer"))
    if orc and orc["verdict"] == "no_close_match_in_searched_sources" and orc.get("unavailable"):
        ids.append(_add(ctx, cid, "originality", "No close competitor appeared, but these sources could not be "
                        f"searched: {', '.join(orc['unavailable'])}. Low visibility is not low competition; check "
                        "whether the gap reflects weak demand or real barriers.", "minor", "calculation",
                        "R_VISIBILITY_NOT_COMPETITION", "critical_reviewer"))
    unver = ctx.db.scalar("SELECT COUNT(*) FROM claims WHERE project_id=? AND support='source_unverified'", (ctx.project_id,))
    if unver:
        ids.append(_add(ctx, cid, "evidence", f"{unver} extracted claim(s) had quotes that could not be found in "
                        "their sources and were excluded from evidence.", "minor", "calculation",
                        "R_UNVERIFIED_QUOTES", "critical_reviewer"))
    return ids


def model_critique(ctx: Ctx, concept: dict, briefing: str) -> dict | None:
    prompt = (f"CONCEPT UNDER REVIEW: {concept['title']}\n{briefing}\n\nAnswer these questions as an independent critic. "
              "Each objection needs a basis: 'source' (give source_ids from the briefing), 'calculation' (from the "
              "economics shown), or 'reasoning' (say so). Do not invent facts. Do not object for show: if a point is "
              "strong, say so in strongest_point. If you dispute another specialist's finding, name that role in "
              "disputes_role.\n" + "\n".join(f"- {q}" for q in CRITIC_QUESTIONS))
    res = ctx.generate([GenTask(role="critical_reviewer", purpose=f"critique:{concept['id']}",
                                system="You are the Critical Reviewer. Your job is to find what would make this fail.",
                                prompt=prompt, schema=CRITIC_SCHEMA, temperature=0.3, max_tokens=2500)])
    if not res:
        return None
    out = res[0]
    valid_src = {r["id"] for r in ctx.db.query("sources", "project_id=?", (ctx.project_id,))}
    valid_clm = {r["id"]: r for r in ctx.db.query("claims", "project_id=?", (ctx.project_id,))}
    for o in out["objections"]:
        sids = [s for s in (o.get("source_ids") or []) if s in valid_src]
        cids = [c for c in (o.get("claim_ids") or []) if c in valid_clm]
        basis = o["basis"]
        if basis == "source" and not (sids or cids):
            basis = "reasoning"  # cited nothing that exists
        cid = _add(ctx, concept["id"], "review", f"{o['question']} {o['objection']}", o["severity"], basis, None,
                   "critical_reviewer", sids, cids)
        disputed = o.get("disputes_role")
        if disputed and disputed != "critical_reviewer":
            with ctx.db.tx():
                ctx.db.insert("disagreements", {
                    "project_id": ctx.project_id, "topic": f"{concept['title']}: {o['question']}", "role_a": disputed,
                    "position_a": "finding as recorded by " + disputed, "evidence_a": [],
                    "role_b": "critical_reviewer", "position_b": o["objection"],
                    "evidence_b": {"sources": sids, "claims": cids, "basis": basis, "critique": cid},
                    "status": "unresolved"})
    return out


def structural_disagreements(ctx: Ctx, concept: dict, state: dict) -> None:
    """Record conflicts between specialists that the numbers expose."""
    econ = state.get("econ")
    orc = state.get("originality")
    plan = state.get("plan") or {}
    rows = []
    if econ and econ["verdict"] in ("viable_on_paper", "marginal") and state.get("demand_level", 0) <= 1:
        rows.append(("Is the business viable?", "commercial_analyst",
                     f"Economics verdict '{econ['verdict']}' on stated inputs", {"economics": econ.get("id")},
                     "critical_reviewer", "Inputs rest on unproven demand and assumed price; viability is not shown",
                     {"demand_level": state.get("demand_level", 0)}))
    if orc and orc["verdict"] == "close_match_found" and (concept.get("detail") or {}).get("why_different"):
        rows.append(("Is the concept meaningfully different?", "inventor",
                     concept["detail"]["why_different"][:300], {}, "originality_investigator",
                     orc["note"][:300], {"originality_check": orc["id"]}))
    if plan.get("maturity") in ("prototype_tested", "validated_design") and not ctx.db.query(
            "learnings", "project_id=? AND kind='outcome'", (ctx.project_id,)):
        rows.append(("How mature is the design?", "engineering_analyst", f"Plan says {plan['maturity']}", {},
                     "critical_reviewer", "No recorded test outcome supports that maturity", {}))
    with ctx.db.tx():
        for topic, ra, pa, ea, rb, pb, eb in rows:
            ctx.db.insert("disagreements", {"project_id": ctx.project_id, "topic": f"{concept['title']}: {topic}",
                                            "role_a": ra, "position_a": pa, "evidence_a": ea, "role_b": rb,
                                            "position_b": pb, "evidence_b": eb, "status": "unresolved"})
