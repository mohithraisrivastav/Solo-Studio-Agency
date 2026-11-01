# Honey pre-screen economics. All inputs are assumptions unless the audit file says sourced.
import itertools
# 1. Hunter's arithmetic check: value of screening per lot = p_fail*NMR_fee - screen_cost (only failures save an NMR run)
for fee in (500, 5000, 15000, 25000):
    for p in (0.02, 0.05, 0.15):
        for sens in (1.0, 0.5, 0.1):   # share of failing lots the screen actually flags
            gross = p*sens*fee
            print(f"fee={fee:6} p_fail={p:.2f} sens={sens:.1f} saved/lot={gross:8.1f} net_of_300={gross-300:8.1f}")
print("hunter's 5% x 15000 =", 0.05*15000, "(hunter wrote ~775; net of INR 300 is", 0.05*15000-300, ")")
# 2. Buyer pool and revenue (counts partly sourced: 97 honey FPOs; others assumed)
pools = {"honey_FPOs":97, "exporters_assumed":150, "big_aggregators_assumed":100}
total=sum(pools.values()); print("reachable orgs", total)
for price in (30000, 60000, 100000):
    for share in (0.05, 0.10, 0.20):
        n=total*share; rev=n*price
        print(f"device INR{price} share{share:.0%} units={n:.0f} revenue=INR{rev/1e5:.1f} lakh")
# 3. BOM (ALL assumed, no catalogue price found): handheld NIR/FTIR-class module
bom = {"NIR spectral sensor+optics":12000,"MCU/display/battery":5000,"enclosure/cuvette":3000,"assembly/test":2000}
b=sum(bom.values()); print("BOM assumed INR",b)
# 4. Calibration data: authentic honey library
samples_needed=(500,2000)   # assumed; portable NIR studies used 59-244 samples
cost_per_ref=(3000,15000)   # assumed: collect + NMR/lab reference label
for s,c in itertools.product(samples_needed,cost_per_ref):
    print(f"library n={s} ref cost={c} -> INR {s*c/1e5:.1f} lakh")
print("founder default capital INR 5,00,000")
