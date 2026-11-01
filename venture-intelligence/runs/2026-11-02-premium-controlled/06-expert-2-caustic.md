# Expert 2: Caustic-image architectural panel (optics and manufacturing feasibility only)

Date: 2026-11-01. Role: Multidisciplinary Expert. Scope: optics and manufacturing only. Commercial questions are out of scope.

**Access note (read first).** WebFetch failed on every host I tried (arxiv.org and infoscience.epfl.ch did not resolve: outside the session network allow-list). Every source below was seen through WebSearch summaries only, so each consequential source claim is marked `[S#, unverified at source]`. Under the opportunity standard the best outcome from this file is INVESTIGATE, never ADVANCE. Calculations are my own and saved: `06-expert-2-caustic-calc.py`, output `06-expert-2-caustic-calc.out`; results tagged [I] below come from that script (source 17).

## 0. Verdict in brief

- Class: **plausible** as a one-off art object with a *moving, soft* image; **proven** only at hobby and lab scale (small acrylic pieces, lab demos) [S1, unverified at source][S4, unverified at source]. Not proven at 0.5 m+ architectural scale with sunlight.
- The panel cannot hold a registered image. A fixed panel puts the image in its designed place within a tolerance of 2.9 degrees for about 22 hours a year (about 0.5% of daylight) [I][A]. The rest of the time the image slides across the floor at about 0.26 m per hour per metre of throw [I].
- Image is soft: roughly 40 to 110 resolvable pixels across, set by angle, not by distance [I]. Bold, simple, high-contrast pictures work. Photographs with fine detail do not.
- Biggest unknown: the contrast the finished, polished surface actually gives in hazy Indian sun (scatter floor). Decisive test in section 10.

## 1. Disciplines and deciding questions

| Discipline | Deciding question |
|---|---|
| Geometric and non-imaging optics | How sharp, how large, how contrasty can an image from a 0.53 degree source be? |
| Solar geometry | How far and how fast does the image move, and for how many hours is it usable at Delhi, Bengaluru, Kochi? |
| Computational design | Which published algorithm and software can produce the surface? |
| Metrology and tolerance | What surface slope and height error can be tolerated? |
| Manufacturing | Which route gives optical-quality surface at 0.3 to 1 m size at survivable cost? |
| Materials | UV, thermal, cleaning, scratch behaviour of PMMA vs low-iron glass |
| IP | Is there freedom to operate? |

## 2. Findings by discipline

### 2.1 Published methods (all `unverified at source`: search summaries only)

- Papas et al., "Goal-based caustics", Computer Graphics Forum 30(2), 503-511, 2011. Decomposes the target into overlapping anisotropic Gaussian kernels, one surface patch focuses onto each kernel; physical samples milled; demonstrated a natural image with few patches [S2, unverified at source].
- Schwartzburg, Testuz, Tagliasacchi, Pauly (EPFL), "High-contrast computational caustic design", ACM TOG 33(4), 2014. Optimal-transport mapping from input to target, then a 3D surface optimisation; claims high contrast including fully black areas and singularities of infinite density; simulated and fabricated examples [S1, unverified at source].
- Yue, Iwasaki, Chen, Dobashi, Nishita, "Poisson-based continuous surface generation for goal-based caustics", ACM TOG 33(3), 2014. Two Poisson-equation steps give a smooth continuous surface (smoothness matters for milling and for scatter) [S3, unverified at source].
- Disney patent US9188783 covers surfaces projecting a desired caustic made of summed micro-patch caustics [S7, unverified at source]. A related EPFL-author patent US10732405 "Refractive surface" is named in a search summary; I could not confirm its claims [S1, unverified at source].
- Software seen: Matt Ferraro's "Magic Window" code, MIT licence, with a Fusion 360 roughing toolpath workflow [S4, unverified at source]. Blender add-ons seen (Lightsheet, Vitrage Generator, Caustica) are renderers for faked or simulated caustics, not surface solvers [S13, unverified at source]. Papas, Schwartzburg and Yue implementations: not found as downloadable code after 3 searches (queries: "Goal-based caustics", "High-contrast computational caustic design", "Poisson-based continuous surface generation for goal-based caustics"). A hobby Instructables workflow used ray-tracing software to check a milled lens and noted a slightly blurry image [S5, unverified at source].
- Prior art is substantial: Ferraro's open-code window, the EPFL/Disney papers, a banknote security feature using caustic microlens profiles, and a hobby caustic clock [S4, unverified at source][S7, unverified at source][S16, unverified at source]. An EPFL summary says a flat-looking window can produce a person's image on the floor from sunlight alone [S16, unverified at source].

### 2.2 Materials and manufacturing (sources thin; flagged)

- Hobby route: back surface carries the height map, front stays flat; CNC router, then sanding through grits and automotive polish to clarity [S4, unverified at source].
- Machining vendor blog: standard tolerance on optical-grade acrylic +/-0.1 mm, tighter work to +/-0.01 mm; a commercial claim, not tied to image quality [S6, unverified at source].
- As-machined acrylic Ra 0.8 to 3.2 um, below 0.4 um after vapour polishing (vendor claims); vapour polishing can craze unannealed acrylic [S8, unverified at source].
- PMMA diamond-turns with better surface than polycarbonate but is prone to brittle fracture in microlens cutting [S15, unverified at source].
- Kiln-cast glass from sand moulds comes out rough and opaque, needing post-processing (TU Delft study) [S9, unverified at source]. Precision glass moulding is limited to roughly 0.5 to 70 mm diameter parts [S9, unverified at source]. No published tolerance for kiln-cast optical panels: Not found after 3 searches (queries: "kiln cast glass optical lens surface quality", "precision glass moulding limits large panels", "fire polish mold").
- India: Optics & Allied Engineering Pvt Ltd (Bengaluru, Bommasandra) lists precision diamond turning, and prototype lenses in PMMA, PC and metals; freeform and maximum part size not confirmed [S10, unverified at source]. Precitech held a diamond-turning workshop at CSIO Chandigarh; IIT Delhi publishes freeform ultra-precision machining work [S10, unverified at source]. No Indian price list found: Not found after 2 searches (queries: "India diamond turning freeform optics job shop PMMA", "caustic lens CNC acrylic India").
- Low-iron glass: Starphire transmittance above 91% at 6 mm (manufacturer datasheet) [S12][S12, unverified at source]. No India per-m2 price found after 1 search (query: "low iron glass Starphire Diamant Optiwhite price per m2 India").
- PMMA outdoors: sources claim no UV stabiliser needed and 10+ years without yellowing, but cite no test data; ASTM G154/G155 named as the test [S11, unverified at source]. Treat as hypothesis [H].

## 3. Calculations (all in the saved script; inputs and results)

Inputs: sun disc 0.53 degrees; PMMA n = 1.49 [K]; glass n = 1.52 [K]; Abbe numbers 57 (PMMA) and about 64 (glass) [K]; direct-beam illuminance 100,000 lux [A]; panel transmission 0.90 [A]; sun position formula: simple declination model, equation of time ignored (+/-16 min) [A].

**3.1 Blur versus distance.** Blur = d x tan(0.53 degrees). d = 0.5 m: 4.6 mm; 1 m: 9.3 mm; 2 m: 18.5 mm; 3 m: 27.8 mm; 5 m: 46.3 mm [I].

**3.2 Resolution is angle-limited, not distance-limited.** Blur and image size both scale with d, so resolvable pixels across = full angular extent of the image divided by 0.53 degrees. 20 degrees full angle gives about 38 px; 30 degrees about 57 px; 60 degrees about 113 px [I]. For a 0.6 m panel at d = 2 m and a 10 degree half-angle: image 1.31 m wide, 71 px; at 20 degrees half-angle: 2.06 m, 111 px [I]. Large angles need steep surface slopes and raise dispersion and Fresnel loss [K]. Honest summary: 40 to 110 px images. Bold line art, silhouettes, text: good. Portrait photograph: coarse, like a 64-pixel icon.

**3.3 Image size.** Set by deflection angle: L about W + 2 d tan(theta). A larger image dims inversely with area. Panel 0.6 m into image 1 m: mean image illuminance about 28,000 lux; into 2 m: about 7,000 lux [I: calc S17, inputs [A]].

**3.4 Contrast.** Ratio of mean image lux to room ambient (300, 1000, 3000 lux [A]): 1 m image gives 95:1, 29:1, 10:1; 2 m image gives 24:1, 8:1, 3:1 [I]. Scatter sets the black floor: if 2%, 5%, 15% of transmitted light scatters uniformly, the best possible image contrast is about 50:1, 20:1, 7:1 [I]. Hazy skies add a circumsolar glow that I did not quantify. The published "completely black areas" are for ideal point-like sources and simulation [S1, unverified at source]; a 0.53 degree extended source blurs black regions smaller than the blur. Realistic expectation: 10:1 to 30:1 in a dim room, 3:1 to 8:1 in a bright room [H, test in section 10].

**3.5 Dispersion.** Colour fringe about 0.18 degrees (PMMA, 10 degree deviation) and 0.35 degrees (20 degree deviation); glass 0.16 and 0.31 degrees. Same order as the sun disc, so edges show a coloured rim, a visible effect at wide angles [I].

**3.6 Sun movement.** The sun moves about 15 degrees per hour, so the image shifts about d x 0.26 rad per hour: 0.26 m/h at 1 m, 0.52 m/h at 2 m, 0.79 m/h at 3 m. It moves one blur width in about 2.1 minutes at any distance [I]. A thin-wedge refraction model shows deflection also changes with incidence: for a 20 degree tilted surface, deflection changes by up to 0.6 degrees for 10 to 20 degrees off design, and by 3 to 6 degrees at 50 to 60 degrees off design, so the image also distorts, not just slides [I]. The designed-for position is hit only near one sun direction.

**3.7 Registered hours (fixed glass).** With the image required within 2.9 degrees of the design direction (about 10% of a 1 m image at 2 m throw [A]): about 22 hours a year for a solstice-noon or solstice-morning design, about 9 hours a year for an equinox design; same at Delhi, Bengaluru and Kochi [I]. That is about 4 minutes a day averaged, on clear days only; with weather, fewer. Sun path repeats a given direction only near two dates a year, and about once at a solstice [I].

**3.8 Sliding-image hours** (vertical window, horizontal floor, window centre 1.5 m above floor, glass incidence up to 60 degrees, image landing 0.5 to 4 m inside; floor stretch 1/cos(zenith)). Hours per day, clear sky [I]:

| City | Date | N | E | S | W |
|---|---|---|---|---|---|
| Delhi | 21 Jun | 0 | 3.0 | 0 | 3.0 |
| Delhi | 21 Mar/Sep | 0 | 2.4 | 0 | 2.4 |
| Delhi | 21 Dec | 0 | 1.0 | 6.4 | 1.0 |
| Bengaluru | 21 Jun | 0 | 2.6 | 0 | 2.6 |
| Bengaluru | equinox | 0 | 2.6 | 0 | 2.6 |
| Bengaluru | 21 Dec | 0 | 1.8 | 7.6 | 1.8 |
| Kochi | 21 Jun | 0 | 2.6 | 0 | 2.6 |
| Kochi | equinox | 0 | 2.6 | 0 | 2.6 |
| Kochi | 21 Dec | 0 | 1.9 | 6.3 | 1.9 |

Reading: a south-facing window works only in the cooler half of the year (Delhi noon altitude 38 degrees at 21 Dec, 85 degrees at 21 Jun; Bengaluru 54 and 80; Kochi 57 and 77 [I]), when the sun is south and mid-altitude. In summer the sun is nearly overhead and does not enter a vertical south window, and the image lands too close to the wall. East and west windows give 2.4 to 3 hours a day year-round, but low-altitude sun stretches the floor image (1/cos(zenith) is 2 at zenith 60 degrees) and the image sweeps fast. North glass gets effectively none in these latitudes in the hours that count. A horizontal skylight or roof panel above a void gives 5.3 to 5.9 hours a day with altitude above 50 degrees in June, but 0 hours in Delhi in December and 2.2 to 3.0 hours in Bengaluru and Kochi [I]. Tropical Kochi and Bengaluru have the most stable sun geometry; Delhi swings most. Note "legible" here means the image exists on the floor and is not stretched beyond 2x; it is not the same as sitting in the designed place.

**3.9 Surface accuracy.** Deflection error = (n-1) x slope error. For allowed pointing error of 25% of the sun disc (0.133 degrees [A]), slope error must be below about 0.27 degrees (4.7 mrad); for 10%, below 0.11 degrees (1.9 mrad). Height error for a sinusoidal ripple = slope x wavelength / 2 pi: at 25% the allowance is 1.5 um at 2 mm wavelength, 3.8 um at 5 mm, 7.5 um at 10 mm, 22 um at 30 mm. At 10% it is 0.6, 1.5, 3.0, 9.0 um [I]. So: sub-5 micron height accuracy over cell scales of 2 to 10 mm, and roughly 20 um over 30 mm scales. That is far tighter than the vendor-claimed +/-0.1 mm normal CNC tolerance [S6, unverified at source], and at or just beyond the vendor-claimed +/-0.01 mm best case [S6, unverified at source].

**3.10 Scatter from tool marks (the likely killer).** Ball-nose scallop height h = s^2/(8R), max slope = s/(2R). With R = 3 mm and step 0.1 mm: scallop 0.42 um but slope 0.95 degrees, giving a deflection ripple of +/-0.47 degrees, nearly one sun disc; with R = 1 mm and 0.1 mm step: +/-1.4 degrees. Even Ra 0.4 um with 0.2 mm correlation length gives about 0.35 degrees halo; Ra 1.6 um gives 1.4 degrees [I]. These halo angles matter because a scatter cone wider than 0.53 degrees fogs the black regions. Conclusion: a milled surface must be polished by a process that removes ripple at 0.05 to 0.2 mm scale without destroying the 2 to 10 mm form. Hand sanding and automotive polish [S4, unverified at source] will wander in form by amounts I cannot bound [H].

**3.11 Thermal.** PMMA expansion over 0.6 m: 0.42 mm for a 10 K rise, 1.26 mm for 30 K, 1.68 mm for 40 K (coefficient 70e-6 per K [K]); low-iron glass 0.05 to 0.22 mm (9e-6 per K [K]) [I]. Uniform growth scales the image negligibly; sun-heated gradients bow the sheet and may add slope error. Not computed [H]. Fresnel loss at two surfaces about 7.6% at normal incidence [I].

## 4. Feasibility class and confidence

- Image on a floor from a sunlit freeform acrylic piece: **proven** at hobby and lab scale, confidence medium (sources are search summaries) [S1, unverified at source][S4, unverified at source].
- 0.5 m+ architectural panel with stable high contrast in Indian sun: **plausible**, confidence low. Depends on polish scatter and haze (unknown), and on the drifting image.
- Registered fixed image for hours a day: **infeasible** for a fixed panel [I]. Needs a tracker (heliostat or sun-following mount) or a design that is intentionally a moving image.
- Kiln-formed or cast glass at optical tolerance and size: **speculative**; no published tolerance found.

## 5. Production routes compared

All costs are my planning ranges [A] unless tagged; no quotes were obtained and none sourced. Basis for the [A]: none. Test: three quotes from Indian job shops for a 300 x 300 mm PMMA coupon.

| Route | Quality fit | Setup | Unit cost driver | MOQ | Risk |
|---|---|---|---|---|---|
| 3-axis or 5-axis CNC mill of cast PMMA, then polish | Form fits; ripple scatter after polish unknown | Low; CAM file | Machine hours (long, small step-over) plus polish labour | 1 | Ripple and haze; polishing destroys form [A] |
| Diamond turning or fly-cutting PMMA | Best surface finish in plastic [S15, unverified at source] | Needs ultra-precision machine; in India seen at Bengaluru and Chandigarh [S10, unverified at source] | Machine hours; limited to machine travel | 1 | Brittle fracture in PMMA [S15, unverified at source]; freeform on large panels unconfirmed |
| Cast resin or PMMA from a polished master (replication) | Good copies once master is good | Master plus silicone or metal mould | Material | Low per copy | Master still needs the above; shrinkage [K] |
| CNC mill of glass, then polish | Glass hardness; scratch-proof | High; diamond tooling, long polishing | Polishing hours | 1 | Freeform polishing of glass to micron accuracy: no supplier found; very costly [H] |
| Kiln-cast or slumped glass | Rough or opaque as-cast [S9, unverified at source] | Mould making | Kiln time | 1 | Cannot meet 5 um form at 0.5 m scale [H] |
| Injection moulded | Excellent for tiny lenses | Tooling high [A] | Low per piece at volume | High | Thick-part sink and warp; irrelevant for one-off art |
| 3D printing (SLA) | Hobby caustic clock worked, image slightly blurry [S5, unverified at source] | None | Resin | 1 | Layer lines, yellowing [H] |

Cheapest route that could meet the quality: cast PMMA, CNC mill with a large-radius tool and fine step-over, vapour or flame polish, test coupon first. For durability, laminate or bond to low-iron glass [H].

## 6. Bill of materials and delivery cost sketch (every line tagged)

No sourced costs exist for this concept. The following are placeholders for the Director to replace with quotes.

- Cast PMMA sheet 600 x 600 x 10 mm: price not found after 2 searches (queries: "cast acrylic sheet price India", "PMMA sheet price per kg India"). Unquoted [A].
- CNC machining: hours unknown. Rough estimate 10 to 30 machine hours for fine step-over [A], basis: scallop calc above; rate unquoted. Test: one quote.
- Polishing and metrology: unknown; metrology of a freeform surface to 2 um needs a coordinate measuring or optical profiler, not found at a vendor after 1 search [H].
- Low-iron glass lamination: unquoted; Indian low-iron float exists (Borosil solar glass) [S12, unverified at source] but price not found.
- Frame, install, site sun study: unquoted.

## 7. Safety, compliance, certification

- Concentration hazard: a panel that throws 28,000 lux onto a 1 m image is not a burning risk, but local focus within the design (singularities of infinite density in the published method [S1, unverified at source]) can create bright hot spots on flammable fabric, wood or skin. Designs that avoid high local concentration should be required [I: sun irradiance 1 kW/m2 [K] multiplied by local concentration; calc not run]. Needs a lab check.
- Architectural glazing in India: safety glass (toughened or laminated) rules for human impact apply to glazed openings; I did not research the BIS standard. Not checked. A PMMA panel as glazing may not meet fire or impact rules. A qualified glazing engineer must say.
- Fire behaviour of PMMA (burns, drips) matters for buildings. Not checked.

## 8. Intellectual property

- Methods are published and at least two patents exist: US9188783 (Disney) [S7, unverified at source] and US10732405 (EPFL authors) [S1, unverified at source], claims not read. Freedom to operate unknown: a patent attorney must read the claims. Ferraro's code is MIT-licensed [S4, unverified at source].
- What can be protected: the design of each artwork (registered design or copyright), process know-how in polishing, sun-study methods as trade secret.

## 9. Critical technical risks (failure modes)

1. Haze from tool-mark ripple and polish: lowers contrast to 7:1 to 20:1 or worse [I].
2. Form loss during polishing: slope error above 0.27 degrees ruins registration of detail [I].
3. Image drift: 0.26 m/h per metre of throw; fixed registration for about 22 h/yr [I].
4. Bright room: contrast falls to 3:1 to 10:1 at 2 m image and 3000 lux ambient [I].
5. Hazy Indian skies, diffuse monsoon light: direct beam share unknown; no DNI data checked [H].
6. Dirt, fingerprints and scratches on the structured face: scatter. Put relief on the inside face; PMMA scratches under cleaning [K, unverified].
7. Thermal bow from sun heating of PMMA [H].
8. UV yellowing of PMMA over years: claims of 10+ years lack test data [S11, unverified at source].
9. Dispersion rim at wide angle: 0.3 degrees [I].
10. Shadowing by window mullions, neighbouring buildings, and trees: site-specific.

## 10. Single most important technical unknown and the decisive test

**Unknown:** the achieved contrast and sharpness of the *finished, polished* surface under real Indian sun, i.e. the scatter floor after polishing. The geometry (drift, blur, pixel count) is calculable and bad but known. The scatter is not known.

**Test (no prototype built by this run; a future step):**
- Method: order one 150 x 150 mm cast PMMA coupon with a simple designed image (e.g. a high-contrast 40 x 40 px logo) from a job shop with the best finish they offer, plus a plain polished PMMA blank as reference. Take both outdoors in direct sun at a measured distance of 1 m. Photograph the image, measure the lux ratio of the brightest to darkest area with a lux meter and photograph; measure edge width.
- Cost: about Rs 10,000 to 40,000 for coupons, plus a lux meter [A]; basis none sourced, test by getting 2 quotes. Duration: 2 to 4 weeks [A].
- Pass: bright to black-region ratio above 10:1 in a shaded room; edge width within 2x the predicted blur (9 mm at 1 m); no visible stripes from tool marks.
- Fail: ratio below 5:1, or visible banding, or edge width above 3x blur.
- Cheaper first step: confirm by simulation (Blender Cycles with real index and an imported height map) before ordering anything.

Unknown inputs to retest by halving: if scatter is 2x my assumed 5% [A], best contrast falls to about 10:1 [I]; the verdict stays "soft, drifting image" [I]. The drift conclusion does not depend on any unsourced input (it is geometry). The contrast conclusion is driven by the polish scatter ("Unknown. Driven by polish scatter.").

## 11. What a qualified expert or lab must review

- A freeform optics engineer or metrology lab: slope and haze budget, measurement method.
- A glazing or façade engineer: safety, fire, and load for any building use.
- A patent attorney: US9188783 and US10732405 claims.
- A solar resource source: direct-beam data for the specific site and haze statistics (not checked).
- Not checked: Indian BIS standards for glazing, any quoted price, any Indian supplier beyond the one directory listing, whether sun-tracking mounts are affordable.

## Comparison across concepts

Single concept in this file. As a technical matter it is easier than a sun-tracking heliostat art piece and harder than a lamp-lit caustic (fixed point source, no drift). A sun-tracking mount or a fixed lamp-driven version removes the drift problem but changes the product.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | High-contrast computational caustic design (Schwartzburg et al.) | ACM TOG 33(4) / EPFL Infoscience | https://infoscience.epfl.ch/record/201509 | 2014 | 2026-11-01 | Optimal transport method; US10732405 mention | search summary |
| 2 | Goal-based caustics (Papas et al.) | Computer Graphics Forum 30(2) / Princeton | https://gfx.cs.princeton.edu/pubs/Papas_2011_GC/gbc.pdf | 2011 | 2026-11-01 | Gaussian-kernel patch method | search summary |
| 3 | Poisson-based continuous surface generation for goal-based caustics (Yue et al.) | ACM TOG 33(3) / SIGGRAPH history | https://history.siggraph.org/?p=106824 | 2014 | 2026-11-01 | Smooth continuous surface method | search summary |
| 4 | Math, optics and CNC combine to hide secret images in acrylic (Ferraro Magic Window) | Hackaday | https://hackaday.com/2021/08/23/math-optics-and-cnc-combine-to-hide-secret-images-in-acrylic | 2021-08-23 | 2026-11-01 | Hobby workflow, MIT code, polish | search summary |
| 5 | Introduction: 3D printing and CNCing weird freeform lenses | Instructables | https://instructables.com/Making-Custom-Lenses | undated | 2026-11-01 | Milled acrylic n 1.49, blur | search summary |
| 6 | What tolerances can be achieved when CNC machining optical-grade acrylic | Worthy Hardware blog | https://www.worthyhardware.com/?p=37444 | undated | 2026-11-01 | +/-0.1 mm and +/-0.01 mm claims | search summary |
| 7 | US9188783B2 Reflective and refractive surfaces configured to project desired caustic pattern | Google Patents | https://patents.google.com/patent/US9188783 | undated | 2026-11-01 | Disney patent | search summary |
| 8 | Vapor polishing for CNC machined plastics | JLCCNC | https://jlccnc.com/blog/vapor-polishing-cnc-plastics | undated | 2026-11-01 | Ra before and after polish, crazing | search summary |
| 9 | Precision glass moulding; TU Delft kiln-casting surface quality | Wikipedia; TU Delft repository | https://en.wikipedia.org/wiki/Precision_glass_moulding | undated | 2026-11-01 | Glass moulding size limit, rough cast surface | search summary |
| 10 | Optics & Allied Engineering Pvt Ltd listings; Precitech CSIO workshop | IndiaMART / Photonics.com / Precitech | https://m.indiamart.com/opticsindia/infrastructure.html | undated | 2026-11-01 | Indian diamond turning and PMMA prototype supplier | search summary |
| 11 | Acrylic (PMMA) properties and UV behaviour | Infinita Lab; Plastic Ranger | https://infinitalab.com/blog/acrylic-pmma-material-properties-testing | undated | 2026-11-01 | UV durability claims, ASTM G154 | search summary |
| 12 | Starphire technical data sheet; Borosil low-iron glass India | Vitro; Solar Thermal World | https://www.vitroglazings.com/media/gpvmzllx/vitro-starphire-vitro-technical-pds.pdf | undated | 2026-11-01 | Transmittance above 91% | search summary |
| 13 | Blender Lightsheet; Vitrage Generator; Caustica | GitHub; Superhive; 80.lv | https://www.github.com/markus-ebke/Blender-Lightsheet | undated | 2026-11-01 | Simulation tools are renderers | search summary |
| 14 | Declination and maximum altitude of the sun | PlanetCalc | https://planetcalc.com/10491/ | undated | 2026-11-01 | Altitude formula check | search summary |
| 15 | Diamond-turned PMMA tutorials and brittle fracture study | Univ. of Arizona optomech; BIT | https://pure.bit.edu.cn/zh/publications/mechanism-of-brittle-fracture-in-diamond-turning-of-microlens-arr | undated | 2026-11-01 | PMMA turning behaviour | search summary |
| 16 | Caustic engineering; Hiding images in plain sight | BLDGBLOG; dotat.at | https://bldgblog.com/2013/02/caustic-engineering/ | 2013-02 | 2026-11-01 | Window-scale projection and prior art | search summary |
| 17 | Local calculation script and output | This run | https://local.invalid/runs/2026-11-02-premium-controlled/06-expert-2-caustic-calc.py (local file) | 2026-11-01 | 2026-11-01 | All calculations | page |
