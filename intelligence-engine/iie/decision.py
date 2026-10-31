"""Evidence gates, decisions, spending limits, and experiment templates."""
from __future__ import annotations

# Maximum share of the budget that should be spent before reaching each demand level.
SPEND_GATES = {0: 0.05, 1: 0.05, 2: 0.15, 3: 0.40, 4: 1.0, 5: 1.0}


def spend_limit(level: int, budget: float | None) -> str:
    if not budget:
        return "Set a budget to get a spending limit."
    share = SPEND_GATES.get(level, 0.05)
    return (f"At demand level {level}, spend at most ₹{budget * share:,.0f} ({share * 100:.0f}% of the "
            f"₹{budget:,.0f} budget) until the next level is reached.")


def gates(state: dict) -> list[dict]:
    g = []
    orc = state.get("originality")
    if not orc or orc["verdict"] == "not_checked":
        g.append({"gate": "originality", "status": "unknown", "why": "existing solutions not searched"})
    elif orc["verdict"] == "close_match_found":
        g.append({"gate": "originality", "status": "fail", "why": orc["note"][:200]})
    else:
        g.append({"gate": "originality", "status": "pass", "why": orc["verdict"].replace("_", " ")})
    lvl = state.get("demand_level", 0)
    g.append({"gate": "demand", "status": "pass" if lvl >= 3 else ("partial" if lvl == 2 else "fail"),
              "why": f"demand evidence level {lvl}"})
    econ, cons = state.get("econ"), state.get("econ_conservative")
    if not econ:
        g.append({"gate": "economics", "status": "unknown", "why": "no economics model"})
    else:
        st = {"viable_on_paper": "pass", "marginal": "partial", "weak": "fail", "not_viable": "fail"}[econ["verdict"]]
        why = f"base: {econ['verdict']}" + (f", conservative: {cons['verdict']}" if cons else "")
        g.append({"gate": "economics", "status": st, "why": why})
        peak = econ["outputs"]["peak_cash_need"]
        budget = state.get("budget")
        if budget:
            g.append({"gate": "capital", "status": "pass" if peak <= budget else "fail",
                      "why": f"peak cash need ₹{peak:,.0f} vs budget ₹{budget:,.0f}"})
    hz = state.get("hazards") or []
    g.append({"gate": "safety", "status": "review_required" if hz else "pass",
              "why": ", ".join(h["category"] for h in hz) or "no hazards detected"})
    return g


def decide(state: dict) -> tuple[str, str]:
    """Return (verdict, rationale). Verdicts: reject, revise, validate_before_building, advance_to_prototype."""
    gs = {g["gate"]: g for g in gates(state)}
    econ = state.get("econ")
    cons = state.get("econ_conservative")
    reasons = []
    if econ and econ["verdict"] == "not_viable":
        fat = [f["message"] for f in econ["findings"] if f["severity"] == "fatal"]
        return "reject", "Base-case economics fail: " + "; ".join(fat)
    if econ and econ["verdict"] == "weak" and cons and cons["verdict"] == "not_viable":
        return "reject", "Economics are weak in the base case and fail in the conservative case."
    if gs["originality"]["status"] == "fail":
        return "revise", "Close existing work found; the concept needs a meaningful difference or should be dropped. " + gs["originality"]["why"]
    if gs.get("capital", {}).get("status") == "fail":
        reasons.append("capital need exceeds budget")
    if econ and econ["verdict"] == "weak":
        reasons.append("base-case economics are weak")
    if reasons:
        return "revise", "Revise before validation: " + "; ".join(reasons) + "."
    lvl = state.get("demand_level", 0)
    if lvl < 3:
        why = f"Demand is at level {lvl}. Run the cheap tests below before building or buying anything."
        if not econ:
            why += " Economics are not modelled yet."
        return "validate_before_building", why
    if gs["economics"]["status"] in ("pass", "partial"):
        return "advance_to_prototype", "Qualified demand exists and economics hold on stated inputs."
    return "revise", "Demand is shown but economics are unknown or weak."


def experiment_templates(state: dict, concept: dict, flips: list[str]) -> list[dict]:
    """Cheap tests aimed at the assumptions that would change the decision."""
    lvl = state.get("demand_level", 0)
    econ = state.get("econ")
    price = econ["inputs"]["price"] if econ else None
    title = concept["title"]
    out = []
    if lvl <= 1:
        out.append({"assumption": "The target buyer has this problem and pays to solve it today",
                    "hypothesis": f"At least 6 of 10 target buyers describe the problem unprompted and name what they spend on it.",
                    "method": "10 problem interviews (no pitch) with people matching the target buyer; record each one "
                              "with name/company, date, and current spend.",
                    "cost_inr": 2000, "duration_days": 14,
                    "success_criteria": "6+ of 10 confirm the problem and a current spend",
                    "failure_criteria": "3 or fewer confirm it", "evidence_level_target": 2, "gated_actions": []})
    if lvl <= 2:
        out.append({"assumption": "Buyers will commit at the proposed price",
                    "hypothesis": f"At least 2 of 15 qualified prospects place a refundable deposit for '{title}'"
                                  + (f" at ₹{price:,.0f}" if price else "") + ".",
                    "method": "Deposit-backed pre-order offer to qualified prospects from the interviews; refundable "
                              "if not delivered. Messages and any page need user approval before sending or publishing.",
                    "cost_inr": 5000, "duration_days": 21, "success_criteria": "2+ deposits",
                    "failure_criteria": "0 deposits after 15 qualified conversations", "evidence_level_target": 4,
                    "gated_actions": ["send_message", "publish"]})
    if econ:
        assumed = [m["name"] for m in econ["inputs"].get("materials", []) if m.get("source") == "assumption"
                   and not any(w in m["name"].lower() for w in ("travel", "consumable", "report"))]
        if assumed:
            out.append({"assumption": "Material and production costs are as modelled",
                        "hypothesis": "Written quotes for the largest cost items fall within 15% of the model.",
                        "method": f"Request 3 written quotes each for: {', '.join(assumed[:4])}.",
                        "cost_inr": 0, "duration_days": 10, "success_criteria": "quotes within 15% of model",
                        "failure_criteria": "quotes over 30% higher", "evidence_level_target": 1,
                        "gated_actions": ["send_message"]})
    if "units_per_month" in flips or "cac" in flips:
        out.append({"assumption": "Buyers can be reached at the modelled acquisition cost",
                    "hypothesis": "A small channel test produces qualified leads at or below the modelled cost per sale.",
                    "method": "Run one channel test (partner outreach, marketplace listing, or a capped paid test).",
                    "cost_inr": 8000, "duration_days": 21, "success_criteria": "cost per qualified lead within model",
                    "failure_criteria": "cost per lead over 2x model", "evidence_level_target": 2,
                    "gated_actions": ["spend_money", "publish"]})
    mode = (concept.get("axes") or {}).get("interaction_mode")
    if (state.get("hazards") or state.get("plan")) and mode not in ("service_delivered", "software"):
        out.append({"assumption": "The core principle works at prototype scale",
                    "hypothesis": "A bench prototype meets the main technical requirement.",
                    "method": "Build the smallest prototype that tests the core principle only; follow the safety "
                              "review list before any user handles it.",
                    "cost_inr": 15000, "duration_days": 21, "success_criteria": "meets the stated requirement",
                    "failure_criteria": "fails requirement after two iterations", "evidence_level_target": 1,
                    "gated_actions": ["purchase"]})
    orc = state.get("originality")
    if not orc or orc["verdict"] in ("not_checked",) or (orc.get("unavailable") and "patentsview" in orc["unavailable"]):
        out.append({"assumption": "No close prior art or registered design exists",
                    "hypothesis": "A manual patent and design registry search finds no close match.",
                    "method": "Search Google Patents, the Indian Patent Office, and the Indian design registry for the "
                              "core principle; record each close result.",
                    "cost_inr": 0, "duration_days": 3, "success_criteria": "no close match",
                    "failure_criteria": "a close match exists", "evidence_level_target": 1, "gated_actions": []})
    return out
