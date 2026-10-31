"""Unit economics, cash flow, scenarios, sensitivity, and economic findings.

All amounts carry a currency. Every input line records whether it is an
assumption, an observed listing, a supplier quote, or user-provided. The
calculations are deterministic and reproducible; the verdicts follow fixed rules
documented in ``assess``.
"""
from __future__ import annotations

import copy
import math
from dataclasses import asdict, dataclass, field
from typing import Any

SOURCES = ("assumption", "observed", "quote", "user", "calculated")


@dataclass
class Line:
    name: str
    amount: float
    source: str = "assumption"
    ref: str | None = None
    note: str = ""
    capex: bool = False  # equipment or tooling, depreciated in accounting profit


@dataclass
class EconInputs:
    currency: str = "INR"
    price: float = 0.0
    price_includes_tax: bool = True
    tax_rate: float = 0.18
    tax_note: str = "GST rate is an assumption; confirm the HSN code and current rate."
    price_source: str = "assumption"
    price_ref: str | None = None
    materials: list[Line] = field(default_factory=list)          # per unit
    hired_labour_hours: float = 0.0
    hired_labour_rate: float = 0.0
    founder_hours_per_unit: float = 0.0
    founder_hourly_value: float = 600.0
    reject_rate: float = 0.05
    packaging: float = 0.0
    shipping: float = 0.0
    installation: float = 0.0
    aftercare_reserve: float = 0.0
    channel_commission_rate: float = 0.0
    payment_fee_rate: float = 0.02
    returns_rate: float = 0.0
    return_loss_fraction: float = 0.5
    cac: float = 0.0
    units_per_customer: float = 1.0
    one_time: list[Line] = field(default_factory=list)
    monthly_fixed: list[Line] = field(default_factory=list)
    units_per_month: float = 0.0
    founder_hours_available_per_month: float = 140.0
    founder_overhead_hours_per_month: float = 30.0   # selling, admin, sourcing
    ramp_months: float = 3.0
    dev_weeks: float = 4.0
    lead_time_days: float = 14.0
    sales_cycle_days: float = 14.0
    batch_units: float = 0.0
    receivable_days: float = 0.0
    payable_days: float = 0.0
    inventory_days: float = 30.0
    equipment_life_months: float = 36.0
    horizon_months: int = 12
    budget: float | None = None
    notes: str = ""

    @classmethod
    def from_dict(cls, d: dict) -> "EconInputs":
        d = dict(d)
        for k in ("materials", "one_time", "monthly_fixed"):
            d[k] = [x if isinstance(x, Line) else Line(**x) for x in d.get(k, [])]
        known = {f for f in cls.__dataclass_fields__}
        return cls(**{k: v for k, v in d.items() if k in known})

    def to_dict(self) -> dict:
        return asdict(self)


def _sum(lines: list[Line]) -> float:
    return float(sum(l.amount for l in lines))


def compute(inp: EconInputs) -> dict[str, Any]:
    if not (0 <= inp.reject_rate < 0.95):
        raise ValueError("reject_rate must be between 0 and 0.95")
    yf = 1.0 / (1.0 - inp.reject_rate)
    net_price = inp.price / (1 + inp.tax_rate) if inp.price_includes_tax else inp.price
    gross_to_buyer = inp.price if inp.price_includes_tax else inp.price * (1 + inp.tax_rate)
    tax = gross_to_buyer - net_price
    commission = net_price * inp.channel_commission_rate
    payment_fee = gross_to_buyer * inp.payment_fee_rate
    returns_cost = inp.returns_rate * net_price * inp.return_loss_fraction
    net_revenue = net_price - commission - payment_fee - returns_cost

    materials = _sum(inp.materials) * yf
    hired_labour = inp.hired_labour_hours * inp.hired_labour_rate * yf
    founder_hours_unit = inp.founder_hours_per_unit * yf
    founder_value_unit = founder_hours_unit * inp.founder_hourly_value
    cogs_cash = materials + hired_labour + inp.packaging
    cogs_full = cogs_cash + founder_value_unit
    fulfilment = inp.shipping + inp.installation + inp.aftercare_reserve
    acquisition = inp.cac / max(inp.units_per_customer, 1e-9)
    variable_cash = cogs_cash + fulfilment + acquisition
    contribution_cash = net_revenue - variable_cash
    contribution_full = contribution_cash - founder_value_unit

    one_time_total = _sum(inp.one_time)
    capex = sum(l.amount for l in inp.one_time if l.capex)
    fixed = _sum(inp.monthly_fixed)

    prod_hours = max(inp.founder_hours_available_per_month - inp.founder_overhead_hours_per_month, 0)
    capacity = (prod_hours / founder_hours_unit) if founder_hours_unit > 0 else math.inf
    units = min(inp.units_per_month, capacity)
    capacity_bound = inp.units_per_month > capacity

    monthly_contribution = units * contribution_cash
    monthly_cash_profit = monthly_contribution - fixed
    depreciation = capex / max(inp.equipment_life_months, 1)
    monthly_accounting_profit = monthly_cash_profit - depreciation
    founder_hours_month = units * founder_hours_unit + inp.founder_overhead_hours_per_month
    monthly_economic_profit = monthly_accounting_profit - founder_hours_month * inp.founder_hourly_value
    founder_hourly = (monthly_cash_profit / founder_hours_month) if founder_hours_month > 0 else None

    ttfr_days = inp.dev_weeks * 7 + inp.lead_time_days + inp.sales_cycle_days
    first_sale_month = int(math.ceil(ttfr_days / 30.0))
    ccc_days = inp.inventory_days + inp.receivable_days - inp.payable_days
    daily_var_cost = units * variable_cash / 30.0
    working_capital = max(ccc_days, 0) * daily_var_cost
    batch_cost = inp.batch_units * cogs_cash

    # Month-by-month cash, with a linear sales ramp and receivable lag.
    lag = int(math.ceil(inp.receivable_days / 30.0)) if inp.receivable_days > 0 else 0
    cash, cum, curve = 0.0, 0.0, []
    units_sold_total = 0.0
    for m in range(inp.horizon_months + 1):
        out = fixed if m > 0 else 0.0
        if m == 0:
            out += one_time_total + batch_cost
        sell_m = 0.0
        if m >= first_sale_month and m > 0:
            ramp = min(1.0, (m - first_sale_month + 1) / max(inp.ramp_months, 1))
            sell_m = units * ramp
        units_sold_total += sell_m
        # production cost paid when sold (batch already paid up front)
        out += sell_m * variable_cash
        recv_m = m - lag
        rec = 0.0
        if recv_m >= first_sale_month and recv_m > 0:
            ramp_r = min(1.0, (recv_m - first_sale_month + 1) / max(inp.ramp_months, 1))
            rec = units * ramp_r * net_revenue
        cash = rec - out
        cum += cash
        curve.append({"month": m, "units_sold": round(sell_m, 2), "cash_in": round(rec), "cash_out": round(out),
                      "cumulative": round(cum)})
    min_cum = min(c["cumulative"] for c in curve)
    peak_cash_need = max(0.0, -min_cum) + working_capital
    min_month = min(curve, key=lambda c: c["cumulative"])["month"]
    payback_month = 0 if min_cum >= 0 else next(
        (c["month"] for c in curve if c["month"] > min_month and c["cumulative"] >= 0), None)

    be_units = ((one_time_total + fixed * inp.horizon_months) / contribution_cash) if contribution_cash > 0 else math.inf
    be_units_fixed_only = (fixed / contribution_cash) if contribution_cash > 0 else math.inf

    total_cost_unit = variable_cash + founder_value_unit + commission + payment_fee + returns_cost
    material_share = (materials / total_cost_unit) if total_cost_unit > 0 else 0.0

    lines = inp.materials + inp.one_time + inp.monthly_fixed
    n_assumed = sum(1 for l in lines if l.source == "assumption") + (inp.price_source == "assumption")
    assumption_share = n_assumed / max(1, len(lines) + 1)

    r = lambda x: (round(x, 2) if isinstance(x, (int, float)) and math.isfinite(x) else x)  # noqa: E731
    return {k: r(v) for k, v in {
        "currency": inp.currency,
        "price_to_buyer": gross_to_buyer, "net_price_ex_tax": net_price, "tax_per_unit": tax,
        "commission_per_unit": commission, "payment_fee_per_unit": payment_fee, "returns_cost_per_unit": returns_cost,
        "net_revenue_per_unit": net_revenue,
        "materials_per_unit_incl_rejects": materials, "hired_labour_per_unit": hired_labour,
        "founder_hours_per_unit_incl_rejects": founder_hours_unit, "founder_time_value_per_unit": founder_value_unit,
        "cogs_cash_per_unit": cogs_cash, "cogs_incl_founder_time": cogs_full,
        "fulfilment_per_unit": fulfilment, "acquisition_per_unit": acquisition,
        "variable_cash_cost_per_unit": variable_cash,
        "contribution_per_unit_founder_unpaid": contribution_cash,
        "contribution_per_unit_founder_paid": contribution_full,
        "gross_margin_pct": ((net_price - cogs_full) / net_price * 100) if net_price else None,
        "contribution_margin_pct": (contribution_full / net_price * 100) if net_price else None,
        "price_to_material_ratio": (gross_to_buyer / materials) if materials else None,
        "material_share_of_unit_cost_pct": material_share * 100,
        "one_time_costs": one_time_total, "capex": capex, "fixed_monthly": fixed,
        "capacity_units_per_month": capacity, "expected_units_per_month": inp.units_per_month,
        "units_per_month_used": units, "capacity_bound": capacity_bound,
        "monthly_cash_profit_steady": monthly_cash_profit, "monthly_accounting_profit_steady": monthly_accounting_profit,
        "monthly_economic_profit_steady": monthly_economic_profit,
        "founder_hours_per_month": founder_hours_month, "founder_effective_hourly": founder_hourly,
        "founder_hourly_value": inp.founder_hourly_value,
        "break_even_units_in_horizon": be_units, "units_per_month_to_cover_fixed": be_units_fixed_only,
        "units_sold_in_horizon": units_sold_total,
        "time_to_first_revenue_days": ttfr_days, "first_sale_month": first_sale_month,
        "cash_conversion_cycle_days": ccc_days, "working_capital_need": working_capital,
        "batch_cost": batch_cost, "peak_cash_need": peak_cash_need, "payback_month": payback_month,
        "horizon_months": inp.horizon_months, "assumption_share_pct": assumption_share * 100,
        "cash_curve": curve,
    }.items()}


@dataclass
class Finding:
    severity: str  # fatal | major | minor | info
    code: str
    message: str

    def to_dict(self) -> dict:
        return asdict(self)


def assess(out: dict, inp: EconInputs) -> list[Finding]:
    """Fixed rules. Each finding says why, using the computed numbers."""
    f: list[Finding] = []
    cur = inp.currency
    cc, cf = out["contribution_per_unit_founder_unpaid"], out["contribution_per_unit_founder_paid"]
    if cc <= 0:
        f.append(Finding("fatal", "LOSES_MONEY_PER_UNIT",
                         f"Each sale loses {cur} {abs(cc):,.0f} before fixed costs, even with the founder working free."))
    elif cf <= 0:
        f.append(Finding("major", "PROFIT_ONLY_IF_FOUNDER_UNPAID",
                         f"Positive only while founder time is free; at {cur} {inp.founder_hourly_value:,.0f}/h each unit "
                         f"loses {cur} {abs(cf):,.0f}."))
    cm = out.get("contribution_margin_pct")
    if cm is not None and 0 < cm < 20 and cc > 0:
        f.append(Finding("major", "THIN_MARGIN", f"Contribution margin is {cm:.0f}% of net price; small cost or price "
                         "shifts erase it."))
    if out["monthly_cash_profit_steady"] <= 0 and cc > 0:
        f.append(Finding("major", "NO_MONTHLY_PROFIT",
                         f"At {out['units_per_month_used']:.1f} units/month the business does not cover fixed costs "
                         f"({cur} {out['fixed_monthly']:,.0f}/month); needs {out['units_per_month_to_cover_fixed']} units/month."))
    if out["capacity_bound"]:
        f.append(Finding("major", "CAPACITY_LIMIT",
                         f"Founder time caps output at {out['capacity_units_per_month']:.1f} units/month, below the "
                         f"expected {inp.units_per_month:.1f}."))
    be = out["break_even_units_in_horizon"]
    if isinstance(be, (int, float)) and math.isfinite(be) and be > out["units_sold_in_horizon"] and cc > 0:
        f.append(Finding("major", "NO_BREAK_EVEN_IN_HORIZON",
                         f"Needs {be:.0f} units to recover setup and fixed costs in {inp.horizon_months} months; the plan "
                         f"sells about {out['units_sold_in_horizon']:.0f}."))
    if inp.budget is not None and out["peak_cash_need"] > inp.budget:
        sev = "fatal" if out["peak_cash_need"] > 2 * inp.budget else "major"
        f.append(Finding(sev, "CAPITAL_EXCEEDS_BUDGET",
                         f"Peak cash need {cur} {out['peak_cash_need']:,.0f} exceeds the budget {cur} {inp.budget:,.0f}."))
    fh = out.get("founder_effective_hourly")
    if fh is not None and fh < inp.founder_hourly_value and cc > 0:
        f.append(Finding("major", "BELOW_FOUNDER_VALUE",
                         f"Founder earns about {cur} {fh:,.0f}/hour, below the {cur} {inp.founder_hourly_value:,.0f}/hour "
                         "opportunity cost."))
    if out["time_to_first_revenue_days"] > 180:
        f.append(Finding("minor", "SLOW_TO_REVENUE", f"First revenue in about {out['time_to_first_revenue_days']:.0f} days."))
    ratio = out.get("price_to_material_ratio")
    if ratio and ratio >= 4 and out["material_share_of_unit_cost_pct"] < 40:
        f.append(Finding("info", "PRICE_MATERIAL_ILLUSION",
                         f"Price is {ratio:.1f}x material cost, but materials are only "
                         f"{out['material_share_of_unit_cost_pct']:.0f}% of the real unit cost (labour, channel, "
                         "delivery, acquisition, tax take the rest)."))
    if inp.price_source == "assumption":
        f.append(Finding("major", "PRICE_UNSUPPORTED", "The selling price is an assumption with no observed comparable, "
                         "quote, or buyer commitment behind it."))
    if out["assumption_share_pct"] > 60:
        f.append(Finding("info", "MOSTLY_ASSUMPTIONS",
                         f"{out['assumption_share_pct']:.0f}% of inputs are assumptions; treat results as a sketch."))
    return f


def verdict(findings: list[Finding]) -> str:
    sev = [x.severity for x in findings]
    if "fatal" in sev:
        return "not_viable"
    majors = sev.count("major")
    if majors >= 3:
        return "weak"
    if majors >= 1:
        return "marginal"
    return "viable_on_paper"


DEFAULT_SCENARIOS: dict[str, dict[str, Any]] = {
    "conservative": {"price": "*0.85", "units_per_month": "*0.5", "reject_rate": "*1.5", "cac": "*1.5",
                     "materials": "*1.15", "returns_rate": "+0.03", "lead_time_days": "*1.5",
                     "sales_cycle_days": "*2", "founder_hours_per_unit": "*1.25"},
    "base": {},
    "optimistic": {"price": "*1.05", "units_per_month": "*1.3", "reject_rate": "*0.7", "cac": "*0.7",
                   "materials": "*0.95", "sales_cycle_days": "*0.7", "founder_hours_per_unit": "*0.9"},
}


def _apply(value: float, rule: Any) -> float:
    if isinstance(rule, str) and rule[:1] in "*+":
        x = float(rule[1:])
        return value * x if rule[0] == "*" else value + x
    return float(rule)


def apply_overrides(inp: EconInputs, overrides: dict[str, Any]) -> EconInputs:
    new = copy.deepcopy(inp)
    for k, rule in overrides.items():
        if k == "materials":
            for l in new.materials:
                l.amount = _apply(l.amount, rule)
        elif hasattr(new, k):
            val = _apply(getattr(new, k), rule)
            if k == "reject_rate":
                val = min(val, 0.6)
            setattr(new, k, val)
    return new


def run_scenarios(inp: EconInputs, scenarios: dict[str, dict] | None = None) -> dict[str, dict]:
    res = {}
    for name, ov in (scenarios or DEFAULT_SCENARIOS).items():
        si = apply_overrides(inp, ov)
        out = compute(si)
        fnd = assess(out, si)
        res[name] = {"overrides": ov, "inputs": si.to_dict(), "outputs": out,
                     "findings": [x.to_dict() for x in fnd], "verdict": verdict(fnd)}
    return res


SENSITIVE_FIELDS = ["price", "materials", "founder_hours_per_unit", "units_per_month", "cac",
                    "channel_commission_rate", "shipping", "reject_rate"]


def sensitivity(inp: EconInputs, delta: float = 0.2) -> list[dict]:
    """Effect of +/- delta on monthly cash profit, and whether the verdict flips."""
    base_out = compute(inp)
    base_v = verdict(assess(base_out, inp))
    base_p = base_out["monthly_cash_profit_steady"]
    rows = []
    for k in SENSITIVE_FIELDS:
        lo = apply_overrides(inp, {k: f"*{1 - delta}"})
        hi = apply_overrides(inp, {k: f"*{1 + delta}"})
        olo, ohi = compute(lo), compute(hi)
        vlo, vhi = verdict(assess(olo, lo)), verdict(assess(ohi, hi))
        rows.append({
            "input": k, "profit_at_minus": olo["monthly_cash_profit_steady"],
            "profit_at_plus": ohi["monthly_cash_profit_steady"],
            "swing": round(abs(ohi["monthly_cash_profit_steady"] - olo["monthly_cash_profit_steady"]), 2),
            "verdict_minus": vlo, "verdict_plus": vhi, "flips_verdict": (vlo != base_v or vhi != base_v),
        })
    rows.sort(key=lambda r: -r["swing"])
    return [{"base_monthly_cash_profit": base_p, "base_verdict": base_v}] + rows


def _bisect(fn, lo: float, hi: float, increasing: bool, iters: int = 60) -> float | None:
    """Smallest (increasing fn) or largest (decreasing fn) x in [lo, hi] with fn(x) >= 0."""
    flo, fhi = fn(lo), fn(hi)
    if increasing:
        if fhi < 0:
            return None
        if flo >= 0:
            return lo
    else:
        if flo < 0:
            return None
        if fhi >= 0:
            return hi
    for _ in range(iters):
        mid = (lo + hi) / 2
        ok = fn(mid) >= 0
        if increasing:
            hi, lo = (mid, lo) if ok else (hi, mid)
        else:
            lo, hi = (mid, hi) if ok else (lo, mid)
    return hi if increasing else lo


def what_it_would_take(inp: EconInputs, target_margin: float = 0.25) -> dict:
    """Numbers a commercially stronger version would need (each solved alone, others unchanged)."""
    def margin_gap(o: dict) -> float:
        return o["contribution_per_unit_founder_paid"] - target_margin * o["net_price_ex_tax"]

    base = compute(inp)
    price = _bisect(lambda p: margin_gap(compute(apply_overrides(inp, {"price": p}))),
                    max(inp.price, 1.0), max(inp.price, 1.0) * 30, increasing=True)
    hours = None
    if inp.founder_hours_per_unit > 0:
        hours = _bisect(lambda h: margin_gap(compute(apply_overrides(inp, {"founder_hours_per_unit": h}))),
                        0.0, inp.founder_hours_per_unit, increasing=False)
    mats_total = _sum(inp.materials)
    mat_scale = None
    if mats_total > 0:
        mat_scale = _bisect(lambda s: margin_gap(compute(apply_overrides(inp, {"materials": f"*{s}"}))),
                            0.0, 1.0, increasing=False)
    return {
        "target_contribution_margin_pct": target_margin * 100,
        "current_contribution_margin_pct": base["contribution_margin_pct"],
        "price_needed": round(price, 0) if price else None,
        "max_founder_hours_per_unit": round(hours, 2) if hours is not None else None,
        "max_material_cost_per_unit": round(mats_total * mat_scale, 0) if mat_scale is not None else None,
        "units_per_month_to_cover_fixed": base["units_per_month_to_cover_fixed"],
        "currency": inp.currency,
    }
