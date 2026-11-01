#!/usr/bin/env python3
"""Round 2 buyer economics for hunt A ideas. INR. Inputs are tagged in 02-hunt-A-r2.md.
S = sourced, A = assumption with basis, H = hypothesis to test."""

def pb(cost, per_year):
    return float("inf") if per_year <= 0 else 12 * cost / per_year

print("== I1 Broiler live-haul cooling/handling kit, per truck ==")
birds = 2236            # S: Chennai study birds per truck
wt = 2.0                # A: kg live weight at ~39 days
for price in (90, 130): # S: agrifarming range 90-130 INR/kg
    for shrink in (0.0236, 0.0301):  # S: Chennai
        loss_trip = birds * wt * price * shrink
        for recov in (0.05, 0.15, 0.30):   # H: share of shrinkage a kit avoids
            for trips in (150, 250):       # A: trips per year
                val = loss_trip * recov * trips
                kit = 50000                # H: misting/ventilation kit
                print(f"price {price} shrink {shrink:.2%} recov {recov:.0%} trips {trips}: "
                      f"loss/trip {loss_trip:,.0f} value/yr {val:,.0f} payback {pb(kit,val):.1f} mo")
        # mortality
mort = 0.0053; bird_val = wt*100
print("mortality loss per trip (summer, 100/kg):", round(birds*mort*bird_val))

print("\n== I2 Detention claims desk on success fee ==")
for boxes in (5, 20):
    for days_over in (3, 7):
        for rate in (3000, 8000):   # S: vendor blog daily rate range
            bill = boxes * days_over * rate
            for p in (0.1, 0.3):    # H: share of disputed bills partly recovered
                for fee in (0.25,):
                    rev = bill * p * 0.5 * fee   # H: recovered half of bill when claim succeeds
                    print(f"boxes {boxes} over {days_over}d rate {rate} bill {bill:,} p {p:.0%}: expected fee/claim {rev:,.0f}")
founder_rate = 750
hours_per_claim = 6   # H
print("founder cost per claim at 6 h:", founder_rate*hours_per_claim)

print("\n== I3 PCM fish tote rental, small boat ==")
for catch in (300000, 600000, 1200000):  # A: INR/yr catch value
    avoided = catch * 0.043 * 0.5        # S 4.3% landing loss, A half avoidable
    trips = 200                           # A
    print(f"catch {catch:,}: value/yr {avoided:,.0f} value/trip {avoided/trips:,.0f} -> max rental/trip")

print("\n== I4 Crate QR + UPI deposit service ==")
for price in (225, 380):
    for loss in (0.05, 0.10, 0.25):
        for cut in (0.3, 0.6):
            v = price*loss*cut
            print(f"crate {price} loss {loss:.0%} cut {cut:.0%}: value/crate/yr {v:.0f}; at 20% value capture fee {0.2*v:.1f}")
fleet = 20000
print("fee per dairy-year at Rs 6/crate/yr, 20k crates:", 6*fleet)

print("\n== I5 Weighbridge tyre scan add-on ==")
hw = 800000  # H: drive-over reader + install
for scans_day in (50, 100, 200):
    for fee in (10, 20):  # H
        monthly = scans_day*30*fee
        print(f"scans/day {scans_day} fee {fee}: monthly {monthly:,}; payback {pb(hw, monthly*12):.1f} mo")

print("\n== I6 Mobile steriliser cooperative service ==")
capex = 1100000 + 800000   # S ~10-12 lakh steriliser; H 8 lakh truck/boiler/power
for util_days in (20, 60, 120):
    kg = 500*4*util_days     # S 500 kg/hr class; A 4 h/day
    for toll in (10, 15, 25):  # S weak 15-25 from blog; 10 H
        rev = kg*toll
        cost = kg*6 + 150000   # H variable 6/kg; fixed 1.5 lakh
        print(f"days {util_days} toll {toll}: kg {kg:,} revenue {rev:,} margin {rev-cost:,} payback {pb(capex, max(rev-cost,1)):.1f} mo")

print("\n== I7 Egg shell coating at packer ==")
for loss_cut in (0.005, 0.01, 0.02):
    for egg in (4.3, 5.4):  # S dtnext farm price INR/egg
        print(f"loss cut {loss_cut:.1%} egg {egg}: value/egg {egg*loss_cut:.3f} vs coating cost 0.03-0.08 (H)")

print("\n== I8 Steam-trap indicator labels, one SME plant ==")
for traps in (50, 200):
    for fail in (0.10, 0.25):     # S ranges: 9.4% managed to 25-30% unmanaged
        for kgph in (2, 5):       # H steam lost per failed trap
            for steam in (1.5, 3.0):  # A INR per kg steam
                loss = traps*fail*kgph*steam*6000   # A 6000 h/yr
                print(f"traps {traps} fail {fail:.0%} {kgph}kg/h Rs{steam}/kg: loss/yr {loss:,.0f}")
