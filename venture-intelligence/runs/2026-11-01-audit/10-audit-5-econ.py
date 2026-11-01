# Economics for C4 grading lab. All inputs are assumptions unless noted.
fee=3000
for name,cost,fixed in [("hunter",1200,1050000),("rented lab, cost 2000/sample, fixed 4 lakh",2000,400000),("own GC-MS, cost 800, fixed 25 lakh",800,2500000)]:
    be=fixed/(fee-cost); print(name,"break-even samples/yr",round(be))
# kg chips value
price_kg=235e5/112; print("first export Rs/kg",round(price_kg),"fee % of 1kg",round(fee/price_kg*100,2))
# lot-count scenarios: kg exported per year vs lots
for kg in (112,1000,10000,151080):
    for lot in (5,20):
        lots=kg/lot; print("export kg",kg,"lot kg",lot,"lots",round(lots),"samples@2/lot",round(lots*2),"revenue Rs",round(lots*2*fee))
# own GC-MS capital 25 lakh at 5 samples/day utilisation
print("revenue at 583 samples", 583*fee)
