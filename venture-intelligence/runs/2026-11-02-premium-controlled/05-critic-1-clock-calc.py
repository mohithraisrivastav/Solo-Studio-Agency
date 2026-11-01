"""Unit economics of a hand-built tithi/nakshatra table clock, Rs 8 lakh. All inputs are [A] assumptions
(no workshop quote exists); the point is sensitivity, not a forecast."""
import itertools
PRICE = 800_000          # Rs, ex-GST (assume the 8 lakh is net of GST)
FOUNDER_RATE = 750       # Rs/h stated by the brief
BASE = dict(
    dev_hours=1200,      # design + prototype of a true-motion tithi/nakshatra train (cams for lunar anomaly)
    dev_rate=1500,       # Rs/h for a skilled independent watchmaker in India (assumed)
    build_hours=250,     # hand build, finish, regulate, test per piece
    build_rate=1000,     # Rs/h
    parts=150_000,       # Rs per piece: metal, wheels, jewels, dial (enamel/engraved), case, wooden/ glass
    scrap_pct=0.15,      # remake allowance on parts+build
    founder_hours=250,   # selling, trust paperwork, coordination, delivery, per piece
    warranty_pct=0.05,   # of price, service/after-sales provision
    commission_pct=0.10, # introducer / intermediary fee
)
def unit(n, **kw):
    p = {**BASE, **kw}
    dev = p['dev_hours']*p['dev_rate']/n
    build = p['build_hours']*p['build_rate']*(1+p['scrap_pct'])
    parts = p['parts']*(1+p['scrap_pct'])
    other = PRICE*(p['warranty_pct']+p['commission_pct'])
    cost = dev+build+parts+other
    fh = p['founder_hours']
    gross = PRICE-cost
    founder_value = fh*FOUNDER_RATE
    return dict(n=n, dev=dev, build=build, parts=parts, other=other, cost=cost, margin=gross,
                margin_pct=gross/PRICE, after_founder_time=gross-founder_value,
                per_founder_hour=gross/fh)
def show(label, **kw):
    print(label)
    for n in (1,3,10,25):
        u = unit(n, **kw)
        print(f"  n={n:>2} cost Rs{u['cost']:>10,.0f} margin Rs{u['margin']:>10,.0f} ({u['margin_pct']:6.1%})  "
              f"after founder time Rs{u['after_founder_time']:>10,.0f}  Rs/founder-hour {u['per_founder_hour']:,.0f}")
show("BASE")
show("DEV HOURS halved (favourable)", dev_hours=600)
show("DEV HOURS x2 (unfavourable)", dev_hours=2400)
show("RATES x2 (Swiss-like independent)", dev_rate=3000, build_rate=2000)
show("PARTS x2", parts=300_000)
show("BUILD HOURS x2", build_hours=500)
show("ALL unfavourable by half (dev x1.5, rates x1.5, parts x1.5, build x1.5)",
     dev_hours=1800, dev_rate=2250, build_hours=375, build_rate=1500, parts=225_000)
show("ALL favourable by half", dev_hours=600, dev_rate=750, build_hours=125, build_rate=500, parts=75_000)
# Deposit funding: 50% deposit pre-build, and whether it covers dev + build cash
for dep in (0.3,0.5):
    cash_need_first = BASE['dev_hours']*BASE['dev_rate'] + BASE['build_hours']*BASE['build_rate'] + BASE['parts']
    print(f"deposit {dep:.0%} = Rs{PRICE*dep:,.0f}; cash needed before delivery of piece 1 = Rs{cash_need_first:,.0f}; "
          f"gap = Rs{cash_need_first-PRICE*dep:,.0f}")
# Pieces per year needed for the margin to pay Rs 15 lakh (2000 h x Rs 750) of founder time, series of 10
target = 2000*750
for n in (10,25):
    u = unit(n)
    if u['margin']<=0: print(f"series {n}: margin negative, no volume pays the founder"); continue
    k = target/u['margin']
    print(f"series {n}: margin/piece Rs{u['margin']:,.0f}; pieces/yr for Rs{target:,} = {k:.1f}; founder hours at 250/piece = {k*250:,.0f}; watchmakers needed (250 h/piece, 1800 h/yr) = {k*250/1800:.1f}")
cash = BASE['dev_hours']*BASE['dev_rate']+BASE['build_hours']*BASE['build_rate']+BASE['parts']
for dep in (0.3,0.5):
    print(f"deposit {dep:.0%}=Rs{PRICE*dep:,.0f}; cash before delivery of piece 1=Rs{cash:,.0f}; gap=Rs{cash-PRICE*dep:,.0f}; deposits needed to cover = {cash/(PRICE*dep):.1f} buyers")
