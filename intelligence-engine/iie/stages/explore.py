"""Question, research, discovery, invention, and comparison stages."""
from __future__ import annotations

import random

from ..context import Ctx
from ..invention import diversity, originality
from ..invention.methods import CONCEPTS_SCHEMA, METHODS, method_prompt
from ..llm import GenTask
from ..memory import evidence_context, history_duplicates
from ..research.connectors import STACK_SITES
from ..research.engine import RQuery, extract_claims, run_research
from ..evidence import detect_contradictions
from ..schema import STR, STRS, arr, obj
from ..util import clip, sha256
from . import Stage, active_concepts, selected_opportunity

# Broad, unrelated sectors. Discovery samples across groups so picks are not neighbours.
INDUSTRIES: list[tuple[str, str, list[str]]] = [
    ("home repair and maintenance", "built_environment", ["home"]),
    ("construction and building engineering", "built_environment", ["construction"]),
    ("small-scale food processing and cooking", "food", ["food"]),
    ("homebrewing and fermentation", "food", ["brewing"]),
    ("hospitality and guest stays", "services", ["hospitality"]),
    ("personal finance and small business accounting", "services", ["finance"]),
    ("workplace and freelance operations", "services", ["work"]),
    ("bicycles and urban mobility", "mobility", ["cycling"]),
    ("vehicle maintenance", "mobility", ["vehicles"]),
    ("gardening and urban farming", "agriculture", ["gardening"]),
    ("electronics repair and hobby electronics", "technology", ["electronics"]),
    ("software development tooling", "technology", ["software"]),
    ("woodworking and furniture making", "manufacturing", ["woodworking"]),
    ("3D printing and small-batch manufacturing", "manufacturing", ["manufacturing"]),
    ("education and teaching", "education", ["education"]),
    ("pets and animal care", "consumer", ["pets"]),
    ("parenting and childcare", "family", ["parenting"]),
    ("outdoor recreation and trekking", "leisure", ["outdoors"]),
    ("photography and imaging", "creative", ["photography"]),
    ("music and instruments", "creative", ["music"]),
    ("textiles and crafts", "materials", ["crafts"]),
    ("sustainability and household waste", "infrastructure", ["sustainability"]),
    ("fitness and physical training", "health", ["health_fitness"]),
    ("travel and logistics", "logistics", ["travel"]),
]


def pick_industries(seed: int, n: int = 3) -> list[tuple[str, str, list[str]]]:
    rng = random.Random(seed)
    pool = INDUSTRIES[:]
    rng.shuffle(pool)
    chosen, groups = [], set()
    for ind in pool:
        if ind[1] in groups:
            continue
        chosen.append(ind)
        groups.add(ind[1])
        if len(chosen) == n:
            break
    return chosen


def discovery_queries(name: str, keys: list[str]) -> list[RQuery]:
    sites = sorted({s for k in keys for s in STACK_SITES.get(k, [])})[:1]
    qs = [RQuery(term, "problem", ["stackexchange"], {"site": site, "sort": "votes"}, name)
          for site in sites for term in ("expensive", "better way")]
    qs += [
        RQuery(f"{name} problem", "problem", ["hackernews", "searxng", "brave"], {}, name),
        RQuery(f"{name} costly frustration customers", "problem", ["searxng", "brave"], {}, name),
        RQuery(name, "market", ["wikipedia"], {}, name),
        RQuery(f"{name} low cost innovation", "emerging", ["openalex"], {"from_year": 2022}, name),
    ]
    return qs


PLAN_SCHEMA = obj(["framing", "queries"], framing=STR,
                  queries=arr(obj(["text", "purpose"], text=STR,
                                  purpose={"type": "string", "enum": ["background", "problem", "market", "technical",
                                                                      "emerging", "prior_art", "competitor", "price"]}),
                              1, 14))


def run_question(ctx: Ctx) -> dict:
    p = ctx.project
    st = p.get("settings") or {}
    wf = p.get("workflow")
    if wf in ("full", "discovery") and not st.get("concept"):
        seed = int(st.get("seed", 0)) or int(sha256(p["id"])[:8], 16) % 10_000
        given = st.get("industries")
        inds = ([(i, "user", [k for k in STACK_SITES if k in i.lower()] or ["home"]) for i in given]
                if given else pick_industries(seed))
        queries = [q for name, _, keys in inds for q in discovery_queries(name, keys)]
        ctx.log("decision_director", "framing", f"Discovery with no starting idea across: {', '.join(i[0] for i in inds)} "
                f"(seed {seed})")
        return {"industries": [i[0] for i in inds], "seed": seed, "queries": [q.to_dict() for q in queries],
                "framing": "Open discovery: find recurring problems and costly compromises in unrelated industries."}
    # A specific question or concept.
    subject = st.get("concept", {}).get("title") or p["question"]
    if st.get("concept"):
        _ensure_user_concept(ctx, st["concept"])
    templates = [
        RQuery(subject, "background"), RQuery(f"{subject} problems complaints", "problem"),
        RQuery(f"{subject} existing products competitors", "competitor"), RQuery(f"{subject} price", "price"),
        RQuery(f"{subject} technology", "technical"),
    ]
    queries = templates
    framing = f"Investigate: {subject}"
    res = ctx.generate([GenTask(role="decision_director", purpose="plan_research",
                                system="You are the Decision Director framing a research plan.",
                                prompt=f"QUESTION: {p['question']}\nSUBJECT: {subject}\nWrite a short framing of what "
                                       "must be true for this to be worth pursuing, then up to 10 search queries that "
                                       "would test it (mix purposes: problem, competitor, price, technical, prior_art, "
                                       "market). Queries should be plain search phrases.",
                                schema=PLAN_SCHEMA, temperature=0.3)])
    if res:
        framing = res[0]["framing"]
        queries = [RQuery(q["text"], q["purpose"]) for q in res[0]["queries"]] + templates[:2]
    return {"industries": [], "queries": [q.to_dict() for q in queries], "framing": framing}


def _ensure_user_concept(ctx: Ctx, c: dict) -> None:
    if ctx.db.one("concepts", "project_id=? AND title=?", (ctx.project_id, c["title"])):
        return
    with ctx.db.tx():
        ctx.db.insert("concepts", {
            "project_id": ctx.project_id, "title": c["title"], "method": c.get("method", "user_supplied"),
            "principle": c.get("core_principle", c.get("principle", "")), "user_value": c.get("user_value", ""),
            "business_model": c.get("business_model", ""), "axes": c.get("axes", {}),
            "detail": {k: v for k, v in c.items() if k not in ("title",)}, "status": "shortlisted",
            "generation_mode": "user", "created_by": "user"})


def check_question(ctx: Ctx, out: dict) -> tuple[bool, str]:
    return (bool(out.get("queries")), "research plan has queries" if out.get("queries") else "no queries planned")


def _stage_output(ctx: Ctx, key: str) -> dict:
    row = ctx.db.one("jobs", "project_id=? AND stage=? AND status IN ('done','incomplete') ORDER BY created_at DESC",
                     (ctx.project_id, key))
    return (row or {}).get("output") or {}


def run_research_stage(ctx: Ctx) -> dict:
    q = _stage_output(ctx, "question")
    queries = [RQuery.from_dict(d) for d in q.get("queries", [])]
    summary = run_research(ctx, queries, label="research", max_queries=30)
    src_ids = [s["id"] for s in ctx.db.query("sources", "project_id=?", (ctx.project_id,))]
    focus = q.get("framing") or ctx.project["question"]
    ext = extract_claims(ctx, src_ids, focus)
    contra = detect_contradictions(ctx.db, ctx.project_id)
    return {**summary, "sources_total": len(src_ids), **{k: v for k, v in ext.items() if k != "problems"},
            "quote_problems": len(ext["problems"]), "contradictions": len(contra)}


def check_research(ctx: Ctx, out: dict) -> tuple[bool, str]:
    if out.get("sources_total", 0) == 0:
        return False, ("no sources retrieved; every downstream claim stays an assumption. Unavailable: "
                       + ", ".join(f"{k} ({v[:60]})" for k, v in (out.get("unavailable_connectors") or {}).items()))
    return True, f"{out['sources_total']} sources stored"


OPP_SCHEMA = obj(
    ["opportunities"],
    opportunities=arr(obj(
        ["title", "problem", "who", "claim_ids", "frequency_intensity", "current_alternatives", "why_gap_exists",
         "gap_explanation", "weakest_assumption", "test_for_weakest_assumption"],
        title=STR, problem=STR, who=STR, claim_ids=STRS, frequency_intensity=STR, current_alternatives=STR,
        current_spend=STR,
        why_gap_exists={"type": "string", "enum": ["weak_demand", "technical_barrier", "regulatory_barrier",
                                                   "capital_barrier", "distribution_barrier", "new_enabler",
                                                   "overlooked_segment", "unknown"]},
        gap_explanation=STR, weakest_assumption=STR, test_for_weakest_assumption=STR), 0, 3),
)


def run_discovery(ctx: Ctx) -> dict:
    db = ctx.db
    q = _stage_output(ctx, "question")
    industries = q.get("industries") or [None]
    cp = ctx.checkpoint()
    if cp.get("discovery_stored"):
        return cp["discovery_out"]
    claims = db.query("claims", "project_id=? AND support='verified_quote'", (ctx.project_id,))
    src_ind = {s["id"]: (s.get("meta") or {}).get("industry") for s in db.query("sources", "project_id=?", (ctx.project_id,))}
    cl_src = {}
    for r in db.conn.execute("SELECT claim_id, source_id FROM claim_sources WHERE verified=1").fetchall():
        cl_src.setdefault(r[0], []).append(r[1])
    by_ind: dict[str | None, list[dict]] = {i: [] for i in industries}
    for c in claims:
        inds = {src_ind.get(s) for s in cl_src.get(c["id"], [])}
        for i in industries:
            if i is None or i in inds:
                by_ind[i].append(c)
    tasks, order = [], []
    for ind, cl in by_ind.items():
        if not cl:
            continue
        lines = [f"{c['id']} [{c['claim_type']}]: {clip(c['text'], 240)}" for c in cl[:40]]
        tasks.append(GenTask(
            role="opportunity_scout", purpose=f"discover:{ind}", system="You are the Opportunity Scout.",
            prompt=(f"INDUSTRY: {ind or ctx.project['question']}\n\nVERIFIED EVIDENCE:\n" + "\n".join(lines) +
                    "\n\nFind up to 3 opportunities: recurring problems, costly compromises, or poorly served buyers "
                    "where a better offering could command real value. Cite the claim ids behind each. For "
                    "why_gap_exists, decide whether the gap exists because demand is weak, because of a real barrier, "
                    "because a segment is overlooked, or because something new makes a solution possible. Low online "
                    "visibility is not low competition. Return zero opportunities if the evidence does not support any."),
            schema=OPP_SCHEMA, temperature=0.4, max_tokens=2500))
        order.append(ind)
    results = ctx.generate(tasks) if tasks else []
    valid = {c["id"]: c for c in claims}
    created = []
    with db.tx():
        if results is None:
            # No model: group problem titles per industry as raw candidates.
            for ind, cl in by_ind.items():
                probs = [c for c in cl if c["claim_type"] == "problem_signal"][:5]
                for c in probs:
                    created.append(db.insert("opportunities", {
                        "project_id": ctx.project_id, "industry": ind, "title": clip(c["text"], 120),
                        "problem": c["text"], "who": "unknown (needs model or human analysis)",
                        "detail": {"why_gap_exists": "unknown", "note": "raw problem signal; not analysed"},
                        "claim_ids": [c["id"]], "status": "candidate", "created_by": "extractor"}))
        else:
            for ind, res in zip(order, results):
                for o in res.get("opportunities", []):
                    cids = [x for x in o.get("claim_ids", []) if x in valid]
                    status = "candidate" if cids else "unsupported"
                    created.append(db.insert("opportunities", {
                        "project_id": ctx.project_id, "industry": ind, "title": o["title"], "problem": o["problem"],
                        "who": o["who"], "claim_ids": cids, "status": status, "created_by": "opportunity_scout",
                        "detail": {k: o.get(k) for k in ("frequency_intensity", "current_alternatives", "current_spend",
                                                         "why_gap_exists", "gap_explanation", "weakest_assumption",
                                                         "test_for_weakest_assumption")}}))
    ranking = rank_opportunities(ctx)
    out = {"opportunities": len(created), "ranking": ranking, "model_used": results is not None}
    with db.tx():
        if ranking:
            db.execute("UPDATE opportunities SET status='selected' WHERE id=?", (ranking[0]["id"],))
        ctx.save_checkpoint({**ctx.checkpoint(), "discovery_stored": True, "discovery_out": out})
    return out


def rank_opportunities(ctx: Ctx) -> list[dict]:
    """Order by evidence breadth; explain the basis. This is an ordering, not a score of quality."""
    db = ctx.db
    rows = db.query("opportunities", "project_id=? AND status IN ('candidate','ranked','selected')", (ctx.project_id,))
    ranked = []
    for o in rows:
        cids = o.get("claim_ids") or []
        srcs = set()
        signal = 0
        for cid in cids:
            for r in db.conn.execute("SELECT s.id, s.meta FROM claim_sources x JOIN sources s ON s.id=x.source_id "
                                     "WHERE x.claim_id=? AND x.verified=1", (cid,)).fetchall():
                srcs.add(r[0])
                meta = __import__("json").loads(r[1] or "{}")
                signal += int(meta.get("score") or 0) + int(meta.get("points") or 0)
        gap = (o.get("detail") or {}).get("why_gap_exists", "unknown")
        ranked.append({"id": o["id"], "title": o["title"], "industry": o["industry"], "sources": len(srcs),
                       "claims": len(cids), "public_votes": signal, "gap": gap,
                       "basis": f"{len(srcs)} independent source(s), {len(cids)} claim(s), public votes {signal}, gap: {gap}"})
    ranked.sort(key=lambda r: (r["gap"] != "weak_demand", r["sources"], r["claims"], r["public_votes"]), reverse=True)
    with db.tx():
        for r in ranked:
            db.execute("UPDATE opportunities SET status='ranked' WHERE id=? AND status='candidate'", (r["id"],))
    return ranked


def check_discovery(ctx: Ctx, out: dict) -> tuple[bool, str]:
    n = len(out.get("ranking") or [])
    return (n > 0, f"{n} evidence-backed opportunities" if n else "no opportunity is supported by verified evidence")


DEFAULT_METHODS = list(METHODS)


def _opportunity_for_invention(ctx: Ctx) -> dict:
    opp = selected_opportunity(ctx)
    if opp:
        return opp
    return {"id": None, "title": ctx.project["question"], "problem": ctx.project["question"], "who": "to be determined",
            "detail": {}, "claim_ids": []}


def _facts(ctx: Ctx, opp: dict) -> list[str]:
    db = ctx.db
    first = [db.get("claims", c) for c in (opp.get("claim_ids") or [])]
    rest = db.query("claims", "project_id=? AND support='verified_quote'", (ctx.project_id,), "created_at")
    seen, out = set(), []
    for c in [x for x in first if x] + rest:
        if c["id"] in seen:
            continue
        seen.add(c["id"])
        out.append(f"{c['id']}: {clip(c['text'], 220)}")
    return out[:30]


def generate_concepts(ctx: Ctx, methods: list[str], avoid: list[str], tag: str) -> int | None:
    opp = _opportunity_for_invention(ctx)
    facts = _facts(ctx, opp)
    prior = evidence_context(ctx.db, opp["title"] + " " + opp["problem"], ctx.project_id) if ctx.mode == "evidence" else []
    tasks = [GenTask(role="cross_disciplinary_researcher" if m == "cross_domain" else "inventor",
                     purpose=f"invent:{m}:{tag}", system=f"You are the Inventor using the {METHODS[m]['title']} method.",
                     prompt=method_prompt(m, opp, facts, avoid, prior), schema=CONCEPTS_SCHEMA, temperature=0.8,
                     max_tokens=2000) for m in methods]
    results = ctx.generate(tasks)
    if results is None:
        _worksheet(ctx, opp, facts, methods)
        return None
    valid = {c["id"] for c in ctx.db.query("claims", "project_id=?", (ctx.project_id,))}
    n = 0
    with ctx.db.tx():
        for m, res in zip(methods, results):
            for c in res["concepts"]:
                c["evidence_claim_ids"] = [x for x in c.get("evidence_claim_ids", []) or [] if x in valid]
                ctx.db.insert("concepts", {
                    "project_id": ctx.project_id, "opportunity_id": opp.get("id"), "title": c["title"], "method": m,
                    "principle": c["core_principle"], "user_value": c["user_value"], "business_model": c["business_model"],
                    "axes": c["axes"], "detail": c, "status": "active", "generation_mode": ctx.mode,
                    "created_by": "cross_disciplinary_researcher" if m == "cross_domain" else "inventor"})
                n += 1
        ctx.save_checkpoint({**ctx.checkpoint(), f"invent_{tag}": n})
    return n


def _worksheet(ctx: Ctx, opp: dict, facts: list[str], methods: list[str]) -> None:
    lines = [f"# Invention worksheet: {opp['title']}", "", "No model was available, so concepts were not generated.",
             "Fill these in through the Invention Lab, then rerun comparison.", "", "## Evidence", *facts, ""]
    for m in methods:
        lines += [f"## {METHODS[m]['title']}", METHODS[m]["instructions"], "", "- Concept:", "- Core principle:", ""]
    path = ctx.tools.call("write_workspace_file", {"relpath": f"{ctx.project_id}/invention_worksheet.md",
                                                   "text": "\n".join(lines)}, "inventor", ctx.project_id, ctx.job_id)
    with ctx.db.tx():
        ctx.db.insert("artifacts", {"project_id": ctx.project_id, "kind": "worksheet", "path": path,
                                    "description": "invention method worksheet (no model)", "validated": 0})


def run_invention(ctx: Ctx) -> dict:
    cp = ctx.checkpoint()
    cycle = (ctx.project.get("settings") or {}).get("cycle", 0)
    tag = f"c{cycle}"
    if f"invent_{tag}" not in cp:
        avoid = []
        if cycle > 0:
            avoid = [f"{c['title']}: {c['principle']}" for c in
                     ctx.db.query("concepts", "project_id=?", (ctx.project_id,))]
        methods = (ctx.project.get("settings") or {}).get("methods") or DEFAULT_METHODS
        n = generate_concepts(ctx, methods, avoid, tag)
    else:
        n = cp[f"invent_{tag}"]
    total = len(active_concepts(ctx))
    return {"generated": n, "active_concepts": total, "model_used": n is not None}


def check_invention(ctx: Ctx, out: dict) -> tuple[bool, str]:
    if out["active_concepts"] >= 3:
        return True, f"{out['active_concepts']} concepts available"
    if not out["model_used"]:
        return False, "no model available; worksheet written. Add concepts manually or configure a model."
    return False, f"only {out['active_concepts']} concepts"


def run_comparison(ctx: Ctx) -> dict:
    db = ctx.db
    cp = ctx.checkpoint()
    concepts = active_concepts(ctx)
    rep = diversity.diversity_report(concepts)
    if not rep["meets_requirement"] and not cp.get("reinvented") and ctx.has_model() and len(concepts) > 0:
        avoid = [f"{c['title']}: {c['principle']}" for c in concepts]
        generate_concepts(ctx, ["radical", "inversion", "cross_domain"], avoid, "diversity")
        ctx.save_checkpoint({**ctx.checkpoint(), "reinvented": True})
        concepts = active_concepts(ctx)
        rep = diversity.diversity_report(concepts)
    by_id = {c["id"]: c for c in concepts}
    with db.tx():
        db.execute("DELETE FROM concept_overlaps WHERE project_id=?", (ctx.project_id,))
        for pr in rep["pairs"]:
            db.insert("concept_overlaps", {"project_id": ctx.project_id, "a_id": pr["a_id"], "b_id": pr["b_id"],
                                           "text_similarity": pr["text_similarity"], "shared_axes": pr["shared_axes"],
                                           "verdict": pr["verdict"], "reason": pr["reason"]})
    for root, members in rep["families"].items():
        for m in members:
            db.update("concepts", m, {"family_id": root, "status": "active" if m == members[0] else "merged",
                                      "merged_into": None if m == members[0] else members[0]}, "inventor")
    ctx.log("inventor", "diversity", rep["explanation"])

    reps = [by_id[r] for r in rep["representatives"]]
    unchecked = [c for c in reps if not db.one("originality_checks", "concept_id=?", (c["id"],))]
    if not cp.get("originality_done") and unchecked:
        queries = []
        for c in unchecked:
            queries += [RQuery(t, p) for t, p in originality.queries_for(c)]
        summary = run_research(ctx, queries, actor="originality_investigator", label="originality", max_queries=24)
        cands = [s for s in db.query("sources", "project_id=?", (ctx.project_id,))
                 if (s.get("meta") or {}).get("label") in ("originality", "research")]
        searched = summary.get("used", [])
        results = {}
        for c in unchecked:
            r = originality.assess(ctx, c, cands, searched, summary["unavailable_connectors"])
            results[c["id"]] = r["verdict"]
            dups = history_duplicates(db, c)
            if dups:
                ctx.log("originality_investigator", "history_duplicate",
                        f"'{c['title']}' resembles earlier concepts: {dups[:3]}")
        ctx.save_checkpoint({**ctx.checkpoint(), "originality_done": True, "originality": results})
    results = {c["id"]: (db.one("originality_checks", "concept_id=? ORDER BY created_at DESC", (c["id"],)) or {})
               .get("verdict", "not_checked") for c in reps}
    order = {"no_close_match_in_searched_sources": 0, "related_work_found": 1, "not_checked": 2, "close_match_found": 3}
    reps.sort(key=lambda c: order.get(results.get(c["id"], "not_checked"), 2))
    short = reps[:3]
    for c in short:
        db.update("concepts", c["id"], {"status": "shortlisted"}, "decision_director")
    return {"families": rep["family_count"], "meets_diversity": rep["meets_requirement"],
            "explanation": rep["explanation"], "originality": results, "shortlisted": [c["id"] for c in short],
            "distinct_principles": rep["distinct_principle_classes"], "distinct_models": rep["distinct_business_models"]}


def check_comparison(ctx: Ctx, out: dict) -> tuple[bool, str]:
    if not out["meets_diversity"]:
        return False, f"only {out['families']} distinct solution families (need 3)"
    if all(v == "not_checked" for v in out["originality"].values()):
        return False, "diversity met, but no originality search could run"
    return True, out["explanation"]


STAGES = [
    Stage("question", "Question", ["decision_director"], "project question, workflow, settings",
          "framing, industries, research queries", ["model (optional)"], "none",
          "at least one query planned", "no queries", run_question, check_question),
    Stage("research", "Research", ["research_investigator", "extractor"], "planned queries",
          "sources with retrieval dates, verified claims, contradictions, research gaps",
          ["wikipedia", "openalex", "crossref", "arxiv", "semantic_scholar", "stackexchange", "hackernews",
           "worldbank", "searxng", "brave", "patentsview", "operator_bundle"],
          "every claim quotes its stored source verbatim", "at least one source stored",
          "no source reachable; gaps recorded, nothing invented", run_research_stage, check_research),
    Stage("discovery", "Opportunity discovery", ["opportunity_scout", "buyer_researcher"], "verified claims by industry",
          "opportunities with cited claims, gap type, weakest assumption, ranked by evidence breadth",
          ["model"], "each opportunity cites at least one verified claim", "at least one supported opportunity",
          "no evidence-backed opportunity", run_discovery, check_discovery),
    Stage("invention", "Invention", ["inventor", "cross_disciplinary_researcher"], "selected opportunity, evidence",
          "concepts from seven methods with principle and axes", ["model"],
          "fresh mode excludes concept history", "3+ concepts", "no model: worksheet only", run_invention,
          check_invention),
    Stage("comparison", "Comparison and originality", ["inventor", "originality_investigator"], "active concepts",
          "overlap matrix, solution families, originality checks, shortlist", ["tf-idf", "research connectors", "model"],
          "originality verdicts list what was searched and what was not", "3+ families and an originality search",
          "fewer than 3 families after one extra round", run_comparison, check_comparison),
]
