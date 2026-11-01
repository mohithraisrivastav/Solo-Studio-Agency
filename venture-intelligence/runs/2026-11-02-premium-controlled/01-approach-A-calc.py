#!/usr/bin/env python3
"""Approach A arithmetic: size-first pools, three kept ideas, sensitivity (each unsourced input made unfavourable by half).
All money INR. Inputs tagged S (sourced, search summary), A (assumption), in comments."""
import copy

HOUR = 750            # A: default founder hour value from tools/econ.py
FT_HOURS = 1920       # A: 160 h x 12 months
LAKH = 1e5; CRORE = 1e7

def fmt(x): return f"Rs {x/LAKH:,.1f} lakh"

print("=== SIZE FIRST (pool a one-person firm could reach in 24 months) ===")
# Elephants: S: PETA says at least 26 units since 2023 (Onmanorama 2026); another report ~40; price Rs 5-6 lakh
for units in (26, 40):
    for p in (5.0, 6.0):
        print(f"mechanical elephants, cumulative {units} units x Rs {p} lakh = {fmt(units*p*LAKH)} over ~3 years, one funder (PETA) buys most")
# Ship salvage: no sourced pool; yard utilisation 25% (S) -> shrinking
# RECD: price range per 500 kVA (S listings) 0.7 / 3.5 / 6.7 / 9.15 / 12.5(benchmark) lakh; base count not found
print("RECD 500 kVA listed range: Rs 3.5 to 9.15 lakh (outlier 0.7 and gazette benchmark 12.5); installed base not found -> pool not computable")
# REPM scheme
print("REPM scheme outlay Rs 7,280 crore for 6,000 tpa; 25 firms at pre-bid; capex route, not Rs 0")

print("\n=== T1: field tester for scrap CRGO in distribution transformers (instrument, B2B) ===")
base = dict(utilities=70, sites_per_util=3, labs=30, price=6*LAKH, share24=0.15, margin=0.40,
            hours_per_unit=80, dev_cost=15*LAKH, fixed_month=40000, months=24, deposit=0.5)
def t1(p):
    sites = p['utilities']*p['sites_per_util'] + p['labs']
    units = sites*p['share24']
    rev = units*p['price']
    gm = rev*p['margin']
    fixed = p['dev_cost'] + p['fixed_month']*p['months']
    hours = units*p['hours_per_unit']
    own = hours*HOUR
    net = gm - fixed - own
    annual = (gm - fixed)/ (p['months']/12)
    return dict(sites=sites, units=units, rev=rev, gm=gm, fixed=fixed, hours=hours, hours_per_month=hours/p['months'],
                net_after_own_time=net, annual_pay_before_own_time=annual,
                preorders_needed=p['dev_cost']/(p['deposit']*p['price']))
r = t1(base)
for k,v in r.items(): print(f"  {k}: {v:,.1f}")
print("  verdict base:", "positive after own time" if r['net_after_own_time']>0 else "negative", "| FT-equivalent:", r['annual_pay_before_own_time']>=HOUR*FT_HOURS)
print("  sensitivity (one unsourced input halved at a time):")
for k in ('utilities','sites_per_util','labs','price','share24','margin'):
    q = copy.deepcopy(base); q[k] = q[k]/2
    rr = t1(q)
    print(f"   {k} halved -> net after own time {fmt(rr['net_after_own_time'])}; annual pay {fmt(rr['annual_pay_before_own_time'])}; FT-equiv {rr['annual_pay_before_own_time']>=HOUR*FT_HOURS}")
q = copy.deepcopy(base); q['dev_cost'] *= 2
rr = t1(q); print(f"   dev_cost doubled -> net {fmt(rr['net_after_own_time'])}; pre-orders needed {rr['preorders_needed']:.1f}")
q = copy.deepcopy(base); q['share24']=0.0
print("   share24 = 0 (no utility funds it): loss =", fmt(-(base['dev_cost']+base['fixed_month']*24)))

print("\n=== T2 bet: harmonically tuned large temple bell, cast by subcontract foundry ===")
bell = dict(weight_kg=700, cost_per_kg=(1000,1190), price=10*LAKH, units_year=10, design_hours=80, deposit=0.40, foundry_advance=0.5)
# S: Rs 21 lakh and Rs 25 lakh for ~2,100/2,400 kg bell => cost per kg
print("  cost/kg from reports: 21 lakh/2100 kg =", 21*LAKH/2100, "; 25 lakh/2400 kg =", round(25*LAKH/2400), "; 25 lakh/2100 =", round(25*LAKH/2100))
def bellcalc(price, cpk, units, hrs):
    cost = bell['weight_kg']*cpk
    margin = price - cost
    pay_unit = margin - hrs*HOUR
    return cost, margin, pay_unit, pay_unit*units, margin*units
for cpk in bell['cost_per_kg']:
    c,m,pu,py,gy = bellcalc(bell['price'],cpk,bell['units_year'],bell['design_hours'])
    print(f"  cost/kg {cpk}: foundry cost {fmt(c)}, margin/bell {fmt(m)}, net after own time/bell {fmt(pu)}, per year {fmt(py)}, FT-equiv {gy>=HOUR*FT_HOURS}")
    adv = c*bell['foundry_advance']; dep = bell['price']*bell['deposit']
    print(f"    foundry advance {fmt(adv)} vs buyer deposit {fmt(dep)} -> cash gap {fmt(max(0,adv-dep))}")
print("  sensitivity: premium over foundry cost halved (premium = price - cost)")
for cpk in bell['cost_per_kg']:
    cost = bell['weight_kg']*cpk
    prem = bell['price']-cost
    c,m,pu,py,gy = bellcalc(cost+prem/2,cpk,bell['units_year'],bell['design_hours'])
    print(f"   cost/kg {cpk}: premium {fmt(prem)} -> {fmt(prem/2)}; net/bell {fmt(pu)}; per year {fmt(py)}; positive={pu>0}")
for name,kw in (("units/year halved",dict(units=5)),("design hours doubled",dict(hrs=160))):
    cpk=1190
    args=dict(price=bell['price'],cpk=cpk,units=bell['units_year'],hrs=bell['design_hours']); args.update(kw)
    c,m,pu,py,gy = bellcalc(**args)
    print(f"   {name} (cost/kg {cpk}): net/bell {fmt(pu)}, per year {fmt(py)}, FT-equiv {gy>=HOUR*FT_HOURS}")
print("  buyers' pricing check: bell price Rs 8 lakh at 1000-1190/kg buys", round(8*LAKH/1190), "to", round(8*LAKH/1000), "kg of cost-equivalent bell")

print("\n=== T3 bet: magnetic-domain display table (grain-oriented steel + viewing film) ===")
art = dict(price=7.5*LAKH, cost_frac=0.45, units=4, hours=150)
def artc(price,cost_frac,units,hours):
    m = price*(1-cost_frac); pu = m - hours*HOUR; return m,pu,pu*units,m*units
m,pu,py,gy = artc(**art)
print(f"  margin/piece {fmt(m)}, net after own time {fmt(pu)}, year {fmt(py)}, FT-equiv {gy>=HOUR*FT_HOURS} (FT needs {fmt(HOUR*FT_HOURS)} gross margin)")
for u in (8,12):
    a=dict(art); a['units']=u; m,pu,py,gy=artc(**a); print(f"  units/year {u}: year {fmt(py)}, FT-equiv {gy>=HOUR*FT_HOURS}")
a=dict(art); a['price']/=2; m,pu,py,gy=artc(**a); print(f"  price halved: net/piece {fmt(pu)}, year {fmt(py)}")
a=dict(art); a['units']/=2; m,pu,py,gy=artc(**a); print(f"  units halved: year {fmt(py)}")
