# Broiler kit audit calc. All inputs are assumptions unless stated in the audit file.
birds=2236; wt=2.0; kg=birds*wt
print("load kg",kg)
# 1 reproduce hunter
for name,shr,price,trips in [("low",.0236,90,150),("high",.0301,130,250)]:
    loss=kg*shr*price; save=loss*.05; yr=save*trips
    print(name,"loss/trip",round(loss),"5%/trip",round(save),"yr",round(yr),"payback mo",round(50000/yr*12,1))
# 2 mismatched pairing: same trips, low/high loss
# 3 realistic: heat-avoidable share only in hot trips
kit_cost=0
bom={"tank 500 L":4000,"12V pump":3000,"nozzles+hose":2500,"4 DC fans":6000,"wiring+battery/inverter":6000,"install labour":3000}
kit_cost=sum(bom.values()); print("BOM",kit_cost,bom)
sell=round(kit_cost/0.6,-3); print("sell price ex GST at 40% GM",sell,"incl 18% GST",round(sell*1.18))
print("capital first 50 kits: build",50*kit_cost,"+ 3 mo working cap, 1 install tech, demo truck")
# benefit scenarios: who captures? hot trips only
for hot_trips in (60,100,150):
  for price in (90,110,130):
    for rec_pp in (0.1,0.3,0.65):   # recovery in percentage points of body weight
        v=kg*rec_pp/100*price*hot_trips
        print(f"hot{hot_trips} price{price} rec{rec_pp}pp: Rs/yr {v:,.0f}  payback@{sell} {sell/v*12:.1f} mo")
# 5% of loss in pp terms
print("5% of 2.36..3.01pp =",.05*2.36,.05*3.01,"pp; summer-winter gap",3.01-2.36,"pp (not significant per study)")
# mortality: 0.5% of 2236 birds =
dead=birds*.0053; print("dead/trip",dead, "value Rs",dead*wt*110)
