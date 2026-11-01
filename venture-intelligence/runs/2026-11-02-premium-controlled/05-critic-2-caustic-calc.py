"""Caustic panel: physics of legibility and unit economics. Pure stdlib. All inputs marked A are assumptions."""
import math, itertools

# ---- 1. Resolution set by sun's angular size ----
SUN_DIAM_RAD = math.radians(0.533)   # K: mean angular diameter of the sun
print("Sun angular diameter mrad: %.2f" % (SUN_DIAM_RAD*1000))
print("Blur width = throw * 0.0093 (any lens: each panel point images the whole sun disc)")
for throw in (1.0, 2.0, 3.0, 4.0):
    blur = throw*SUN_DIAM_RAD
    for img in (0.5, 1.0, 2.0):
        print(f" throw {throw:.0f} m: blur {blur*100:4.1f} cm; image {img:.1f} m wide -> ~{img/blur:4.0f} resolvable elements across")

# ---- 2. Daily and seasonal movement (Delhi 28.6N, vertical south-facing glazing) ----
def sun(lat, doy, hour):
    dec = math.radians(23.44)*math.sin(2*math.pi*(284+doy)/365)
    ha = math.radians(15*(hour-12))
    la = math.radians(lat)
    sin_alt = math.sin(la)*math.sin(dec)+math.cos(la)*math.cos(dec)*math.cos(ha)
    alt = math.asin(sin_alt)
    az = math.atan2(math.sin(ha), math.cos(ha)*math.sin(la)-math.tan(dec)*math.cos(la)) + math.pi  # from north, clockwise
    return math.degrees(alt), math.degrees(az)

def vec(alt, az):
    a, z = math.radians(alt), math.radians(az)
    return (math.cos(a)*math.sin(z), math.cos(a)*math.cos(z), math.sin(a))
def ang(u, v):
    d = sum(x*y for x, y in zip(u, v)); return math.degrees(math.acos(max(-1, min(1, d))))

lat = 28.6
print("\nDelhi noon altitude: solstice-summer %.1f, equinox %.1f, winter %.1f deg" %
      (sun(lat,172,12)[0], sun(lat,80,12)[0], sun(lat,355,12)[0]))
print("Sun moves 15 deg/hour; at 2 m throw the image shifts %.0f cm per hour (small-angle)" % (2*math.radians(15)*100))
# Design sun position: 21 Mar-ish (doy 80), 11:00 solar time. Count days/yr when sun passes within tol of design direction, and minutes/day
design = vec(*sun(lat, 80, 11.0))
for tol in (1.0, 2.0, 5.0):
    days = 0; mins = 0
    for d in range(1, 366):
        m = sum(1 for k in range(0, 24*60, 2) if sun(lat, d, k/60)[0] > 5 and ang(vec(*sun(lat, d, k/60)), design) <= tol)*2
        if m: days += 1; mins += m
    print(f" tolerance {tol} deg of design direction: {days} days/yr touch it, avg {mins/max(days,1):.0f} min on those days, {mins/60:.1f} h/yr total")
# fraction of daylight hours (alt>5) in the year
tot = sum(1 for d in range(1,366) for k in range(0,24*60,10) if sun(lat,d,k/60)[0]>5)*10/60
print(f" total sun-above-5deg hours/yr: {tot:.0f}; share within 5 deg of design: see above")

# ---- 3. Unit economics at Rs 7 lakh ----
HOURLY = 750
def unit(price=700000, gst=0.18, material=60000, cnc_hours=20, cnc_rate=1500, polish_hours=25, polish_rate=300,
         design_h=60, site_h=15, install_h=20, sales_h=120, install_cash=40000, travel=25000, framing=50000,
         redo_prob=0.35, redo_frac=0.6, comm=0.0, advance=0.5):
    net = price/(1+gst)  # assume price is GST-inclusive [A]
    make = material + cnc_hours*cnc_rate + polish_hours*polish_rate
    cash = make*(1+redo_prob*redo_frac) + install_cash + travel + framing + net*comm
    hours = design_h+site_h+install_h+sales_h
    profit_before_labour = net - cash
    profit_after_labour = profit_before_labour - hours*HOURLY
    return net, cash, hours, profit_before_labour, profit_after_labour
base = unit()
print("\nBase: net-of-GST %.0f, cash cost %.0f, founder hours %d, profit before founder time %.0f, after founder time %.0f" % base)
print(" effective Rs/hour on founder time: %.0f" % (base[3]/base[2]))
print("\nSensitivity: each input made unfavourable by 50 pct (cost up 1.5x or hours up 1.5x) one at a time; and price at 3.5 lakh")
for name, kw in [("material",dict(material=90000)),("cnc hours",dict(cnc_hours=30)),("polish hours",dict(polish_hours=38)),
                 ("sales hours (one sale per 240h)",dict(sales_h=240)),("redo prob 0.7",dict(redo_prob=0.7)),
                 ("install cash",dict(install_cash=60000)),("framing",dict(framing=75000)),
                 ("architect/designer commission 15%",dict(comm=0.15)),("price 3.5 lakh",dict(price=350000)),
                 ("price 4.5 lakh",dict(price=450000))]:
    r = unit(**kw); print(f" {name:36s} profit pre-labour {r[3]:9.0f}  Rs/h {r[3]/r[2]:6.0f}  after labour {r[4]:9.0f}")
# contracting a polishing/milling vendor at 2x
r = unit(cnc_rate=3000, polish_rate=600, comm=0.15, sales_h=240, price=450000)
print(" combined bad case (comm 15 pct, sales 240h, price 4.5L, vendor 2x): pre-labour %.0f, Rs/h %.0f" % (r[3], r[3]/r[2]))
# Units/yr needed for founder to earn e.g. Rs 12 lakh/yr after cash cost at base margin
target = 1200000
print("\nPieces per year for Rs %d founder income at base: %.1f; founder hours then: %.0f" % (target, target/base[3], target/base[3]*base[2]))
print("Hours available if full time 1800 h: max pieces by hours = %.1f" % (1800/base[2]))
