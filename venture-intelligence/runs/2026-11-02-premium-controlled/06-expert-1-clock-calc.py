#!/usr/bin/env python3
"""Tithi / nakshatra timing and clock-mechanism accuracy model.
Truncated Meeus (Astronomical Algorithms ch.47/25) series, tropical longitudes.
Not an ephemeris: truncation error is quantified at the end against full-precision-free checks.
Run: python3 06-expert-1-clock-calc.py
"""
import math, statistics as st
from fractions import Fraction

D2R = math.pi/180
def jd_from_days(d): return 2451545.0 + d     # d = days since J2000.0 (TT~UT, ignoring dT ~ 70 s)
def args(d):
    T = d/36525.0
    Lp = 218.3164477 + 481267.88123421*T
    D  = 297.8501921 + 445267.1114034*T
    M  = 357.5291092 + 35999.0502909*T
    Mp = 134.9633964 + 477198.8675055*T
    F  = 93.2720950 + 483202.0175233*T
    return T, Lp, D, M, Mp, F
def sinr(x): return math.sin(x*D2R)

# Moon periodic terms (deg), Meeus ch.47 largest terms
def moon_terms(D,M,Mp,F):
    return {
     'evec_centre(M\')': 6.288774*sinr(Mp),
     'evection(2D-M\')': 1.274027*sinr(2*D-Mp),
     'variation(2D)':    0.658314*sinr(2*D),
     '2M\'':             0.213618*sinr(2*Mp),
     'annual(M)':       -0.185116*sinr(M),
     '2F':              -0.114332*sinr(2*F),
     '2D-2M\'':          0.058793*sinr(2*D-2*Mp),
     '2D-M-M\'':         0.057066*sinr(2*D-M-Mp),
     '2D+M\'':           0.053322*sinr(2*D+Mp),
     '2D-M':             0.045758*sinr(2*D-M),
     'M-M\'':           -0.040923*sinr(M-Mp),
     'D(parallactic)':  -0.034720*sinr(D),
     'M+M\'':           -0.030383*sinr(M+Mp)}
def moon_lon(d):
    T,Lp,D,M,Mp,F = args(d)
    return (Lp + sum(moon_terms(D,M,Mp,F).values()))%360
def sun_lon(d):
    T,Lp,D,M,Mp,F = args(d)
    L0 = 280.46646 + 36000.76983*T
    C = (1.914602-0.004817*T)*sinr(M) + 0.019993*sinr(2*M) + 0.000289*sinr(3*M)
    return (L0 + C)%360
def elong(d): return (moon_lon(d)-sun_lon(d))%360

def unwrap_elong(d, ref):  # continuous elongation near ref
    e = elong(d)
    return e + 360*round((ref-e)/360)

# ---- time base: 2026-11-01 00:00 UT -> days since J2000.0 (2000-01-01 12:00)
import datetime as dt
EPOCH = dt.datetime(2000,1,1,12,0)
def d_of(y,m,dd,h=0): return (dt.datetime(y,m,dd,h)-EPOCH).total_seconds()/86400
START = d_of(2026,11,1)
YEAR = 365.2422
# mean rates
mean_elong_rate = 445267.1114034*36525/36525 - 35999.0502909 # not used (see below)
def lin_elong(d):   # mean elongation: Moon mean L' minus Sun mean L0 (linear part)
    T = d/36525.0
    return (218.3164477+481267.88123421*T) - (280.46646+36000.76983*T)
RATE = (481267.88123421-36000.76983)/36525   # deg/day mean elongation
SYN = 360/RATE
SID = 360/(481267.88123421/36525)
ANOM = 360/(477198.8675055/36525)
print(f"Mean synodic month (this series, J2000) {SYN:.6f} d ; sidereal-ish (tropical) {SID:.6f} d ; anomalistic {ANOM:.6f} d")

def bisect(f, a, b, n=60):
    fa = f(a)
    for _ in range(n):
        m = 0.5*(a+b); fm = f(m)
        if (fm>0)==(fa>0): a, fa = m, fm
        else: b = m
    return 0.5*(a+b)

def crossings(fn, target_step, d0, d1, step=0.25):
    """times when continuous fn(d) crosses k*target_step, k integer"""
    out=[]; d=d0
    prev=fn(d)
    while d<d1:
        nxt=fn(d+step)
        k0=math.floor(prev/target_step); k1=math.floor(nxt/target_step)
        for k in range(k0+1,k1+1):
            tgt=k*target_step
            t=bisect(lambda x: fn(x)-tgt, d, d+step)
            out.append((k,t))
        prev=nxt; d+=step
    return out

# continuous true elongation
E0 = elong(START)
def Etrue(d): return unwrap_elong(d, E0 + RATE*(d-START))
# ---------- 1. tithi durations over one year
d1 = START+YEAR+35
cr = crossings(Etrue, 12.0, START-35, d1)
cr = [(k,t) for k,t in cr]
dur = [(cr[i][0], (cr[i+1][1]-cr[i][1])*24) for i in range(len(cr)-1)]
inyear=[(k,h) for (k,h),(kk,t) in zip(dur,cr) if START<=t<=START+YEAR]
hs=[h for k,h in inyear]
print(f"\nTITHI durations in 1 yr from 2026-11-01 (n={len(hs)}): min {min(hs):.2f} h, max {max(hs):.2f} h, mean {st.mean(hs):.2f} h, sd {st.pstdev(hs):.2f}")
print(f"mean tithi = synodic/30 = {SYN*24/30:.2f} h")
# per tithi number (1..30) stats
by={}
for k,h in inyear: by.setdefault(k%30,[]).append(h)
print("Tithi#(k mod 30; 0 = new-moon boundary ->tithi 1 starts) min/mean/max hours")
for n in sorted(by): print(f"  boundary {n:2d}->tithi {n+1:2d}: {min(by[n]):.1f} / {st.mean(by[n]):.1f} / {max(by[n]):.1f}")
# lunation lengths
lun=[]
newm=[t for k,t in cr if k%30==0 and START<=t<=START+YEAR+30]
for a,b in zip(newm,newm[1:]): lun.append(b-a)
print(f"Lunation (new moon to new moon) in this period: min {min(lun):.3f} d max {max(lun):.3f} d mean {st.mean(lun):.4f}")
def fmt(d): return (EPOCH+dt.timedelta(days=d)).strftime('%Y-%m-%d %H:%M UT')
print("Next new moons (this model):", [fmt(t) for t in newm[:3]])
# tithi shorter than a civil sunrise-to-sunrise day? count tithis < 24h ( may be skipped at some sunrises) and >24h
print("Tithis shorter than 24 h:", sum(1 for h in hs if h<24), "of", len(hs), "; longer than 24h:", sum(1 for h in hs if h>=24))
print("Tithis < 20 h:", sum(1 for h in hs if h<20), "; > 26 h:", sum(1 for h in hs if h>26))

# ---------- 2. nakshatra durations (sidereal): 13deg20' = 13.3333 deg, Lahiri ayanamsa offsets boundaries only
ayan0 = 23.85306+ 1.3972*0   # placeholder, ayanamsa effect is a constant offset in longitude: affects phase not duration
def Mtrue(d): 
    ref = moon_lon(START)+ (481267.88123421/36525)*(d-START)
    x=moon_lon(d); return x+360*round((ref-x)/360)
AY = 24.2   # [A] approx Lahiri for 2026; secular 0.0140 deg/yr
def Mid(d): return Mtrue(d) - AY - 0.0140*(d-START)/365.25
ncr = crossings(Mid, 360/27.0, START-35, START+YEAR+35)
ndur=[(ncr[i+1][1]-ncr[i][1])*24 for i in range(len(ncr)-1) if START<=ncr[i][1]<=START+YEAR]
print(f"\nNAKSHATRA durations (n={len(ndur)}): min {min(ndur):.2f} h max {max(ndur):.2f} h mean {st.mean(ndur):.2f} h")
print(f"moon daily motion range this series: ", end='')
sp=[(moon_lon(START+i/24+1/24)-moon_lon(START+i/24))*24 if True else 0 for i in range(0,24*60,6)]
sp=[ (s+180)%360-180 for s in sp]
print(f"{min(sp):.2f}-{max(sp):.2f} deg/day")

# ---------- 3. mechanism models of elongation
def model(name):
    def f(d):
        T,Lp,D,M,Mp,F = args(d)
        t = moon_terms(D,M,Mp,F)
        lin = lin_elong(d)
        # constant ratio: only the mean linear motion
        if name=='A_const': return lin
        sun_c = (1.914602)*sinr(M)       # solar equation of centre (annual cam / EoT-style)
        # B1: lunar anomaly cam only
        if name=='B1_moonC': return lin + t["evec_centre(M')"]
        # B2: lunar anomaly + solar annual cam
        if name=='B2_moonC+sunC': return lin + t["evec_centre(M')"] - sun_c
        # B3: + evection and variation (needs differential / extra cams)
        if name=='B3_+evec+var': return lin + t["evec_centre(M')"]+t["evection(2D-M')"]+t["variation(2D)"] - sun_c
        # B4: + 2M', annual(M) (moon), 
        if name=='B4_+3more': return lin + t["evec_centre(M')"]+t["evection(2D-M')"]+t["variation(2D)"]+t["2M'"]+t["annual(M)"] - sun_c
        # EoT-style only: sun anomaly cam, no lunar cam
        if name=='C_sunC_only': return lin - sun_c
    return f

def err_hours(fm, d0, d1):
    """time error of model's tithi boundaries vs true, hours; best constant offset applied (minimax)"""
    # Align integer offsets: model elongation at start approx = true; build continuous
    base = fm(START); off = E0 - (base%360)
    off = ((off+180)%360)-180
    def Em(d):
        x = fm(d)+off
        ref = E0+RATE*(d-START)
        return x+360*round((ref-x)/360)
    cm = crossings(Em, 12.0, d0, d1)
    tm = dict(cm); tt = dict(cr)
    es=[(tm[k]-tt[k])*24 for k in tm if k in tt and d0+5<tt[k]<d1-5]
    mid=(max(es)+min(es))/2
    return es, mid
YR0, YR1 = START, START+YEAR
print("\nTITHI boundary timing error vs this model's 'true' (hours), whole year, best constant offset (phase set once):")
res={}
for nm in ['A_const','C_sunC_only','B1_moonC','B2_moonC+sunC','B3_+evec+var','B4_+3more']:
    es,mid=err_hours(model(nm),YR0,YR1)
    e2=[e-mid for e in es]
    res[nm]=e2
    print(f"  {nm:16s}: max|err| {max(abs(x) for x in e2):6.2f} h  rms {math.sqrt(sum(x*x for x in e2)/len(e2)):5.2f} h   (n={len(e2)}, offset removed {mid:+.2f} h)")
# 'set once, no offset optimisation, at a new moon' variant: offset chosen so error is zero at first new moon
print("\n(same, but clock set exactly at a true new moon i.e. error zero there, as a customer would do)")
for nm in ['A_const','B1_moonC','B2_moonC+sunC','B3_+evec+var']:
    es,mid=err_hours(model(nm),YR0,YR1)
    e0=es[0] # first boundary error
    # find new moon error: choose k%30==0 earliest
    fm=model(nm); 
    print(f"  {nm:16s}: error span (max-min) {max(es)-min(es):5.2f} h ; worst if set at new moon ~ up to {max(abs(x-es[0]) for x in es):5.2f} h")

# ---------- 4. same for nakshatra
def nmodel(name):
    def f(d):
        T,Lp,D,M,Mp,F=args(d); t=moon_terms(D,M,Mp,F)
        lin = 218.3164477+481267.88123421*T
        if name=='A_const': return lin
        if name=='B1_moonC': return lin+t["evec_centre(M')"]
        if name=='B3_+evec+var': return lin+t["evec_centre(M')"]+t["evection(2D-M')"]+t["variation(2D)"]
        if name=='B4_+3more': return lin+t["evec_centre(M')"]+t["evection(2D-M')"]+t["variation(2D)"]+t["2M'"]+t["annual(M)"]
    return f
print("\nNAKSHATRA boundary timing error (hours), best constant offset:")
M0=Mid(START)
def nerr(fm):
    off=Mid(START)-(fm(START)-AY)
    off=((off+180)%360)-180
    def Mm(d):
        x=fm(d)+off-AY-0.0140*(d-START)/365.25
        ref=Mid(d)
        return x+360*round((ref-x)/360)
    cm=dict(crossings(Mm,360/27.0,START-35,START+YEAR+35)); tt=dict(ncr)
    es=[(cm[k]-tt[k])*24 for k in cm if k in tt and START+5<tt[k]<START+YEAR-5]
    mid=(max(es)+min(es))/2
    return [e-mid for e in es]
for nm in ['A_const','B1_moonC','B3_+evec+var','B4_+3more']:
    e=nerr(nmodel(nm))
    print(f"  {nm:14s}: max|err| {max(abs(x) for x in e):6.2f} h rms {math.sqrt(sum(x*x for x in e)/len(e)):5.2f} h")

# ---------- 5. amplitude in time units
print("\nAmplitude of each term converted to hours of tithi timing (deg / 12.19 deg/day mean relative rate *24):")
for nm,a in [("lunar equation of centre",6.2888),("evection",1.2740),("variation",0.6583),("solar equation of centre (EoT-style annual cam)",1.9146),("2M' term",0.2136),("annual (moon M)",0.1851)]:
    print(f"  {nm:48s} {a:6.3f} deg -> +/- {a/RATE*24:5.2f} h")

# ---------- 6. gear-ratio rounding: error per year from approximating synodic month
print("\nGEAR-RATIO ROUNDING. Wheel train from 24h-hour wheel to tithi disc. Required: mean tithi period (hours)=",f"{SYN*24/30:.5f}")
target=SYN  # days per full disc (30 tithis)
def best_ratio(maxn, target):
    best=[]
    for q in range(1,maxn+1):
        p=round(target*q)
        if p<=maxn*3: best.append((abs(p/q-target),p,q))
    best.sort(); return best[:5]
print("Single-stage-like p/q with q<=200 (p=days per rev of disc, q = hour-wheel turns): ")
for e,p,q in best_ratio(200,target)[:4]:
    print(f"   {p}/{q} = {p/q:.6f} d ; drift {(p/q-target)*24:+.4f} h per lunation ; per year {(p/q-target)*365.2422/target*24:+.3f} h")
print("Common watch moon discs:")
for name,val in [("59/2 teeth (29.5 d)",29.5),("135-tooth wheel, 27 + 20 * ... =29.530612 (a=135/2... )",29.530612),("Atmos/Hermle-type 29.53059 ",29.53059)]:
    print(f"   {name:40s}: {val:.6f} -> {(val-target)*365.2422/target*24:+.3f} h/yr (phase), days per year {(val-target)*365.2422/target:+.4f}")
# Fractions for 3-stage trains with prime-limited wheels
print("Best p/q with p,q products of two wheels <=120 teeth (4 wheels) for SYN*2 (hour wheel 12h/24h): ")
import itertools
cands=[]
for a in range(10,121):
  for b in range(a,121):
     pass
# faster: continued fraction convergents of SYN in days per day (tithi disc rev per mean sun day = 1/SYN)
cf=Fraction(target).limit_denominator(100000)
conv=[]
x=target; a0=int(x); h0,k0,h1,k1=1,0,a0,1; fr=x-a0; conv.append((h1,k1))
for _ in range(8):
    if fr<1e-12: break
    x=1/fr; a=int(x); fr=x-a
    h0,h1=h1,a*h1+h0; k0,k1=k1,a*k1+k0; conv.append((h1,k1))
print("Convergents of synodic month in days:")
for h,k in conv: print(f"   {h}/{k} = {h/k:.7f} ; drift {(h/k-target)/target*365.2422*24:+.4f} h/yr")

# ---------- 7. going-train rate contribution
print("\nGoing-train rate contribution (clock time error accumulates 1:1 into display):")
for s_per_day in (2,5,10,30,60):
    print(f"   {s_per_day:3d} s/day mean rate error -> {s_per_day*365.2422/3600:5.2f} h over 365 d")
# Display resolution
r=40.0
print(f"\nDisplay: tithi ring 12 deg per tithi at r={r} mm -> {r*12*D2R:.1f} mm per mean tithi; 1 h = {r*12*D2R/(SYN*24/30):.2f} mm")
# cam geometry: lunar anomaly cam amplitude and needed machining tolerance
for lift in (10.0,20.0):
    for hrs in (0.5,1.0):
        tol_deg=hrs*RATE/24
        print(f"   cam max lift +/-{lift} mm for 6.29 deg: tolerance for {hrs} h error = {tol_deg/6.288774*lift*1000:.0f} micron (profile)")
# follower load power
P_cam = 1e-3 * 2*math.pi/(ANOM*86400)
print(f"Cam load power (1 mN.m at slow cam): {P_cam:.2e} W (vs ~5e-6 W for an 8-day table clock, [A])")
# truncation check
print("\nTruncation: next Meeus terms are <=0.03 deg ~ <=0.06 h; sum of omitted largest ~0.1 deg ~ 0.2 h (order of magnitude)")
