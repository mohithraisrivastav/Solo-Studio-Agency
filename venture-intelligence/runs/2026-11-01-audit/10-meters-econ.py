"""Rental economics for a CGWA flow meter. All inputs are assumptions (A) unless noted.
Usage: python3 10-meters-econ.py"""
def run(meter=18900, install=3000, sim_cloud=1500, calib=5000, truck_per_yr=1.0, truck_cost=2500,
        theft_loss_pct=0.04, ke=0.15, years=5, salvage_frac=0.0, overhead_per_yr=1200, label=""):
    # annual cash cost to vendor
    annual_opex = sim_cloud + calib + truck_per_yr*truck_cost + overhead_per_yr
    # annualised capex via capital recovery factor
    capex = meter + install
    crf = ke*(1+ke)**years/((1+ke)**years-1)
    ann_capex = capex*crf - salvage_frac*meter*ke/((1+ke)**years-1)
    loss = theft_loss_pct*meter
    ann_total = ann_capex + annual_opex + loss
    monthly = ann_total/12
    print(f"{label:28s} capex={capex:6.0f} opex/yr={annual_opex:6.0f} breakeven Rs/month={monthly:6.0f}")
    return monthly, capex
def buyer_cost(meter=18900, install=3000, sim_cloud=1500, calib=5000, years=5, ke=0.12):
    capex = meter+install
    crf = ke*(1+ke)**years/((1+ke)**years-1)
    ann = capex*crf + sim_cloud + calib
    return ann/12, capex + years*(sim_cloud+calib)
print("VENDOR BREAKEVEN (5 yr life, zero margin)")
run(label="base (meter 18,900)")
run(meter=15000, label="cheap meter 15,000")
run(meter=30999, label="battery meter 30,999")
run(meter=15000, calib=2800, sim_cloud=1000, truck_per_yr=0.5, label="optimistic")
run(meter=30999, calib=12000, truck_per_yr=2, theft_loss_pct=0.08, label="pessimistic")
run(life:=0, label="") if False else None
run(years=3, label="base, 3 yr churn life")
print("\nBUYER OWN COST (cost of capital 12%, same meter, calib, SIM)")
for lab, kw in [("base",{}),("cheap",dict(meter=15000)),("battery",dict(meter=30999)),("calib 2800",dict(calib=2800))]:
    m,t = buyer_cost(**kw); print(f"{lab:12s} Rs/month equiv={m:6.0f}  5yr cash={t:7.0f}")
print("\nHunter check: 5yr cost per meter 75,500 -> Rs/month", round(75500/60))
print("Hunter check: 2,000/month x60 =",2000*60,"; 28,000 capital per meter -> 5,00,000 buys",int(500000/28000))
print("\nCAPITAL TO PLACE METERS (meter+install, 6 months opex float, 10% spares)")
for n in (100,1000):
    cap=(18900+3000)*n*1.10 + n*(1500+5000)/2
    print(n,"meters: Rs",round(cap), " = Rs lakh", round(cap/1e5,1))
print("\nREACH: 12,650 NOCs/5yr -> 2,530/yr; meters per NOC unknown. 2,833 illegal cases (2,370 ind,385 infra,78 mining)")
for share in (0.01,0.03,0.05):
    print(f"capture {share:.0%} of 2,530 new NOCs/yr = {2530*share:.0f} sites/yr")
