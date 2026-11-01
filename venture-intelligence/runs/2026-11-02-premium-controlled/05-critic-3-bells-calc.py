"""Critic 3: unit economics of one tuned cast bronze bell, India. All inputs labelled.
Run: python3 05-critic-3-bells-calc.py"""
import itertools
USD_INR=89  # [A]
def unit(price_ex_gst, kg, cu=1000, sn_usd_t=52913, melt_loss=0.08, cast_labour_per_kg=250,
         tune_hours=40, tune_rate=400, tooling=15000, design_hours=60, logistics=15000,
         foundry_margin=0.15, founder_rate=750, founder_hours_sale=60, buyer_acq=20000):
    sn=sn_usd_t*USD_INR/1000
    metal_per_kg=(0.78*cu+0.22*sn)/(1-melt_loss)
    metal=kg*metal_per_kg
    cast=kg*cast_labour_per_kg
    tune=tune_hours*tune_rate
    foundry_cost=(metal+cast+tune+tooling)*(1+foundry_margin)  # foundry's price to founder
    founder_time=(design_hours+founder_hours_sale)*founder_rate
    total=foundry_cost+logistics+buyer_acq+founder_time
    return dict(metal_per_kg=round(metal_per_kg),foundry_price=round(foundry_cost),
                founder_time=founder_time,total=round(total),net=round(price_ex_gst-total),
                net_cash_before_time=round(price_ex_gst-(foundry_cost+logistics+buyer_acq)))
print("BASE: Rs 7.5 lakh ex-GST, 300 kg")
print(unit(750000,300))
print("\nMarket price per kg implied by listings: 500kg Rs8.5L=%d, 750kg Rs15L=%d, 1000kg Rs18L=%d, Ayodhya 2400kg Rs25L=%d, 2100kg Rs21L=%d"%(
 850000/500,1500000/750,1800000/1000,2500000/2400,2100000/2100))
print("\nWeight a Rs 5/7.5/10 lakh bell buys at 1,700-2,000 per kg:",[round(p/k) for p in (500000,750000,1000000) for k in (1700,2000)])
print("\nSENSITIVITY (each unsourced input made unfavourable by half, i.e. cost x1.5 or hours x1.5; one at a time)")
base=unit(750000,300)['net']
tests={'tune_hours 40->60':dict(tune_hours=60),'tune_rate 400->600':dict(tune_rate=600),
 'cast_labour 250->375':dict(cast_labour_per_kg=375),'tooling 15k->22.5k':dict(tooling=22500),
 'foundry_margin 15%->22.5%':dict(foundry_margin=0.225),'logistics 15k->22.5k':dict(logistics=22500),
 'founder_hours_sale 60->90':dict(founder_hours_sale=90),'buyer_acq 20k->30k':dict(buyer_acq=30000),
 'Cu Rs1000->1500':dict(cu=1500)}
for k,v in tests.items(): print(f"{k:28s} net Rs {unit(750000,300,**v)['net']:>9,} (base {base:,})")
print("\nGRID net (founder time included) by price and kg, base other inputs")
for p in (500000,750000,1000000):
    print(p,[ (kg,unit(p,kg)['net']) for kg in (150,250,350,500)])
print("\nCo-owned set of 12, each bell Rs 7.5L ex-GST, 12 x 120 kg bells, shared design 120h, 12 buyers each 60h sale")
s=[unit(750000,120,design_hours=10,tune_hours=40) for _ in range(12)]
print("net per bell",s[0]['net'],"set net",sum(x['net'] for x in s))
print("\nBuyers needed for the set: 12 distinct buyers; if conversion from conversation to Rs7.5L purchase is 2%, conversations needed =",12/0.02)
print("\nYearly: founder income at Rs750/h, 1800 h = Rs",750*1800)
for n in (2,4,6,8):
    b=unit(750000,300)
    print(n,"bells/yr: cash net before founder time",n*b['net_cash_before_time'],"vs hours cost",n*(60+60)*750)
