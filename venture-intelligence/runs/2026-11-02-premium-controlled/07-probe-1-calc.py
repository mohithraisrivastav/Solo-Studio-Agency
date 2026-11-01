"""Probe 1: acoustic crack-grading station for Morbi. All inputs below are [A] unless noted.
Run: python3 07-probe-1-calc.py"""
import itertools
RATE=750  # Rs/h founder time (brief)
base=dict(
 tiles_per_hr=1200,        # A: 3 s per tap incl. handling, one operator
 hrs_per_day=20, days=300, util=0.5,   # A
 crack_rate=0.005,         # A: share of tiles with hidden crack reaching packing (no source found)
 catch=0.90,               # A: detection rate (RUV vendor claims 91-95% on other ceramics [S, search summary])
 false_rej=0.01,           # A: good tiles wrongly rejected
 cost_escape=300,          # A Rs: claim/replace/goodwill cost per cracked tile that escapes (no source found)
 tile_value=250,           # A Rs ex-factory value of a good tile, lost on false reject (downgrade to 50%)
 manual_catch=0.40,        # A: what manual tapping/eye already catches
 labour_saved_per_yr=0,    # A: tapping workers not replaced (conservative)
 price=600000, bom=150000, # price brief; BOM A
 sell_h=80, install_h=40, service_h_yr=20, # A founder hours
 life_yr=5)
def buyer(p):
    n=p['tiles_per_hr']*p['hrs_per_day']*p['days']*p['util']
    extra=p['catch']-p['manual_catch']
    gain=n*p['crack_rate']*extra*p['cost_escape']
    loss=n*(1-p['crack_rate'])*p['false_rej']*p['tile_value']*0.5
    net=gain-loss+p['labour_saved_per_yr']
    return n,gain,loss,net
def seller(p):
    gm=p['price']-p['bom']
    hrs=p['sell_h']+p['install_h']
    cost_time=hrs*RATE
    first_year=gm-cost_time-p['service_h_yr']*RATE
    return gm,hrs,cost_time,first_year
n,g,l,net=buyer(base)
print("tiles/yr per station",int(n)); print("gain",int(g),"loss",int(l),"net saving/yr",int(net))
print("payback yr", round(base['price']/net,2) if net>0 else "never")
gm,hrs,ct,fy=seller(base)
print("seller gross margin/unit",gm,"founder h/unit",hrs,"time cost",ct,"net per unit yr1",fy)
# units/yr needed to pay founder Rs 12 lakh/yr (1600 h x 750) 
target=1600*RATE
print("units/yr to earn",target,":",round(target/fy,1),"founder h:",round(target/fy*hrs))
print("100 customers: capital for BOM",100*base['bom'],"founder hours",100*hrs)
# sensitivity: each unsourced input made unfavourable by half
unfav=dict(crack_rate=lambda v:v/2,catch=lambda v:v-(v-base['manual_catch'])/2,
 cost_escape=lambda v:v/2,manual_catch=lambda v:v+(1-v)/2*0.5,util=lambda v:v/2,
 false_rej=lambda v:v*2,bom=lambda v:v*1.5,sell_h=lambda v:v*2)
print("\nsensitivity (payback yr, net saving/yr):")
for k,f in unfav.items():
    p=dict(base); p[k]=f(p[k]); _,_,_,nt=buyer(p); gm2,_,_,fy2=seller(p)
    print(f"{k:12s} net={int(nt):>9} payback={'never' if nt<=0 else round(p['price']/nt,2)} seller_yr1={int(fy2)}")
p=dict(base)
for k,f in unfav.items(): p[k]=f(p[k])
_,_,_,nt=buyer(p); print("ALL unfavourable: net",int(nt),"payback","never" if nt<=0 else round(p['price']/nt,1))
# break-even crack rate for 2-yr payback (Rs 6L)
for cr in (0.001,0.002,0.005,0.01,0.02):
    p=dict(base); p['crack_rate']=cr; print("crack_rate",cr,"net",int(buyer(p)[3]),"payback",round(p['price']/buyer(p)[3],2) if buyer(p)[3]>0 else 'never')
# reachable
for units in (400,1200):
    print("units",units,"x 1 station each at 5% adoption yr",units*0.05)
# even-if-true case: open points resolve favourably (crack 1%, false reject 0.3%, escape cost Rs 500)
p=dict(base); p.update(crack_rate=0.01,false_rej=0.003,cost_escape=500)
n_,g_,l_,nt_=buyer(p); print("\nEVEN-IF-TRUE net",int(nt_),"payback",round(p['price']/nt_,2))
# prior-art-free single price check: seller needs 3.5 units/yr; reachable 400-1200 factories; stations/line = tiles per line/1200
print("stations per 60,000 tiles/day line at 20h:",round(60000/20/1200,1))
