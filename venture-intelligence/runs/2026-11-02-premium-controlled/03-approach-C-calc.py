"""Approach C sizing and sensitivity. All inputs tagged in the report. INR."""
HOURLY=1000; HOURS=1800
threshold=HOURLY*HOURS  # [A] founder alternative value Rs 18 lakh/yr
print("founder alternative threshold Rs", threshold)

def clock(price=750000, cogs_share=0.60, pieces=8, hours_per_piece=120, other=300000):
    rev=price*pieces; gm=rev*(1-cogs_share)
    net=gm-other; hrs=hours_per_piece*pieces
    return rev, net, hrs
print("\nA. Mechanical tithi clock (own-sale, pre-order)")
for label,kw in [("base",{}),("pieces halved",{"pieces":4}),("price halved",{"price":375000}),
                 ("cogs share 0.8",{"cogs_share":0.8}),("hours/piece doubled",{"hours_per_piece":240})]:
    rev,net,hrs=clock(**kw); print(f"{label:22s} rev {rev:>9,.0f} net {net:>9,.0f} hours {hrs:>5} net/hr {net/hrs:>7,.0f} beats threshold {net>=threshold}")
# licence variant: royalty on a maker's sales
for roy,units in [(0.08,20),(0.08,10),(0.04,20)]:
    inc=roy*750000*units; print(f"licence royalty {roy:.0%} x {units} units/yr: Rs {inc:,.0f}")
# deposits fund first unit
price=750000; dep=0.5; cogs=price*0.60
print("deposit 50% =",price*dep,"vs cogs",cogs,"-> covers cogs:",price*dep>=cogs)
print("deposit 50% covers cogs if cogs share <=",dep)

print("\nB. Predator-proof pen kits to forest depts")
def pen(units=1000,price=30000,margin=0.15,sales_cost=400000):
    rev=units*price; return rev, rev*margin-sales_cost
for label,kw in [("base",{}),("units halved",{"units":500}),("margin halved",{"margin":0.075}),("both halved",{"units":500,"margin":0.075})]:
    rev,net=pen(**kw); print(f"{label:16s} rev {rev:>10,.0f} net {net:>10,.0f} beats {net>=threshold}")
print("goat kills avoided to repay Rs 30000 shed at Rs 15000 compensation:",30000/15000)
print("Nashik cages Rs 6.5 crore /500 =",6.5e7/500)
print("Junnar fence subsidy 75% of 30000 =",0.75*30000,"; farmers 660 x 30000 =",660*30000)

print("\nC. Forensic evidence kits, one-state tender stream")
def kit(districts=75,tender=1200000,margin=0.10,cost=500000):
    rev=districts*tender; return rev, rev*margin-cost
for label,kw in [("base",{}),("districts halved",{"districts":37}),("margin halved",{"margin":0.05}),("both",{"districts":37,"margin":0.05}),("win rate 20% of base",{"districts":15})]:
    rev,net=kit(**kw); print(f"{label:22s} rev {rev:>11,.0f} net {net:>10,.0f} beats {net>=threshold}")
print("Prayagraj 13.6 lakh, Mirzapur 10.6 lakh; mean",(1360000+1060000)/2)
print("\nD. Memorial gem: Rs per unit at USD 1400-3000 @ Rs 88/USD [A]:",1400*88,3000*88)
print("E. Hi-fi: Rethm USD 10750 @88 =",10750*88)
