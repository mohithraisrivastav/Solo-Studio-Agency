#!/usr/bin/env python3
"""Lens C hunt economics. All money in INR. Run: python3 01-hunt-C-econ.py
Inputs marked SRC are from the Sources table of 01-hunt-C.md; ASM are unsourced assumptions.
The sensitivity rule: each ASM input made unfavourable by half; report if the verdict flips."""
HOUR = 750            # founder hour value, brief default
CAP = 500000          # founder capital, brief default
HRS_YEAR = 12 * (160 - 40)   # available founder hours per year after fixed admin (econ.py convention)

def pr(*a): print(*a)

# ---------- T1 Agarwood export-lot grade assay ----------
def t1(fee_lot=25000, lots_per_cust=4, cust=100, samples_per_lot=2,
       lab_per_sample=4000, gst=0.18, hours_per_lot=3, verdict_floor=HOUR*0):
    lab = lab_per_sample * samples_per_lot            # SRC IIHR industry tariff Rs 4,000 + GST; GST claimable if registered
    labour = hours_per_lot * HOUR
    margin = fee_lot - lab - labour
    lots = cust * lots_per_cust
    hours = lots * hours_per_lot
    return dict(margin_lot=margin, lots=lots, hours=hours, annual_margin=margin*lots,
                hours_ok=hours <= HRS_YEAR, rev=fee_lot*lots)
pr("== T1 agarwood lot assay ==")
base = t1()
pr("base 100 cust x4 lots:", base)
pr("10 cust x4 lots:", t1(cust=10))
pr("fee halved (ASM):", t1(fee_lot=12500))
pr("lots/cust halved (ASM):", t1(lots_per_cust=2))
pr("lab cost doubled (ASM if outsourced rate higher):", t1(lab_per_sample=8000))
pr("fee as share of first-export lot Rs 2.35 cr (SRC):", 25000/23500000)
pr("first export unit price Rs/kg (SRC 2.35 cr / 112 kg):", 23500000/112)
# verdict: positive annual margin after labour, and hours within year
for k, v in dict(fee_halved=t1(fee_lot=12500), lots_halved=t1(lots_per_cust=2), cust10=t1(cust=10)).items():
    pr(k, "verdict_flips:", (v['annual_margin'] < 0.5*CAP*0 + 1_000_000))   # below Rs 10 lakh a year = not worth it

# ---------- T2 Sports wheelchair, domestic ----------
pr("\n== T2 sports wheelchair ==")
def t2(price=85000, bom=32000, hours=12, units=100, jig=200000, stock_months=2):
    unit_margin = price - bom - hours*HOUR
    cap = jig + bom*units/12*stock_months
    return dict(unit_margin_after_labour=unit_margin, hours_100=hours*units, capital_100_per_yr=cap,
                annual_margin=unit_margin*units, hours_ok=hours*units <= HRS_YEAR)
pr("base:", t2())
pr("price at Rs 65,000 (SRC family quote for domestic chair):", t2(price=65000))
pr("BOM +50%:", t2(bom=48000))
pr("hours 20/chair:", t2(hours=20))
# demand ceiling
pr("buyers: 1,500 serious wheelchair athletes (ASM) / 4 yr life => chairs/yr:", 1500/4)

# ---------- T3 Sandalwood heartwood probe ----------
pr("\n== T3 sandalwood probe ==")
growers = 1000   # SRC KSDL estimate 'at least 1,000'
trees_per_grower = 400  # ASM; one source 400-450 per acre, ~1 acre assumed typical for small grower
fee = 500        # ASM per tree
pr("one-time scan market Rs:", growers*trees_per_grower*fee)
pr("Rs/tree value 10-15 kg x Rs 6,000-10,000 (SRC):", 10*6000, 15*10000)

# ---------- B1 Standing-tree acoustic assay (agarwood) ----------
pr("\n== B1 standing-tree assay ==")
def b1(trees=143300, share=0.10, fee=400, mins=15, travel_mins=10):
    scans = trees*share
    hrs = scans*(mins+travel_mins)/60
    return dict(scans=scans, revenue=scans*fee, hours=hrs, rev_per_hour=scans*fee/hrs, years_at_cap=hrs/HRS_YEAR)
pr("10% of 1.433 million trees (SRC), Rs 400, 25 min/tree:", b1(trees=1433000))
pr("fee halved:", b1(trees=1433000, fee=200))
pr("100 customers x 100 trees = 10,000 scans hours:", 10000*25/60, "vs available", HRS_YEAR)
pr("instrument: ArborSonic-class ~USD 3,000 SRC(old) x Rs 85/USD ASM =", 3000*85)

# ---------- B2 Rackhouse mapping ----------
pr("\n== B2 rackhouse mapping ==")
buyers = 20     # ASM upper bound from named Indian malt makers in sources (about 6 named)
setup = 200000; yearly = 60000   # ASM
pr("20 buyers: first-year revenue", buyers*(setup+yearly), "recurring", buyers*yearly)
pr("6 buyers (named in sources):", 6*(setup+yearly), "recurring", 6*yearly)
pr("hours 6 buyers: mapping 80 h each", 6*80)
pr("value test: 5,000 casks x Rs 60,000 spirit value (ASM) x 2 pt loss change:", 5000*60000*0.02)

# ---------- B3 Native-wood staves ----------
pr("\n== B3 native wood staves ==")
buyers = 15; order = 800000  # ASM per buyer per yr
pr("ceiling revenue/yr:", buyers*order)
pr("seasoning inventory 24 months for Rs 12 lakh/yr sales at wood cost 40% (ASM):", 0.4*buyers*order*2)
pr("founder capital:", CAP)

# ---------- T4 Archive boxes ----------
pr("\n== T4 archival boxes ==")
dom_low, dom_high, imp = 100, 1000, 8245   # SRC listings
pr("imported/domestic-high ratio:", imp/dom_high, "imported/domestic-low:", imp/dom_low)
boxes_100_customers = 100*200   # ASM 200 boxes a year per institution
for p in (400, 800):
    pr("price", p, "cost 250 (ASM) margin/box", p-250, "annual margin", (p-250)*boxes_100_customers)
