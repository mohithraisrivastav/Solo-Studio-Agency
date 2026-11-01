"""Round 2 economics for Lens C ideas. Labels: S sourced, I inferred, A assumption, H hypothesis."""
INR_PER_EUR = 100   # A: rounded; check at purchase
founder_hr, hrs = 750, 1200   # brief default; A: 1,200 h/yr half-time
founder_cost = founder_hr*hrs

print("== C1 Cask passport (sensor + record per cask) ==")
cask_price_low, cask_price_high = 200_000, 1_400_000   # S: Business Today, Rs 2 lakh to over Rs 14 lakh
tag_bom, tag_price_year = 4_000, 2_500                 # H: unit cost and annual service fee per cask
for price_pct in (cask_price_low, cask_price_high):
    print(f"annual fee as % of cask price Rs {price_pct:,}: {tag_price_year/price_pct*100:.2f}%")
for casks in (500, 2_000):                             # H: casks per customer programme
    rev = casks*tag_price_year
    capex = casks*tag_bom
    print(f"{casks} casks: tag capex Rs {capex:,}, yearly fee Rs {rev:,}, payback on tags {capex/rev:.1f} yr")
print(f"2 customers x 1,000 casks: yearly fee Rs {2*1000*tag_price_year:,} vs founder time Rs {founder_cost:,}")
print(f"Customers needed for fee to cover founder time (1,000 casks each): {founder_cost/(1000*tag_price_year):.1f}")

print("\n== C2 Passive RH buffer for a collection case ==")
prosorb_eur_500g = 45.82   # S: silica-gel.it
per_kg_inr = prosorb_eur_500g*2*INR_PER_EUR
for vol_m3, kg_per_m3 in ((0.5,2),(0.5,4),(1.0,4)):    # S sizing 2-4 kg/m3
    kg = vol_m3*kg_per_m3
    print(f"case {vol_m3} m3 at {kg_per_m3} kg/m3 -> {kg:.1f} kg imported buffer ~Rs {kg*per_kg_inr:,.0f}")
local_per_kg = 1_200       # H: local conditioned silica gel, Rs/kg
print(f"imported buffer ~Rs {per_kg_inr:,.0f}/kg [A rate]; H local Rs {local_per_kg}/kg -> buffer cost for 1 kg Rs {local_per_kg:,}")
case_price, case_cogs = 40_000, 22_000                 # H: price and cost of a sealed buffered case
print(f"H case margin Rs {case_price-case_cogs:,}; cases/yr to cover founder time {founder_cost/(case_price-case_cogs):.0f}")

print("\n== C3 Shared coffee drying service ==")
holdings = 3.66e5; small_share = 0.98                  # S: farmers, share small
print(f"small farmers ~{holdings*small_share:,.0f}")
# H: service parameters
season_days, batch_t, price_per_kg_dried = 100, 2.0, 6.0   # tonnes per batch/day-slot; Rs/kg dried parchment
util = 0.5
tonnes = season_days*batch_t*util
rev = tonnes*1000*price_per_kg_dried
print(f"H: {tonnes:.0f} t dried/season at Rs {price_per_kg_dried}/kg = Rs {rev:,.0f}")
dryer_capex = 1_500_000   # H: used dryer + trailer
opex = 0.5*rev
print(f"H: dryer Rs {dryer_capex:,} exceeds the Rs 5,00,000 capital; operating surplus Rs {rev-opex:,.0f}/season; payback {dryer_capex/(rev-opex):.1f} seasons")
print("Break-even at Rs 5,00,000 capital needs a leased or subsidised dryer (curing-unit scheme 40% to Rs 25 lakh, S)")

print("\n== C4 Authenticity lab (agarwood grade, attar fingerprint) ==")
fee_sample, cost_sample = 3_000, 1_200       # H: per sample fee and variable cost at a partner lab
fixed = founder_cost + 150_000               # A: founder time + method validation/accreditation costs
for n in (200, 500, 1000):
    print(f"{n} samples/yr: contribution Rs {n*(fee_sample-cost_sample):,} vs fixed Rs {fixed:,}")
print(f"Break-even samples {fixed/(fee_sample-cost_sample):.0f}")
price_kg = 2.35e7/112
print(f"S-derived export price Rs {price_kg:,.0f}/kg; fee Rs {fee_sample} per sample is {fee_sample/price_kg*100:.2f}% of 1 kg")

print("\n== C5 Sport chair lending pool ==")
chair_cost_import = 450_000; local_cost = 150_000       # S midpoint of Rs 4-5 lakh; A local
fleet = 20; lend_fee_year = 15_000                      # H fee per athlete per year, chairs in pool
rev = fleet*lend_fee_year*1.0
print(f"fleet {fleet} chairs cost Rs {fleet*local_cost:,}; fee income Rs {rev:,}/yr; payback {fleet*local_cost/rev:.0f} yr -> needs grant or CSR capital")
print(f"CSR/grant funded fleet: fleet cost Rs {fleet*local_cost:,} vs imported Rs {fleet*chair_cost_import:,}; saving Rs {fleet*(chair_cost_import-local_cost):,}")

print("\n== C6 Cask revitalisation ==")
reco_cost_abroad_low, reco_cost_abroad_high = 50, 150    # S: USD per wine barrel reconditioning (patent text)
new_oak = 700
print(f"abroad: reconditioning USD {reco_cost_abroad_low}-{reco_cost_abroad_high} vs new oak USD {new_oak}+ => {reco_cost_abroad_high/new_oak:.0%} max of new")
local_fee, casks_year = 6_000, 1_500                     # H
print(f"H: Rs {local_fee:,} per cask x {casks_year} casks = Rs {local_fee*casks_year:,}/yr revenue")

print("\n== C7 Tactile STEM diagrams ==")
print("No priced inputs found; economics left as missing information.")
