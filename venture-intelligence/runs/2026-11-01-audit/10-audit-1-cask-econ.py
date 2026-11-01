#!/usr/bin/env python3
"""Cask passport economics. All inputs are assumptions (no catalogue prices could be fetched
in this run; see audit file). Run: python3 10-audit-1-cask-econ.py"""
import math
# ---- BOM per tag, INR, volume ~1,000 units, ASSUMED (low / high)
bom = {
 "MCU + LoRa radio module (STM32WL / ESP32-class)": (500, 900),
 "Level sensor (ToF/ultrasonic/capacitive probe, ethanol-vapour tolerant)": (700, 2500),
 "Temp+humidity sensor (SHT3x class)": (250, 500),
 "Primary lithium cell (ER26500-class, 5y target)": (400, 800),
 "Bung adapter / enclosure, sealed, food-safe": (400, 1200),
 "PCB, assembly, test": (400, 800),
 "Calibration per unit (jig, labour 15 min)": (100, 250),
}
lo = sum(v[0] for v in bom.values()); hi = sum(v[1] for v in bom.values())
print(f"Tag BOM+assembly INR {lo}-{hi} (mid {(lo+hi)//2})")
gateway = (15000, 30000)          # per warehouse, ASSUMED
install_per_tag = (150, 400)      # labour, ASSUMED; excludes excise-officer attendance
# ---- battery life check: 1 uplink/6h, 40 mJ... simplified
cap_mAh = 3000*0.7                # derated
avg_uA = 25                       # sleep 5uA + sensing/radio average, ASSUMED
life_y = cap_mAh*1000/avg_uA/8760
print(f"Battery life ~{life_y:.1f} y at {avg_uA} uA average (ASSUMED)")
# ---- level resolution: horizontal 200 L barrel, belly diameter ~0.68 m, length ~0.9 m (K)
D, L = 0.68, 0.90
def vol(h):
    r=D/2; h=min(max(h,0),D)
    seg = r*r*math.acos((r-h)/r) - (r-h)*math.sqrt(max(2*r*h-h*h,0))
    return seg*L*1000
for loss in (0.02, 0.10):
    full = D*0.97   # ullage at fill ~3%
    target = vol(full)*(1-loss)
    h=full
    while vol(h)>target: h-=0.0005
    print(f"Loss {loss:.0%}/y -> level drop {1000*(full-h):.0f} mm (needs sensor error well under this)")
# ---- selling price
for cost in (lo, hi):
    print(f"Cost {cost} -> price at 40% margin {cost/0.6:.0f}; hunter tag price 4000")
# ---- annual running cost per cask (ASSUMED)
battery_swap = 600/5; support = 250; cloud = 60; recal = 150; field = 200
run = battery_swap+support+cloud+recal+field
print(f"Running cost per cask per year ~INR {run:.0f} vs hunter fee 2500")
# ---- customer pool scenarios: programmes x casks tagged x uptake
fee, tagprice = 2500, 4000
print("\nscenario: programmes, tagged casks each -> revenue/yr, tag capex")
for name,(n,c,up) in {"verified-ish (Diageo, Paul John + 3 more, small)":(5,300,0.3),
                      "optimistic (12 programmes)":(12,800,0.4),
                      "hunter (2 x 1000)":(2,1000,1.0)}.items():
    casks=n*c*up if name!="hunter (2 x 1000)" else n*c
    rev=casks*fee; capex=casks*(hi+install_per_tag[1])
    gross=casks*(fee-run)
    print(f"{name}: casks {casks:.0f}, revenue INR {rev/1e5:.1f} lakh, gross after running cost INR {gross/1e5:.1f} lakh, tag capex INR {capex/1e5:.1f} lakh")
print("\nFounder capital INR 5,00,000 buys ~", int(500000/(hi+install_per_tag[1])), "tags at high-end cost, ~", int(500000/(lo+install_per_tag[0])), "at low-end, before gateways, legal, certification")
print("Fixed cost to sustain one founder at INR 60,000/month plus tools: break-even casks =", math.ceil((60000+10000)*12/(fee-run)))
