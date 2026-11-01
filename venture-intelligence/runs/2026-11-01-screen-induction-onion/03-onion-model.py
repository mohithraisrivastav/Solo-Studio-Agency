# Buyer value and payback for a 25 t onion shed retrofit. All inputs are assumptions [A] except where noted in the report.
cap_t = 25
for kit in (25000, 40000):
    print("kit price INR", kit)
    for pts in (3, 5, 10):
        for p_q in (1000, 2000, 4000):   # INR per quintal at sale
            saved_q = cap_t*10*pts/100
            val = saved_q*p_q
            print(f" loss cut {pts} pts price {p_q}/q: saved {saved_q:.2f} q, value INR {val:,.0f}/season, simple payback {kit/val:.1f} seasons")
# Break-even loss reduction at price, kit 30000, 3 seasons life
for p_q in (1000,2000,4000):
    print("break-even pts for 1-season payback at kit 30000, price", p_q, "=", round(30000/(cap_t*10*p_q)*100,1))
# Fan energy cost small; ignore. Subsidised structure comparison
print("subsidy on standard 25t at 10000/t, 50%:", cap_t*10000*0.5, "owner pays", cap_t*10000*0.5)
