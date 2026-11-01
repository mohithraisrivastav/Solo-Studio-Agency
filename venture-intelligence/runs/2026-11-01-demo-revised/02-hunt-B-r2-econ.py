#!/usr/bin/env python3
"""Economics for round-2 ideas in 02-hunt-B-r2.md. Tags: S=listing/search, A=assumption, H=hypothesis.
Run: python3 02-hunt-B-r2-econ.py"""
H = 750  # INR/hour founder time (brief)

def sec(t): print("\n== " + t + " ==")

sec("I1 Groundwater meter-as-a-service (rental bundle)")
meter=25000      # S listing mid 18,900-30,999
calib=6500       # S listing mid
sim=3000         # A
install=3000     # A per meter, travel + commissioning
life=5           # A years NOC validity / meter life
cost_to_serve = meter + install + (calib+sim)*life
for fee in (1500,2000,2500):   # H monthly rental per meter
    rev = fee*12*life
    margin = rev - cost_to_serve
    print(f"fee {fee}/mo/meter: 5yr revenue {rev:,.0f}, cost {cost_to_serve:,.0f}, margin {margin:,.0f} ({margin/rev:.0%}); cash tied up per meter {meter+install:,.0f}")
cap=500000
print("meters financeable with 5,00,000 capital:", int(cap/(meter+install)))
print("buyer outright cost over 5 yrs per meter:", meter+install+(calib+sim)*life)

sec("I2 Pump-health add-on on mandated telemetry")
pump_kw=7.5; hrs=16*300; tariff=8   # A pump kW, h/yr, INR/kWh (S: 7-9 blended HT range for industrial)
energy=pump_kw*hrs*tariff
print(f"pump energy/yr {energy:,.0f}")
for save in (0.03,0.05,0.10):
    print(f"saving {save:.0%} (H): {energy*save:,.0f}/yr per pump")

sec("I3 Tyre-crumb cow mat")
crumb_kg_price=(18,38); mat_kg=40; mat_price=(1500,2800)
binder_per_kg=(30,60)  # A: binder+additives INR per kg of mat (H, no source)
mould_cost_per_mat=100 # A energy/labour
for cp in crumb_kg_price:
    for bp in binder_per_kg:
        unit_cost=mat_kg*(cp*0.85+bp*0.15*3)+mould_cost_per_mat   # A: 85% crumb, binder 15% mass at 3x per-kg figure
        print(f"crumb {cp}/kg binder {bp}: unit cost {unit_cost:,.0f}; margin at 1500 {(1500-unit_cost)/1500:.0%}, at 2100 {(2100-unit_cost)/2100:.0%}")
print("mats per 100-cow farm (1 per cow) at 2100:", 100*2100)

sec("I4 Kabadi AC gas bounty")
r22=700; kg=1.2; bounty_share=0.35; sell_disc=0.30; handling=100
sell=r22*(1-sell_disc)
for share in (0.2,0.35,0.5):
    pay=r22*kg*share*0  # placeholder
    bounty=sell*kg*share
    margin=sell*kg - bounty - handling*kg
    print(f"bounty share {share:.0%} of sale value: pay kabadi {bounty:,.0f}/AC, margin {margin:,.0f}/AC")
print("recovery kit 34,500 (S) -> kits financeable:", int(500000*0.5/34500))

sec("I5 Honey pre-screen at collection point")
for nmr in (500, 15000, 25000):   # S conflict: 'few hundred' vs 15,000-25,000
    for fail in (0.05,0.15):      # H share of lots failing
        screen=300                # H per screened lot
        saved = fail*nmr*0        # NMR still needed on passes; saving is avoiding sending bad lots
        # value: avoided cost of NMR + freight on failing lots, plus avoided rejected shipment
        avoided_per_lot = fail*(nmr+500)
        print(f"NMR {nmr:,} fail {fail:.0%}: avoided per lot {avoided_per_lot:,.0f} vs screen fee {screen} -> {'worth' if avoided_per_lot>screen else 'not worth'} on testing cost alone")
print("A rejected export lot is the real prize; value unknown (no data found).")

sec("I6 DDGS cleaned lots for small feed mills / dairy FPOs")
ddgs=23; # S listing 17-30 INR/kg
soy_usd=416; ddgs_usd=225; fx=88   # S export unit values, A fx 88 INR/USD
print(f"export-unit gap soymeal-DDGS: INR {(soy_usd-ddgs_usd)*fx/1000:.1f}/kg")
for up in (1.0,2.0,3.0):  # H premium INR/kg for sieved, aflatoxin-tested lots
    t_month=50  # A tonnes/month
    print(f"premium {up}/kg on {t_month} t/month: gross {up*t_month*1000:,.0f}/month; testing 1 sample/10t at 1500 -> {t_month/10*1500:,.0f}")

sec("I7 Shared spice steam sterilisation (tolling)")
machine=1000000   # S listing 0-500 kg/hr general sterilizer (weak)
kg_hr=250; hrs=6; days=25; util=0.5
cap_kg_month=kg_hr*hrs*days*util
for toll in (3,5,8):   # H INR/kg
    rev=cap_kg_month*toll
    cost_var=cap_kg_month*1.5   # A steam+labour per kg
    print(f"toll {toll}/kg: {cap_kg_month:,.0f} kg/month, rev {rev:,.0f}, var cost {cost_var:,.0f}, contribution {rev-cost_var:,.0f}/month, payback of machine {machine/max(rev-cost_var,1):.0f} months (excl. building, boiler)")

sec("I8 Footwear test kit (corrected with listing prices)")
kit=(79000+132000+190000+85000)   # S flex, crease-flex, taber, de-mattia listings; excludes bond tester (no price)
print("kit total", kit)
for variants in (10,40):
    for fee in (2000,10000):
        print(f"variants/yr {variants}, lab fee {fee}: lab spend {variants*fee:,.0f}, payback {kit/(variants*fee):.1f} yrs")
