#!/usr/bin/env python3
"""Deterministic unit economics and cash model for the Financial Investigator.

Agents must not do business arithmetic in their heads. Same inputs, same answer.

A "unit" is whatever is sold once: a product, an order, a service visit, or one
month of a subscription. Say which in "unit_label".

Input JSON (all money in one currency; omit what does not apply):
{
  "currency": "INR", "unit_label": "per kit",
  "price": 2499, "price_includes_tax": true, "tax_rate": 0.18,
  "variable_costs": {"materials": 600, "packaging": 40, "shipping": 90},   # cash cost per unit sold
  "reject_rate": 0.05,                 # share of units scrapped; inflates variable cost and founder time
  "channel_fee_rate": 0.15,            # marketplace, distributor, or agent share of the ex-tax price
  "payment_fee_rate": 0.02,            # on the price paid by the buyer
  "returns_rate": 0.03, "return_cost_fraction": 0.5,   # share of ex-tax price lost per return
  "cac": 400, "orders_per_customer": 2,                 # acquisition cost spread over a customer's orders
  "founder_hours_per_unit": 0.5, "founder_hour_value": 750,
  "founder_hours_available_per_month": 160, "founder_fixed_hours_per_month": 40,
  "hired_cost_per_unit": 0,            # paid labour per unit, cash
  "fixed_monthly": {"workspace": 8000, "software": 1500},
  "one_time": {"tooling": 60000, "certification": 40000},
  "depreciable": ["tooling"],          # one_time items depreciated over depreciation_months
  "depreciation_months": 36,
  "units_per_month_at_scale": 120, "pre_revenue_months": 3, "ramp_months": 6,
  "inventory_months": 1.0,             # stock held ahead of sales, as months of sales
  "receivable_days": 0,
  "months": 24,
  "capital_available": 500000,
  "scenarios": {"conservative": {"units_per_month_at_scale": "*0.5", "ramp_months": 9},
                "optimistic": {"units_per_month_at_scale": "*1.3"}}
}
Scenario overrides replace values; "*0.5" multiplies, "+2" adds. Nested dicts override per key.

Usage: python3 tools/econ.py input.json [--json]
"""
from __future__ import annotations

import copy
import json
import math
import sys

DEFAULTS = {
    "currency": "INR", "unit_label": "per unit", "price": 0.0, "price_includes_tax": True, "tax_rate": 0.18,
    "variable_costs": {}, "reject_rate": 0.0, "channel_fee_rate": 0.0, "payment_fee_rate": 0.0,
    "returns_rate": 0.0, "return_cost_fraction": 0.5, "cac": 0.0, "orders_per_customer": 1.0,
    "founder_hours_per_unit": 0.0, "founder_hour_value": 750.0, "founder_hours_available_per_month": 160.0,
    "founder_fixed_hours_per_month": 40.0, "hired_cost_per_unit": 0.0, "fixed_monthly": {}, "one_time": {},
    "depreciable": [], "depreciation_months": 36, "units_per_month_at_scale": 0.0, "pre_revenue_months": 3,
    "ramp_months": 6, "inventory_months": 1.0, "receivable_days": 0, "months": 24, "capital_available": None,
}


def _apply(base, rule):
    if isinstance(rule, str) and rule[:1] in "*+":
        x = float(rule[1:])
        return base * x if rule[0] == "*" else base + x
    return rule


def merge(base: dict, over: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in over.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            for kk, vv in v.items():
                out[k][kk] = _apply(out[k].get(kk, 0.0), vv)
        else:
            out[k] = _apply(out.get(k, 0.0), v)
    return out


def model(p: dict) -> dict:
    keep = 1.0 - p["reject_rate"]
    gross = p["price"] if p["price_includes_tax"] else p["price"] * (1 + p["tax_rate"])
    net_price = gross / (1 + p["tax_rate"])
    channel = net_price * p["channel_fee_rate"]
    payment = gross * p["payment_fee_rate"]
    returns = p["returns_rate"] * net_price * p["return_cost_fraction"]
    net_revenue = net_price - channel - payment - returns
    variable = (sum(p["variable_costs"].values()) + p["hired_cost_per_unit"]) / keep
    acquisition = p["cac"] / max(p["orders_per_customer"], 1e-9)
    contribution = net_revenue - variable - acquisition
    f_hours_unit = p["founder_hours_per_unit"] / keep
    contribution_after_founder = contribution - f_hours_unit * p["founder_hour_value"]
    fixed = sum(p["fixed_monthly"].values())
    one_time = sum(p["one_time"].values())
    depreciation = sum(v for k, v in p["one_time"].items() if k in p["depreciable"]) / max(p["depreciation_months"], 1)

    spare = p["founder_hours_available_per_month"] - p["founder_fixed_hours_per_month"]
    capacity = spare / f_hours_unit if f_hours_unit > 0 else math.inf
    scale_units = min(p["units_per_month_at_scale"], capacity)

    def units(m: int) -> float:
        if m <= p["pre_revenue_months"]:
            return 0.0
        k = m - p["pre_revenue_months"]
        return min(scale_units, p["units_per_month_at_scale"] * min(1.0, k / max(p["ramp_months"], 1)))

    lag = math.ceil(p["receivable_days"] / 30) if p["receivable_days"] > 0 else 0
    cum, curve, inv_prev = -one_time, [{"month": 0, "units": 0, "cash": round(-one_time), "cumulative": round(-one_time)}], 0.0
    for m in range(1, p["months"] + 1):
        u = units(m)
        inv_now = p["inventory_months"] * units(m + 1) * variable
        cash_in = net_revenue * units(m - lag) if m - lag >= 1 else 0.0
        cash_out = fixed + variable * u + acquisition * u + (inv_now - inv_prev)
        inv_prev = inv_now
        cum += cash_in - cash_out
        curve.append({"month": m, "units": round(u, 1), "cash": round(cash_in - cash_out), "cumulative": round(cum)})
    low = min(c["cumulative"] for c in curve)
    low_m = min(curve, key=lambda c: c["cumulative"])["month"]
    payback = next((c["month"] for c in curve if c["month"] > low_m and c["cumulative"] >= 0), None)
    founder_hours = scale_units * f_hours_unit + p["founder_fixed_hours_per_month"]
    cash_profit = scale_units * contribution - fixed
    return {
        "price_paid_by_buyer": gross, "net_price_ex_tax": net_price, "tax_per_unit": gross - net_price,
        "channel_fee_per_unit": channel, "payment_fee_per_unit": payment, "returns_cost_per_unit": returns,
        "net_revenue_per_unit": net_revenue, "variable_cost_per_unit": variable, "acquisition_per_unit": acquisition,
        "contribution_per_unit": contribution, "contribution_margin_pct": 100 * contribution / net_price if net_price else 0,
        "founder_cost_per_unit": f_hours_unit * p["founder_hour_value"],
        "contribution_after_founder_per_unit": contribution_after_founder,
        "fixed_per_month": fixed, "one_time_total": one_time,
        "break_even_units_per_month": fixed / contribution if contribution > 0 else math.inf,
        "capacity_units_per_month": capacity, "units_per_month_used": scale_units,
        "steady_cash_profit_per_month": cash_profit,
        "steady_accounting_profit_per_month": cash_profit - depreciation,
        "steady_profit_after_founder_pay_per_month": cash_profit - founder_hours * p["founder_hour_value"],
        "founder_hours_per_month": founder_hours,
        "founder_earnings_per_hour": cash_profit / founder_hours if founder_hours else None,
        "peak_cash_needed": -low if low < 0 else 0.0, "month_of_lowest_cash": low_m, "payback_month": payback,
        "cumulative_cash_month_12": curve[min(12, p["months"])]["cumulative"],
        "cumulative_cash_end": curve[-1]["cumulative"], "curve": curve,
    }


def flags(p: dict, r: dict) -> list[str]:
    f = []
    if r["contribution_per_unit"] <= 0:
        f.append("FATAL: each sale loses money before fixed costs.")
    elif r["contribution_after_founder_per_unit"] <= 0:
        f.append("Each sale loses money once founder time is paid at the stated rate.")
    if 0 < r["contribution_margin_pct"] < 25:
        f.append(f"Thin contribution margin ({r['contribution_margin_pct']:.0f}% of ex-tax price).")
    if r["units_per_month_used"] < p["units_per_month_at_scale"]:
        f.append(f"Founder capacity caps sales at {r['capacity_units_per_month']:.1f} units a month.")
    if r["units_per_month_used"] < r["break_even_units_per_month"]:
        f.append("Planned volume never covers fixed costs.")
    if p["capital_available"] is not None and r["peak_cash_needed"] > p["capital_available"]:
        f.append(f"Peak cash need exceeds available capital ({p['capital_available']:,.0f}).")
    if r["payback_month"] is None:
        f.append(f"Cash does not pay back within {p['months']} months.")
    fe = r["founder_earnings_per_hour"]
    if fe is not None and fe < p["founder_hour_value"]:
        f.append(f"Founder earns {fe:,.0f} an hour, below the stated value of {p['founder_hour_value']:,.0f}.")
    mat = sum(p["variable_costs"].values())
    if mat and r["price_paid_by_buyer"] / mat > 4 and r["contribution_margin_pct"] < 35:
        f.append("Large markup over direct costs, yet a modest margin: channel, tax, acquisition, or labour absorb it.")
    return f


def fmt(v, cur):
    if v is None:
        return "never"
    if isinstance(v, float) and math.isinf(v):
        return "not reachable"
    if isinstance(v, (int, float)):
        return f"{cur} {v:,.0f}" if abs(v) >= 1 or v == 0 else f"{v:.2f}"
    return str(v)


ROWS = [
    ("price_paid_by_buyer", "Price paid by buyer", True), ("net_revenue_per_unit", "Net revenue per unit", True),
    ("variable_cost_per_unit", "Variable cost per unit", True), ("acquisition_per_unit", "Acquisition per unit", True),
    ("contribution_per_unit", "Contribution per unit", True), ("contribution_margin_pct", "Contribution margin %", False),
    ("contribution_after_founder_per_unit", "Contribution after founder time", True),
    ("fixed_per_month", "Fixed costs per month", True), ("break_even_units_per_month", "Break-even units per month", False),
    ("capacity_units_per_month", "Founder capacity units per month", False), ("units_per_month_used", "Units per month at scale", False),
    ("steady_cash_profit_per_month", "Cash profit per month at scale", True),
    ("steady_profit_after_founder_pay_per_month", "Profit after paying founder", True),
    ("founder_earnings_per_hour", "Founder earnings per hour", True), ("one_time_total", "One-time costs", True),
    ("peak_cash_needed", "Peak cash needed", True), ("payback_month", "Cash payback month", False),
    ("cumulative_cash_end", "Cumulative cash at end", True),
]


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    raw = json.loads(open(argv[0], encoding="utf-8").read())
    scen = raw.pop("scenarios", {})
    base = merge(DEFAULTS, raw)
    plans = {"base": base}
    for name, over in scen.items():
        plans[name] = merge(base, over)
    order = [n for n in ("conservative", "base", "optimistic") if n in plans] + [n for n in plans if n not in ("conservative", "base", "optimistic")]
    results = {n: model(plans[n]) for n in order}
    if "--json" in argv:
        print(json.dumps({n: {k: v for k, v in r.items()} for n, r in results.items()}, indent=2, default=str))
        return 0
    cur = base["currency"]
    print(f"Unit: {base['unit_label']}. Currency: {cur}. Founder time valued at {cur} {base['founder_hour_value']:,.0f}/h.\n")
    print("| Metric | " + " | ".join(order) + " |")
    print("|---|" + "---|" * len(order))
    for key, label, money in ROWS:
        vals = []
        for n in order:
            v = results[n][key]
            vals.append(fmt(v, cur) if money else ("not reachable" if isinstance(v, float) and math.isinf(v) else
                                                    (f"{v:.1f}" if isinstance(v, float) else str(v))))
        print(f"| {label} | " + " | ".join(vals) + " |")
    for n in order:
        fl = flags(plans[n], results[n])
        print(f"\nFlags ({n}):" + ("".join(f"\n- {x}" for x in fl) if fl else " none"))
    print("\nCash by quarter (base): " + ", ".join(f"m{c['month']}: {c['cumulative']:,}" for c in results["base"]["curve"] if c["month"] % 3 == 0))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
