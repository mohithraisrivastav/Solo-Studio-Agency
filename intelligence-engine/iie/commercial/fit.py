"""Premium-market checks and business model fit, computed from stored evidence and economics."""
from __future__ import annotations

from ..db import DB
from .economics import EconInputs


def premium_checks(db: DB, project_id: str, inp: EconInputs, out: dict, demand_lvl: int,
                   threshold: float = 200000.0) -> list[dict]:
    """Rules for high-price offers. Returns findings (severity, code, message)."""
    f: list[dict] = []
    if inp.currency != "INR" or inp.price < threshold:
        return f
    prices = db.query("claims", "project_id=? AND claim_type='price_observation' AND value IS NOT NULL AND "
                      "support='verified_quote' AND currency='INR'", (project_id,))
    comps = [p for p in prices if 0.5 * inp.price <= p["value"] <= 2 * inp.price]
    if len(comps) < 3:
        f.append({"severity": "major", "code": "FEW_COMPARABLES_AT_PRICE",
                  "message": f"Only {len(comps)} verified INR price observation(s) within 0.5x to 2x of the "
                             f"target ₹{inp.price:,.0f}. The price lacks market support."})
    units_year = out["units_per_month_used"] * 12
    if inp.price >= 400000 and units_year > 12:
        f.append({"severity": "major", "code": "NEEDS_MANY_HIGH_VALUE_BUYERS",
                  "message": f"The plan needs about {units_year:.0f} buyers a year at ₹{inp.price:,.0f}. That buyer "
                             "pool must be shown, not assumed."})
    if inp.channel_commission_rate < 0.3 and inp.cac < 0.05 * inp.price:
        f.append({"severity": "minor", "code": "CHANNEL_COST_LOW",
                  "message": "Galleries and design retailers commonly take a large share of retail price; "
                             "a low commission and low acquisition cost together look optimistic. Verify with "
                             "two real channel terms."})
    if inp.shipping + inp.installation + inp.aftercare_reserve == 0:
        f.append({"severity": "minor", "code": "DELIVERY_AFTERCARE_MISSING",
                  "message": "No delivery, installation, or aftercare cost is included for a high-value object."})
    if demand_lvl < 3:
        f.append({"severity": "major", "code": "NO_QUALIFIED_INTEREST_AT_PRICE",
                  "message": f"Demand evidence is level {demand_lvl}. No buyer has shown qualified interest at "
                             "this price. Treat the price as a hypothesis."})
    return f


def business_model_fit(inp: EconInputs, out: dict, originality_verdict: str | None, hazards: list[dict],
                       demand_lvl: int) -> list[dict]:
    """Structural questions about the business, answered from numbers where possible."""
    rows = []
    fh_share = (out["founder_hours_per_month"] / max(inp.founder_hours_available_per_month, 1)) * 100
    rows.append({"question": "Dependent on continuous founder labour?",
                 "answer": "yes" if inp.founder_hours_per_unit > 0 and inp.hired_labour_hours == 0 else "partly",
                 "basis": f"founder uses {fh_share:.0f}% of available monthly hours; "
                          f"{out['founder_hours_per_unit_incl_rejects']} h per unit"})
    rows.append({"question": "Capable of repeat production?",
                 "answer": "constrained" if out["capacity_bound"] else "yes within capacity",
                 "basis": f"capacity {out['capacity_units_per_month']} units/month vs expected {inp.units_per_month}"})
    cap_ratio = (out["peak_cash_need"] / inp.budget) if inp.budget else None
    rows.append({"question": "Capital intensive?",
                 "answer": "unknown (no budget set)" if cap_ratio is None else ("yes" if cap_ratio > 1 else "no"),
                 "basis": f"peak cash need {inp.currency} {out['peak_cash_need']:,.0f}"
                          + (f" = {cap_ratio:.1f}x budget" if cap_ratio is not None else "")})
    rows.append({"question": "Easy to imitate?",
                 "answer": {"close_match_found": "likely (close existing work found)",
                            "related_work_found": "possibly (related work exists)",
                            "no_close_match_in_searched_sources": "unclear; nothing close found in searched sources",
                            "not_checked": "unknown; not searched"}.get(originality_verdict or "not_checked", "unknown"),
                 "basis": f"originality verdict: {originality_verdict or 'not_checked'}"})
    acq_share = (out["acquisition_per_unit"] / out["net_price_ex_tax"] * 100) if out["net_price_ex_tax"] else 0
    rows.append({"question": "Difficult to distribute?",
                 "answer": "yes" if acq_share > 25 or inp.channel_commission_rate >= 0.4 else "moderate",
                 "basis": f"acquisition is {acq_share:.0f}% of net price; channel commission "
                          f"{inp.channel_commission_rate * 100:.0f}%"})
    inv_share = (out["batch_cost"] / inp.budget * 100) if inp.budget else None
    rows.append({"question": "High inventory risk?",
                 "answer": "unknown" if inv_share is None else ("yes" if inv_share > 30 else "low"),
                 "basis": f"first batch costs {inp.currency} {out['batch_cost']:,.0f}"})
    units_year = out["units_per_month_used"] * 12
    rows.append({"question": "Dependent on a very small buyer pool?",
                 "answer": "yes" if inp.price >= 200000 else "not necessarily",
                 "basis": f"{units_year:.0f} sales/year needed at {inp.currency} {inp.price:,.0f}"})
    rows.append({"question": "Exposed to regulatory or technical risk?",
                 "answer": "yes" if hazards else "no hazards detected in the description",
                 "basis": ", ".join(h["category"] for h in hazards) or "keyword scan found none"})
    rows.append({"question": "Demand proven?", "answer": f"level {demand_lvl}",
                 "basis": "direct buyer evidence recorded by the user" if demand_lvl >= 2 else "public/indirect only"})
    return rows
