"""Markdown report of a project, built only from stored records."""
from __future__ import annotations

from .db import DB
from .evidence import age_label, freshness, level_label
from .roles import title as role_title
from .util import clip, money


def _tbl(headers: list[str], rows: list[list]) -> list[str]:
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for r in rows:
        out.append("| " + " | ".join(str(x).replace("|", "/").replace("\n", " ") for x in r) + " |")
    return out


def _latest(rows: list[dict], key: str = "concept_id") -> list[dict]:
    """Keep the newest row per concept (rows must be ordered by created_at)."""
    out: dict = {}
    for r in rows:
        out[r.get(key) or r["id"]] = r
    return list(out.values())


def project_report(db: DB, pid: str) -> str:
    p = db.get("projects", pid)
    L: list[str] = [f"# {p['title']}", "", f"Question: {p['question']}", "",
                    f"Workflow: {p['workflow']} | Mode: {p['mode']} | Status: {p['status']} | Budget: {money(p['budget_inr'])}",
                    f"Project id: {p['id']} | Created: {p['created_at']}", ""]

    # provenance of generation
    ops = db.query("operator_tasks", "project_id=? AND status='answered'", (pid,))
    models = db.query("events", "project_id=? AND kind='model_request'", (pid,))
    L += ["## How this was produced", ""]
    provs = sorted({m["summary"].split(" via ")[-1] for m in models})
    distinct = len({m["summary"].split(" via ")[0] for m in models})
    L.append(f"- Distinct structured requests: {distinct} via {', '.join(provs) or 'none'} "
             f"({len(models)} request events; repeats after reruns were served from stored answers)")
    sup = db.query("jobs", "project_id=? AND status='superseded'", (pid,), "created_at")
    if sup:
        L.append(f"- {len(sup)} stage runs were superseded and rerun: " +
                 "; ".join(sorted({f"{j['stage']}: {clip(j['error'] or '', 120)}" for j in sup})))
    if ops:
        who = sorted({o['answered_by'] for o in ops})
        L.append(f"- {len(ops)} structured requests were answered through the operator queue by: {', '.join(who)}")
    gaps = db.query("research_gaps", "project_id=?", (pid,))
    if gaps:
        by = {}
        for g in gaps:
            by.setdefault(g["connector"], g["reason"])
        L.append("- Research connectors that could not be used: " + "; ".join(f"{k} ({clip(v, 80)})" for k, v in by.items()))
    L.append("")

    # framing
    q = db.one("jobs", "project_id=? AND stage='question' ORDER BY created_at DESC", (pid,))
    if q and q.get("output"):
        o = q["output"]
        L += ["## Framing", "", o.get("framing", ""), ""]
        if o.get("industries"):
            L += [f"Industries investigated (seed {o.get('seed')}): " + ", ".join(o["industries"]), ""]

    srcs = db.query("sources", "project_id=?", (pid,), "created_at")
    L += [f"## Research evidence ({len(srcs)} sources)", ""]
    if srcs:
        L += _tbl(["id", "title", "publisher", "type", "published", "retrieved", "method", "url"],
                  [[s["id"], clip(s["title"], 70), clip(s["publisher"] or "", 30), s["source_type"], s["published_at"] or "unknown",
                    (s["retrieved_at"] or "")[:10], s["retrieval_method"], s["url"]] for s in srcs])
    L.append("")
    claims = db.query("claims", "project_id=?", (pid,), "evidence_level DESC, created_at")
    if claims:
        L += [f"### Claims ({len(claims)})", ""]
        rows = []
        for c in claims:
            refs = db.conn.execute("SELECT source_id, verified FROM claim_sources WHERE claim_id=?", (c["id"],)).fetchall()
            src = db.get("sources", refs[0][0]) if refs else None
            fr = freshness(c["claim_type"], (src or {}).get("published_at"), (src or {}).get("retrieved_at"))
            rows.append([c["id"], c["claim_type"], clip(c["text"], 120), c["support"], f"L{c['evidence_level']}",
                         ", ".join(r[0] for r in refs) or "-", f"{fr[0]} ({age_label(fr[1])})", role_title(c["created_by"])])
        L += _tbl(["id", "type", "claim", "support", "level", "sources", "freshness", "by"], rows) + [""]
    con = db.query("contradictions", "project_id=?", (pid,))
    if con:
        L += ["### Contradictions", ""] + [f"- {c['metric']}: {c['note']} (claims {c['claim_a']} vs {c['claim_b']}, ratio {c['ratio']})" for c in con] + [""]

    opps = db.query("opportunities", "project_id=?", (pid,), "created_at")
    if opps:
        L += ["## Opportunities", ""]
        for o in opps:
            d = o.get("detail") or {}
            L += [f"### {o['title']} [{o['status']}]", f"- Industry: {o['industry']}", f"- Problem: {o['problem']}",
                  f"- Who: {o['who']}", f"- Evidence claims: {', '.join(o.get('claim_ids') or []) or 'none'}",
                  f"- Frequency and intensity: {d.get('frequency_intensity')}",
                  f"- Current alternatives: {d.get('current_alternatives')}",
                  f"- Why the gap exists: {d.get('why_gap_exists')} ({d.get('gap_explanation')})",
                  f"- Weakest assumption: {d.get('weakest_assumption')}",
                  f"- Test: {d.get('test_for_weakest_assumption')}", ""]

    concepts = db.query("concepts", "project_id=?", (pid,), "created_at")
    if concepts:
        L += [f"## Concepts ({len(concepts)})", ""]
        for c in concepts:
            d = c.get("detail") or {}
            ax = c.get("axes") or {}
            L += [f"### {c['title']} [{c['status']}{', family ' + c['family_id'] if c.get('family_id') else ''}]",
                  f"- Method: {c['method']} | by {role_title(c['created_by'])} | mode: {c['generation_mode']}",
                  f"- Core principle: {c['principle']}", f"- How it works: {d.get('how_it_works')}",
                  f"- Assumption challenged: {d.get('assumption_challenged')}", f"- Buyer: {d.get('target_buyer')}",
                  f"- Value: {c['user_value']}", f"- Business model: {c['business_model']}",
                  f"- Why different: {d.get('why_different')}", f"- Risks: {'; '.join(d.get('key_risks') or [])}",
                  f"- Axes: {', '.join(f'{k}={v}' for k, v in ax.items())}", ""]
        ovl = db.query("concept_overlaps", "project_id=?", (pid,))
        if ovl:
            L += ["### Overlap checks", ""] + _tbl(["a", "b", "similarity", "verdict", "reason"],
                                                   [[o["a_id"], o["b_id"], o["text_similarity"], o["verdict"], o["reason"]] for o in ovl]) + [""]
        orc = db.query("originality_checks", "project_id=?", (pid,))
        if orc:
            L += ["### Originality", ""]
            for o in orc:
                c = db.get("concepts", o["concept_id"])
                L.append(f"- {c['title']}: **{o['verdict']}**. {clip(o['note'], 400)}. Searched: {', '.join(o['searched'] or []) or 'nothing'}.")
                for pa in db.query("prior_art", "concept_id=? ORDER BY similarity DESC LIMIT 3", (o["concept_id"],)):
                    s = db.get("sources", pa["source_id"])
                    L.append(f"  - {pa['similarity']}: {clip(s['title'], 100)} ({s['url']})")
            L.append("")

    plans = _latest(db.query("technical_plans", "project_id=?", (pid,), "created_at"))
    if plans:
        L += ["## Technical analysis", ""]
        for t in plans:
            c = db.get("concepts", t["concept_id"])
            pl = t.get("plan") or {}
            L += [f"### {c['title']} (maturity: {t['maturity']})"]
            for h in t.get("hazards") or []:
                L.append(f"- HAZARD {h['category']}: {h['mandatory_review']}")
            for k in ("functional_principles", "technical_requirements", "construction_sequence", "failure_modes", "tests"):
                if pl.get(k):
                    L.append(f"- {k.replace('_', ' ').title()}: " + "; ".join(pl[k][:6]))
            for pr in pl.get("production_comparison") or []:
                L.append(f"  - {pr['method']}: {pr['fit']} ({clip(pr['notes'], 140)})")
            if pl.get("low_cost_validation"):
                L.append(f"- Low-cost validation: {pl['low_cost_validation']}")
            for a in db.query("artifacts", "concept_id=?", (t["concept_id"],)):
                L.append(f"- File: {a['kind']} at {a['path']} ({a['description']})")
            L.append("")

    econ = db.query("economics", "project_id=?", (pid,), "created_at")
    if econ:
        L += ["## Commercial analysis", ""]
        by_c: dict[str, list] = {}
        for e in econ:
            by_c.setdefault(e["concept_id"], []).append(e)
        for cid, rows in by_c.items():
            c = db.get("concepts", cid)
            L += [f"### {c['title']}", ""]
            keys = [("price_to_buyer", "Price to buyer (incl. tax)"), ("net_price_ex_tax", "Net price ex tax"),
                    ("net_revenue_per_unit", "Net revenue per unit"), ("materials_per_unit_incl_rejects", "Materials incl. rejects"),
                    ("founder_time_value_per_unit", "Founder time value per unit"), ("variable_cash_cost_per_unit", "Variable cash cost"),
                    ("contribution_per_unit_founder_unpaid", "Contribution (founder unpaid)"),
                    ("contribution_per_unit_founder_paid", "Contribution (founder paid)"), ("contribution_margin_pct", "Contribution margin %"),
                    ("monthly_cash_profit_steady", "Monthly cash profit"), ("monthly_accounting_profit_steady", "Monthly accounting profit"),
                    ("founder_effective_hourly", "Founder earnings per hour"), ("break_even_units_in_horizon", "Break-even units (12 mo)"),
                    ("peak_cash_need", "Peak cash need"), ("time_to_first_revenue_days", "Days to first revenue"),
                    ("capacity_units_per_month", "Capacity units/month")]
            sc = {r["scenario"]: r for r in rows}
            names = [n for n in ("conservative", "base", "optimistic") if n in sc]
            trows = []
            for k, label in keys:
                vals = []
                for n in names:
                    v = sc[n]["outputs"].get(k)
                    vals.append(money(v) if isinstance(v, (int, float)) and k not in ("contribution_margin_pct", "break_even_units_in_horizon",
                                                                                    "time_to_first_revenue_days", "capacity_units_per_month") else v)
                trows.append([label] + vals)
            trows.append(["Verdict"] + [(sc[n]["findings"] or {}).get("verdict") for n in names])
            L += _tbl(["INR"] + names, trows) + [""]
            base = sc.get("base")
            if base:
                inp = base["inputs"]
                L.append(f"Price source: {inp.get('price_source')} {('(' + inp['price_ref'] + ')') if inp.get('price_ref') else ''}. "
                         f"Tax: {inp.get('tax_rate')} ({inp.get('tax_note')}).")
                for l in inp.get("materials", []) + inp.get("one_time", []) + inp.get("monthly_fixed", []):
                    L.append(f"- {l['name']}: {money(l['amount'])} [{l['source']}{' ' + l['ref'] if l.get('ref') else ''}] {l.get('note', '')}")
                L += ["", "Findings (base):"] + [f"- {f['severity']} {f['code']}: {f['message']}" for f in (base["findings"] or {}).get("items", [])]
                sens = (base["outputs"] or {}).get("sensitivity") or []
                if len(sens) > 1:
                    L += ["", "Sensitivity (+/-20% on monthly cash profit):"]
                    L += [f"- {r['input']}: {money(r['profit_at_minus'])} to {money(r['profit_at_plus'])}"
                          f"{' (flips verdict)' if r['flips_verdict'] else ''}" for r in sens[1:6]]
                fit = (base["outputs"] or {}).get("business_model_fit") or []
                if fit:
                    L += ["", "Business model fit:"] + [f"- {r['question']} {r['answer']} ({r['basis']})" for r in fit]
            ans = db.query("demand_answers", "concept_id=?", (cid,))
            if ans:
                L += ["", "Twelve commercial questions:"] + [f"- {a['question_key']} [{level_label(a['evidence_level'])}]: {clip(a['answer'], 300)}"
                                                           + (f" (claims: {', '.join(a['claim_ids'])})" if a['claim_ids'] else "") for a in ans]
            L.append("")

    crit = db.query("critiques", "project_id=?", (pid,), "created_at")
    if crit:
        L += ["## Critical review", ""]
        for c in crit:
            tgt = db.get("concepts", c["target_id"])
            L.append(f"- [{c['severity']}] ({(tgt or {}).get('title', '')}, {c['category']}, basis: {c['basis']}"
                     f"{', ' + c['rule_id'] if c['rule_id'] else ''}) {c['objection']}"
                     + (f" Sources: {', '.join(c['source_ids'])}" if c.get('source_ids') else ""))
        L.append("")
    dis = db.query("disagreements", "project_id=?", (pid,))
    if dis:
        L += ["### Disagreements", ""] + [f"- {d['topic']} [{d['status']}]: {role_title(d['role_a'])} says '{clip(d['position_a'], 160)}'; "
                                         f"{role_title(d['role_b'])} says '{clip(d['position_b'], 200)}'" for d in dis] + [""]
    exps = db.query("experiments", "project_id=?", (pid,), "cost_inr")
    if exps:
        L += ["## Validation plan", ""]
        L += _tbl(["concept", "assumption", "test", "cost", "days", "success", "failure", "target", "needs approval"],
                  [[clip((db.get("concepts", e["concept_id"]) or {}).get("title", ""), 30), clip(e["assumption"], 60), clip(e["method"], 120),
                    money(e["cost_inr"]), e["duration_days"], clip(e["success_criteria"], 60), clip(e["failure_criteria"], 60),
                    f"L{e['evidence_level_target']}", ", ".join(e["gated_actions"] or []) or "-"] for e in exps]) + [""]
    decs = _latest(db.query("decisions", "project_id=?", (pid,), "created_at"))
    if decs:
        L += ["## Decision", ""]
        for d in decs:
            c = db.get("concepts", d["concept_id"]) if d.get("concept_id") else None
            L += [f"### {(c or {}).get('title', 'Project')}: **{d['verdict']}**", d["rationale"], ""]
            for g in d.get("gates") or []:
                L.append(f"- Gate {g['gate']}: {g['status']} ({g['why']})")
            for u in d.get("unresolved") or []:
                L.append(f"- Unresolved: {u}")
            for a in d.get("next_actions") or []:
                L.append(f"- Next: {a.get('action')}" + (f" ({money(a.get('cost_inr'))}, target L{a.get('target_level')})" if a.get('cost_inr') is not None else ""))
            L.append("")
    dj = db.one("jobs", "project_id=? AND stage='decision' ORDER BY created_at DESC", (pid,))
    if dj and (dj.get("output") or {}).get("narrative"):
        n = dj["output"]["narrative"]
        L += ["### Decision Director summary", "", n["summary"], "", "Reasons against:"] + [f"- {x}" for x in n["reasons_against"]] + \
             ["", "What would change the decision:"] + [f"- {x}" for x in n["what_would_change_the_decision"]] + [""]
    L += ["## Stage log", ""] + [f"- {j['stage']} (cycle {j['cycle']}): {j['status']}. {clip((j.get('output') or {}).get('_check', '') or j.get('error') or '', 200)}"
                                 for j in db.query("jobs", "project_id=?", (pid,), "created_at")]
    return "\n".join(L) + "\n"
