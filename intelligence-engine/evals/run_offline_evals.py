"""Run the evaluation scenarios that need no model and no network, and write readable results.

Inputs marked as test assumptions are invented test inputs, not market data. Live-research
evaluations (1, 2, 4, 6, and the research half of 3) need a local model and research access;
see evals/RESULTS.md.

Usage: python evals/run_offline_evals.py
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

from conftest import LyingProvider  # noqa: E402  (test double that fabricates on purpose)
from iie.commercial.economics import EconInputs, Line, assess, compute, verdict  # noqa: E402
from iie.config import Settings  # noqa: E402
from iie.orchestrator import Engine  # noqa: E402
from iie.report import project_report  # noqa: E402

OUT = ROOT / "evals" / "results"
OUT.mkdir(parents=True, exist_ok=True)


def engine(provider=None) -> Engine:
    s = Settings(home=Path(tempfile.mkdtemp()) / "home")
    s.ensure_dirs()
    return Engine(s, provider=provider, offline=True)


def t3_premium_object() -> dict:
    """Premium collectible at ₹5 lakh with test-assumption inputs and no market research."""
    e = engine()
    concept = {"title": "Cast bronze and walnut kinetic table sculpture, edition of 12",
               "core_principle": "Balanced bronze arms on a walnut base turn slowly with air currents",
               "user_value": "a collectible kinetic object", "business_model": "edition_collectible",
               "target_buyer": "private collectors and design galleries",
               "axes": {"principle_class": "mechanical", "value_type": "status_meaning", "material_class": "mixed",
                        "business_model_class": "edition_collectible", "interaction_mode": "passive_object"}}
    econ = {"price": 500000, "price_source": "user", "materials": [
        {"name": "bronze casting (outsourced foundry)", "amount": 42000, "source": "assumption"},
        {"name": "walnut and finishing", "amount": 9000, "source": "assumption"},
        {"name": "bearings and fixings", "amount": 4000, "source": "assumption"}],
        "founder_hours_per_unit": 90, "units_per_month": 0.5, "channel_commission_rate": 0.4, "cac": 30000,
        "shipping": 15000, "packaging": 8000, "installation": 0, "aftercare_reserve": 5000, "reject_rate": 0.1,
        "one_time": [{"name": "pattern making and moulds", "amount": 120000, "source": "assumption", "capex": True},
                     {"name": "two prototype castings", "amount": 110000, "source": "assumption"},
                     {"name": "photography and catalogue", "amount": 40000, "source": "assumption"}],
        "monthly_fixed": [{"name": "studio share", "amount": 12000, "source": "assumption"}],
        "dev_weeks": 14, "lead_time_days": 45, "sales_cycle_days": 120, "batch_units": 2}
    pid = e.create_project("Is a ₹5 lakh collectible object credible?", "commercial", budget_inr=500000,
                           settings={"concept": concept, "economics": econ})
    e.run(pid)
    (OUT / "t3_premium_object_report.md").write_text(project_report(e.db, pid))
    base = e.db.one("economics", "project_id=? AND scenario='base'", (pid,))
    d = e.db.one("decisions", "project_id=?", (pid,))
    return {"verdict": d["verdict"], "economics": base["findings"]["verdict"],
            "codes": [f["code"] for f in base["findings"]["items"]], "rationale": d["rationale"]}


def t5_commercial_rejection() -> dict:
    e = engine()
    concept = {"title": "Hand-carved teak bluetooth speaker", "core_principle": "Carved resonant chamber",
               "user_value": "beautiful sound object", "business_model": "product_sale", "target_buyer": "design lovers"}
    econ = {"price": 6500, "price_source": "user", "materials": [{"name": "teak block", "amount": 1800, "source": "assumption"},
            {"name": "speaker module", "amount": 1400, "source": "assumption"}], "founder_hours_per_unit": 9,
            "units_per_month": 10, "channel_commission_rate": 0.3, "cac": 900, "shipping": 250, "packaging": 200,
            "one_time": [{"name": "carving jigs", "amount": 40000, "source": "assumption", "capex": True}],
            "monthly_fixed": [{"name": "workshop", "amount": 8000, "source": "assumption"}]}
    pid = e.create_project("Is this worth making?", "commercial", budget_inr=150000,
                           settings={"concept": concept, "economics": econ})
    e.run(pid)
    (OUT / "t5_commercial_rejection_report.md").write_text(project_report(e.db, pid))
    d = e.db.one("decisions", "project_id=?", (pid,))
    return {"verdict": d["verdict"], "rationale": d["rationale"], "stronger_direction": d["next_actions"][0]["action"]}


def t7_evidence_integrity() -> dict:
    e = engine(LyingProvider())
    pid = e.create_project("Find an overlooked opportunity", "full", budget_inr=200000,
                           settings={"industries": ["bicycles and urban mobility cycling"]})
    e.run(pid)

    def q(sql: str):
        return e.db.scalar(sql)

    return {"sources": q("SELECT COUNT(*) FROM sources"),
            "verified_claims": q("SELECT COUNT(*) FROM claims WHERE support='verified_quote'"),
            "claims_above_L0": q("SELECT COUNT(*) FROM claims WHERE evidence_level>0"),
            "fabricated_claims_kept_at_L0": q("SELECT COUNT(*) FROM claims WHERE support!='verified_quote'"),
            "unsupported_opportunities": q("SELECT COUNT(*) FROM opportunities WHERE status='unsupported'"),
            "direct_buyer_evidence": q("SELECT COUNT(*) FROM direct_evidence"),
            "research_gaps_recorded": q("SELECT COUNT(*) FROM research_gaps"),
            "decisions": [d["verdict"] for d in e.db.query("decisions", "project_id=?", (pid,))]}


def t10_business_reality() -> dict:
    inp = EconInputs(price=250000, materials=[Line("copper sheet", 6000), Line("stone base", 4000)],
                     founder_hours_per_unit=60, packaging=5000, shipping=9000, channel_commission_rate=0.35, cac=20000,
                     units_per_month=1, returns_rate=0.05, reject_rate=0.1, one_time=[Line("tooling", 80000, capex=True)],
                     monthly_fixed=[Line("studio", 10000)], budget=300000, sales_cycle_days=60)
    out = compute(inp)
    f = assess(out, inp)
    return {"price_to_material_ratio": out["price_to_material_ratio"],
            "material_share_of_unit_cost_pct": out["material_share_of_unit_cost_pct"],
            "contribution_founder_paid_inr": out["contribution_per_unit_founder_paid"],
            "founder_hourly_inr": out["founder_effective_hourly"], "peak_cash_need_inr": out["peak_cash_need"],
            "verdict": verdict(f), "findings": [x.code for x in f]}


if __name__ == "__main__":
    results = {"t3_premium_object (partial, no research)": t3_premium_object(),
               "t5_commercial_rejection": t5_commercial_rejection(),
               "t7_evidence_integrity": t7_evidence_integrity(),
               "t10_business_reality": t10_business_reality()}
    (OUT / "offline_evals.json").write_text(json.dumps(results, indent=2, ensure_ascii=False, default=str))
    print(json.dumps(results, indent=2, ensure_ascii=False, default=str))
