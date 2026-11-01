#!/usr/bin/env python3
# Independent recalculation of the Rs 3.5 lakh/yr battery-buffered induction claim.
# All inputs labelled; unofficial tariff numbers are the hunter's/NoBroker values, UNVERIFIED against MERC.
import json
LPG_PRICE = {"low":2091.0,"base":2764.5,"high":3128.0}   # Rs per 19 kg
KWH_PER_KG=12.8; KG=19; DAYS=30
GAS_EFF=0.40; IND_EFF=0.85
T_LOW=dict(energy=10.11, fixed=540.0)        # <=20 kW, per kWh (incl wheeling) + Rs/month
T_HIGH=dict(energy=13.92, demand=550.0)      # >20 kW per kVAh + Rs/kVA/month
useful_day = KG*KWH_PER_KG*GAS_EFF           # kWh useful heat per cylinder-day
elec_day = useful_day/IND_EFF
E = elec_day*DAYS
print(f"useful {useful_day:.1f} kWh/day, elec {elec_day:.1f} kWh/day, {E:.0f} kWh/month, avg draw over 12h {elec_day/12:.1f} kW")
cases = {
 "favourable":   dict(lpg="high", peak=26, rush_h=1.5, kwh_cost=18000, pcs=100000, inst=30000, cycles=5000),
 "base":         dict(lpg="base", peak=30, rush_h=2.0, kwh_cost=21600, pcs=160000, inst=50000, cycles=4000),
 "conservative": dict(lpg="low",  peak=32, rush_h=2.5, kwh_cost=30000, pcs=240000, inst=80000, cycles=3000),
}
out={}
for n,c in cases.items():
    lpg_m = LPG_PRICE[c["lpg"]]*DAYS
    cost_low = E*T_LOW["energy"]+T_LOW["fixed"]
    cost_high = E*T_HIGH["energy"]+c["peak"]*T_HIGH["demand"]
    induction_part = lpg_m-cost_high           # saving anyone selling induction gets, at >20 kW tariff
    step_part = cost_high-cost_low             # saving only if battery keeps sanctioned load/tariff <=20 kW
    excess = c["peak"]-20
    usable = excess*c["rush_h"]
    nominal = usable/0.90
    capex = nominal*c["kwh_cost"]+c["pcs"]+c["inst"]
    # two rushes/day -> 2 cycles/day
    thr = 2*usable
    loss_kwh_m = thr*(1/0.92-1)*DAYS
    loss_cost_m = loss_kwh_m*T_LOW["energy"]
    maint_m = 0.02*capex/12
    life_y = c["cycles"]/(2*365)
    net_m = step_part - loss_cost_m - maint_m
    payback_y = capex/(net_m*12) if net_m>0 else float("inf")
    repl_cost = nominal*c["kwh_cost"]*0.6   # assume pack price falls 40% by replacement
    repl = life_y<5
    net5 = net_m*60 - capex - (repl_cost if repl else 0)
    # alternative: stay at 20 kW with induction, cover excess energy with LPG
    shifted_elec = thr  # kWh/day elec above cap
    gas_kwh_fuel = shifted_elec*IND_EFF/GAS_EFF
    gas_cost_m = gas_kwh_fuel/KWH_PER_KG/KG*LPG_PRICE[c["lpg"]]*DAYS
    elec_m_hybrid = (E-thr*DAYS)*T_LOW["energy"]+T_LOW["fixed"]
    hybrid_total = gas_cost_m+elec_m_hybrid
    out[n]=dict(lpg_month=round(lpg_m),elec_month_over20=round(cost_high),elec_month_under20=round(cost_low),
      induction_part_month=round(induction_part),step_part_month=round(step_part),step_part_year=round(step_part*12),
      usable_kwh=usable,nominal_kwh=round(nominal,1),capex=round(capex),loss_cost_m=round(loss_cost_m),maint_m=round(maint_m),
      net_m=round(net_m),payback_years=round(payback_y,2),life_years=round(life_y,1),replacement_in_5y=repl,
      replacement_cost=round(repl_cost) if repl else 0,net5y=round(net5),
      hybrid_lpg_assist_month_total=round(hybrid_total),hybrid_vs_over20_saving_m=round(cost_high-hybrid_total),
      hybrid_vs_battery_m=round(hybrid_total-(cost_low+loss_cost_m+maint_m)))
    # if discom refuses: step_part = 0
    out[n]["net5y_if_discom_refuses"]=round(-capex)
# hunter reproduction
hunter_step=(3430*13.92+30*550)-(3430*10.11+540)
out["hunter_repro_step_year"]=round(hunter_step*12)
json.dump(out,open("03-recalc-output.json","w"),indent=1)
print(json.dumps(out,indent=1))
