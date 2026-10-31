"""Technical, commercial, critique, validation, decision, and learning stages."""
from __future__ import annotations

import json

from ..commercial.demand import build_demand_task, store_demand
from ..commercial.economics import EconInputs, Line, run_scenarios, sensitivity, verdict, what_it_would_take
from ..commercial.fit import business_model_fit, premium_checks
from ..context import Ctx
from ..critique import model_critique, rule_critiques, structural_disagreements
from ..decision import decide, experiment_templates, gates, spend_limit
from ..engineering import PLAN_SCHEMA, bom_csv, detect_hazards, hazard_text, openscad
from ..evidence import demand_level
from ..invention.diversity import full_text
from ..llm import GenTask
from ..schema import BOOL, NUM, STR, STRS, arr, obj
from ..util import clip, money
from . import Stage, concept_state, relevant_claims, shortlisted

# ---------------------------------------------------------------- technical


def _concept_brief(c: dict) -> str:
    d = c.get("detail") or {}
    return (f"TITLE: {c['title']}\nMETHOD: {c.get('method')}\nPRINCIPLE: {c.get('principle')}\nHOW IT WORKS: "
            f"{d.get('how_it_works')}\nBUYER: {d.get('target_buyer')}\nVALUE: {c.get('user_value')}\nMATERIALS: "
            f"{', '.join(d.get('materials') or [])}\nPROCESS: {d.get('process')}\nBUSINESS MODEL: {c.get('business_model')}\n"
            f"RISKS: {'; '.join(d.get('key_risks') or [])}")


def _technical_task(ctx: Ctx, c: dict, hazards: list[dict]) -> GenTask:
    tech_claims = relevant_claims(ctx, c, types=("technical_finding", "cost_observation", "supply_signal",
                                                  "regulation", "competitor"), limit=20)
    prompt = (_concept_brief(c) + "\n\nDETECTED HAZARD CATEGORIES: " + (", ".join(h["category"] for h in hazards) or "none")
              + "\n\nTECHNICAL EVIDENCE:\n" + "\n".join(f"{x['id']}: {clip(x['text'], 200)}" for x in tech_claims[:20])
              + "\n\nAs Product Designer, Engineering Analyst, and Materials and Manufacturing Specialist, write a "
                "practical development plan. Compare manual, 3D printing, CNC, casting/moulding, traditional craft, "
                "hybrid, outsourced-component, and fully outsourced production. Do not recommend expensive equipment "
                "before demand is proven; give a low-cost validation route that keeps the required quality. Give "
                "prototype dimensions and tolerances only where they are justified. List BOM items with INR unit "
                "costs marked as assumption unless a claim id supports them. Provide a simple parts list (boxes, "
                "cylinders, tubes) for concept CAD if the product is physical. Be honest about maturity.")
    return GenTask(role="engineering_analyst", purpose=f"technical:{c['id']}",
                   system="You are the Engineering Analyst leading a technical review with the Product "
                          "Designer and the Materials and Manufacturing Specialist.",
                   prompt=prompt, schema=PLAN_SCHEMA, temperature=0.3, max_tokens=4000)


def run_technical(ctx: Ctx) -> dict:
    cp = ctx.checkpoint()
    done = set(cp.get("technical_done", []))
    todo = [c for c in shortlisted(ctx) if c["id"] not in done]
    hz = {c["id"]: detect_hazards(hazard_text(c)) for c in todo}
    tasks = [_technical_task(ctx, c, hz[c["id"]]) for c in todo]
    results = ctx.generate(tasks) if tasks else []
    out = {}
    for c, res in zip(todo, results if results is not None else [None] * len(todo)):
        hazards = hz[c["id"]]
        plan = res if res else {"maturity": "rough_concept", "note": "not performed: no model available"}
        if res:
            plan["maturity"] = "rough_concept" if plan.get("maturity") in ("prototype_tested", "validated_design") \
                and not ctx.db.query("learnings", "project_id=? AND kind='outcome'", (ctx.project_id,)) else plan["maturity"]
            plan_text = " ".join(plan.get("functional_principles") or []) + " " + \
                " ".join(plan.get("technical_requirements") or []) + " " + \
                " ".join(plan.get("safety_requirements") or []) + " " + \
                " ".join(f"{x.get('process')} {x.get('equipment')}" for x in plan.get("processes") or [])
            hazards = hazards + [h for h in detect_hazards(plan_text) if h["category"] not in
                                 {x["category"] for x in hazards}]
        arts = []
        if res:
            base = f"{ctx.project_id}/{c['id']}"
            arts.append(("plan", ctx.tools.call("write_workspace_file", {"relpath": f"{base}/technical_plan.json",
                         "text": json.dumps(plan, indent=2, ensure_ascii=False)}, "engineering_analyst", ctx.project_id,
                         ctx.job_id), "technical plan (concept stage)"))
            if plan.get("parts"):
                arts.append(("cad_openscad", ctx.tools.call("write_workspace_file", {"relpath": f"{base}/concept.scad",
                             "text": openscad(c["title"], plan["parts"])}, "product_designer", ctx.project_id,
                             ctx.job_id), "OpenSCAD concept geometry, not a validated drawing"))
            if plan.get("bom"):
                arts.append(("bom_csv", ctx.tools.call("write_workspace_file", {"relpath": f"{base}/bom.csv",
                             "text": bom_csv(plan["bom"])}, "materials_manufacturing", ctx.project_id, ctx.job_id),
                             "bill of materials with cost sources"))
        with ctx.db.tx():
            ctx.db.insert("technical_plans", {"project_id": ctx.project_id, "concept_id": c["id"], "plan": plan,
                                              "hazards": hazards, "maturity": plan.get("maturity"),
                                              "created_by": "engineering_analyst" if res else "system"})
            for kind, path, desc in arts:
                ctx.db.insert("artifacts", {"project_id": ctx.project_id, "concept_id": c["id"], "kind": kind,
                                            "path": path, "description": desc, "validated": 0})
            done.add(c["id"])
            ctx.save_checkpoint({**ctx.checkpoint(), "technical_done": sorted(done)})
        out[c["id"]] = {"maturity": plan.get("maturity"), "hazards": [h["category"] for h in hazards],
                        "artifacts": [a[0] for a in arts]}
    return {"plans": out, "model_used": ctx.has_model()}

def check_technical(ctx: Ctx, out: dict) -> tuple[bool, str]:
    n = ctx.db.scalar("SELECT COUNT(*) FROM technical_plans WHERE project_id=? AND created_by!='system'", (ctx.project_id,))
    return (bool(n), f"{n} technical plan(s)" if n else "no technical plan produced (no model)")


# ---------------------------------------------------------------- commercial

LINE = obj(["name", "amount", "source"], name=STR, amount=NUM,
           source={"type": "string", "enum": ["assumption", "observed", "quote"]}, ref=STR, note=STR, capex=BOOL)
ECON_SCHEMA = obj(
    ["price", "price_source", "materials", "founder_hours_per_unit", "units_per_month", "one_time", "monthly_fixed",
     "channel", "channel_commission_rate", "cac", "shipping", "packaging", "rationale"],
    price=NUM, price_source={"type": "string", "enum": ["assumption", "observed"]}, price_ref=STR,
    price_includes_tax=BOOL, tax_rate=NUM, materials=arr(LINE), hired_labour_hours=NUM, hired_labour_rate=NUM,
    founder_hours_per_unit=NUM, reject_rate=NUM, packaging=NUM, shipping=NUM, installation=NUM, aftercare_reserve=NUM,
    channel=STR, channel_commission_rate=NUM, payment_fee_rate=NUM, returns_rate=NUM, cac=NUM, units_per_customer=NUM,
    one_time=arr(LINE), monthly_fixed=arr(LINE), units_per_month=NUM, dev_weeks=NUM, lead_time_days=NUM,
    sales_cycle_days=NUM, batch_units=NUM, receivable_days=NUM, payable_days=NUM, inventory_days=NUM, rationale=STR,
)
PRICE_KINDS = {"price_observation"}
COST_KINDS = {"cost_observation", "price_observation", "supply_signal"}


def _verify_lines(lines: list[dict], valid: dict, kinds: set) -> list[Line]:
    out = []
    for l in lines:
        note = l.get("note", "")
        src = l.get("source", "assumption")
        ref = l.get("ref")
        if src in ("observed", "quote"):
            c = valid.get(ref or "")
            if not c or c["support"] != "verified_quote" or c["claim_type"] not in kinds:
                src = "assumption"
                note = (note + " (downgraded to assumption: reference not a verified claim)").strip()
        out.append(Line(name=l["name"], amount=float(l["amount"]), source=src, ref=ref, note=note,
                        capex=bool(l.get("capex"))))
    return out


def build_inputs(ctx: Ctx, data: dict, budget: float | None) -> EconInputs:
    valid = {c["id"]: c for c in ctx.db.query("claims", "project_id=?", (ctx.project_id,))}
    keys = {k for k in EconInputs.__dataclass_fields__}
    simple = {k: v for k, v in data.items() if k in keys and k not in ("materials", "one_time", "monthly_fixed")}
    inp = EconInputs(**simple)
    inp.materials = _verify_lines(data.get("materials", []), valid, COST_KINDS)
    inp.one_time = _verify_lines(data.get("one_time", []), valid, COST_KINDS)
    inp.monthly_fixed = _verify_lines(data.get("monthly_fixed", []), valid, COST_KINDS)
    pc = valid.get(data.get("price_ref") or "")
    if data.get("price_source") == "observed" and pc and pc["support"] == "verified_quote" and pc["claim_type"] in PRICE_KINDS:
        inp.price_source = "observed"
    else:
        inp.price_source = "assumption" if data.get("price_source") != "user" else "user"
    inp.founder_hourly_value = data.get("founder_hourly_value", ctx.settings.founder_hourly_value_inr)
    inp.budget = budget
    inp.notes = data.get("rationale", data.get("notes", ""))
    return inp


def econ_summary(e: dict) -> str:
    o = e["outputs"]
    cur = o["currency"]
    return (f"[{e['scenario']}] verdict {e['findings_verdict'] if 'findings_verdict' in e else ''} "
            f"price {money(o['price_to_buyer'], cur)}, net revenue/unit {money(o['net_revenue_per_unit'], cur)}, "
            f"contribution/unit (founder unpaid) {money(o['contribution_per_unit_founder_unpaid'], cur)}, "
            f"(founder paid) {money(o['contribution_per_unit_founder_paid'], cur)}, margin {o['contribution_margin_pct']}%, "
            f"monthly cash profit {money(o['monthly_cash_profit_steady'], cur)}, peak cash need {money(o['peak_cash_need'], cur)}, "
            f"first revenue ~{o['time_to_first_revenue_days']} days, founder {money(o['founder_effective_hourly'], cur)}/h")


def _econ_task(ctx: Ctx, c: dict, plan: dict) -> GenTask:
    price_claims = relevant_claims(ctx, c, types=("price_observation", "cost_observation", "market_size",
                                                   "buyer_behaviour", "competitor", "supply_signal"), limit=30)
    bom = plan.get("bom") or []
    prompt = (_concept_brief(c) + "\n\nBOM FROM TECHNICAL PLAN (INR):\n" +
              "\n".join(f"- {b['item']}: {b['qty']} {b['unit']} x {b['unit_cost_inr']} ({b['source']})" for b in bom)
              + "\n\nPRICE AND COST EVIDENCE (claim id: text):\n" +
              "\n".join(f"{x['id']}: {clip(x['text'], 220)}" for x in price_claims[:30])
              + f"\n\nBudget: {money(ctx.project.get('budget_inr'))}. Founder time value: "
                f"₹{ctx.settings.founder_hourly_value_inr:,.0f}/hour.\nBuild a realistic INR unit-economics model. "
                "Use 'observed' or 'quote' only with a claim id above that shows that number; everything else is "
                "'assumption'. Include labour hours, rejects, packaging, delivery, installation if any, channel "
                "commission, payment fees, returns, acquisition cost per customer, one-time design and tooling, "
                "monthly fixed costs, and a realistic sales volume. Prices are GST-inclusive unless stated. "
                "Do not make it look profitable on purpose.")
    return GenTask(role="commercial_analyst", purpose=f"economics:{c['id']}",
                   system="You are the Commercial Analyst. You build honest unit economics.",
                   prompt=prompt, schema=ECON_SCHEMA, temperature=0.2, max_tokens=3000)


def _store_econ(ctx: Ctx, c: dict, data: dict, source_of_inputs: str, plan_row: dict | None) -> dict:
    db = ctx.db
    from ..commercial.economics import Finding
    inp = build_inputs(ctx, data, ctx.project.get("budget_inr"))
    lvl, _ = demand_level(db, ctx.project_id, c["id"])
    scen = run_scenarios(inp)
    sens = sensitivity(inp)
    with db.tx():
        for name, sc in scen.items():
            si = EconInputs.from_dict(sc["inputs"])
            sc["findings"] += premium_checks(db, ctx.project_id, si, sc["outputs"], lvl,
                                             ctx.settings.premium_price_threshold_inr)
            sc["verdict"] = verdict([Finding(**f) for f in sc["findings"]])
            outputs = dict(sc["outputs"])
            if name == "base":
                orc = db.one("originality_checks", "concept_id=? ORDER BY created_at DESC", (c["id"],))
                outputs["sensitivity"] = sens
                outputs["what_it_would_take"] = what_it_would_take(si)
                outputs["business_model_fit"] = business_model_fit(
                    si, sc["outputs"], (orc or {}).get("verdict"), (plan_row or {}).get("hazards") or [], lvl)
            db.insert("economics", {"project_id": ctx.project_id, "concept_id": c["id"], "scenario": name,
                                    "inputs": sc["inputs"], "outputs": outputs,
                                    "findings": {"items": sc["findings"], "verdict": sc["verdict"],
                                                 "overrides": sc["overrides"]},
                                    "created_by": source_of_inputs})
    return {n: sc["verdict"] for n, sc in scen.items()}


def run_commercial(ctx: Ctx) -> dict:
    """Two batched rounds: economics for every concept, then the twelve questions for every concept."""
    db = ctx.db
    cp = ctx.checkpoint()
    econ_done = dict(cp.get("econ_done", {}))
    demand_done = set(cp.get("demand_done", []))
    user_inputs = (ctx.project.get("settings") or {}).get("economics") or {}
    concepts = shortlisted(ctx)
    plans = {c["id"]: db.one("technical_plans", "concept_id=? ORDER BY created_at DESC", (c["id"],)) for c in concepts}
    need_model, user_data = [], {}
    for c in concepts:
        if c["id"] in econ_done:
            continue
        data = user_inputs.get(c["id"]) or user_inputs.get(c["title"]) or (user_inputs if "price" in user_inputs else None)
        if data is not None:
            user_data[c["id"]] = data
        else:
            need_model.append(c)
    tasks = [_econ_task(ctx, c, (plans[c["id"]] or {}).get("plan") or {}) for c in need_model]
    results = ctx.generate(tasks) if tasks else []
    for c in concepts:
        if c["id"] in econ_done:
            continue
        if c["id"] in user_data:
            econ_done[c["id"]] = _store_econ(ctx, c, user_data[c["id"]], "user", plans[c["id"]])
        elif results:
            econ_done[c["id"]] = _store_econ(ctx, c, results[need_model.index(c)], "commercial_analyst", plans[c["id"]])
        else:
            econ_done[c["id"]] = {"status": "not performed: no model and no user-entered economics"}
        ctx.save_checkpoint({**ctx.checkpoint(), "econ_done": econ_done})
    todo = [c for c in concepts if c["id"] not in demand_done and "base" in econ_done.get(c["id"], {})]
    dtasks = [build_demand_task(ctx, c, "\n".join(f"{n}: {v}" for n, v in econ_done[c["id"]].items())) for c in todo]
    dres = ctx.generate(dtasks) if dtasks else []
    for c, r in zip(todo, dres if dres is not None else [None] * len(todo)):
        store_demand(ctx, c, r)
        demand_done.add(c["id"])
        ctx.save_checkpoint({**ctx.checkpoint(), "demand_done": sorted(demand_done)})
    return {"economics": econ_done}

def _norm_econ(row: dict | None) -> dict | None:
    if not row:
        return None
    f = row.get("findings") or {}
    return {"id": row["id"], "scenario": row["scenario"], "inputs": row["inputs"], "outputs": row["outputs"],
            "findings": f.get("items", []), "verdict": f.get("verdict")}


def full_state(ctx: Ctx, c: dict) -> dict:
    st = concept_state(ctx, c)
    st["econ"] = _norm_econ(st["econ"])
    st["econ_conservative"] = _norm_econ(st["econ_conservative"])
    st["econ_optimistic"] = _norm_econ(st["econ_optimistic"])
    return st


def check_commercial(ctx: Ctx, out: dict) -> tuple[bool, str]:
    n = sum(1 for v in out["economics"].values() if "base" in v)
    return (n > 0, f"economics for {n} concept(s)" if n else "no economics could be modelled")


# ---------------------------------------------------------------- critique


def _briefing(ctx: Ctx, c: dict, st: dict) -> str:
    parts = [_concept_brief(c), "", f"DEMAND EVIDENCE: level {st['demand_level']} ({st['demand_why']})"]
    for key in ("econ", "econ_conservative"):
        e = st.get(key)
        if e:
            o = e["outputs"]
            parts.append(f"ECONOMICS {e['scenario']}: verdict {e['verdict']}; price {money(o['price_to_buyer'])}; "
                         f"contribution/unit founder paid {money(o['contribution_per_unit_founder_paid'])}; "
                         f"monthly cash profit {money(o['monthly_cash_profit_steady'])}; peak cash "
                         f"{money(o['peak_cash_need'])}; findings: " + "; ".join(f["code"] for f in e["findings"]))
    orc = st.get("originality")
    if orc:
        parts.append(f"ORIGINALITY: {orc['verdict']} ({clip(orc['note'], 300)}); searched {orc['searched']}; "
                     f"unavailable {list((orc.get('unavailable') or {}).keys())}")
        for pa in ctx.db.query("prior_art", "concept_id=? ORDER BY similarity DESC LIMIT 3", (c["id"],)):
            s = ctx.db.get("sources", pa["source_id"])
            if s:
                parts.append(f"  prior art {s['id']} ({pa['similarity']}): {clip(s['title'], 120)}")
    parts.append("HAZARDS: " + (", ".join(h["category"] for h in st["hazards"]) or "none detected"))
    if st.get("plan"):
        parts.append(f"TECHNICAL MATURITY: {st['plan'].get('maturity')}")
    ans = ctx.db.query("demand_answers", "concept_id=?", (c["id"],))
    for a in ans:
        parts.append(f"Q {a['question_key']} (L{a['evidence_level']}): {clip(a['answer'], 160)}")
    return "\n".join(parts)


def run_critique(ctx: Ctx) -> dict:
    """Ask the model for every review first, then write rule and model objections together (safe to resume)."""
    from ..critique import CRITIC_QUESTIONS, CRITIC_SCHEMA, record_model_critique
    cp = ctx.checkpoint()
    done = set(cp.get("critique_done", []))
    todo = [c for c in shortlisted(ctx) if c["id"] not in done]
    states = {c["id"]: full_state(ctx, c) for c in todo}
    tasks = [GenTask(role="critical_reviewer", purpose=f"critique:{c['id']}",
                     system="You are the Critical Reviewer. Your job is to find what would make this fail.",
                     prompt=(f"CONCEPT UNDER REVIEW: {c['title']}\n{_briefing(ctx, c, states[c['id']])}\n\nAnswer these questions "
                             "as an independent critic. Each objection needs a basis: 'source' (give source_ids from the "
                             "briefing), 'calculation' (from the economics shown), or 'reasoning' (say so). Do not invent "
                             "facts. Do not object for show: if a point is strong, say so in strongest_point. If you "
                             "dispute another specialist's finding, name that role in disputes_role.\n"
                             + "\n".join(f"- {q}" for q in CRITIC_QUESTIONS)),
                     schema=CRITIC_SCHEMA, temperature=0.3, max_tokens=2500) for c in todo]
    results = ctx.generate(tasks) if tasks else []
    out = {}
    for c, mc in zip(todo, results if results is not None else [None] * len(todo)):
        st = states[c["id"]]
        ids = rule_critiques(ctx, c, st)
        if mc:
            record_model_critique(ctx, c, mc)
        structural_disagreements(ctx, c, st)
        with ctx.db.tx():
            done.add(c["id"])
            ctx.save_checkpoint({**ctx.checkpoint(), "critique_done": sorted(done)})
        out[c["id"]] = {"rule_objections": len(ids), "model_review": bool(mc),
                        "strongest_point": (mc or {}).get("strongest_point"),
                        "simpler_alternative": (mc or {}).get("simpler_alternative")}
    return {"reviews": out}

def check_critique(ctx: Ctx, out: dict) -> tuple[bool, str]:
    n = ctx.db.scalar("SELECT COUNT(*) FROM critiques WHERE project_id=?", (ctx.project_id,))
    return (True, f"{n} objections recorded")


# ---------------------------------------------------------------- validation

EXP_SCHEMA = obj(["experiments"], experiments=arr(obj(
    ["assumption", "hypothesis", "method", "cost_inr", "duration_days", "success_criteria", "failure_criteria",
     "evidence_level_target"], assumption=STR, hypothesis=STR, method=STR, cost_inr=NUM, duration_days=NUM,
    success_criteria=STR, failure_criteria=STR, evidence_level_target={"type": "integer", "minimum": 0, "maximum": 5},
    gated_actions=STRS), 0, 3))


def run_validation(ctx: Ctx) -> dict:
    cp = ctx.checkpoint()
    done = set(cp.get("validation_done", []))
    todo = [c for c in shortlisted(ctx) if c["id"] not in done]
    plans, tasks = {}, []
    for c in todo:
        st = full_state(ctx, c)
        sens = ((st.get("econ") or {}).get("outputs") or {}).get("sensitivity") or []
        flips = [r["input"] for r in sens[1:] if r.get("flips_verdict")]
        exps = experiment_templates(st, c, flips)
        weakest = [x["objection"] for x in ctx.db.query("critiques", "target_id=? AND severity IN ('fatal','major')",
                                                         (c["id"],))][:8]
        plans[c["id"]] = exps
        tasks.append(GenTask(role="experiment_designer", purpose=f"experiments:{c['id']}",
                             system="You are the Experiment Designer. You design the cheapest test that could change the decision.",
                             prompt=_concept_brief(c) + "\n\nMAJOR OBJECTIONS:\n" + "\n".join(f"- {w}" for w in weakest)
                             + f"\n\nInputs that flip the economics verdict: {flips or 'none'}\n\nAlready planned:\n"
                             + "\n".join(f"- {e['assumption']}" for e in exps)
                             + "\n\nAdd up to 3 further tests for important uncertainties not covered above. Costs in INR. "
                               "Any test that sends messages, publishes, buys, or spends must list those in gated_actions.",
                             schema=EXP_SCHEMA, temperature=0.4))
    results = ctx.generate(tasks) if tasks else []
    out = {}
    for c, res in zip(todo, results if results is not None else [None] * len(todo)):
        exps = plans[c["id"]]
        if res:
            for e in res["experiments"]:
                e.setdefault("gated_actions", [])
                exps.append(e)
        with ctx.db.tx():
            for e in exps:
                ctx.db.insert("experiments", {"project_id": ctx.project_id, "concept_id": c["id"], **e, "status": "planned",
                                              "created_by": "experiment_designer"})
            done.add(c["id"])
            ctx.save_checkpoint({**ctx.checkpoint(), "validation_done": sorted(done)})
        out[c["id"]] = len(exps)
    return {"experiments": out}

def check_validation(ctx: Ctx, out: dict) -> tuple[bool, str]:
    n = ctx.db.scalar("SELECT COUNT(*) FROM experiments WHERE project_id=?", (ctx.project_id,))
    return (n > 0, f"{n} experiments planned" if n else "no experiments planned")


# ---------------------------------------------------------------- decision

NARRATIVE_SCHEMA = obj(["summary", "reasons_against", "what_would_change_the_decision"], summary=STR,
                       reasons_against=STRS, what_would_change_the_decision=STRS)
VERDICT_ORDER = {"advance_to_prototype": 0, "validate_before_building": 1, "revise": 2, "reject": 3}


def run_decision(ctx: Ctx) -> dict:
    db = ctx.db
    concepts = shortlisted(ctx) if ctx.project.get("workflow") != "discovery" else []
    cycle = (ctx.project.get("settings") or {}).get("cycle", 0)
    if not concepts:
        return _opportunity_decision(ctx)
    # Compute every decision in memory, ask for the narrative, then write (safe to pause and resume).
    pending_rows, results = [], []
    for c in concepts:
        st = full_state(ctx, c)
        v, why = decide(st)
        g = gates(st)
        unresolved = [d["topic"] + ": " + clip(d["position_b"], 160) for d in
                      db.query("disagreements", "project_id=? AND status='unresolved' AND topic LIKE ?",
                               (ctx.project_id, c["title"] + "%"))]
        exps = db.query("experiments", "concept_id=? AND status='planned'", (c["id"],), "cost_inr")
        next_actions = [{"experiment_id": e["id"], "action": e["method"], "cost_inr": e["cost_inr"],
                         "target_level": e["evidence_level_target"], "needs_approval": e["gated_actions"]} for e in exps]
        wit = ((st.get("econ") or {}).get("outputs") or {}).get("what_it_would_take")
        if wit and st["econ"]["verdict"] in ("not_viable", "weak", "marginal"):
            parts = []
            if wit.get("price_needed"):
                parts.append(f"price of at least {money(wit['price_needed'])}")
            if wit.get("max_founder_hours_per_unit") is not None:
                parts.append(f"founder time of at most {wit['max_founder_hours_per_unit']} h per unit")
            if wit.get("max_material_cost_per_unit") is not None:
                parts.append(f"materials of at most {money(wit['max_material_cost_per_unit'])} per unit")
            next_actions.insert(0, {"action": "Commercially stronger direction: a "
                                    f"{wit['target_contribution_margin_pct']:.0f}% contribution margin needs one of: "
                                    + ("; ".join(parts) or "no single lever is enough")
                                    + ". If none is credible with evidence, change the business model (for example "
                                      "licensing the design, commissioned work, or a lower-labour production method)."})
        next_actions.append({"action": spend_limit(st["demand_level"], st.get("budget"))})
        pending_rows.append({"project_id": ctx.project_id, "concept_id": c["id"], "verdict": v, "rationale": why,
                             "gates": g, "unresolved": unresolved, "next_actions": next_actions,
                             "decided_by": "decision_director"})
        results.append({"concept_id": c["id"], "title": c["title"], "verdict": v, "why": why,
                        "monthly_cash_profit": ((st.get("econ") or {}).get("outputs") or {}).get("monthly_cash_profit_steady")})
    results.sort(key=lambda r: (VERDICT_ORDER[r["verdict"]], -(r["monthly_cash_profit"] or -1e12)))
    best = results[0]
    lines = "\n".join(f"- {r['title']}: {r['verdict']} ({r['why']})" for r in results)
    narr = ctx.generate([GenTask(role="decision_director", purpose=f"decision:c{cycle}",
                                 system="You are the Decision Director. Explain the decision plainly and do not soften it.",
                                 prompt=f"DECISIONS FROM EVIDENCE GATES:\n{lines}\n\nWrite a short summary, the strongest "
                                        "reasons against the leading option, and what evidence would change the decision. "
                                        "Do not add facts that are not above.", schema=NARRATIVE_SCHEMA, temperature=0.2)])
    with db.tx():
        for row, r in zip(pending_rows, results):
            r["decision_id"] = db.insert("decisions", row)
    revisit = None
    if all(r["verdict"] in ("revise", "reject") for r in results) and cycle < ctx.settings.max_revisits \
            and ctx.has_model() and ctx.project.get("workflow") in ("full", "invention"):
        revisit = "invention"
    overall = ("No concept is worth building yet. " if best["verdict"] in ("revise", "reject") else "") + \
        f"Leading option: {best['title']} ({best['verdict']})."
    return {"decisions": results, "overall": overall, "narrative": narr[0] if narr else None, "revisit": revisit}


def _opportunity_decision(ctx: Ctx) -> dict:
    db = ctx.db
    opps = db.query("opportunities", "project_id=? AND status IN ('ranked','selected')", (ctx.project_id,))
    if not opps:
        with db.tx():
            db.insert("decisions", {"project_id": ctx.project_id, "verdict": "insufficient_evidence",
                                    "rationale": "No opportunity is supported by verified evidence. Nothing is recommended.",
                                    "gates": [], "unresolved": [], "next_actions": [{"action": "Enable research access or "
                                    "supply sources, then rerun."}], "decided_by": "decision_director"})
        return {"decisions": [], "overall": "insufficient evidence; no recommendation", "revisit": None}
    results = []
    for o in opps[:3]:
        d = o.get("detail") or {}
        lvl, why = demand_level(db, ctx.project_id)
        with db.tx():
            did = db.insert("decisions", {
                "project_id": ctx.project_id, "verdict": "investigate", "rationale":
                f"{o['title']}: evidence {why}. Gap type: {d.get('why_gap_exists')}. Weakest assumption: "
                f"{d.get('weakest_assumption')}.", "gates": [{"gate": "demand", "status": "fail" if lvl < 2 else "partial",
                                                              "why": f"level {lvl}"}],
                "unresolved": [], "next_actions": [{"action": d.get("test_for_weakest_assumption") or "test the weakest assumption"}],
                "decided_by": "decision_director"})
        results.append({"decision_id": did, "title": o["title"], "verdict": "investigate"})
    return {"decisions": results, "overall": f"Investigate: {results[0]['title']}", "revisit": None}


def check_decision(ctx: Ctx, out: dict) -> tuple[bool, str]:
    return True, out.get("overall", "")


# ---------------------------------------------------------------- learning


def run_learning(ctx: Ctx) -> dict:
    db = ctx.db
    cp = ctx.checkpoint()
    if cp.get("learning_done"):
        return cp["learning_out"]
    n = 0
    with db.tx():
        for d in db.query("decisions", "project_id=?", (ctx.project_id,)):
            c = db.get("concepts", d["concept_id"]) if d.get("concept_id") else None
            kind = "failed_hypothesis" if d["verdict"] in ("reject", "revise") else "decision"
            db.insert("learnings", {"project_id": ctx.project_id, "kind": kind, "ref_type": "decision", "ref_id": d["id"],
                                    "text": f"{(c or {}).get('title', 'project')}: {d['verdict']} because {d['rationale']}",
                                    "data": {"gates": d["gates"]}, "created_by": "decision_director"})
            n += 1
        gaps = db.query("research_gaps", "project_id=?", (ctx.project_id,))
        if gaps:
            by = {}
            for g in gaps:
                by[g["connector"]] = g["reason"][:120]
            db.insert("learnings", {"project_id": ctx.project_id, "kind": "lesson", "ref_type": "research", "ref_id": None,
                                    "text": f"Research gaps in {len(by)} connector(s): " + "; ".join(f"{k}: {v}" for k, v in by.items()),
                                    "data": {"count": len(gaps)}, "created_by": "research_investigator"})
            n += 1
        unv = db.scalar("SELECT COUNT(*) FROM claims WHERE project_id=? AND support='source_unverified'", (ctx.project_id,))
        tot = db.scalar("SELECT COUNT(*) FROM claims WHERE project_id=? AND origin='model_extraction'", (ctx.project_id,))
        if tot:
            db.insert("learnings", {"project_id": ctx.project_id, "kind": "lesson", "ref_type": "model", "ref_id": None,
                                    "text": f"Model extraction: {unv} of {tot} quotes failed verification.",
                                    "data": {"unverified": unv, "total": tot}, "created_by": "research_investigator"})
            n += 1
        out = {"learnings_recorded": n}
        ctx.save_checkpoint({**ctx.checkpoint(), "learning_done": True, "learning_out": out})
    return out


STAGES = [
    Stage("technical", "Technical analysis", ["product_designer", "engineering_analyst", "materials_manufacturing"],
          "shortlisted concepts, technical evidence", "development plan, hazards, OpenSCAD concept CAD, BOM CSV",
          ["model", "write_workspace_file"], "maturity cannot exceed recorded test outcomes",
          "a plan per shortlisted concept", "no model: hazards only", run_technical, check_technical),
    Stage("commercial", "Commercial analysis", ["commercial_analyst", "buyer_researcher"],
          "shortlisted concepts, price/cost claims, BOM", "three scenarios, sensitivity, premium checks, fit, 12 answers",
          ["model", "economics calculator"], "observed numbers must reference verified claims",
          "economics for at least one concept", "no model and no user economics", run_commercial, check_commercial),
    Stage("critique", "Critical review", ["critical_reviewer"], "everything above",
          "rule objections, model objections, disagreements", ["rules", "model"],
          "objections citing nonexistent sources are downgraded to reasoning", "review recorded", "none",
          run_critique, check_critique),
    Stage("validation", "Validation plan", ["experiment_designer"], "objections, sensitivity flips",
          "experiments with costs, criteria, target evidence level, gated actions", ["templates", "model"],
          "gated actions need user approval", "at least one experiment", "none", run_validation, check_validation),
    Stage("decision", "Decision", ["decision_director"], "gates, objections, disagreements",
          "verdict per concept, unresolved disputes, next actions, spending limit", ["gates", "model"],
          "verdicts follow fixed gates", "decision recorded", "may send the cycle back to invention",
          run_decision, check_decision),
    Stage("learning", "Learning", ["decision_director"], "decisions, gaps, verification stats",
          "learning records", [], "records only this engine's own work", "records written", "none",
          run_learning, lambda ctx, out: (True, f"{out['learnings_recorded']} learning records")),
]
