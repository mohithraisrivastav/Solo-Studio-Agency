"""Test 10 (business reality) and Test 5 (commercial rejection), plus core economics checks.

Inputs here are test assumptions, not market data.
"""
import math

from iie.commercial.economics import EconInputs, Line, assess, compute, run_scenarios, sensitivity, verdict, what_it_would_take
from iie.orchestrator import Engine


def luxury_object(**kw) -> EconInputs:
    base = dict(price=500000, materials=[Line("brass sheet", 14000), Line("walnut", 8000), Line("hardware", 3000)],
                founder_hours_per_unit=110, founder_hourly_value=800, reject_rate=0.1, packaging=7000, shipping=15000,
                installation=6000, aftercare_reserve=5000, channel_commission_rate=0.4, payment_fee_rate=0.02,
                returns_rate=0.02, cac=35000, units_per_month=0.5, budget=400000,
                one_time=[Line("jigs and tooling", 120000, capex=True), Line("prototype rounds", 90000)],
                monthly_fixed=[Line("studio share", 12000)], dev_weeks=10, sales_cycle_days=90)
    base.update(kw)
    return EconInputs(**base)


def test_high_price_low_material_is_not_called_profitable_by_markup():
    inp = luxury_object()
    out = compute(inp)
    assert out["price_to_material_ratio"] > 15  # looks like a huge markup
    codes = {f.code for f in assess(out, inp)}
    # the engine looks past the markup
    assert "PRICE_MATERIAL_ILLUSION" in codes
    assert out["material_share_of_unit_cost_pct"] < 15
    assert out["founder_time_value_per_unit"] > out["materials_per_unit_incl_rejects"]
    assert out["commission_per_unit"] > 100000  # channel takes a large share
    assert out["tax_per_unit"] > 70000  # GST inclusive price
    assert out["time_to_first_revenue_days"] > 150
    assert out["capacity_units_per_month"] < 1.2
    assert verdict(assess(out, inp)) != "viable_on_paper"


def test_cash_profit_differs_from_accounting_and_economic_profit():
    out = compute(luxury_object())
    assert out["monthly_accounting_profit_steady"] < out["monthly_cash_profit_steady"]  # depreciation
    assert out["monthly_economic_profit_steady"] < out["monthly_accounting_profit_steady"]  # founder time


def test_returns_rejects_and_volume_change_the_answer():
    a = compute(luxury_object())
    b = compute(luxury_object(returns_rate=0.15, reject_rate=0.3))
    assert b["net_revenue_per_unit"] < a["net_revenue_per_unit"]
    assert b["materials_per_unit_incl_rejects"] > a["materials_per_unit_incl_rejects"]
    low = compute(luxury_object(units_per_month=0.1))
    assert low["break_even_units_in_horizon"] > low["units_sold_in_horizon"]


def test_scenarios_and_sensitivity_are_explicit():
    sc = run_scenarios(luxury_object())
    assert set(sc) == {"conservative", "base", "optimistic"}
    assert sc["conservative"]["overrides"]["units_per_month"] == "*0.5"
    assert sc["conservative"]["outputs"]["monthly_cash_profit_steady"] < sc["optimistic"]["outputs"]["monthly_cash_profit_steady"]
    sens = sensitivity(luxury_object())
    assert sens[0]["base_verdict"]
    assert {r["input"] for r in sens[1:]} >= {"price", "units_per_month", "cac"}


def test_capital_and_loss_making_rules():
    loss = EconInputs(price=1000, materials=[Line("m", 900)], shipping=150, units_per_month=50)
    codes = {f.code for f in assess(compute(loss), loss)}
    assert "LOSES_MONEY_PER_UNIT" in codes and verdict(assess(compute(loss), loss)) == "not_viable"
    big = luxury_object(budget=50000)
    codes = {f.code: f.severity for f in assess(compute(big), big)}
    assert codes["CAPITAL_EXCEEDS_BUDGET"] == "fatal"


def test_currency_on_every_output():
    out = compute(luxury_object())
    assert out["currency"] == "INR"


def test_what_it_would_take_points_to_a_stronger_direction():
    w = what_it_would_take(luxury_object())
    assert w["price_needed"] and w["price_needed"] > 500000
    assert w["max_founder_hours_per_unit"] is None or w["max_founder_hours_per_unit"] < 110


def test_commercial_rejection_of_attractive_concept(settings):
    """Test 5: a beautiful concept with weak economics is rejected with reasons and a stronger direction."""
    concept = {"title": "Hand-carved teak bluetooth speaker", "core_principle": "Carved resonant chamber",
               "user_value": "beautiful sound object", "business_model": "product_sale", "target_buyer": "design lovers"}
    econ = {"price": 6500, "price_source": "user", "materials": [{"name": "teak block", "amount": 1800, "source": "assumption"},
            {"name": "speaker module", "amount": 1400, "source": "assumption"}], "founder_hours_per_unit": 9,
            "units_per_month": 10, "channel_commission_rate": 0.3, "cac": 900, "shipping": 250, "packaging": 200,
            "one_time": [{"name": "carving jigs", "amount": 40000, "source": "assumption", "capex": True}],
            "monthly_fixed": [{"name": "workshop", "amount": 8000, "source": "assumption"}]}
    e = Engine(settings, offline=True)
    pid = e.create_project("Is this worth making?", "commercial", budget_inr=150000,
                           settings={"concept": concept, "economics": econ})
    assert e.run(pid)["status"] == "complete"
    d = e.db.one("decisions", "project_id=?", (pid,))
    assert d["verdict"] == "reject", d["rationale"]
    assert "lose" in d["rationale"].lower() or "fail" in d["rationale"].lower()
    actions = " ".join(a["action"] for a in d["next_actions"])
    assert "Commercially stronger direction" in actions and "price of at least" in actions
    hz = e.db.one("technical_plans", "project_id=?", (pid,))
    crit = " ".join(c["objection"] for c in e.db.query("critiques", "project_id=?", (pid,)))
    assert "LOSES_MONEY_PER_UNIT" in " ".join(c["rule_id"] or "" for c in e.db.query("critiques", "project_id=?", (pid,)))
    assert "electrical" in crit  # bluetooth speaker flags an electrical review even without a model
    assert hz is None
    assert math.isfinite(e.db.one("economics", "project_id=? AND scenario='base'", (pid,))["outputs"]["peak_cash_need"])
