"""Caustic panel feasibility calcs. python3 06-expert-2-caustic-calc.py"""
import math
D=math.radians
SUN=0.53
n=1.49  # PMMA (glass 1.52)
print("== 1. Blur vs distance (sun disc 0.53 deg) ==")
for d in (0.5,1,2,3,5):
    print(f"d={d} m blur={d*math.tan(D(SUN))*1000:.1f} mm")
print("\n== 2. Resolution: pixels across ~ full angular extent / 0.53 deg (distance cancels) ==")
for full in (10,20,30,40,60):
    print(f"image full angle {full} deg -> ~{full/SUN:.0f} resolvable px across")
print("\nImage width for panel W=0.6 m, d, half-angle theta (flat target): L=W+2 d tan(theta)")
for d in (1,2,3):
    for th in (10,20):
        L=0.6+2*d*math.tan(D(th)); blur=d*math.tan(D(SUN))
        print(f"d={d} th={th}: L={L:.2f} m, blur={blur*1000:.0f} mm, px~{L/blur:.0f}")
print("\n== 3. Contrast / brightness (assumptions [A]) ==")
DNI_lux=100e3; T=0.90; amb=[300,1000,3000]
for Wp,L in ((0.6,1.0),(0.6,2.0),(1.0,1.5)):
    conc=(Wp**2)/(L**2); E=DNI_lux*T*conc*math.cos(D(30))  # 30 deg incidence
    print(f"panel {Wp} m -> image {L} m: mean image lux {E:.0f}; ratio to ambient "+", ".join(f"{a} lx:{(E+a)/a:.0f}:1" for a in amb))
print("hazy-sky circumsolar/haze floor: if 5% or 15% of transmitted light is scattered uniformly over image area, black-level lux=")
for f in (0.02,0.05,0.15):
    Wp=0.6;L=1.0
    print(f" scatter {f*100:.0f}%: black-level floor ~{DNI_lux*T*Wp**2*f/L**2:.0f} lx extra; max contrast mean/black ~{1/f:.0f}:1 (upper bound)")
print("\n== 4. Dispersion (PMMA Abbe 57, glass ~64) ==")
for V,nd,name in ((57,1.49,'PMMA'),(64,1.52,'low-iron glass')):
    for dev in (10,20):
        spread=dev*((nd-1)/V)/(nd-1)
        print(f"{name} deviation {dev} deg: colour fringe ~{spread:.2f} deg vs sun disc {SUN}")
print("\n== 5. Surface accuracy ==")
for pt_frac in (0.5,0.25,0.1):
    deflect_err=D(SUN)*pt_frac  # rad allowed deflection error
    slope_err=deflect_err/(n-1)
    print(f"allowed pointing error = {pt_frac}*sun disc = {math.degrees(deflect_err):.3f} deg -> slope error {math.degrees(slope_err):.3f} deg ({slope_err*1e3:.1f} mrad)")
    for lam in (2,5,10,30):
        amp=slope_err*lam/ (2*math.pi)*1000
        print(f"   ripple wavelength {lam} mm -> height amp {amp:.1f} um")
print("Ball-nose scallop: h=s^2/(8R); max slope = (s/2)/R rad")
for R in (1,3,6):
    for s in (0.05,0.1,0.3):
        h=s**2/(8*R)*1000; sl=(s/2)/R
        print(f" R={R} mm step={s} mm: scallop {h:.2f} um, slope {math.degrees(sl):.2f} deg -> deflection scatter +/-{math.degrees(sl*(n-1)):.2f} deg")
print("Roughness scatter: rms slope sig_s -> halo ~ (n-1)*sig_s. Ra 0.4 um at corr length 50 um: slope ~2pi*Ra/lambda")
for Ra in (0.1,0.4,1.6):
    for lam in (0.05,0.2):
        sl=2*math.pi*Ra*1e-3/lam
        print(f" Ra {Ra} um lam {lam} mm: slope {math.degrees(sl):.2f} deg, halo ~{math.degrees(sl*(n-1)):.2f} deg (vs 0.53 sun)")
print("\n== 6. Image shift with sun motion ==")
print("sun moves ~15 deg/h (hour angle); image shifts ~ d*dalpha")
for d in (1,2,3):
    print(f"d={d} m: shift {d*math.radians(15):.2f} m/h; time to shift 1 blur ({d*math.tan(D(SUN))*1000:.0f} mm): {SUN/15*60:.1f} min")
# nonlinear deviation change of a wedge-type surface with incidence
def dev(inc_deg, slope_deg):
    """back surface (air side) tilted by slope_deg relative to front flat; ray inc on front flat."""
    i=D(inc_deg); r=math.asin(math.sin(i)/n)
    a=D(slope_deg); r2=r-a  # incidence on tilted back surface
    s=n*math.sin(r2)
    if abs(s)>=1: return None
    t=math.asin(s)
    return math.degrees(t+a-i)  # deviation from straight line... sign: net bend toward base
print("\nDeviation of tilted back surface (tilt 20 deg) vs incidence on front (thin-wedge model)")
base=dev(0,20)
for inc in (0,10,20,30,40,50,60):
    d_=dev(inc,20)
    print(f" inc {inc}: deflection {d_ if d_ is None else round(d_,2)} deg; relative to normal-incidence {None if d_ is None else round(d_-base,2)} deg")
print("Rigid image shift = d*dalpha; extra distortion = change in deflection above (deg), e.g. 10 deg off-design -> 1 to 2 deg change, >sun disc")

print("\n== 7. Sun geometry & legible hours ==")
def sunpos(lat,doy,hour):
    dec=23.44*math.sin(D(360/365*(doy-81)))
    # equation of time ignored (+-16 min) [A]
    ha=15*(hour-12)
    la=D(lat);de=D(dec);h=D(ha)
    sin_alt=math.sin(la)*math.sin(de)+math.cos(la)*math.cos(de)*math.cos(h)
    alt=math.asin(sin_alt)
    cosaz=(math.sin(de)-math.sin(alt)*math.sin(la))/(math.cos(alt)*math.cos(la))
    az=math.acos(max(-1,min(1,cosaz)))
    if ha>0: az=2*math.pi-az   # azimuth from north clockwise
    return math.degrees(alt),math.degrees(az)
def vec(alt,az):
    a=D(alt);z=D(az)
    return (math.cos(a)*math.sin(z),math.cos(a)*math.cos(z),math.sin(a))
def ang(v,w):
    c=sum(x*y for x,y in zip(v,w)); return math.degrees(math.acos(max(-1,min(1,c))))
cities={'Delhi':28.6,'Bengaluru':13.0,'Kochi':10.0}
print("noon altitude (deg) [calc] at solstices/equinox")
for c,l in cities.items():
    print(c,[round(sunpos(l,doy,12)[0],1) for doy in (172,80,355)])
# (a) registered-position hours: design = sun at design doy/time; tolerance on direction
tol=2.9  # deg ~10% of 1 m image at 2 m
print(f"\n(a) Registered hours/year with sun within {tol} deg of design direction (fixed panel, clear sky)")
for c,l in cities.items():
    for dd,dh in ((355,12),(80,10),(172,9)):
        a0=sunpos(l,dd,dh); v0=vec(*a0)
        tot=0.0
        for doy in range(1,366):
            for k in range(0,24*60,2):
                h=k/60
                al,az=sunpos(l,doy,h)
                if al<=0: continue
                if ang(v0,vec(al,az))<=tol: tot+=2/60
        print(f" {c} design doy{dd} {dh}h (alt {a0[0]:.0f}, az {a0[1]:.0f}): {tot:.0f} h/yr within tol, ~{tot/365*60:.0f} min/day avg; days={tot}")
# (b) sliding-image legible hours: vertical window, horizontal floor, h=1.5 m above floor, room depth 4 m
print("\n(b) Sliding-image hours/day: vertical window facing az_w; sun incidence on glass <=60 deg; central ray lands 0.5-4.0 m inside (h=1.5 m); floor stretch 1/cos(zenith)")
def hours(l,doy,azw,hh=1.5,inc_max=60,dmin=0.5,dmax=4.0):
    cnt=0.0;sl=[]
    nvec=vec(0,azw)  # outward normal horizontal; sun in front means sun.dot(n)>0
    for k in range(0,24*60,2):
        h=k/60
        al,az=sunpos(l,doy,h)
        if al<=0: continue
        v=vec(al,az)
        inc=ang(v,nvec)
        if inc>inc_max: continue
        z=90-al
        # horizontal offset inside the room: hh*tan(zenith) along sun-away dir; component along room normal = hh*tan(z)*cos(inc_az)
        off=hh*math.tan(D(z))*math.cos(D(inc)) if z<89 else 99
        # use horizontal distance along ray = hh*tan z
        dist=hh*math.tan(D(z))
        if dmin<=dist<=dmax:
            cnt+=2/60; sl.append(1/math.cos(D(z)))
    return cnt, (max(sl) if sl else 0)
for c,l in cities.items():
    for name,doy in (('Jun21',172),('Mar21/Sep23',80),('Dec21',355)):
        row=[]
        for fac,azw in (('N',0),('E',90),('S',180),('W',270)):
            hrs,st=hours(l,doy,azw)
            row.append(f"{fac}:{hrs:.1f}h")
        print(f" {c:9s} {name:12s} "+"  ".join(row))
print("\n(c) Skylight/horizontal panel: sun incidence=zenith; image on floor below at depth H=3 m shifts H*tan(z) horizontally")
for c,l in cities.items():
    for name,doy in (('Jun21',172),('Dec21',355)):
        al_n=sunpos(l,doy,12)[0]
        # time when zenith angle < 40 deg
        t=sum(2/60 for k in range(0,1440,2) if sunpos(l,doy,k/60)[0]>50)
        print(f" {c} {name}: hours with altitude>50deg = {t:.1f}; noon alt {al_n:.0f}")
print("\n== 8. Thermal / material ==")
alpha=70e-6
for dT in (10,30,40):
    print(f"PMMA 0.6 m panel dT {dT} K: expansion {alpha*dT*600:.2f} mm ({alpha*dT*100:.2f} %); glass 9e-6: {9e-6*dT*600:.2f} mm")
print("PMMA water uptake, creep etc: not computed [K]")
print("Fresnel loss per surface at normal incidence n=1.49:", round(((n-1)/(n+1))**2*100,1),"%; two surfaces ~",round((1-(1-((n-1)/(n+1))**2)**2)*100,1),"%")
