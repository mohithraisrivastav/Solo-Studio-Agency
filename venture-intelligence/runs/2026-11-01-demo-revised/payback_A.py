#!/usr/bin/env python3
"""Buyer payback for near-miss theses in hunt A. All inputs are labelled in 01-hunt-A.md.
Payback months = solution cost / (annual value / 12). INR."""

def payback(cost, annual_value):
    return float("inf") if annual_value <= 0 else 12 * cost / annual_value

print("== Truck tyre pressure monitor, one small-fleet truck (6 tyres) ==")
for tyre_spend in (60000, 120000):            # INR per truck per year [A]
    for share_underinflated in (0.1, 0.2):    # share of tyre-life run >=20% underinflated [A]
        life_lost = 0.30                      # life lost when 20% under [S: TMC via Fleetx search summary]
        recovered = 0.7                       # share of that loss the alert prevents [A]
        value = tyre_spend * share_underinflated * life_lost * recovered
        for cost in (6090, 14999):            # listing prices [S]
            print(f"tyre spend {tyre_spend:>7} under {share_underinflated:.0%} cost {cost:>6}: "
                  f"value/yr {value:>7.0f} payback {payback(cost, value):6.1f} months")

print("\n== Dairy crate tracking, 20,000-crate fleet ==")
for crate_price in (225, 380):                # INR per crate [S listings]
    for loss in (0.05, 0.10, 0.25):           # annual loss: 25% is vendor claim [S], others [A]
        fleet = 20000
        lost_value = fleet * crate_price * loss
        for cut in (0.3, 0.6):                # share of loss tracking prevents [A]
            value = lost_value * cut
            tag_cost = fleet * 40 + 300000    # Rs 40 per tag, Rs 3 lakh readers/software [A]
            print(f"crate {crate_price} loss {loss:.0%} cut {cut:.0%}: value/yr {value:>8.0f} "
                  f"cost {tag_cost} payback {payback(tag_cost, value):6.1f} months")

print("\n== Boat ice/insulated box, small traditional boat ==")
for catch_value_year in (300000, 600000):     # INR per boat per year [A]
    loss = 0.043                              # traditional-sector landing-centre loss [S: CIFT pilot]
    value = catch_value_year * loss * 0.5     # half avoidable [A]
    for box_cost, subsidy in ((12000, 0.0), (12000, 0.4)):   # box cost [A], subsidy rate [S: state listings, other items]
        cost = box_cost * (1 - subsidy)
        print(f"catch {catch_value_year}: value/yr {value:.0f} cost {cost:.0f} payback {payback(cost, value):.1f} months")
