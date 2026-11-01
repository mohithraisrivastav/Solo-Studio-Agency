#!/usr/bin/env python3
"""Arithmetic for 01-hunt-B.md. Run: python3 01-hunt-B-calc.py
All money INR. Inputs marked SRC come from listings/search summaries in the Sources table;
ASM are assumptions named in the file. Founder: capital 500000, 750/h, 160 h/month available."""
USD = 88.0  # ASM rate
CAP, HVAL, HRS = 500000, 750, 160

print("== A. DDGS lot-grading (aflatoxin strip + moisture/NIR) ==")
def ddgs(fee_t, strip=950, lot_t=25, tech_h_per_lot=0.75, tech_rate=200,
         plant_klpd=200, kg_per_l=0.55, days=330, reader=200000):
    tpd = plant_klpd*1000*kg_per_l/1000
    lots_day = tpd/lot_t
    cost_lot = strip + tech_h_per_lot*tech_rate
    rev_lot = fee_t*lot_t
    margin_lot = rev_lot-cost_lot
    annual_margin = margin_lot*lots_day*days
    return tpd, lots_day, cost_lot, rev_lot, margin_lot, annual_margin
base = dict(fee_t=60)
for label, kw in [("base fee 60/t, strip 950", {}),
                  ("fee halved 30/t", dict(fee_t=30)),
                  ("strip 1015 (Rs 20300/20)", dict(strip=1015)),
                  ("strip 880 (USD10)", dict(strip=880)),
                  ("yield 0.79 kg/L", dict(kg_per_l=0.79)),
                  ("fee 100/t", dict(fee_t=100))]:
    p = dict(base); p.update(kw)
    tpd, ld, cl, rl, ml, am = ddgs(**p)
    print(f"{label:28s} t/day {tpd:6.0f} lots/day {ld:4.1f} cost/lot {cl:6.0f} rev/lot {rl:6.0f} margin/lot {ml:6.0f} plant margin/yr {am/1e5:6.1f} lakh (before on-site tech salary)")
# on-site technician per plant: 25000/month loaded 30000
tech_year = 30000*12
tpd, ld, cl, rl, ml, am = ddgs(fee_t=60)
print("plant margin after one on-site tech (fee 60):", round((am-tech_year)/1e5,1), "lakh/yr")
tpd, ld, cl, rl, ml, am30 = ddgs(fee_t=30)
print("plant margin after one on-site tech (fee 30):", round((am30-tech_year)/1e5,1), "lakh/yr")
print("value of DDGS per t: rice 30000, maize 24000 (SRC); fee 60 =", round(60/30000*100,2), "% of rice,", round(60/24000*100,2), "% of maize")
# 100 plants
n=100
print("100 plants: readers", n*200000/1e5, "lakh (ASM 2 lakh each) vs capital", CAP/1e5, "lakh")
print("100 plants: founder hours/month at 4 h per plant:", n*4, "vs available", HRS)
print("Buyer's own cheapest alternative = same strip cost per t:", round((950+0.75*200)/25,1), "Rs/t")

print("\n== B. Footwear MSE in-house lab vs outsource ==")
flex=117000; scott=132000; abrasion=150000; tensile=400000; oven_bath=50000  # flex,scott SRC; abrasion,tensile,oven ASM
lab = flex+scott+abrasion+tensile+oven_bath
print("core lab equipment Rs", lab, "(abrasion, tensile, oven are ASM)")
for fee, rounds in [(15540,4),(22140,4),(15540,2),(22140,8)]:
    yr = fee*rounds
    print(f"outsource fee {fee} x {rounds}/yr = {yr}; payback of own lab {lab/yr:.1f} yr")
print("halve equipment cost -> payback at 22140x4:", round(lab/2/(22140*4),1), "yr")

print("\n== C. Bet: weigh-in receipt scale for AC platforms ==")
bom = dict(load_cell=400, hx711=80, esp32=450, battery_charger=350, case=300, pcb_assembly=400, cal_test=150)  # all ASM
unit = sum(bom.values())
print("BOM per unit (ASM)", unit, "vs commercial 50 kg scale listing 7500-10500 (SRC)")
price=5500
print("margin/unit at price 5500:", price-unit)
print("100 units capital:", 100*unit, "of", CAP)
for plats, techs in [(1,500),(5,500),(5,5000)]:
    u=plats*techs
    print(f"{plats} platforms x {techs} techs = {u} units: stock cash {u*unit/1e5:.1f} lakh; one-time margin {(price-unit)*u/1e5:.1f} lakh")
bom2=unit*2; print("BOM doubled ->", bom2, "margin", price-bom2, "(still positive; verdict driven by buyer count and self-build, not BOM)")

print("\n== D. Bet: hive-scale telemetry ==")
b = dict(cells=600, mcu_cell_module=900, solar_batt=800, case=400)  # ASM
hu=sum(b.values()); print("BOM", hu, " data/yr 500 ASM; BroodMinder cell hub USD 545 =", round(545*USD), "(SRC)")
for fee in (300,600,1000):
    print(f"fee/hive/season {fee}: 10000 hives revenue {fee*10000/1e5:.1f} lakh; 100 hives capital {100*hu/1e5:.1f} lakh")
print("Colony price context: beekeeper price fell Rs150 -> Rs60-70/kg (SRC); fraud located at processors/importers (SRC)")

print("\n== E. Refrigerant identifier incumbents ==")
for name, usd in [("Mini ID R-134a (AUD?)",3044),("Mini ID R-1234yf CAD",1723),("Ultima ID",2200)]:
    print(name, "approx Rs", round(usd*USD))
print("vs technician-owned recovery machine listing Rs 33500 (SRC); a Rs 6000 device would need ~", round(1500*USD/6000,1),"x cost cut")
