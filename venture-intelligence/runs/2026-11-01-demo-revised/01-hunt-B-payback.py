#!/usr/bin/env python3
"""Buyer payback and entrant earnings for the near-miss theses in 01-hunt-B.md.
Inputs marked SRC come from listings/search summaries; ASSUMED are assumptions to test.
Run: python3 01-hunt-B-payback.py"""
FOUNDER_HR = 750  # INR/hour, brief default

print("== T1 Groundwater flow meter + telemetry (CGWA NOC holders) ==")
meter = 25000          # INR, mid of listings 18,900-30,999 (SRC, IndiaMART/TradeIndia)
calib = 6500           # INR/yr, mid of listed 2,800-12,000 NABL flow meter calibration (SRC, vendor listings)
sim_cloud = 3000       # INR/yr ASSUMED
penalty_min = 100000   # INR, min compensation w/o NOC, secondary source (SRC, unverified)
structures = 2         # ASSUMED structures per NOC holder
viol_rate = 2833 / 12650  # crude: detected violations / NOCs issued in 5 yrs (different bases; proxy only)
buyer_capex = meter * structures
buyer_opex = (calib + sim_cloud) * structures
print(f"buyer capex {buyer_capex:,.0f}  opex/yr {buyer_opex:,.0f}")
print("buyer 'saving' is avoided penalty, not a cash saving; payback undefined (compliance cost, no return).")
print(f"crude violation proxy {viol_rate:.1%}; expected penalty avoided/yr if 1-in-5-yr event: {penalty_min*viol_rate/5:,.0f}")
nocs_per_yr = 12650 / 5
for share in (0.01, 0.02, 0.05):
    n = nocs_per_yr * share
    margin_hw = 0.30 * meter * structures * n          # ASSUMED 30% gross margin
    recurring = 0.40 * (calib + sim_cloud) * structures * n  # ASSUMED 40% margin on service
    print(f"share {share:.0%}: {n:.0f} new NOCs/yr, hardware margin {margin_hw:,.0f}, recurring margin {recurring:,.0f}")
hours_per_install = 12  # ASSUMED incl. travel, commissioning, portal upload
n = nocs_per_yr * 0.02
cost_time = n * structures * hours_per_install * FOUNDER_HR
print(f"2% share founder time cost at {FOUNDER_HR}/hr: {cost_time:,.0f}")

print("\n== T2 Refrigerant recovery/reclaim (R22) ==")
r22_price = 700        # INR/kg undated forum range 680-720 (SRC, weak)
kg_per_unit = 1.2      # kg per scrapped split AC ASSUMED
disc = 0.30            # reclaim sells 30% below virgin ASSUMED
handling = 150         # INR/kg collection+testing ASSUMED
machine = 34500        # INR, recovery machine listing (SRC)
net_kg = r22_price * (1 - disc) - handling
print(f"net margin per kg {net_kg:,.0f}; per AC unit {net_kg*kg_per_unit:,.0f}")
print(f"units to repay recovery machine: {machine/(net_kg*kg_per_unit):,.0f}")
for kg_month in (200, 500, 1000):
    print(f"{kg_month} kg/month -> margin {kg_month*net_kg:,.0f}/month; founder hours at 0.5h/kg {kg_month*0.5*FOUNDER_HR:,.0f}")
print("No Indian mandate to reclaim found; no 2026 India price found. Demand driver unproven.")

print("\n== T3 Footwear QCO in-house test kit vs subsidised lab ==")
fee_full = 10000       # INR per variant low end (SRC, secondary: 10,000-50,000 certification fee)
disc_micro = 0.80      # 80% testing charge cut (SRC, 2023, secondary)
print(f"certification/test fee after 80% cut on 10,000: {fee_full*(1-disc_micro):,.0f}")
kit = 1000000          # INR ASSUMED in-house bench kit (no price found)
variants_yr = 10       # ASSUMED
print(f"kit {kit:,.0f} vs lab spend {variants_yr*fee_full*(1-disc_micro):,.0f}/yr -> payback {kit/(variants_yr*fee_full*(1-disc_micro)):.0f} years")
print(f"even at full fee: {kit/(variants_yr*fee_full):.0f} years")
