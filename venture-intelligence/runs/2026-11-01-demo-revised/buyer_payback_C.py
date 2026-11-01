"""Buyer/entrant arithmetic for Lens C near-misses. Run: python3 buyer_payback_C.py
Every input is labelled: S = sourced (see 01-hunt-C.md), A = assumption."""

print("== 1. Sports wheelchair / para-sport (closest miss) ==")
import_chair = 450_000      # S: Rs 4-5 lakh, midpoint (ToI via search summary)
local_chair = 150_000       # A: what a local maker might charge
athletes = 1_300            # S: Khelo India Para Games 2025 participants (all sports, not only chairs)
chair_share = 0.30          # A: share needing a sport wheelchair
life_years = 4              # A: replacement cycle
share = 0.30                # A: entrant share of replacements
gm = 0.30                   # A: gross margin
chairs_users = athletes * chair_share
per_year = chairs_users / life_years
market = per_year * local_chair
rev = market * share
gp = rev * gm
print(f"chair users ~{chairs_users:.0f}; replacements/yr ~{per_year:.0f}")
print(f"whole-market spend at local price Rs {market:,.0f}/yr; entrant revenue Rs {rev:,.0f}; gross profit Rs {gp:,.0f}")
print(f"buyer saving per chair vs import Rs {import_chair-local_chair:,.0f} (one-off, no income to repay it)")
founder_hr = 750
hours = 1_200               # A: half-time year
print(f"founder time at Rs {founder_hr}/h x {hours}h = Rs {founder_hr*hours:,.0f}; gross profit covers it {gp/(founder_hr*hours):.2f}x")

print("\n== 2. Agarwood compliant-export desk (closest miss) ==")
consign_value = 2.35e7      # S: Rs 2.35 crore first legal consignment
consign_kg = 112            # S: 100 kg Saudi + 12 kg UAE
price_kg = consign_value / consign_kg
print(f"implied export price Rs {price_kg:,.0f}/kg")
quota_kg = 151_080          # S: national chips quota per year
print(f"quota x that price = Rs {quota_kg*price_kg/1e7:,.0f} crore/yr -> unrealistic, so first-consignment price is not a market average")
capital = 500_000           # S: brief
kg_bought = capital / (price_kg * 0.80)   # A: buy at 80% of export price
margin_per_cycle = kg_bought * price_kg * 0.20  # A: 20% gross margin before permits/freight
print(f"Rs 5 lakh buys ~{kg_bought:.1f} kg; gross margin per cycle Rs {margin_per_cycle:,.0f}")
for cycles in (2, 4):
    print(f"  {cycles} cycles/yr -> Rs {margin_per_cycle*cycles:,.0f}/yr vs founder time Rs {founder_hr*1200:,.0f}")

print("\n== 3. Tea plucker, cheapest rival after subsidy ==")
cap_single = 40_000         # S: Himachal 50% subsidy cap, single-person machine
print(f"Subsidy cap alone Rs {cap_single:,}; Assam general category subsidy 25% (S, 2019 report) so rival net price falls 25-50%")

print("\n== 4. Bowling machine (academy) ==")
print("Indian listings Rs 56,000 to Rs 2,09,500 (S); Indian makers exist, so import-gap thesis fails")
