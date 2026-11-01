# Expert 1 (Multidisciplinary): mechanical tithi and nakshatra table clock, Rs 8 lakh

Date: 2026-11-01. Scope: engineering and craft feasibility only. Commercial questions are out of scope.

**Source access warning.** WebFetch could not open any page. Every host failed DNS resolution in this session (timeanddate.com, en.wikipedia.org, revolution.watch). All source facts below come from WebSearch result text. Every Sources row is `Via: search summary`. Where a source decides a point it is marked `[S#, unverified at source]`. Calculations are my own and do not depend on web pages. The script is `06-expert-1-clock-calc.py`, its output `06-expert-1-clock-calc.out`, both in this folder (`[S20]`).

## 0. Verdict in one paragraph

**Plausible, not proven.** A mechanical display of tithi and nakshatra is feasible. The accuracy is set by how many lunar and solar terms the mechanism carries. A plain constant-ratio train is useless for a tithi: it is wrong by up to about 17 hours at some tithi boundaries `[I]`. A single lunar-anomaly cam brings that to about 7 hours. Lunar cam plus solar annual cam gives about 4 hours. Adding evection and variation brings it near 1 hour `[I]`. The last step needs two or more further cams plus a summing differential or linkage, which is a tide-predictor-class design. No commercial mechanical clock or watch was found that does this for tithi `[A, not found after 6 searches]`. Class: **plausible** for +/-1 h; **proven** for +/-1 day-class moon displays. The decisive unknown is whether a real train (backlash, cam error, differential play, spring-driven torque) holds the ideal +/-1 h over 12 months. Section 10 gives a test.

## 1. Disciplines and deciding questions

| Discipline | Deciding question |
|---|---|
| Celestial mechanics | How far does the true tithi boundary move from a uniform clock, and which terms matter? |
| Mechanical design (kinematics) | Can cams plus a differential sum 3 to 4 periodic terms onto a uniform shaft in a table-clock envelope? |
| Horology / movement | Buy a movement or make one? What rate stability does the going train give? |
| Manufacturing / materials | Can cams and wheels of the needed accuracy be made in India? |
| Product definition (borderline, flagged) | Which tithi does the user mean: instantaneous, or the one at local sunrise? |

## 2. Findings by discipline

### 2.1 Facts about tithi and nakshatra

- A tithi is the time the Moon gains 12 degrees of elongation on the Sun. Reported mean about 23 h 37 min, range about 19 h 59 min to 26 h 47 min (`[S1]` (unverified at source)). Moon speed quoted 11.7 to 15.4 deg/day `[S1]` (unverified at source).
- Panchang sources differ by a few minutes on tithi end times (ayanamsa and Moon-position accuracy) `[S15]` (unverified at source). A Surya Siddhanta panchang and a drik (ephemeris) panchang can differ by a day on a festival date `[S15]` (unverified at source).
- Nakshatra depends on the Moon's position against the stars only, and tithi on Sun-Moon elongation `[S9]` (unverified at source).
- A 2025 electronic "Panchanga clock" exists with tithi and nakshatra, configured to latitude, longitude and time zone `[S9]` (unverified at source). No mechanical panchang clock was found after 3 searches (queries: "panchang clock mechanical tithi nakshatra display", "tithi mechanical watch", "Hindu calendar mechanical clock").

### 2.2 How comparable devices solve irregularity (all from search summaries)

| Device | Approach | Lesson |
|---|---|---|
| Antikythera mechanism | Pin-and-slot on two offset gears gives the Moon's first anomaly; the pair sits on a 9-year turntable to model apsidal rotation `[S2]` (unverified at source). A spiral Metonic dial (19-year) handles lunar-solar cycle `[S2]` (unverified at source) | Anomaly can be a gear-pair feature, not only a cam. Roughly 2,000 years of precedent for a mechanical lunar anomaly |
| Ordinary moon-phase watch | Constant-ratio train, usually 59/2 or 135-tooth wheel. Deviation from the true phase up to about 20 h is normal `[S16]` (unverified at source) | This is the "plain train" case in section 3 |
| High-accuracy moon-phase gearing | Quoted drift of one day in 122 years (135-tooth), one day in about 3,887 years (Duometre Spherotourbillon Moon) `[S7]` (unverified at source); one day in 40.3 years for Blast Moonstruck `[S18]` (unverified at source) | These claims are **mean-period** accuracy only. They say nothing about the +/-12 h anomaly |
| Arnold & Son True Moon (2010) | Marketed as tracking the true waxing and waning faces `[S8]` (unverified at source). Technical detail not found | Shows a commercial wristwatch attempt at the anomaly, method unverified |
| Ochs & Junior / Oechslin astronomy | Cam stack with Janvier-type variable differentials for the Moon. Correction cams for tilt are latitude-dependent unlike the equation-of-time cam `[S16]` (unverified at source) | Direct precedent for cam+differential, and a warning on location dependence |
| Jens Olsen's World Clock | Displays Moon longitude, nodes, perigee and phase `[S17]` (unverified at source) | Precedent for multi-term lunar position in one large mechanical clock (not table size) |
| Chinese calendar (Blancpain; Parmigiani Xiali; Moser) | Month number and leap month by cam system. Parmigiani covers 12 years, then reset `[S3]` (unverified at source). Blancpain needs manual adjustment for leap months `[S3]` (unverified at source) | Lunisolar logic is done by long-period cams and **resets**, not true astronomy |
| Hebrew calendar (Vacheron 57260; patent CH711072) | 19-year Metonic cycle, 7 leap years, mechanical perpetual `[S4]` (unverified at source) | Rule-based calendars are mechanisable exactly because they are arithmetic |
| Islamic Hijri (Parmigiani PF009; Chaykin Lunar Hijra clock) | 29/30-day month indicator, automatic; month and year corrected by hand. Parmigiani claims theoretical accuracy for 2,500 years `[S5]` (unverified at source). Chaykin table clock has tourbillon, 10-day reserve `[S6]` (unverified at source) | Arithmetic (tabular) lunar calendar, **not** observed or astronomical. Parmigiani did it in a table clock in 2011 `[S5]` (unverified at source) |

Key point `[I]`: every mechanical lunar calendar found is **arithmetic** (mean month, fixed cycles). A tithi display that follows the true Moon-Sun elongation to hours is a different, harder object. It resembles an astronomical clock lunar module more than a calendar.

## 3. Calculations (script `06-expert-1-clock-calc.py`; all numbers below `[S20]` unless stated)

**Method.** Truncated Meeus series for Moon longitude (13 largest periodic terms) and Sun longitude (equation of centre, 3 terms). Tithi boundaries are every 12 degrees of elongation, found by bisection over 2026-11-01 to 2027-11-01. Mechanism models are the mean linear elongation plus chosen terms. Each is compared with the full truncated model, with one best constant phase offset removed (clock set once).

**Model check.** The script gives new moon 2026-11-09 07:04 UT. Web sources give 07:02 to 07:03 UTC (`[S13]` (unverified at source)). Agreement about 1 to 2 minutes. `[I]`. Truncation of omitted terms is about 0.1 degree, roughly 0.2 h of timing `[I]`. The "1 h" results below therefore carry about +/-0.2 h of model uncertainty.

**3.1 How long a tithi lasts (371 tithis in the year).**

- Mean 23.62 h (equals synodic month 29.5306 d / 30). Range 20.19 h to 26.73 h. Standard deviation 2.04 h. Agrees with the quoted 19.98 to 26.78 h in `[S1]` (unverified at source) at the long end. My short end (20.2 h) is above the quoted 19.98 h. I trust the quoted range for the whole millennium and my one-year window for 2026-27 `[I]`.
- 207 of 371 tithis are shorter than 24 h, 164 are longer. 74 are longer than 26 h.
- Lunation (new moon to new moon) in this year: 29.291 to 29.814 days; mean 29.527 d.
- Within the month, the mean duration is shortest near boundaries 13 to 15 (about 23.3 h) and longest near boundaries 20 to 22 (about 24.4 h). The big spread (20 to 27 h) is the lunar anomaly (period 27.55 d) and its beat with the solar year, not the phase position.

**3.2 Size of each irregularity in hours of tithi timing** (amplitude in degrees divided by the mean relative rate of about 12.19 deg/day):

| Term | Amplitude | Timing effect | Period `[I]` |
|---|---|---|---|
| Lunar equation of centre | 6.289 deg | +/-12.4 h | 27.55 d (anomalistic month) |
| Solar equation of centre (the "equation of time"-style annual cam) | 1.915 deg | +/-3.8 h | 365.26 d |
| Evection | 1.274 deg | +/-2.5 h | about 31.8 d (from 2D minus M') |
| Variation | 0.658 deg | +/-1.3 h | about 14.77 d (2D) |
| 2M' term | 0.214 deg | +/-0.4 h | 13.78 d |
| Annual term (Moon, M) | 0.185 deg | +/-0.4 h | 365.26 d |

**3.3 Accuracy over one year without setting** (max absolute boundary error, best one-time phase; rms in brackets):

| Mechanism | Tithi | Nakshatra |
|---|---|---|
| A. Constant-ratio train only | 16.9 h (9.6) | 14.2 h (8.5) |
| C. Solar annual cam only (EoT-style, no lunar cam) | 15.3 h (9.2) | not applicable |
| B1. + lunar anomaly cam | 6.9 h (3.5) | 4.0 h (1.9) |
| B2. B1 + solar annual cam | 4.3 h (2.1) | not applicable |
| B3. B2 + evection + variation | 1.0 h (0.4) | 0.9 h (0.4) |
| B4. B3 + 2M' + annual term | 0.7 h (0.3) | 0.6 h (0.2) |

Reading `[I]`: an "equation-of-time style" correction alone is worthless for tithi because the lunar anomaly is 3 times larger. Nakshatra is easier than tithi: it needs no Sun term, only the Moon's own cams. But nakshatra needs an ayanamsa offset. Lahiri value taken as about 24.2 degrees `[A, basis: general knowledge of 2026 value, check against Indian Astronomical Ephemeris]`, drifting 0.0140 deg/yr, which is under 2 minutes per year of boundary shift `[I]`. A fixed-star offset is simply a one-time dial placement.

If the customer sets the clock at a true new moon instead of the best one-time offset, the worst error rises (script: A about 30 h, B1 about 8.5 h, B2 about 6.2 h, B3 about 1.1 h; those use the first boundary as the zero, so treat them as approximate) `[I]`.

**3.4 Gear-ratio rounding (the mean term)**

- True mean synodic month for the model: 29.530589 d.
- 59/2 = 29.5 d drifts -9.1 h per year in phase (-0.378 d per year). This is the common cheap moon disc `[I]`.
- 1447/49 = 29.530612 d drifts +0.007 h per year. 443/15 is +0.8 h/yr; 502/17 is -0.35 h/yr.
- A 135-tooth style train matches 29.5306 d to well under 0.1 h/yr `[I]`.
- Conclusion: the mean ratio is solved. Use a continued-fraction train (1447/49 or better). Mean-ratio error is negligible next to the periodic terms.

**3.5 Going-train rate error adds 1:1.** A rate error of 10 s/day gives 1.0 h over a year; 30 s/day gives 3.0 h; 60 s/day gives 6.1 h. A table clock at +/-10 s/day is `[A]` typical for a good 8-day balance movement (basis: general knowledge; test by timing a bought movement). It consumes the whole B3 budget. If the clock hands are reset for time, the lunar train must not be reset with them (see 9).

**3.6 Cam and display geometry.**

- Tithi ring at 40 mm radius: one mean tithi spans 8.4 mm of arc; 1 h of error is 0.35 mm. A reader can see 1 h only on a large ring, so display resolution, not mechanism, may limit what is readable `[I]`.
- Lunar-anomaly cam with +/-10 mm lift: a 1 h error budget needs profile accuracy about 0.8 mm; 0.5 h needs about 0.4 mm. That is easy for wire EDM or CNC `[I]`. The harder error sources are backlash, cam follower lash and wheel eccentricity, which add to the budget.
- Cam load power is about 2.6 nW at 1 mN.m on the slow cam, against about 5 microwatts for a spring-driven 8-day clock `[A, basis: 8-day table clock with about 2 to 4 J in the mainspring over 8 days; test by measuring]`. So torque is not the limit, but friction in a long train of 5 to 8 stages (hour wheel to 27.5 d wheel is a ratio of about 55 for the anomaly shaft after the 12 h wheel `[I]`) is worth measuring.

**3.7 Inputs I did not source and what happens if they are unfavourable by half.**

- Truncated-series error (about 0.2 h). If doubled to 0.4 h, B3 is still about 1.0 to 1.4 h. The verdict class does not flip.
- Going-train rate (10 s/day). If it is 15 s/day, add 0.5 h. B3 total is about 1.5 h. Still plausible, but fails a 1 h target. **Unknown. Driven by the going-train rate.**
- Backlash and cam error: not modelled. This is the main unknown (section 10).

## 4. Feasibility class and confidence

| Target | Class | Confidence |
|---|---|---|
| Day-correct tithi, mean train, reset every 1 to 2 months | Proven (same as moon-phase watches) | High `[S7][K]` (unverified at source) |
| +/-4 to 7 h (lunar cam, with or without solar cam) | Plausible | Medium. Maths solid `[S20]`; real-train error untested |
| +/-1 h over 12 months (lunar, solar, evection, variation) | Plausible, near speculative as a table-clock product | Low to medium. No commercial precedent found for tithi `[A, 6 searches]` |
| Whole religious panchang logic (sunrise tithi, kshaya/vriddhi, adhika masa, regional systems) | Not a mechanical-timing question. Needs a product decision | Not assessed |

## 5. Production routes compared

| Route | Setup / tooling | Unit cost drivers | MOQ | Lead time | Quality risk |
|---|---|---|---|---|---|
| Buy a conventional 8-day or 14-day table-clock movement and add a lunar module on the dial side | Low (module design and cams only) | Movement plus module parts plus fitting | 1 | Months | Mating to a movement not built for it; the user's time-setting must not move the lunar train. Hermle 8-day moon-phase table clocks sell complete at about EUR 949 (German retail, with VAT) `[S12]` (unverified at source); movement alone not found after 2 searches |
| Make a bespoke movement and lunar module | High; many hours of design | Skilled labour dominates | 1 | A year or more | Highest. Needs a plant that does not exist in India for clock-size trains `[A]` |
| Contract a Swiss/German independent maker | Quote required | Hours of a master | 1 | Months to years `[A]` | Lowest execution risk, highest price. Chaykin's Lunar Hijra table clock has price on request `[S6]` (unverified at source) |
| Purely mechanical vs mechanical display with small electronic correction | See 5.1 | | | | |

### 5.1 Purely mechanical versus hybrid

- **Purely mechanical** gives +/-1 h only with 4 cams and summing; it also depends on a spring-driven going train staying within about 10 s/day for a year (3.5).
- **Hybrid**: a mechanical lunar display driven by a cheap electronic or battery-regulated step, or a periodic electronic correction (for example a calendar-year lookup table driving a micro-motor to nudge the discs once per day). That reaches minutes of accuracy with one cam or a software lookup `[H, test: bench model]`. Cost is a battery or a charging cycle, and the product is no longer "purely mechanical". Whether that matters is a commercial question for others. Technically it removes the main unknown.
- My view `[I]`: for an Rs 8 lakh object whose point is craft, a pure mechanical +/-4 h (B2) is the realistic honest claim; +/-1 h (B3) is a development stretch. The hybrid is the engineering-safe fallback.

## 6. Bill of materials and cost sketch (every line is an estimate)

Currency INR. EUR to INR at about Rs 100 per EUR `[A]` (approximate rate, check before use).

| Line | Estimate | Tag |
|---|---|---|
| Base 8-day movement (bought) | EUR 100 to 300, about Rs 10,000 to 30,000 | `[A]`, basis: complete Hermle clocks sell at about EUR 949 retail `[S12]` (unverified at source); bare movement price not found |
| Lunar module: 3 to 4 cams, 1 differential, about 20 to 30 wheels, brass/steel | Rs 30,000 to 80,000 materials and outsourced cutting | `[A]` |
| Wire-EDM cams (outsourced) | Rs 300 to 600 per hour; a cam is under 1 hour of cut time | `[S10]` (unverified at source) quotes about Rs 400/h on IndiaMART; `[I]` cam cost under Rs 2,000 each |
| Dial, hands, case, finishing | Rs 50,000 to 1.5 lakh for a premium finish | `[A]` |
| Skilled assembly and adjustment labour | 150 to 250 hours at Rs 1,000 to 1,500/h = Rs 1.5 to 3.75 lakh | `[A]`, hourly rate not sourced |
| One-time development (design, simulation, 2 to 3 prototypes) | 800 to 1,500 hours = Rs 8 to 20 lakh | `[A]` |
| **Unit cost excluding development** | **Rs 2.5 to 6 lakh** | `[I]` sum of lines above |

`[I]` At Rs 8 lakh, unit materials and labour fit under the price only if each unit is under about 250 hours. Development cost cannot be recovered on a few units without a deposit-funded route. That is a commercial point, noted not judged.

**Lead time** `[A]`: 6 to 12 months to a working prototype with a simulation-first approach; 3 to 5 months per unit afterwards. For scale, an off-the-shelf bespoke mechanical tide clock lists a 10 to 12 week design process `[S19]` (unverified at source), and a Corum clock table takes at least four months per piece `[S19]` (unverified at source). These are different products; they are rough comparators only.

## 7. Who could build it (sources are weak; I could open none)

| Candidate | What was found | Fit |
|---|---|---|
| Aditya Sambhare (Pune), A. D. Sambhare | Self-taught, full-time commissioned custom mechanical watches, restoration and modification `[S14]` (unverified at source) | Watch-scale; no evidence of table-clock astronomical work |
| Bangalore Watch Company; Rotoris; Argos | Assemble watches around bought movements `[S14]` (unverified at source) | Not movement makers |
| EPOS (partnership with Swiss master Jean Fillon, moonphase and regulators) | Brand partnership, not an Indian workshop `[S14]` (unverified at source) | Shows Swiss route exists with an Indian link |
| Indian tower-clock makers (listed on IndiaMART: NMC / Tower Clocks India, Medieval India New Delhi, Silver Scientific, Tool & Time) | Self-descriptions, unverified `[S11]` (unverified at source) | Large-scale mechanical clock craft, plausible for case and gear cutting; not for fine astronomical modules |
| Wire-EDM job shops (Chennai, Ahmedabad and many others) | About Rs 400/h `[S10]` (unverified at source) | Suitable for cams and wheel blanks |
| Swiss/German independents (Chaykin in Russia, Parmigiani, Ochs & Junior) | Have built lunar calendars and cam-stack moon modules `[S5, S6, S16]` (unverified at source) | Capability exists abroad; price and lead time not found |

Not found after 3 searches (queries: "independent watchmaker India handmade mechanical clock complication", "tower clock manufacturer India", "commission bespoke mechanical table clock lead time"): any Indian workshop with a published astronomical-clock or lunar-cam product. `[H: the in-house talent to design the module is the scarce resource; test: ask 3 named makers for a design-hours quote]`.

## 8. Safety, compliance, certification

A mechanical table clock carries no certification burden I could identify for sale in India `[K, not checked]`. I did not research BIS or Legal Metrology applicability. Listed as unchecked. Mainspring release and finish materials (lacquer, brass) have ordinary product-safety content only `[K]`.

## 9. Critical technical risks (failure modes)

1. **Cumulative backlash and cam-follower lash** across 5 to 8 stages: the 1 h budget is 0.35 mm at the dial `[S20]`. Likelihood high, impact high.
2. **Going-train rate**: 10 s/day error equals 1 h per year on the display `[S20]`. Needs regulation and temperature behaviour known.
3. **Time-setting disturbs the lunar train** unless taken off before the hand-setting clutch. Design must isolate it.
4. **Power**: a pendulum or balance table clock must run the lunar load for a year between settings. An 8-day movement needs winding; "over a year without setting" assumes the owner winds it. Lunar train stopped by an unwound spring loses the phase `[I]`. A stop of N days means the discs lag N days: a stopped clock cannot self-correct. This is the biggest practical failure mode.
5. **Differential or linkage jamming** where a long-period cam meets a fast mean shaft.
6. **Wear**: cams run at under 1 rev per 27 d, lubricant creep and dust are the issue, not wear.
7. **Product-definition mismatch**: the clock shows the instantaneous tithi. Panchang days use the tithi at local sunrise and local rules (kshaya, vriddhi) `[S15]` (unverified at source), and regional Surya Siddhanta vs drik differences exist `[S15]` (unverified at source). A buyer reading the clock against a printed panchang will see disagreements even if the mechanism is perfect. This is a product-definition risk, not mechanical.
8. **Long-term**: the mean month and anomaly change slowly. Over decades the fitted ratios drift minutes per year, small beside the other items `[I]`.

## 10. The single most important technical unknown and the decisive test

**Unknown:** whether a real cam-plus-differential train built to table-clock tolerances holds the ideal +/-1 h (or at worst +/-4 h) tithi accuracy over 12 simulated months, given backlash, cam lash and tooth error.

**Cheapest decisive test** (to be run by the founder with an expert; I ran none):
1. Method: build a bench model of the lunar-anomaly cam plus the summing differential (laser-cut brass or 3D-printed plus brass shafts), driven by a stepper at 1 simulated day per minute, so 12 months run in about 6.6 hours. Read the output angle against the script's elongation with an encoder or camera, every simulated hour.
2. Cost `[A]`: Rs 15,000 to 40,000 for stepper, encoder, hardware and cut parts; a few hundred wire-EDM rupees for cams `[S10]` (unverified at source); plus 40 to 80 hours of the founder or an engineer.
3. Duration: 3 to 6 weeks including build.
4. **Pass:** output within +/-1 h equivalent (0.5 degree of elongation) of the script after accounting for fixed offset, for every one of the 12 simulated months, with the load of a real going train added through a torque gauge. **Fail:** error above +/-2 h, or any jam, or backlash alone above 0.5 h equivalent. If it fails at B3, retreat to B2 (+/-4 h) or the hybrid.

Before the bench model, a zero-cost check: verify the script against a published ephemeris/panchang for 10 tithi boundaries (drikpanchang or an almanac). Not done, because web pages could not be opened.

## 11. What a qualified expert or lab must review

- A horologist or mechanism designer: gear train layout, differential choice, going-train regulation.
- A panchang specialist or astronomer: which tithi definition (instantaneous drik, sunrise tithi, Surya Siddhanta), ayanamsa, and the amount of disagreement buyers will tolerate.
- My ephemeris code against a full ephemeris (for example JPL/Swiss Ephemeris); I used a truncated series.
- A metrologist: timing a sample movement for rate stability over a month.

## 12. Verified, calculated, hypothesis, missing

- **Verified (only via search summaries, so weakly):** tithi range and definition `[S1]`; Antikythera pin-and-slot `[S2]`; Chinese, Hebrew, Hijri watches exist `[S3, S4, S5]`; electronic Panchanga clock exists `[S9]`; wire-EDM rate `[S10]`; new moon time `[S13]`. None opened.
- **Calculated:** sections 3.1 to 3.6 `[S20]`.
- **Hypotheses:** hybrid reaches minutes of accuracy; a design-hours quote is the scarce item; bench model passes at B3. All `[H]` with tests above.
- **Missing:** a bare 8-day movement price; Indian clock-module makers; real-train error; Indian gear-cutting rates; regulatory content; a true-moon mechanism's technical detail (Arnold & Son).

## 13. Comparison across concepts

Single concept. Not applicable.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Tithi | Wikipedia | https://en.wikipedia.org/wiki/Tithi | undated | 2026-11-01 | Tithi definition, mean and range | search summary |
| 2 | Antikythera mechanism | Britannica | https://britannica.com/topic/Antikythera-mechanism | undated | 2026-11-01 | Pin-and-slot lunar anomaly, 9-year turntable | search summary |
| 3 | Perpetual Calendar Dethroned: Blancpain Calendrier Chinois Traditionnel; When The Moon And The Sun Unite | Revolution; Worldtempus | https://www.revolution.watch/perpetual-calendar-dethroned-meet-blancpains-calendrier-chinois-traditionnel/ | undated | 2026-11-01 | Chinese calendar cams, leap-month resets | search summary |
| 4 | CH711072A2 Hebrew mechanical perpetual calendar | Google Patents | https://patents.google.com/patent/CH711072A2/en | undated | 2026-11-01 | Hebrew 19-year mechanism | search summary |
| 5 | Parmigiani Hijri Perpetual Calendar | Watchonista; Parmigiani PDF | https://www.watchonista.com/articles/novelties/parmigiani-unveils-world-premiere-hijri-perpetual-calendar | 2019-12 | 2026-11-01 | Hijri mechanism, table clock 2011 | search summary |
| 6 | Lunar Hijra | Konstantin Chaykin | https://chaykin.ru/collections/watches/interior-clocks/lunar-hijra/ | undated | 2026-11-01 | Hijri table clock, price on request | search summary |
| 7 | Moon-phase accuracy: JLC models | WatchProSite; Daily Telegraph | https://www.watchprosite.com/editors-picks/jlc-models-moonphase-accuracy-question/2.904173.6196143/ | undated | 2026-11-01 | 122-year and 3,887-year moon claims | search summary |
| 8 | Arnold & Son True Moon 7828 | Worldtempus | https://en.worldtempus.com/article/arnold-et-son-true-moon-7828.html | 2010 | 2026-11-01 | True-moon watch exists | search summary |
| 9 | World's first Panchanga clock unveiled | Organiser | https://organiser.org/2025/05/26/294049/bharat/timekeeping-with-sanatana-science-worlds-first-panchanga-clock-unveiled-blending-with-modern-technology/ | 2025-05-26 | 2026-11-01 | Electronic panchang clock | search summary |
| 10 | Wire cutting services | IndiaMART | https://m.indiamart.com/impcat/wire-cutting-services.html | undated | 2026-11-01 | Wire-EDM about Rs 400/h | search summary |
| 11 | Tower Clocks India | IndiaMART | https://m.indiamart.com/nmctimemachines/tower-clocks.html | undated | 2026-11-01 | Indian tower-clock makers | search summary |
| 12 | Hermle 23054-030340 | Tribbensee | https://www.tribbensee.de/shop/hermle_en/23054-030340-hermle/?lang=en | undated | 2026-11-01 | 8-day moon-phase clock price | search summary |
| 13 | New Moon of November 2026 | Theskylive; Universaltimedate | https://theskylive.com/new-moon-november-2026 | undated | 2026-11-01 | New moon 07:02-07:03 UTC check | search summary |
| 14 | Person of Interest; Aditya Sambhare skeleton review | WatchTime India; WatchProSite | https://www.watchprosite.com/digest/aditya-sambhare-skeleton-unitas-custom-review/ | undated | 2026-11-01 | Indian independent watchmakers | search summary |
| 15 | Accuracy; Thiruganita versus Vakyam | Dekho Panchang; Drik Panchang | https://dekhopanchang.com/en/accuracy | undated | 2026-11-01 | Panchang source differences, sunrise rule | search summary |
| 16 | Watches and astronomy; My Time Machines astro | Ochs und Junior; my-time-machines | https://www.ochsundjunior.swiss/watches-and-astronomy/ | undated | 2026-11-01 | Cam-stack and Janvier differentials; 20 h deviation | search summary |
| 17 | Jens Olsen's World Clock | Copenhagen Museum; Wikipedia | https://cphmuseum.kk.dk/en/visit-us/current-exhibitions/jens-olsens-world-clock | undated | 2026-11-01 | Moon longitude, nodes, perigee dial | search summary |
| 18 | Ulysse Nardin Blast Moonstruck | Deployant; Watchprosite | https://deployant.com/the-fascinating-ulysse-nardin-moonstruck-now-back-in-a-new-blast-case/ | undated | 2026-11-01 | One day in 40.3 years | search summary |
| 19 | Bespoke mechanical tide clock; Corum clock table | Holly.co; A Timely Perspective | https://holly.co/shop/product/bespoke-mechanical-tide-clock/442667cf-a988-43b0-a316-605f91cee3a2 | undated | 2026-11-01 | Lead-time comparators | search summary |
| 20 | Tithi timing and mechanism model (own calculation) | This run | https://localhost/runs/2026-11-02-premium-controlled/06-expert-1-clock-calc.py (local file, not a web page) | 2026-11-01 | 2026-11-01 | Sections 3.1 to 3.6 | page |
