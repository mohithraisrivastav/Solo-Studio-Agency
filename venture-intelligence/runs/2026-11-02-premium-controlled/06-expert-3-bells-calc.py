#!/usr/bin/env python3
"""Bell acoustics, scaling, tolerance and metal-cost sanity calcs. Pure stdlib."""
import math
c = lambda r: 1200*math.log2(r)          # ratio -> cents
note = lambda f: ("C C# D D# E F F# G G# A A# B".split()[round(12*math.log2(f/440)+9)%12]
                  + str(4+(round(12*math.log2(f/440)+9))//12))

print("== 1. Ideal European partial ladder (nominal N=1) ==")
N = 1.0
ideal = {"hum":0.25,"prime":0.5,"tierce":0.6,"quint":0.75,"nominal":1.0,"superquint":1.5}
for k,v in ideal.items(): print(f"{k:11s} ratio to nominal {v:5.3f}  ratio to prime {v/0.5:5.3f}  cents above hum {c(v/0.25):7.1f}")
# strike note: virtual pitch of nominal:superquint:octave-nominal = 2:3:4 -> fundamental N/2 = prime
print("strike note (virtual pitch of 2:3:4 series) = N/2 =", ideal["prime"], "of nominal -> equals prime pitch")
print("tierce/prime = 6/5 (just minor third %.1f cents; ET minor third 300 cents)" % c(1.2))
print("=> a bell sounds 'minor' by design; major-third tuned bells are a special modern design")

print("\n== 2. Scaling: frequency ~ 1/D, mass ~ D^3 for similar shape ==")
# calibration [A]: 1.00 m diameter, 78/22 bronze, English-profile, ~600 kg, prime ~196 Hz (G3)
D0, M0, F0 = 1.00, 600.0, 196.0
print(f"calibration D0={D0} m M0={M0} kg prime F0={F0} Hz  (assumption, +/-20% on mass)")
for sem in (1,12): print(f"{sem} semitone(s) lower pitch at same shape: mass x{2**(3*sem/12):.3f}, diameter x{2**(sem/12):.3f}")
def bell(f): 
    D = D0*F0/f; return D, M0*(D/D0)**3
print("\nLarge single bell options (prime Hz -> D, mass)")
for f in (110,130.8,165,196,261.6):
    D,M = bell(f); print(f"prime {f:6.1f} Hz ({note(f)}) D={D:.2f} m  mass={M:7.0f} kg")
print("check vs reported Ayodhya bell: 2100 kg ->D=", round(D0*(2100/M0)**(1/3),2), "m (reported ~5 ft = 1.52 m); prime", round(F0/(D0*(2100/M0)**(1/3)),1),"Hz")

print("\n== 3. Twelve-bell chromatic set, prime tuned ET, A4=440 ==")
def setmass(f_low):
    tot=0; rows=[]
    for i in range(12):
        f=f_low*2**(i/12); D,M=bell(f); tot+=M; rows.append((note(f),f,D,M))
    return tot,rows
for label,f_low in (("tabletop C5-B5",523.25),("hall G3-F#4",196.0)):
    tot,rows=setmass(f_low)
    print(label, f"total mass {tot:.1f} kg; heaviest {rows[0][3]:.1f} kg D={rows[0][2]:.2f} m; lightest {rows[-1][3]:.1f} kg D={rows[-1][2]:.2f} m")

print("\n== 4. Tolerance: wall-thickness error -> pitch error ==")
# thin-shell: df/f ~ k * dt/t ; k ~0.5-1 for local removal [A]; sound bow t ~ D/15 (English) [K]
for D in (0.4,1.0,1.5):
    t = D/15*1000
    for dt in (0.5,1,2,3):
        for k in (0.5,1.0):
            pass
    print(f"D={D} m, sound-bow t~{t:.0f} mm: " + "; ".join(f"dt={dt} mm -> {c(1-k*dt/t):+.0f}..{c(1-0.5*dt/t):+.0f} cents" for dt,k in ((0.5,1.0),(1,1.0),(2,1.0),(3,1.0))))
print("1% change in thickness/frequency =", round(c(1.01),1), "cents")
for tol_cents in (3,5,10,20,50,100):
    print(f"+/-{tol_cents} cents = +/-{(2**(tol_cents/1200)-1)*100:.2f}% frequency")
print("As-cast scatter if founder holds thickness to +/-3% (sand, core shift): ~ +/-52 cents [I from 1%=17 cents]")
print("Needed to tune to +/-5 cents (0.3%) by turning: remove metal only (lowers some partials, lip cut raises others)")

print("\n== 5. Metal cost, 78Cu/22Sn ==")
cu, sn, fx = 14.415, 50.855, 88.0   # USD/kg from LME cash 2026-10-23 (search summary), fx [A]
for label,cu_,sn_ in (("base",cu,sn),("tin -50%",cu,sn/2),("tin +25%",cu,sn*1.25)):
    p = 0.78*cu_+0.22*sn_
    print(f"{label:9s} alloy metal value {p:6.2f} USD/kg = INR {p*fx:7.0f}/kg (excl. melt loss, GST, fuel, labour)")
p=0.78*cu+0.22*sn
melt_loss = 1.08   # 8% melt/gating loss [A]; yield: fettle+turning loses ~10% [A]
for m in (3,31.6,60,600,1000,2100):
    print(f"cast bell {m:7.1f} kg: metal incl 8% melt loss and gating/returns not credited = INR {m*melt_loss*p*fx:,.0f}")
print("Ayodhya report INR 21 lakh /2100 kg = INR", round(21e5/2100), "/kg all-in (vs alloy metal-only INR", round(p*fx), "/kg) -> not 78/22 tin bronze or price is wrong")
print("Listing asks: INR 2,500/kg (1000 kg brass), 580-750/kg brass church bell, 2,200/kg copper bell-metal church bell")

print("\n== 6. Doublets: axisymmetry error -> beat ==")
for split_cents in (2,5,10,20):
    for f in (130,196,500):
        pass
    print(f"split {split_cents} cents at 196 Hz prime = beat {196*(2**(split_cents/1200)-1):.2f} Hz; at 523 Hz = {523*(2**(split_cents/1200)-1):.2f} Hz")

print("\n== 7. ET vs just vs shruti (cents from Sa) ==")
et=[100*i for i in range(12)]
ji=[0,111.7,203.9,315.6,386.3,498.0,590.2,702.0,813.7,884.4,996.1,1088.3]  # 5-limit/Hindustani-style 12
for n,(a,b) in zip("Sa re Re ga Ga ma Ma Pa dha Dha ni Ni".split(),zip(et,ji)): print(f"{n:3s} ET {a:5.0f}  JI {b:7.1f}  diff {b-a:+6.1f}")
print("22 shrutis: finer than 12 bells can supply; 12-bell set = 12 swarasthanas only")
print("max JI-vs-ET gap",max(abs(b-a) for a,b in zip(et,ji)),"cents -> needs tuning tolerance well below ~10 cents to be audible/defensible")
