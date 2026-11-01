"""Approach B feasibility arithmetic. Run: python3 02-approach-B-calcs.py"""
import math, random
d2r=math.pi/180
# ---- 1. Tithi: mean vs true elongation (Meeus-style low-order terms, degrees) ----
def elong(T):  # T = days since J2000
    D =(297.8502+12.19074912*T)%360   # mean elongation
    M =(357.5291+0.98560028*T)%360    # sun anomaly
    Mp=(134.9634+13.06499295*T)%360   # moon anomaly
    F =(93.2721+13.22935*T)%360
    true = D + 6.289*math.sin(Mp*d2r)+1.274*math.sin((2*D-Mp)*d2r)+0.658*math.sin(2*D*d2r) \
           +0.214*math.sin(2*Mp*d2r)-0.186*math.sin(M*d2r)-0.114*math.sin(2*F*d2r) - 1.915*math.sin(M*d2r)
    terms = {'mean':D,
             '1cam (moon centre)':D+6.289*math.sin(Mp*d2r),
             '3cam (+evection,variation)':D+6.289*math.sin(Mp*d2r)+1.274*math.sin((2*D-Mp)*d2r)+0.658*math.sin(2*D*d2r)}
    return true,terms
rate=12.19074912
res={}
random.seed(1)
for n in range(3000):
    T=random.uniform(0,365.25*30)
    t,terms=elong(T)
    for k,v in terms.items():
        e=((v-t+180)%360)-180
        res.setdefault(k,[]).append(abs(e)/rate*24)
for k,v in res.items():
    v.sort(); print(f"tithi end-time error [{k}]: median {v[len(v)//2]:.1f} h, p95 {v[int(.95*len(v))]:.1f} h, max {v[-1]:.1f} h")
# ---- 2. Bragg band-gap for lattice pitch a: f = c/(2a) ----
c=343
for a in (0.04,0.08,0.15,0.30,0.60):
    print(f"lattice pitch {a*100:.0f} cm -> first Bragg gap ~{c/(2*a):.0f} Hz")
# ---- 3. Speculum mirror light gathering vs glass+Al ----
for D in (0.15,0.20,0.25):
    area=math.pi*(D/2)**2
    print(f"D={D*1000:.0f} mm: effective area speculum(R=0.65) {area*0.65*1e4:.0f} cm2 vs aluminised glass(R=0.88) {area*0.88*1e4:.0f} cm2; ratio {0.65/0.88:.2f}")
# ---- 4. Caustic geometry: image size from a lens-array panel ----
for h in (1.0,2.0,3.0):  # throw distance m
    for ang in (5,10,20):  # max ray deflection deg
        print(f"throw {h} m, max deflection {ang} deg -> image half-width ~{h*math.tan(ang*d2r):.2f} m")
# ---- 5. Unit economics (INR). [A] all inputs; test with unfavourable halves ----
def margin(price,units,cost,fixed,hours_per_unit):
    gm=price-cost; tot=gm*units-fixed; hrs=hours_per_unit*units
    return gm,tot,hrs,(tot/hrs if hrs else 0)
leads={
 'P1 panchang clock':dict(price=800000,units=10,cost=300000,fixed=300000,hrs=250),
 'P2 caustic glass': dict(price=700000,units=8, cost=250000,fixed=200000,hrs=150),
 'P3 acoustic jali': dict(price=600000,units=10,cost=250000,fixed=200000,hrs=120),
 'P4 speculum scope':dict(price=600000,units=8, cost=200000,fixed=150000,hrs=200),
}
for name,p in leads.items():
    base=margin(p['price'],p['units'],p['cost'],p['fixed'],p['hrs'])
    # unfavourable: price -50%? too harsh for price; apply halves to units, and cost +50%, then both
    u=margin(p['price'],p['units']/2,p['cost'],p['fixed'],p['hrs'])
    c_=margin(p['price'],p['units'],p['cost']*1.5,p['fixed'],p['hrs'])
    p_=margin(p['price']*0.5,p['units'],p['cost'],p['fixed'],p['hrs'])
    b=margin(p['price']*0.5,p['units']/2,p['cost']*1.5,p['fixed'],p['hrs'])
    f=lambda x:f"gm/unit {x[0]/1e5:.1f}L, yr surplus {x[1]/1e5:.1f}L, hrs {x[2]:.0f}, Rs/h {x[3]:.0f}"
    print(name); print('  base       ',f(base)); print('  units/2    ',f(u)); print('  cost x1.5  ',f(c_)); print('  price/2    ',f(p_)); print('  all adverse',f(b))
# ---- 6. Tech: tap-test station ----
print('Tap-test: if 1 station replaces 2 inspectors at Rs 20k/month each: annual saving',2*20000*12,'INR [A]; payback on Rs 6 lakh price =',6e5/(2*20000*12),'yr')
# ---- 7. Acoustic ID: per-piece cert fee ----
print('Acoustic ID: 200 pieces/yr x Rs 2,000 [A] =',200*2000,'INR/yr - too small alone; needs licence to many makers')
# ---- 8. Caustic legibility: sun disc 0.533 deg blur and drift ----
sun=0.533*d2r
for h in (1.0,2.0,3.0):
    blur=h*math.tan(sun)
    for ang in (10,20):
        hw=h*math.tan(ang*d2r)
        print(f"throw {h} m: sun blur {blur*100:.1f} cm; image width {2*hw*100:.0f} cm -> ~{2*hw/blur:.0f} resolvable elements across; image drift ~{h*15*d2r:.2f} m/h at normal incidence")
# ---- 9. Acoustic ID: modal drift with temperature (f ~ sqrt(E)); E tempcoef assumed -4e-4/K for bronze [K/A] ----
for dT in (5,10,20):
    print(f"dT {dT} K -> freq shift ~{0.5*4e-4*dT*100:.2f} %  (at 1 kHz: {1000*0.5*4e-4*dT:.1f} Hz)")
# ---- 10. FX assumptions [A]: 1 USD = Rs 85 ; 1 GBP = Rs 110 ----
print('USD 4,500 =',4500*85,'INR; USD 7,800 =',7800*85,'INR; GBP 6,000-11,000 =',6000*110,'-',11000*110,'INR; USD 25,084 =',25084*85,'INR; USD 77,500=',77500*85)
