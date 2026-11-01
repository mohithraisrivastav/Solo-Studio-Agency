"""CRGO core-steel tester: seller economics and sensitivity. INR. All inputs tagged in the report."""
THRESH = 750*1800   # founder hourly value x 1,800 h/yr [A: 1,800 h is an assumption]
print("founder threshold Rs", THRESH)

def model(buyers_instr=60, instr_price=300000, instr_cost=120000, instr_sales_cost_per_unit=40000,
          yrs=3, tests_per_yr=1500, fee=3000, test_cost=1200, fixed_yr=300000, dev_cost=1500000):
    instr_margin = buyers_instr*(instr_price-instr_cost-instr_sales_cost_per_unit)/yrs
    svc_margin = tests_per_yr*(fee-test_cost)
    net_yr = instr_margin + svc_margin - fixed_yr
    return instr_margin, svc_margin, net_yr, dev_cost

base = dict()
cases = [("base",{}),
 ("buyers halved (30)",{"buyers_instr":30}),
 ("price halved (1.5 lakh)",{"instr_price":150000}),
 ("tests/yr halved (750)",{"tests_per_yr":750}),
 ("fee halved (1500)",{"fee":1500}),
 ("unit cost x1.5 (1.8 lakh)",{"instr_cost":180000}),
 ("all unsourced halved",{"buyers_instr":30,"instr_price":150000,"tests_per_yr":750,"fee":1500})]
for lab,kw in cases:
    i,s,n,d = model(**kw)
    print(f"{lab:28s} instr/yr {i:>10,.0f} svc/yr {s:>10,.0f} net/yr {n:>10,.0f} beats threshold {n>=THRESH} payback_dev_yrs {d/n if n>0 else float('inf'):.1f}")

# reachable buyer count
print("\nReachable buyers: DISCOM-type utilities 72 (PFC 12th round) ; inspection agencies [A] 15; labs [A] 30 ->", 72+15+30)
# favourable case: every reachable buyer buys one instrument at 3 lakh
print("ceiling, every reachable buyer buys 1 unit at Rs 3 lakh: Rs", (72+15+30)*300000)
# utility benefit
dt_fail_low, dt_fail_high = 6e5, 8e5   # BIS training slide: 6-8 lakh DT failures/yr
cost_per_fail = 100000                  # [A] Rs 1 lakh replacement/repair net, unsourced
for share in (0.01,0.05,0.2):
    print(f"if {share:.0%} of failures traced to substandard core: Rs {dt_fail_low*share*cost_per_fail:,.0f} to {dt_fail_high*share*cost_per_fail:,.0f} per yr nationally")
# test fee vs existing third-party inspection day
print("\nMSEDCL inspection rate Rs 10,000 + 1,800 travel per visit; my fee Rs 3,000 is", 3000/11800, "of one inspection visit")
# unit cost with no-load test already done: marginal info
print("hours to sell 60 units at 12 months/sale, 40 h per sale:", 60*40, "h =", 60*40*750, "Rs of founder time")
