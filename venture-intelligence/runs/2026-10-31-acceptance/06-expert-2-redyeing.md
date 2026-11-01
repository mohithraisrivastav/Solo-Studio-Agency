# Expert assessment 2: Re-dyeing concepts (ShadeKit, ShadeCert, ShadeCover, DyeWatch)

Specialist: Multidisciplinary Expert. Date: 2026-10-31.
Constraints from the Director: founder capital ₹5,00,000; founder time ₹750 per hour; primary market India [A] (basis: Director's task message; not re-checked).

Method and limits.
- Inputs: 05-invent-2-redyeing.md (Inventor) and 03-market-3-redyeing.md (Market Investigator). I treated their claims as unverified and re-checked the ones the verdict depends on.
- I ran 37 web searches. WebFetch was not used. Every source is marked `search summary`. I opened no pages.
- Rows S55-S75 are sources the Inventor found. I did not re-search them. Their Via column says so.
- Search summaries sometimes did not tie a statement to one URL. Those rows say "mapping uncertain".
- I ran no patent searches of my own (search budget). The IP sections rely on the Inventor's searches plus patent numbers I met in technical searches.
- I contacted no one and ran no lab work. Every model below is a desk model. The models ran in python3 from the shell; inputs and results are in the tables.
- Money is in INR. Equipment listings rarely say whether GST is included; I treat them as ex-GST asks. Fees are shown before GST; add 18% [A] (basis: the usual rate for business services; confirm with a tax adviser).

Deciding questions, ranked. I spent searches on these first.
1. What share of reactive and disperse shade failures comes from dose and dye strength? Lead 1 lives or dies on this.
2. How much does a strength error move ΔE CMC, and can a per-drum assay detect it reliably and cheaply?
3. Which standards govern strength testing in India, and what does a test cost?
4. How are pass/fail and disputes settled today, and would an instrumental clause help or hurt the dyer?
5. Is a guarantee backed by insurance "insurance business" under Indian law, and can the founder sell cover at all?
6. Which handling, storage and trade rules apply to a shared dye kitchen?
7. Can an in-bath monitor survive lint and the dynamic range of a real bath?

## Part A. Common technical base (applies to all concepts)

### A1. Root causes of shade failure and their likely shares

What the sources say.
- An industrial knit study found that enzymatic scouring, raw cotton quality, water and electrolyte significantly affect the dyed shade [S1]. It reported high variation in ΔE for blacks [S1].
- A factorial experiment on cotton knits found temperature and liquor ratio the most influential factors, with significant interactions with salt type [S2].
- Calcium and magnesium shift reactive shades toward red (mapping uncertain) [S3]. Hardness raised ΔE beyond a 1.0 tolerance, more so in pale shades [S17]. Iron and copper dull and blue the shade [S17].
- Dye strength and reactivity vary lot to lot and even drum to drum (mapping uncertain) [S5]. Diluents used to standardise strength differ in moisture uptake, which can cause depth and hue differences between dye batches (mapping uncertain) [S5]. Strength standardisation of reactive powders often cuts strength by 30-40% with diluent [S6].
- A development booklet estimated that recipe errors or not following recipes could lead to about 20% of fabric re-shaded and about 10% re-dyed. These are illustrative estimates, not measurements [S44].
- A dyehouse study found the process very vulnerable to human error, with rejects rising with workload [S45].
- A widely repeated trade claim says 70% of dyeing problems come from pretreatment. I found no study behind it (mapping uncertain) [S46].
- Cotton Incorporated warns that lab dyeings made on lab-prepared fabric or very pure lab water correlate poorly with production [S49].
- For polyester, dispersion stability, particle agglomeration at high temperature, alkaline pH and heating rate above the glass transition drive shade variation [S18].

No source gives a measured breakdown by cause. Not found after 3 searches of mine (queries: "causes of shade variation reactive dyeing cotton percentage contribution root cause reprocessing study", "pareto analysis reasons for reprocessing knit dyeing factory shade not ok percentage dyeing faults case study Bangladesh", "right first time dyeing failure causes breakdown percent weighing dye water fabric preparation lab survey dyehouses"), on top of the Inventor's 3 searches. So the shares below are my prior. It should be replaced by the shadow-audit data in section B1.10.

Reactive dyeing of cotton knits on CETP water (Tirupur type). Shares are of re-processed kg.

| Cause | Mechanism | Who controls it | Likely share (range) | Normalised midpoint | Basis |
|---|---|---|---|---|---|
| Substrate and preparation | Yarn-lot mixing, cotton maturity, uneven scouring and bleaching, residual peroxide or alkali | Fabric owner (yarn); dyer (pretreatment) | 25-40% [A] | 32% [I] | Qualitative ranking in [S1]; unverified 70% claim [S46]; test by cause-coding 3 months of failed lots |
| Process | Liquor ratio, temperature and time profile, salt and alkali dosing rate, pH, machine loading | Dyer | 20-30% [A] | 24% [I] | Temperature and liquor ratio most influential [S2]; human error and workload [S45] |
| Lab-to-bulk recipe transfer | Lab fabric, lab water and lab liquor ratio differ from bulk | Dyer's lab | 5-15% [A] | 10% [I] | [S49]; test by comparing lab-dip and first-bulk ΔE |
| Weighing and dosing | Wrong dye, tare and transcription errors, coarse store scales on small components, pipetting in the lab | Dye store, lab | 8-15% [A] | 11% [I] | Recipe-error estimate [S44]; calculation C2 |
| Dye strength and moisture | Batch strength variation, moisture taken up after opening | Dye maker, trader, store | 5-12% [A] | 8% [I] | [S5, S6]; calculation C1 |
| Water hardness and metals | Ca and Mg precipitation, Fe and Cu shade shifts | Dyer, CETP | 2-8% [A] | 5% [I] | [S3, S17]; CETP RO permeate is soft [K], so the share is lower than in borewell clusters |
| Visual assessment and standards | Observer error, light-source mismatch, metamerism, aged physical standards | Exporter merchandiser, dyer | 5-15% [A] | 10% [I] | Up to 25% wrong visual decisions near tolerance (secondary claim) [S13]; calculation C7 |

Disperse dyeing of polyester (Surat type).

| Cause | Likely share (range) | Normalised midpoint | Basis |
|---|---|---|---|
| Substrate: yarn texturing and heat history, construction, oligomers | 20-35% [A] | 29% [I] | Physical reasoning: dye uptake of polyester depends on its crystallinity and orientation [K] |
| Process: heating rate, holding temperature and time, pH, circulation, liquor ratio | 25-40% [A] | 34% [I] | [S18] |
| Dispersion quality and dye strength | 8-15% [A] | 12% [I] | Agglomeration and pH sensitivity [S18] |
| Weighing and dosing | 8-15% [A] | 12% [I] | As for reactive [A] |
| Water | 1-5% [A] | 3% [I] | Disperse dyes are less sensitive to hardness than reactive dyes [K] |
| Visual and metamerism | 5-15% [A] | 10% [I] | [S13] |

What this means.
- Dose plus strength together is about 13-27% of reactive failures on this prior, midpoint about 20% [I] (chain: 8-15% plus 5-12%). That is below the Inventor's "at least a third" condition for Lead 1, but near the break-even I calculate in C4 (16-22%) [I].
- Most failures sit in substrate and process. Neither Lead 1 nor Lead 2 removes them; Lead 2 can only move their cost to the party that caused them [I].
- Confidence: low. No measured breakdown exists in the sources I found.

### A2. Testing dye strength per drum

Standards.
- The BIS strength-by-dyeing standards are split by reactive group: IS 7842:2022 for vinyl sulphone, IS 7447:2022 for dichlorotriazinyl, IS 7448 for monochlorotriazinyl and IS 7845:2022 for trichloropyrimidyl dyes [S7, S8]. IS 7845 compares a test dye with an agreed standard in repeated dyeings and gives comparative strength only [S7].
- So the Inventor's reference to IS 7845 fits only trichloropyrimidyl dyes [I]. Most Tirupur exhaust recipes probably use vinyl sulphone and bifunctional dyes [A] (basis: common practice in exhaust dyeing of cotton knits; test by reading 3 units' recipe cards). For bifunctional dyes I found no specific IS; a lab would need an agreed in-house method based on IS 7842 or the solution method [I].
- For disperse dyes, IS 12149:1987 covers strength by exhaust dyeing (current status not confirmed) and IS 11635:2023 covers strength by screen printing [S8].
- The solution method is AATCC TM182, technically equivalent to ISO 105-Z10. It compares transmittance of test and reference dye solutions. Users favour it for speed, repeatability and reproducibility [S9]. It is valid for an end use only after showing that solution strength matches strength on the textile [S9]. Test and reference must have similar absorption curves [S10].

Method comparison.

| Method | What it measures | Hands-on time | Elapsed time | In-house cost per test | Outsourced cost | Fit for per-drum use |
|---|---|---|---|---|---|---|
| Solution strength (AATCC 182 / ISO 105-Z10) on a UV-Vis | Colourant content, not fixation | 30-60 min [A] | Under 1 hour [A] | About ₹120 [I] (C6) | Not found [I] | Yes, if correlated to fibre strength for each dye [S9] |
| Dyeing test (IS 7842 family) on a lab dyeing machine plus reflectance spectrophotometer | Strength on cotton, including fixation and shade | About 1.5 h [A] | 3-5 h with wash-off and drying [A] | About ₹350 [I] (C6) | Not found; SITRA lists computer colour matching for ΔE and strength, price not seen [S19] | Only for monthly cross-checks; too imprecise per drum without replicates (C3) |
| Moisture check (oven drying) | Water picked up after opening | 10 min [A] | 2-4 h [A] | Under ₹50 [A] | Not checked | Yes, on each opened drum |

Price anchors: SITRA's 2024 chemical list shows fastness tests at about ₹250-900 a test [S19]. CIRCOT charges ₹900 to identify a dye class [S20]. A dyeing-based strength test at a research association is likely ₹500-1,500 [A] (basis: those anchors; get written quotes from SITRA and Tirupur labs).

Precision is the real constraint. The precision of colour-strength determination has been treated statistically, but I saw only the abstract (mapping uncertain) [S48]. Calculation C3 shows that if a dyeing test has a 2.5% standard deviation [A], detecting a 3% strength deviation needs about 11 replicate pairs [I]. At a 1% standard deviation, typical of a good solution method [A], 2 replicates suffice [I].

How much a strength error matters (calculation C1).
- When every dye in a recipe is weak by the same amount, a 5% error gives only ΔE CMC(2:1) 0.25-0.50 [I]. Lightness changes most, and CMC(2:1) down-weights lightness [K].
- When one component of a compound shade is off, a 3% error gives about 0.5 and a 5% error about 0.85 on beige and grey [I]. That uses most of a 1.0 tolerance.
- So strength control matters most for compound shades (greys, beiges, browns, navies) and for drums that differ from the drum the lab used [I].
- A dispensing patent says a 1% dose error gives a visibly different result [S47]. My model gives ΔE CMC 0.05-0.17 for 1% [I]. "Visible side by side" and "outside tolerance" are different tests. The patent holder also sells dispensing, so I weight the model more, with low-medium confidence because the model uses synthetic dye spectra.

Practical rule for a kitchen [I]: run the solution assay on each manufacturer batch, not each drum. Run a moisture check on each opened drum. Run a monthly dyeing-test cross-check on the 10 highest-volume dyes. Above all, the strength factor must be relative to the dye the lab used to build the recipe, not to an abstract standard.

### A3. Instrumental pass/fail and how disputes are settled

- ISO 105-J03:2009 is the current method for calculating ΔE CMC(l:c) [S12]. Textiles use l:c = 2:1 for acceptability [S11]. ΔE CMC ≤ 1.0 is the usual single-number pass limit (weak vendor source) [S11, S13].
- Tolerances in use: Kohl's sets 0.8 CMC for solid lab dips [S59]. A conference paper used 1.2 CMC as a commercial limit [S60]. A trade explainer says 2.0-3.5 is common for bulk items (weak) [S11].
- ASTM D2244 says instrumental tolerances should be correlated with visual appraisal, and that metamerism needs visual confirmation under non-daylight sources [S16]. CMC(2:1) correlated best with visual decisions in an apparel maker's study [S14].
- Visual approval remains essential in practice [S61]. Up to a quarter of professional visual pass/fail decisions may be wrong. This is a secondary claim: the review attributes it to an earlier reference [S13]. A single instrument was at least as reliable as one observer and more reproducible in a classic study [S15].
- How disputes are settled today: by the buyer's visual decision, then negotiation. Off-shade goods are negotiated or sold as seconds, and a Delhi fabric owner claimed about ₹25.4 lakh against about ₹1.64 lakh of dyeing charges [S55]. I found no standard dispute procedure for Indian job work. Not found after 2 searches (queries: "CMC 2:1 delta E 1.0 commercial tolerance textile pass fail ISO 105-J03 disputes visual assessment overrides instrumental", "brand colour standards manual supplier bulk shade visual assessment prevails over instrumental CMC tolerance 1.0 bulk approval shade band").
- Two instruments of different makes can disagree by a few tenths of a ΔE unit on the same sample [A] (basis: instrument geometry and calibration differences [K]; test by measuring 20 swatches on 2 instruments). So a certificate must name one master instrument, the illuminant and observer, and the standard's physical and spectral form [I].

Calculation C7 asks whether an instrumental clause would help the dyer. It depends on how strict the exporter is today.
- If merchandisers reject at about ΔE 1.0 with noisy judgement, 53-75% of visual rejects are within instrumental tolerance. The clause then cuts the dyer's rejections [I].
- If merchandisers are lenient (effective limit about 1.2), 56-61% of lots that fail instrumentally are passed visually today. The clause would then raise the dyer's rejections [I].
- This is the main hidden risk in Lead 2.

### A4. Equipment and lab setup costs (listing prices, GST not stated)

| Item | Use | Price range | Tag |
|---|---|---|---|
| Double-beam UV-Vis spectrophotometer | Solution strength | ₹1,25,000-3,80,000; GeM model ₹3,28,000 | [S21] |
| Reflectance spectrophotometer | Shade measurement, dyeing-test read-out | ₹1,75,000 entry [S56]; Lovibond LC100 ₹4,75,000; TR series ₹7,45,000 [S23] | [S23, S56] |
| Lab dyeing machine | Dyeing tests, cause tests | ₹80,000-2,45,000; infrared not re-checked | [S57] |
| Light booth D65/TL84/CWF/UV | Visual assessment | ₹17,500-20,000 typical; ₹45,000 premium | [S22] |
| Analytical balance 220 g, 1 mg | Assay weighing | ₹12,300-30,000; 0.1 mg model ₹57,820 | [S24] |
| Bench scale 6 kg, 0.1 g | Kit weighing of small components | ₹10,000-25,000 | [A] (basis: not searched; get quotes) |
| Platform scale 30 kg, 1 g | Kit weighing of large components | ₹8,000-20,000 | [A] (basis: not searched) |
| Local exhaust ventilation (weighing booth) | Dust control for sensitising dyes | ₹60,000-1,50,000 | [A] (basis: not searched; get quotes from a ventilation fabricator) |
| Conditioning (AC, dehumidifier, hygrometer) | Stable sample moisture before measurement | ₹50,000-90,000 | [A] (basis: not searched) |
| Dye dissolving system | In-plant alternative to kits | ₹2,00,000-5,00,000 | [S58] |

Notes.
- The Inventor priced a light booth at ₹40,000-80,000 [A]. Listings show ₹17,500-45,000 for local booths [S22].
- The ₹1,75,000 entry instrument [S56] may not have the repeatability and geometry a certificate needs. Its specification was not checked [I].
- The Inventor's ShadeKit kitchen budget had no UV-Vis, no ventilation and no PPE [I] (chain: equipment list in the Inventor's Lead 1 section). It did include a reflectance instrument and a lab dyeing machine, which can be deferred by outsourcing monthly dyeing tests [I].

### A5. Handling and storage rules for dyes and chemicals

| Rule or hazard | Applies to | What it requires | Source | Status |
|---|---|---|---|---|
| Reactive dyes are respiratory sensitisers (H334) | Anyone weighing powder | Dispense reactive dyes under local exhaust ventilation regardless of quantity; control all significant exposure | [S25, S26] | Checked (UK guidance, EU classification; no Indian equivalent found) |
| Occupational asthma in dye weighers | Kitchen staff | Health questionnaire at hiring and yearly; keep people with respiratory illness off powder work | [S27, S28]; questionnaire is [A] (basis: standard sensitiser practice; confirm with an occupational physician) | Checked (medical literature) |
| Moisture and hydrolysis | Dye powders and solutions | Keep drums closed and dry; never store dissolved reactive dyes. Hydrolysis depends on pH and reactive group: one triazinyl dye solution lost 60% to hydrolysis in 4 weeks at 40 °C and pH 6.5; liquids hydrolyse faster than powders | [S50] | Checked (patents) |
| Legal Metrology: weighing instruments used in transactions | Kitchen balances, because dye is sold by weight | Verification and stamping under section 24; penalties under sections 33-35 | [S40] | Checked; fee and interval vary by state, not found |
| Legal Metrology (Packaged Commodities) Rules 2011, Rule 3 | Sealed kits | Exempt above 25 kg and for industrial consumers who buy directly from the manufacturer. A kitchen is a packer, not the dye manufacturer, so the exemption may not fit; a 2024 draft proposed changing Rule 3 | [S39] | Unresolved: needs a Legal Metrology consultant |
| Hazardous and Other Wastes Rules 2016, Schedule I entry 33.1 | Empty dye drums and liners | Authorisation from the State Pollution Control Board to generate, store and dispose; reuse needs Rule 9 permission under an SOP; one board barred trading drums to others | [S42] | Checked (board documents) |
| MSIHC Rules 1989 | Isolated storage of listed chemicals | Duties start above threshold quantities in the schedules; enforced by pollution boards | [S41] | Thresholds for dyes, caustic soda and peroxide not found; likely not triggered by a dye-only kitchen [A] (basis: dyes are not obvious Schedule 1 entries; confirm with the schedules) |
| Factories Act 1948 and Tamil Nadu Factories Rules | A kitchen with 10 or more workers using power | Licence, safety and welfare duties | Not searched | [A] (basis: the Act's worker threshold as I recall; confirm with a labour consultant) |
| Consent from the State Pollution Control Board | A dye repacking unit | May need consent to establish and operate | Not searched | Unchecked |
| Fine organic powder | Dye store | Dust clouds of organic powders can ignite | [K] | Background principle; housekeeping and no open flames |

### A6. Insurance regulation (summary; detail in Lead 3)

- Only an Indian insurance company registered with IRDAI may carry on insurance business [S29]. Carrying on insurance business without registration attracts a penalty under section 103 [S30].
- Only registered insurers and IRDAI-registered agents and intermediaries may sell insurance products [S31].
- Regulators abroad have treated extended warranties sold by non-insurers as insurance: Saudi Arabia [S32] and the Philippines [S33]. Australia lets retailers issue warranties that insurers indemnify [S34]. I found no IRDAI ruling on a service firm's guarantee backed by insurance. Not found after 3 searches (queries in Lead 3 section 2).

## Part B. Concepts

## Lead 1: ShadeKit (strength-assayed, pre-weighed lot kits from a shared kitchen)

### 1. Disciplines and deciding questions

| Discipline | Governing principle | Deciding question |
|---|---|---|
| Textile chemistry | Shade depends on the dye fixed on the fibre, not on dye weighed [K] | Do dose and strength cause enough failures (C4 break-even 16-22%)? |
| Colour science | Kubelka-Munk: K/S rises roughly in proportion to dye on fibre [K] | Does a 3-5% strength error matter for real shades (C1)? |
| Analytical chemistry | Beer-Lambert absorbance for solution strength [K] | Can solution strength stand in for dyeing strength for each dye [S9]? |
| Logistics | A kit must arrive before the bath is ready | Can 67 kits a day arrive within about 2 hours (C5)? |
| Occupational health | Sensitising dust | Is ventilation affordable inside the budget (A4)? |
| Metrology and trade law | Sale by weight needs verified instruments | Do Legal Metrology rules allow sealed kits without retail labelling (A5)? |

### 2. Findings by discipline

- Chemistry: the kit removes weighing errors and drum-strength differences only. It does nothing for substrate, process, water or judgement, which make up about 80% of failures on my prior [I] (chain: A1 midpoints).
- Colour science: single-component strength errors of 3-5% in compound shades use 50-85% of a 1.0 tolerance [I] (C1). Uniform errors matter much less [I].
- Weighing: in the bulk store, a component of 15-30 g on a scale accurate to ±2-5 g carries a 7-33% error [I] (C2). In the lab, pipetting 0.5-1 mL of stock solution for pale shades carries 1-2% [I] (C2). So the kitchen fixes the bulk side, but pale-shade lab error stays with the dyer [I].
- Reference problem: weight = recipe % × lot weight ÷ strength factor is correct only if the lab built the recipe with dye of factor 1.0 [I]. The kitchen must therefore supply the dyer's lab with the same assayed dyes in small lab packs, or record which drum the lab used [I].
- Moisture: reactive powders take up moisture and diluents differ in hygroscopicity [S5]. A drum assayed on arrival can drift after opening [I]. Sealed single-lot sachets stop that drift after weighing [K].
- Prior art: in-plant central colour kitchens exist (Thies, THEN) [S69]. Strength by solution is a routine dye-maker method [S9].
- Disperse dyes (Surat): process and substrate shares are higher and dispersion quality matters [S18]. The case for kits is weaker there [I].

### 3. Calculations

| # | Inputs | Method | Result |
|---|---|---|---|
| C1 | Synthetic yellow, red and blue spectra; K/S 8 per 1% at peak [A] (basis: order of magnitude for reactive dyes on cotton; test on real dyes); white cotton R 0.88 [A]; 6504 K illuminant and analytic CIE 1931 fit as stand-ins for D65/10° [K] | Kubelka-Munk single-constant, CIELAB, ΔE CMC(2:1) | Uniform -5% strength: ΔE 0.25-0.50; one dye -5%: 0.58-0.87; one dye -3%: 0.34-0.52; uniform -1%: 0.05-0.10 [I] |
| C2 | Lot 300 kg [A] (basis: Inventor's base unit); components 0.005-2% owf [A] | Scale error ÷ grams weighed | 15 g at ±5 g: 33%; 30 g at ±2 g: 6.7%; 150 g at ±0.5 g: 0.3% [I] |
| C3 | Assay standard deviation 0.75-3% [A] (basis: no precision data found [S48]; test with 10 repeat assays) | n = 2(1.96+0.84)²σ²/δ² | Detect 3%: n = 1-2 at σ ≤ 1%; n = 11 at σ = 2.5% [I] |
| C4 | Base unit 6,00,000 kg a year, 6% re-processed, ₹60 extra per kg [A] (basis: Inventor's base case); fee ₹0.50 per kg on good lots [A]; kit removes 60-80% of dose and strength failures [A] (basis: judgement; test in pilot) | Net = failure cost × share × removal − fee | Break-even share 16-22% without the store-hand saving, 6-8% with the Inventor's ₹1.8 lakh saving [I]; at a 20% share the dyer nets -₹25,000 to +₹61,000 a year before that saving [I] |
| C5 | 10 units × 2 t a day [A]; 300 kg lots [A]; 3 dyes per recipe [A]; 2.5 min per weighing [A]; 2.5% average depth [A] (basis: Inventor); 25 kg drums [A] | Arithmetic | 67 lots and about 208 weighings a day; 8.7 weighing-hours a day; 500 kg of dye a day, about 20 drums [I]. Assay per drum: 15 technician-hours a day; per batch of 5 drums [A]: 3 hours [I] |
| C6 | Technician ₹20,000 a month [A] (basis: Inventor); consumables ₹40 per solution test and ₹150 per dyeing test [A]; instrument depreciation over 5 years [A] | Labour + consumables + depreciation | Solution test about ₹120; dyeing test about ₹350 [I] |
| C5b | Running cost at 10 units: 4 staff at ₹20,000 a month, rent ₹25,000 a month, 2 bikes at ₹12,000 a month, outsourced cross-checks ₹1,200 × 10 a month, PPE ₹30,000, sachets ₹6 per kit [A] (basis: Inventor's staffing plus my additions) | Sum | About ₹18.4 lakh a year against fee revenue of about ₹28.7 lakh, so about ₹10.2 lakh contribution before the founder [I] (Inventor said ₹12.5 lakh) |

### 4. Feasibility class and confidence

- Technical: plausible. Every component is proven in some setting: central weighing [S69] and solution strength testing [S9]. The shared, multi-owner kitchen with strength-corrected kits is untested [I].
- Economic: marginal. The value depends on a dose-plus-strength share I could not measure, and my prior midpoint (about 20%) sits at the break-even [I] (chain: A1 and C4).
- Confidence: medium on the technical class; low on the economics.

### 5. Production routes compared

| Route | Setup cost | Unit cost drivers | Minimum scale | Lead time | Quality risk |
|---|---|---|---|---|---|
| Status quo: in-plant manual weighing | Nil [I] | Store labour, coarse scales | None | Same day | High on small components (C2) [I] |
| In-plant dissolving and dosing | ₹2-5 lakh per unit [S58] | Capital, maintenance | One unit | Weeks to install [A] | Weighs to label strength; no drum correction [I] |
| Shared kitchen, manual weighing, solution assay (recommended pilot) | About ₹2.8-6.1 lakh (section 6) [I] | Weighers, delivery, assays | About 3 units to keep 1 weigher busy (60 weighings a day) [I] | 2-4 weeks to set up [A] | Delivery timing; reference mismatch with the dyer's lab [I] |
| Trader-run kitchen with founder's assay service | Assay kit only, about ₹1.5-3 lakh [I] (chain: UV-Vis [S21] plus balance [S24]) | Assay fee per batch | One trader | 2 weeks [A] | Trader may resist exposing weak drums [I] |
| Liquid strength-standardised concentrates | Formulation work, not costed | Stability testing | One dye maker | Months [A] | Hydrolysis and gelling in storage [S50] |

### 6. Bill of materials or delivery cost sketch (pilot kitchen, 3 units)

| Line | Cost | Tag |
|---|---|---|
| UV-Vis double beam | ₹1,25,000-2,45,000 | [S21] |
| Analytical balance 220 g, 1 mg | ₹12,300-30,000 | [S24] |
| Bench scale 6 kg, 0.1 g | ₹10,000-25,000 | [A] (basis: not searched) |
| Platform scale 30 kg, 1 g | ₹8,000-20,000 | [A] (basis: not searched) |
| Legal Metrology verification | ₹1,000-5,000 | [A] (basis: state schedules vary [S40]) |
| Weighing booth with exhaust | ₹60,000-1,50,000 | [A] (basis: not searched) |
| PPE for year 1 (P3 masks, gloves, goggles) | ₹15,000-30,000 | [A] |
| Glassware, pipettes, flasks | ₹15,000-30,000 | [A] |
| Drying oven for moisture checks | ₹15,000-40,000 | [A] |
| Sealer, laminate sachets, QR label printer | ₹15,000-35,000 | [A] (basis: Inventor's ₹15,000 plus a printer) |
| Total setup | ₹2.76-6.10 lakh | [I] (sum of the lines above) |
| Monthly dyeing-test cross-checks, 10 tests at an outside lab | ₹5,000-15,000 a month | [A] (basis: ₹500-1,500 a test, A2) |

The low end fits the capital. The high end exceeds it. A reflectance spectrophotometer and lab dyeing machine are deferred [I].

### 7. Safety, compliance, certification

- Ventilated weighing for reactive dyes is required good practice [S25]. Without it, the kitchen concentrates the sensitisation risk of 10 dye stores into 2-3 people [I].
- Balances used to bill by weight need Legal Metrology verification [S40].
- Packaged Commodities labelling: the industrial-consumer exemption is written for buyers who purchase directly from the manufacturer [S39]. Whether a repacking kitchen qualifies needs a Legal Metrology consultant [I].
- Empty drums are hazardous waste under entry 33.1 and need board authorisation [S42]. Returning drums to the trader may need Rule 9 permission [S42].
- Pollution-board consent and Factories Act registration: unchecked (A5).
- GST on dyes and on the kit fee: not checked [A] (basis: assume 18% on the fee; confirm the dye rate with a tax adviser).

### 8. Intellectual property

- The PVA envelope patent for reactive dyes dates from about 1991 [S70]. It is probably expired [A] (basis: 20-year patent term from filing; confirm on the register).
- The Inventor found no close match for a shared, strength-corrected kit service in 8 searches. I did not re-search.
- A business method is probably not patentable in India [A] (basis: Patents Act section 3(k) as I recall; confirm with a patent agent). Protectable assets: the batch-strength database (trade secret), the brand (trademark) and supply contracts [I].

### 9. Critical technical risks

1. Dose and strength turn out to cause under 15% of failures, below break-even (C4) [I].
2. Reference mismatch: the dyer's lab builds recipes with unassayed dye, so the kitchen's correction makes bulk worse, not better [I].
3. Solution strength does not track fibre strength for some dyes, especially mixtures and bifunctional dyes [S9, S10].
4. Delivery misses the bath window, and the master reverts to his own weighing [A] (basis: Inventor's risk; test with timed runs).
5. Sensitisation of kitchen staff without proper ventilation [S25, S27].

### 10. Cheapest test to retire the biggest technical risk

Risk: the dose-plus-strength share is too small.
- Method: at 3 units, (a) cause-code the last 3 months of failed lots with a retired dyeing master; (b) re-weigh 50 dye issues per unit on a calibrated 0.1 g scale and record each store scale's resolution; (c) collect 30 batch samples (10 high-volume dyes × 3 batches) and run solution strength against the dyer's lab stock at an outside lab, plus 5 dyeing-test cross-checks.
- Cost: lab fees about ₹15,000-25,000 [A] (basis: 30 solution tests at ₹300-600 and 5 dyeing tests at ₹1,000-1,500, A2); scale ₹10,000-25,000 [A]; retired master ₹30,000 [A] (basis: Market Investigator's figure); travel ₹30,000 [A]; founder 60 hours × ₹750 = ₹45,000 [I]. Total about ₹1.3-1.55 lakh [I].
- Duration: 4 weeks [A].
- Pass: dose plus strength coded as the cause in at least 25% of failed lots, and at least 3 of 30 batches more than 3% off the lab stock in a dye used in compound shades [A] (basis: C4 break-even plus margin; C1 shows 3% is about half a tolerance).
- Fail: under 15% of failures, and no more than 1 batch in 30 off by more than 3% [A].

### 11. What a qualified expert or lab must review

- A textile chemist (a dye maker's applications lab or SITRA): validate solution-to-fibre strength correlation for the 10 main dyes.
- An occupational hygienist: ventilation design and exposure monitoring.
- A Legal Metrology consultant: kit labelling and balance verification.
- A pollution-board consultant: consent and drum authorisation.

## Lead 2: ShadeCert (neutral lot certificate with retained samples and a cause test)

### 1. Disciplines and deciding questions

| Discipline | Governing principle | Deciding question |
|---|---|---|
| Colour measurement | ISO 105-J03 CMC(2:1) [S12] | Will instrumental pass/fail reduce or raise the dyer's rejections (C7)? |
| Psychophysics | Visual and instrumental judgements disagree near tolerance [S13, S15] | Will exporters accept instrument-first decisions [S16, S61]? |
| Textile chemistry | Dyeability depends on substrate and pretreatment [S1] | Can a cause test separate yarn fault from pretreatment fault from dye fault? |
| Contract law | Expert-determination clauses | Is a loser-pays clause enforceable and cheap to run? |
| Liability insurance | Certifier errors | Can ShadeCert insure its own errors [S38]? |

### 2. Findings by discipline

- Measurement: certification-grade work needs one master instrument, conditioned samples and a fixed procedure: 4 readings rotated, D65/10° plus TL84 and A for metamerism [A] (basis: common laboratory practice; confirm against ISO 105-J01 and the exporter's manual). Cotton's moisture and temperature change its measured colour [K], so samples need conditioning before reading [A] (basis: standard conditioning practice; test the drift on 10 swatches).
- Psychophysics: CMC(2:1) correlates best with visual decisions [S14]. Visual decisions remain contractually dominant [S16, S61].
- Calculation C7 shows the clause helps the dyer only where the exporter is stricter than the instrument. Where exporters are lenient, it raises rejections [I].
- Cause test: the Inventor's design keeps a swatch of prepared fabric, which is fabric after the dyer's own pretreatment. A dyeability fault in that swatch could be the yarn (fabric owner pays) or the pretreatment (dyer pays) [I]. The test needs a retained greige swatch too, scoured and bleached in the lab by a standard method, then dyed beside a reference fabric [I]. That is about 1-2 days of lab work [A] (basis: lab pretreatment plus dyeing cycles), so the Inventor's 48 hours is tight but possible [I].
- Lab-to-bulk differences from lab water and lab fabric [S49] mean a "process" verdict must allow for the dyer's own lab practice [I].
- Accreditation: NABL charges application, annual and assessor fees per NABL 100, but I found no amounts [S43]. Accreditation can wait until volume exists [I].
- Insurance of the certifier: Indian insurers sell errors-and-omissions and professional indemnity cover [S38]. I found no wording written for testing labs [S38].

### 3. Calculations

| # | Inputs | Method | Result |
|---|---|---|---|
| C7 | True lot ΔE drawn from a 3-D normal so that 6% exceed 1.0 [A] (basis: Inventor's 6% re-processing, used as a stand-in); visual judgement noise 20-40% (log-normal) [A] (basis: tuned so that 21-28% of decisions near tolerance are wrong, matching [S13]); visual limit 1.0 or 1.2 [A] | Monte Carlo, 4,00,000 lots | Strict exporter (limit 1.0): visual rejects 9-15% vs 6% instrumental; 53-75% of visual rejects are within tolerance. Lenient exporter (limit 1.2): visual rejects 3.4-8.4%; 56-61% of instrumental fails pass visually today [I] |
| C8 | 10 units × 2,000 lots a year [A] (basis: Inventor); 50 certificates per technician-day [A] (basis: about 6 minutes a lot plus handling) | Arithmetic | 20,000 certificates a year, 67 a day, 1.3 technicians plus one pick-up rider [I] |
| C8b | ₹100 per certificate [A] (basis: Inventor) | 20,000 × ₹100 | ₹20 lakh a year before GST at 10 units [I] |

### 4. Feasibility class and confidence

- Measurement: proven. Instruments and methods are in commercial use [S12, S16].
- Cause test: plausible. The principle is sound but untested for allocating blame [I].
- Adoption: the deciding risk is commercial, not technical. C7 shows a clause can hurt dyers whose exporters are lenient [I].
- Confidence: medium on the technical class; low on whether dyers gain.

### 5. Production routes compared

| Route | Setup cost | Unit cost drivers | Quality risk |
|---|---|---|---|
| Own hub with benchtop instrument | About ₹2.8-7.1 lakh (section 6) [I] | Technician time, conditioning | Low if one master instrument [A] |
| Rent instrument time at SITRA or a partner lab | Nil [I] | Lab fee per sample, not found [S19] | Turnaround outside your control [A] |
| Rider with a portable instrument | ₹1.75 lakh or more [S56] | Travel | Portable readings on unconditioned samples drift [A] (basis: no conditioning on site) |
| Partner with a compliance lab | Nil [I] | Brand-level prices [A] | Neutrality issue if the lab is dye-maker owned, as Texanlab is [S73] |

### 6. Bill of materials or delivery cost sketch (hub)

| Line | Cost | Tag |
|---|---|---|
| Reflectance spectrophotometer | ₹1,75,000-4,75,000 | [S23, S56] |
| Light booth | ₹17,500-45,000 | [S22] |
| Conditioning: AC, dehumidifier, hygrometer | ₹50,000-90,000 | [A] (basis: not searched) |
| Analytical balance | ₹12,300-30,000 | [S24] |
| Retained-sample storage (dark cabinets, labels) | ₹15,000-30,000 | [A] |
| Professional indemnity cover, year 1 | ₹15,000-40,000 | [A] (basis: products exist [S38]; premium not found) |
| Total setup | ₹2.85-7.10 lakh | [I] (sum) |
| Cause tests: outsource dyeing and lab pretreatment at first | ₹1,000-2,500 a case | [A] (basis: A2 anchors) |

The cheapest credible route is to rent instrument time for the pilot and buy a booth only [I].

### 7. Safety, compliance, certification

- No licence is needed to run a private colour-measurement service [A] (basis: no rule found in my searches; confirm with a lawyer).
- NABL accreditation is optional but strengthens neutrality later [S43].
- The shade clause should name the method (ISO 105-J03), the tolerance, illuminants, instrument, sample conditioning, retention period and a fixed expert-determination step. Enforceability is for a lawyer [I].
- Retained samples hold customer colour standards and recipes, so confidentiality terms are needed [A] (basis: buyer concern in 03-market-3; test in interviews).

### 8. Intellectual property

- The dye-receptivity control patent EP0125556 dates from about 1984 and is probably expired [S72] [A] (basis: 20-year term).
- The Inventor found no service that allocates cost between parties in 8 searches. I did not re-search.
- Protectable: the clause template (copyright), the lot database (trade secret), the brand [I].

### 9. Critical technical risks

1. Instrumental clause raises dyer rejections where exporters are lenient (C7) [I].
2. Cause test cannot separate yarn from pretreatment without a greige swatch and a validated lab pretreatment [I].
3. Inter-instrument disagreement against the exporter's own instrument [A] (A3).
4. Neutrality breaks if run with ShadeKit (agreed with the Inventor) [I].

### 10. Cheapest test to retire the biggest technical risk

Risk: the clause hurts rather than helps the dyer.
- Method: from 2 dyers, collect 60 past lots with their approved standards: 20 rejected and 40 accepted by the exporter. Measure all on one instrument at an outside lab under conditioned settings. Compare with the exporter's visual decisions.
- Cost: lab time ₹20,000-40,000 [A] (basis: 60 measurements at ₹300-600 each; get a quote); light booth ₹17,500 [S22]; travel ₹15,000 [A]; founder 30 hours × ₹750 = ₹22,500 [I]. Total about ₹75,000-95,000 [I].
- Duration: 3 weeks [A].
- Pass: at least 30% of rejected lots are within the agreed CMC tolerance, and under 20% of accepted lots fail it [A] (basis: the clause then cuts the dyer's net rejections; C7).
- Fail: accepted lots that fail instrumentally outnumber rejected lots that pass [A].

### 11. What a qualified expert or lab must review

- A colour scientist or the instrument maker: measurement procedure, conditioning and inter-instrument checks.
- A textile chemist: the cause-test protocol and its repeatability.
- A commercial lawyer: the shade clause and expert-determination step.
- An insurance broker: professional indemnity cover for certificates.

## Lead 3: ShadeCover (inspected, insured cover for high-stakes lots)

### 1. Disciplines and deciding questions

| Discipline | Governing principle | Deciding question |
|---|---|---|
| Insurance law | Only registered insurers may carry on insurance business [S29] | Is ShadeCover's guarantee "insurance business"? |
| Distribution law | Selling insurance needs IRDAI registration [S31] | Can the founder sell cover with ₹5 lakh of capital? |
| Actuarial | Few claims mean volatile results | Can anyone price this on thin data (C9)? |
| Textile chemistry | Cause attribution (as Lead 2) | Can claims be settled on a cause test? |

### 2. Findings by discipline

- Registration: only an Indian insurance company registered with IRDAI may carry on insurance business [S29]. Section 103 penalises carrying on insurance without registration [S30]. The amount was cut off in the search result [S30].
- Classes: miscellaneous insurance business covers contracts not in the fire, marine or life classes [S29]. A shade-failure cover would fall there [I].
- Non-insurer guarantees: Saudi Arabia's regulator says extended warranties may be offered only by licensed insurers [S32]. The Philippines regulator found an extended warranty to be an insurance contract [S33]. In Australia, retailers issue warranties that insurers indemnify [S34]. I found no Indian ruling. Not found after 3 searches (queries: "Insurance Act 1938 section 2(6A) definition insurance business section 3 registration non-insurer warranty guarantee IRDAI", "IRDAI extended warranty sold by non-insurer is it insurance business unregistered entity warning service contract India", "Insurance Act section 3 no person shall carry on any class of insurance business in India penalty without certificate of registration").
- The Inventor's structure (ShadeCover gives the guarantee and insures its own liability, as in Munich Re's aiSure [S62]) carries real risk of being treated as unlicensed insurance in India. It guarantees another party's (the dyer's) performance for a premium-like fee, not ShadeCover's own work [I].
- Distribution: a corporate agent needs ₹50 lakh of net worth [S35]. An insurance marketing firm needs about ₹10 lakh [S36]. Both exceed the founder's ₹5 lakh capital [I].
- Surety: Indian general insurers may write performance bonds. Surety contracts may not cover financial guarantees, and the 2022 guidelines are now governed by the 2024 Product Regulations [S37]. Surety bonds were written for specific projects [S37], so a per-lot dyeing bond is a poor fit [I].
- Existing exclusions: standard wordings exclude faulty workmanship and property in the insured's care, custody or control [S63]. Indian insurers do sell retail warranty insurance [S64].
- The legal route that fits the capital: an insurer files and issues the policy directly to the dyer or exporter. The founder supplies inspection, certificates and data for a service fee paid by the insurer or the insured [I]. Whether that service needs IRDAI surveyor or third-party-administrator licensing was not checked [I].

### 3. Calculations

| # | Inputs | Method | Result |
|---|---|---|---|
| C9 | 20 units × 6,00,000 kg × 20% covered [A] (basis: Inventor); severe claim rate 0.1-0.3% of covered kg [A] (basis: Inventor, no data); claim lot 500 kg [A]; ₹550 per kg loss [A] (basis: Inventor's ₹500-600) | Poisson claim count | 24 lakh kg covered; 4.8-14.4 claims a year; expected loss ₹13.2-39.6 lakh; coefficient of variation 26-46%; a 1-in-20 year at the mid rate costs about ₹41 lakh against ₹26 lakh expected [I] |
| C9b | Worst single lot: 500 kg × ₹280 per kg greige × 2 cap plus ₹60 per kg re-processing [A] (basis: Inventor, greige price [S75]) | Arithmetic | About ₹3.1 lakh for one claim, 62% of the founder's capital [I] |

So the founder cannot hold even one bad lot's risk [I]. An insurer will want loss data first; at under 15 claims a year, a year of data says little [I] (chain: C9 coefficient of variation).

### 4. Feasibility class and confidence

- As designed (founder as guarantor or seller): infeasible. It breaks the capital constraint and likely the registration rule [I] (chain: S29, S35, S36, C9).
- As an insurer-owned product with founder-supplied inspection data: plausible but distant. It needs Lead 2's data first [I].
- Confidence: medium on the legal block (no Indian ruling found); high on the capital block.

### 5. Production routes compared

| Route | Setup cost | Legal risk | Capital need |
|---|---|---|---|
| Founder guarantee plus contractual-liability insurance (Inventor) | Legal work ₹25,000-50,000 [A] | High: may be unlicensed insurance [S32, S33] [I] | High: deductibles and claims float [I] |
| Insurer-issued policy direct to dyer or exporter; founder sells inspection service | Legal work only [I] | Low if the founder does not solicit or sell [I] (chain: S31) | Low [I] |
| Through a licensed broker | Nil [I] | Low [I] | Nil [I] |
| CETP mutual fund (Inventor concept 10) | Nil [I] | High: pooled indemnity is insurance business [I] (chain: S29) | Pool float [I] |

### 6. Delivery cost sketch

| Line | Cost | Tag |
|---|---|---|
| Lawyer's opinion on structure and licensing | ₹25,000-50,000 | [A] (basis: Inventor's estimate; get quotes) |
| Broker meetings and travel | ₹10,000-20,000 | [A] |
| Founder time, 40 hours × ₹750 | ₹30,000 | [I] |
| Total | ₹65,000-1,00,000 | [I] |

### 7. Safety, compliance, certification

- Do not sell, quote or collect money for cover before a lawyer's written opinion [I] (chain: S29, S30, S31).
- If an insurer appoints the founder to inspect or assess claims, check IRDAI surveyor and third-party-administrator rules first. Unchecked.
- Any "re-dye free" promise by ShadeKit to pay third-party losses would raise the same question. Waiving ShadeKit's own fee on a failed lot is a price term, not an indemnity [I].

### 8. Intellectual property

- A patent on batch warranties with sequential inspection exists from about 1997 [S40 of the Inventor; not re-searched]. I did not check its status. Insurance products are not patentable as business methods in India [A] (basis: Patents Act section 3(k); confirm with a patent agent).
- The only moat is lot-level loss data [I].

### 9. Critical technical risks

1. Regulatory: treated as unlicensed insurance [S32, S33] [I].
2. No insurer appetite without data; data volume too thin to price quickly (C9) [I].
3. Adverse selection: dyers insure only lots they expect to fail [A] (basis: Inventor; test by comparing covered and uncovered lots).

### 10. Cheapest test to retire the biggest technical risk

Risk: the structure is illegal or no insurer will write it.
- Method: a written opinion from an insurance lawyer on two structures (founder guarantee; insurer-direct policy with founder inspection fee). In parallel, a two-page term sheet to 3 general insurers through a broker.
- Cost: about ₹65,000-1,00,000 (section 6) [I].
- Duration: 3-4 weeks [A].
- Pass: the lawyer confirms the insurer-direct route needs no registration for the founder, and one insurer gives indicative terms [A].
- Fail: the opinion says the founder needs registration, or all 3 insurers decline without 12 months of data [A]. Then park ShadeCover behind Lead 2.

### 11. What a qualified expert or lab must review

- An insurance lawyer: Insurance Act sections 2, 3 and 103; IRDAI product and distribution rules.
- An insurance broker or actuary: pricing and data needs.
- A tax adviser: GST on service fees versus premiums.

## Wildcard: DyeWatch (in-bath monitor that flags drift before alkali)

### 1. Disciplines and deciding questions

| Discipline | Governing principle | Deciding question |
|---|---|---|
| Optics | Beer-Lambert: absorbance = absorptivity × concentration × path [K] | Can one cell cover pale to dark baths (C10)? |
| Chemometrics | Multi-dye unmixing by least squares [K] | Is unmixing the limit, or sampling? |
| Fluid handling | Lint, foam, temperature | Can a side stream run for months without fouling [S52]? |
| Reactive chemistry | Hydrolysed and active dye have nearly the same spectrum [K] | Does exhaustion predict final shade well enough? |

### 2. Findings by discipline

- Online dyebath monitoring failed to commercialise in the 1970s and 1980s [S51]. A per-dye bath monitor was used in select plants (mapping uncertain) [S65]. A commercial in-line dye-tank monitor exists [S66].
- Lint holds dye, causes analysis errors and clogs drain lines; one patent added a lint filter [S52].
- Transmittance readings struggle to resolve single dyes at very small concentrations (mapping uncertain) [S53]. An EU project used a probe with a path length that adjusts to bath darkness [S54].
- Unmixing math is not the limit: with idealised spectra, 1% absorbance noise gave under 0.4% concentration error per dye (C10b) [I]. Real limits are scattering, baseline drift, auxiliaries and lint [I] (chain: S52, S53).
- Exhaustion is not fixation [K]. A bath reading predicts dye on fibre but not fixation losses at the alkali stage [K].

### 3. Calculations

| # | Inputs | Method | Result |
|---|---|---|---|
| C10 | 300 kg lot, liquor ratio 1:6-1:8 [A] (basis: soft-flow practice; test at the unit); specific absorbance 20 L g⁻¹ cm⁻¹ [A] (basis: order of magnitude for commercial dye; measure); depths 0.1-4% owf | A = ε × c × path | Start of dyeing: 0.1% gives A 2.5-3.3 at 1 cm; 4% gives A 100-133 at 1 cm and 2.0-2.7 at 0.2 mm [I]. So one fixed cell cannot cover the range; dark baths need 0.2 mm paths or 1:50-1:100 dilution [I] |
| C10b | Gaussian yellow, red, blue bands (as C1); absorbance noise 0.5-1% [A] | Least squares, 2,000 trials | Per-dye error 0.13-0.37% (1 SD); condition number 1.6 [I] |

### 4. Feasibility class and confidence

- On-line leased monitor: speculative. It depends on unsolved fouling and range problems, and the history is of failure [S51, S52].
- At-line manual check (draw, filter, dilute, read in a UV-Vis before alkali): plausible and cheap [I] (chain: C10 plus the UV-Vis in A4).
- Confidence: medium.

### 5. Production routes compared

| Route | Setup cost | Risk |
|---|---|---|
| Commercial in-line monitor | Price not found [S66] | Likely above the budget [A] (basis: industrial instrument) |
| Low-cost DIY side-stream prototype | ₹1.5-2.5 lakh [A] (basis: Inventor) | Fouling, calibration per dye, engineering time [I] |
| At-line manual sampling with a UV-Vis and short-path cuvettes | ₹10,000-25,000 extra if a UV-Vis is already owned [I] (section 6) | Technician discipline; 10-15 minutes a sample [A] |
| University collaboration | Low cash [A] | Slow [A] |

### 6. Bill of materials (at-line test, shared UV-Vis from Lead 1)

| Line | Cost | Tag |
|---|---|---|
| Short-path cuvettes 1-2 mm | ₹5,000-15,000 | [A] (basis: not searched) |
| Syringe filters, cooling cups, sampling kit | ₹5,000-10,000 | [A] |
| Total | ₹10,000-25,000 | [I] |

### 7. Safety, compliance, certification

- Sampling hot alkaline baths needs burns and splash protection [K]. HT disperse baths at 130 °C are pressurised and must not be opened for manual sampling [K]. So the at-line route suits reactive dyeing only [I].
- A permanent device on a pressure vessel needs a qualified engineer's sign-off [A] (basis: pressure-vessel practice; confirm the boiler and pressure-vessel rules that apply).

### 8. Intellectual property

- A closed-loop dosing patent from about 1998 [S71] and a dyebath-reuse patent from about 2000 [S52] are probably expired [A] (basis: 20-year term).
- A patent on optical readings of packaged textile during dyeing, from about 2014, may be in force [S53] [A] (basis: patent number; check the register). It matters if DyeWatch is used for yarn packages.

### 9. Critical technical risks

1. Fouling and lint in the sample loop [S52].
2. Dynamic range from pale to dark (C10) [I].
3. Exhaustion data does not predict fixation errors [K].
4. Prototype cost uses half the capital before proof [A] (basis: Inventor).

### 10. Cheapest test to retire the biggest technical risk

Risk: a pre-alkali reading does not predict the final shade.
- Method: at one reactive unit, for 20 lots, draw a bath sample at the end of the salt stage; filter, dilute and read in a UV-Vis; predict the final depth; compare with the lot's measured shade after dyeing.
- Cost: consumables ₹10,000-25,000 [I]; UV-Vis shared with the Lead 1 test or rented [A]; technician 20 hours at ₹96 an hour, about ₹2,000 [I]; founder 20 hours × ₹750 = ₹15,000 [I]. Total about ₹30,000-45,000 [I].
- Duration: 2 weeks [A].
- Pass: the reading flags at least half of the lots that later need an addition, with false alarms on no more than 1 in 10 good lots [A] (basis: judgement thresholds).
- Fail: no better than the dyeing master's own visual check of the bath [A].

### 11. What a qualified expert or lab must review

- An instrumentation engineer: sampling loop, cooling, pressure safety.
- A chemometrician: calibration per dye and drift checks.

## Delivery steps at a consistent standard

ShadeKit (each lot).
1. Receive the drum. Log the batch number. Take a 20 g retained sample [A] (basis: Inventor).
2. Run the solution assay on each new batch against the reference [S9]. Run a moisture check on each opened drum [I].
3. Every month, cross-check the 10 main dyes by dyeing test at an outside lab [I].
4. Supply the dyer's lab with lab packs from the same assayed batches. Recipes are only accepted if built from them [I].
5. Take the recipe and lot weight from the dyer in writing, by app or message [I].
6. Compute weights; a second person checks them [I].
7. Weigh under ventilation on verified scales, using the 0.1 g scale for anything under 200 g [I] (chain: C2).
8. Seal, label with lot, batch, factor and weight; check-weigh the sealed pack [I].
9. Deliver; get proof of delivery with time [I].
10. Daily: balance check with reference weights. Each shift: UV-Vis check with a reference solution. Every month: review all failed lots and their causes [I].

ShadeCert (each lot).
1. Hold the approved standard as a physical swatch plus spectral data [I].
2. At dispatch, receive a sample cut to a fixed size [A].
3. Condition the sample for a fixed time [A].
4. Calibrate the instrument at the start of each shift and check it with a reference tile [I].
5. Take 4 readings, rotating the sample; report ΔE CMC(2:1), its lightness, chroma and hue parts, and a metamerism check under TL84 and A [I].
6. Do a visual check in the booth for any lot within 0.2 of the tolerance [A] (basis: the borderline zone in C7).
7. Issue the certificate the same day [I].
8. Keep retained greige, prepared fabric and dye samples for 90 days [A] (basis: covers claim windows; test with exporters).
9. For a dispute, run the cause test on a fixed protocol within 48 hours, with replicate dyeings [I].

ShadeCover (insurer-led route).
1. The insurer issues the policy [I].
2. ShadeCert data is a condition of cover [I].
3. Claims are decided by the insurer on the certificate and cause test [I].
4. The founder never takes premiums [I].

DyeWatch (at-line test).
1. Sample at a fixed point: end of salt, before alkali [I].
2. Filter, cool and dilute by a fixed factor [I].
3. Read against a calibration made from the lot's own recipe dyes [I].
4. Record the decision and the final outcome [I].

## Comparison across concepts

| | ShadeKit | ShadeCert | ShadeCover | DyeWatch |
|---|---|---|---|---|
| Feasibility class | Plausible technically; marginal economically [I] | Proven measurement; plausible cause test [I] | Infeasible as designed; plausible insurer-led [I] | Speculative on-line; plausible at-line [I] |
| Failures addressed | Dose and strength, about 20% on my prior [I] | Moves the cost of substrate faults and false rejections; no fewer failures [I] | Tail cost only [I] | Process drift caught before alkali, share unknown [I] |
| Setup cost | ₹2.8-6.1 lakh [I] | ₹2.8-7.1 lakh; pilot with rented time under ₹1 lakh [I] | ₹0.65-1 lakh legal [I] | ₹10,000-25,000 at-line [I] |
| Biggest risk | Share of failures too small [I] | Clause raises rejections with lenient exporters [I] | Unlicensed insurance; capital [I] | Fouling and range [S52] [I] |
| Cheapest test | ₹1.3-1.55 lakh, 4 weeks [I] | ₹75,000-95,000, 3 weeks [I] | ₹65,000-1 lakh, 3-4 weeks [I] | ₹30,000-45,000, 2 weeks [I] |
| Safety and regulatory load | Highest: sensitising dust, Legal Metrology, hazardous-waste drums [S25, S39, S42] | Low [I] | Highest legal load [S29] | Low (reactive only) [I] |

Order I would test in: the ShadeCert retro-measurement and the ShadeKit cause-coding share one Tirupur trip. Together they cost about ₹2.1-2.5 lakh [I] (chain: the two tests above). The DyeWatch at-line test can run in the same unit for about ₹30,000-45,000 more [I]. Do ShadeCover's legal opinion only if Lead 2 passes [I].

Corrections to the Inventor's file.
- IS 7845 covers only trichloropyrimidyl dyes. Use IS 7842 for vinyl sulphone dyes, or an agreed solution method [S7, S8, S9].
- A per-drum test dyeing is impractical: 15 technician-hours a day at 10 units (C5), and too imprecise without replicates (C3) [I].
- The "at least a third" threshold for ShadeKit is stricter than needed. Break-even is 16-22% on the Inventor's own numbers (C4) [I].
- Light booths list at ₹17,500-45,000, not ₹40,000-80,000 [S22].
- The ShadeCert cause test needs a retained greige swatch, not only prepared fabric [I].
- The ShadeCover structure is unresolved in India. Foreign regulators treat non-insurer warranties as insurance [S32, S33].

## Not checked (for the Director)

- Measured root-cause shares for Indian units (none found).
- Outside lab prices for strength tests (SITRA lists the service; price not seen) [S19].
- Legal Metrology verification fees and intervals; whether kit labelling is exempt.
- Pollution-board consent for a repacking kitchen; Factories Act registration; GST rate on dyes.
- MSIHC thresholds for dyes, caustic soda and hydrogen peroxide.
- IRDAI's position on service-firm guarantees; surveyor or administrator licensing for inspection services; the section 103 penalty amount.
- Prices of ventilation booths, bench scales, conditioning equipment, short-path cuvettes and spectrometer modules.
- Patent status of the patents named; no new patent searches.
- Inter-instrument agreement figures.
- Searches in Tamil, Gujarati or Hindi.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Industrial knit dyeing shade variation study (Toshikj and Mangovska) | Ss. Cyril and Methodius University repository | https://repository.ukim.mk/handle/20.500.12188/18352?locale=en | 2012 (per summary) | 2026-10-31 | Scouring, raw cotton, water, electrolyte significant; high ΔE variation in blacks | search summary |
| 2 | Experimental design for analyzing shade variation in dyeing process (Sennaroglu) | Marmara University | https://openaccess.marmara.edu.tr/entities/publication/3be8c33b-3a40-4084-b25f-ca924770a59f/full | 2017 (per summary) | 2026-10-31 | Temperature and liquor ratio most influential | search summary |
| 3 | Difficult cotton bottomwear shades | Society of Dyers and Colourists | https://sdc.org.uk/difficult-cotton-bottomwear-shades/ | not shown | 2026-10-31 | Ca and Mg shift shade to red (mapping uncertain) | search summary |
| 4 | Article on strength and colour-difference tolerance for dyes | Textile Value Chain | https://textilevaluechain.in/?p=21857 | not shown | 2026-10-31 | Set a strength tolerance and a colour-difference limit | search summary |
| 5 | Batch to batch shade variation (university slides) and related review | SlideShare; CORE (mapping uncertain) | https://www.slideshare.net/slideshow/batch-to-batch-shade-variation/39863102 ; https://core.ac.uk/works/10694401 | not shown | 2026-10-31 | Strength varies lot to lot and drum to drum; diluent hygroscopicity | search summary |
| 6 | Strength adjustment of reactive dyes | Borregaard | https://www.borregaard.com/markets/dyestuffs/applications/reactive-dyes/strength-adjustment-of-reactive-dyes/ | not shown | 2026-10-31 | Standardisation cuts strength 30-40% | search summary |
| 7 | IS 7845:2022 strength of reactive dyes (trichloropyrimidyl) by dyeing test | Bureau of Indian Standards | https://services.bis.gov.in/tmp/1734843202.pdf | 2022 | 2026-10-31 | Scope limited to trichloropyrimidyl type; repeated dyeings; comparative only | search summary |
| 8 | Know Your Standards listings: IS 7842:2022, IS 7447:2022, IS 7448, IS 11635:2023, IS 12149:1987 | Bureau of Indian Standards | https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/Indian_standards/isdetails/Mjc2ODM= | 2022-2023 | 2026-10-31 | Strength standards by dye type (mapping of each IS to each URL uncertain) | search summary |
| 9 | TM182 Relative Color Strength of Dyes in Solution | AATCC; GlobalSpec | https://members.aatcc.org/store/tm182/578/ ; https://standards.globalspec.com/std/14488643/182 | 2021-01-01 | 2026-10-31 | Equivalent to ISO 105-Z10; fast and repeatable; must correlate with textile strength | search summary |
| 10 | ISO 105-Z10 relative colour strength of dyes in solution | ASN (Senegal standards body listing) | https://www.asn.sn/en/node/47046 | not shown | 2026-10-31 | Strength not a physical constant; similar absorption curves needed | search summary |
| 11 | Delta-E CMC(l:c) documentation | MetricGate | https://metricgate.com/docs/delta-e-cmc-lc/ | 2026-06-10 | 2026-10-31 | 2:1 textile convention; ≤1.0 passes; bulk bands (weak source) | search summary |
| 12 | ISO 105-J03:2009 Calculation of colour differences | AFNOR | https://www.boutique.afnor.org/en-gb/standard/iso-105j032009/textiles-tests-for-colour-fastness-part-j03-calculation-of-colour-differenc/xs119352/115856 | 2009 | 2026-10-31 | Current CMC calculation method | search summary |
| 13 | Instrumental pass/fail review (Westland and Pan) | White Rose eprints | https://eprints.whiterose.ac.uk/id/eprint/155294/1/westland_pan_JTSE_2017.pdf | 2017 | 2026-10-31 | Up to 25% wrong visual decisions (secondary); booth background effects | search summary |
| 14 | Visual and instrumental colour approval (Triumph International) thesis | Hong Kong Polytechnic University | https://theses.lib.polyu.edu.hk/handle/200/6701 | 2012 (per summary) | 2026-10-31 | CMC(2:1) best correlation for tolerance setting | search summary |
| 15 | Colour-difference measurements in relation to visual assessments in the textile field | Czech Academy of Sciences catalogue | https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi...........3f602c9f280e4b7b614c6d7f813bd643 | 1968 (per summary) | 2026-10-31 | 32 observers, 23 instruments; instrument at least as reliable as one observer | search summary |
| 16 | ASTM D2244-21 | ASTM International | https://store.astm.org/d2244-21.html | 2021 | 2026-10-31 | Tolerances must be correlated with visual appraisal; metamerism | search summary |
| 17 | Effect of hardness of water on reactive dyes; related study | figshare; PubMed Central (mapping uncertain) | https://figshare.com/articles/Effect_of_Hardness_of_Water_on_Fixation_and_Total_Wash_off_Percentage_of_Reactive_Dyes_When_Applied_to_Cellulosic_Fiber/1171101 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6682073 | not shown | 2026-10-31 | ΔE rises with hardness, more in pale shades; Fe and Cu shifts | search summary |
| 18 | Problems and their remedies in polyester processing, parts III and IV | Fibre2Fashion | https://www.fibre2fashion.com/industry-article/4436/problems-and-their-remedies-in-polyester-processing-part-iv | not shown | 2026-10-31 | Dispersion, agglomeration, pH, heating rate | search summary |
| 19 | Chemical testing; textile chemical testing charges; revised charges | SITRA | https://sitra.org.in/chemical-testing/ ; https://sitra.org.in/wp-content/uploads/2024/05/Textile-Chemical-Testing-charge.pdf | 2024-05; revised 2025-05-12 | 2026-10-31 | Computer colour matching for ΔE and strength listed; fastness tests about ₹250-900 | search summary |
| 20 | Chemical and physico-chemical test charges | ICAR-CIRCOT | https://circot.icar.gov.in//sites/default/files/Chemical-Physico-Chemical-Tests.pdf | not shown (2023 list exists) | 2026-10-31 | ₹900 to identify a dye class | search summary |
| 21 | UV-Vis double beam listings | IndiaMART (Pulse Life Science); GeM | https://m.indiamart.com/pulse-life-science/spectrophotometer.html ; https://org.gem.gov.in/cart/cart_global/directBuy/948700 | not shown | 2026-10-31 | ₹1,25,000-3,80,000; GeM ₹3,28,000 | search summary |
| 22 | Colour viewing booth listings | IndiaMART; aajjo | https://m.indiamart.com/impcat/color-viewing-booth.html ; https://www.aajjo.com/product/colour-matching-cabinet-in-delhi-fec | not shown | 2026-10-31 | ₹17,500-20,000 typical; ₹45,000 premium | search summary |
| 23 | Reflectance spectrophotometer listings (Lovibond LC100; TR series) | TradeIndia | https://www.tradeindia.com/products/lovibond-tintometer-lc100-reflectance-spectrocolorimeter-c7016370.html ; https://www.tradeindia.com/products/tr-series-reflectance-spectrophotometer-c7016371.html | not shown | 2026-10-31 | ₹4,75,000 and ₹7,45,000 | search summary |
| 24 | Analytical balance listings | IndiaMART; aajjo; GeM | https://m.indiamart.com/impcat/analytical-balances.html ; https://www.aajjo.com/product/auy220-series-analytical-balance-in-new-delhi-lab-sales-corporation | not shown | 2026-10-31 | 220 g/1 mg ₹12,300-30,000; 0.1 mg ₹57,820 | search summary |
| 25 | Dyes and dyeing | UK Health and Safety Executive | https://hse.gov.uk/textiles/dyes-dyeing.htm | not shown | 2026-10-31 | Reactive dyes sensitisers; dispense under ventilation regardless of quantity | search summary |
| 26 | RAC/CLH document on a reactive dye (Reactive Black 5) | European Chemicals Agency | https://chesar.echa.europa.eu/documents/10162/b8438b94-dbca-d689-3a71-ee8da373528e | not shown | 2026-10-31 | H334 respiratory sensitiser classification | search summary |
| 27 | Review of reactive dyes and occupational asthma | PubMed | https://www.pubmed.gov/36473025/ | 2022 | 2026-10-31 | Reactive dyes cause occupational asthma and rhinitis | search summary |
| 28 | Docker et al., asthma in dye weighers | British Journal of Industrial Medicine (CDC archive) | https://ftp.cdc.gov/Pub/Documents/OEL/06.%20Dotson/References/Docker_1987_Br%20J%20Ind%20Med.pdf | 1987 | 2026-10-31 | Asthma among dye-powder weighers; IgE mechanism | search summary |
| 29 | Insurance Act, 1938 (as amended) | Department of Financial Services, Government of India | https://financialservices.gov.in/beta/sites/default/files/2023-08/Insurance-Act-1938.pdf | 2023-08 (upload) | 2026-10-31 | Registration requirement; classes of business; only Indian insurance companies | search summary |
| 30 | Insurance Act section 103 penalty | Indian Kanoon; courtbook (mapping uncertain) | https://future.indiankanoon.org/doc/126892/ ; https://courtbook.in/insurance-act-1938/section-103 | not shown | 2026-10-31 | Penalty for insurance business without registration | search summary |
| 31 | IRDAI urges public to deal only with authorised agents and insurers | Cafemutual | https://cafemutual.com/news/insurance/20499-irdai-urges-general-public-to-deal-only-with-authorized-agents-and-insurers | not shown | 2026-10-31 | Only registered insurers and intermediaries may sell | search summary |
| 32 | Saudi Arabia cracks down on extended warranties by non-insurers | Middle East Insurance Review | https://www.meinsurancereview.com/News/View-NewsLetter-Article/id/93239/Type/MiddleEast | 2025-10-16 | 2026-10-31 | Extended warranties only by licensed insurers | search summary |
| 33 | Insurance Commission legal opinion ICLO 2021-01 | Insurance Commission, Philippines | https://www.insurance.gov.ph/wp-content/uploads/2022/04/ICLO2021_01.pdf | 2021 (per file name) | 2026-10-31 | Extended warranty is an insurance contract | search summary |
| 34 | Extended warranties submission | Insurance Council of Australia | https://insurancecouncil.com.au/wp-content/uploads/resources/Submissions/2018/2018_04/2018_04_Extended%20warranties_Submission.pdf | 2018-04 | 2026-10-31 | Retailer issues warranty; insurer indemnifies retailer | search summary |
| 35 | Requirements for licence as a corporate agent | IRDAI policyholder portal | https://policyholder.gov.in/web/guest/requirements-for-license-as-a-corporate-agent | not shown | 2026-10-31 | ₹50 lakh net worth; ₹10,000 and ₹25,000 fees | search summary |
| 36 | Insurance marketing firms rules | Business Standard; consultancy pages | https://business-standard.com/article/finance/insurance-marketing-firms-can-procure-policies-of-two-life-non-life-health-insurers-each-irdai-115120901073_1.html | 2015-12 | 2026-10-31 | IMF net worth about ₹10 lakh (validity rules conflict) | search summary |
| 37 | IRDAI issues guidelines to surety insurance contracts; later regime | SCC Online; Conventus Law | https://www.scconline.com/blog/post/2022/01/06/irdai-issues-guidelines-to-surety-insurance-contracts/ ; https://conventuslaw.com/?p=131117 | 2022-01-06 | 2026-10-31 | Performance bonds; no financial guarantees; now under 2024 Product Regulations | search summary |
| 38 | Errors and omissions and professional indemnity prospectuses | Universal Sompo; Royal Sundaram | https://universalsompo.com/assets/file/errors-and-ommissions-insurance/errors-and-ommissions-insurance-prospectus.pdf ; https://www.royalsundaram.in/assets/liabilityinsurance/Professional-Indemnity-Policy-Prospectus.pdf | not shown | 2026-10-31 | Indian E&O and PI cover exists; no lab-specific wording | search summary |
| 39 | Legal Metrology (Packaged Commodities) Rules 2011; 2024 amendment proposal | Nagaland Legal Metrology; Department of Consumer Affairs | https://legalmetrology.nagaland.gov.in/documents/11/9_The_Legal_Metrology_Package_Commodities_Rules_2011.pdf ; https://consumeraffairs.nic.in/sites/default/files/02-Aug-2024.pdf | 2011; 2024-08-02 | 2026-10-31 | Rule 3 exemptions; proposed change | search summary |
| 40 | Legal Metrology Act 2009; verification FAQ | India Code; Delhi Weights and Measures | https://www.indiacode.nic.in/bitstream/123456789/2102/1/2009l.pdf ; https://weightnmeasures.delhi.gov.in/faqs | 2009 | 2026-10-31 | Section 24 verification and stamping; penalties | search summary |
| 41 | Manufacture, Storage and Import of Hazardous Chemical Rules 1989 | Inspectorate of Factories and Boilers, Goa | https://ifbgoa.goa.gov.in/sites/default/files/Manufacture_Storage&Import_of_Hazardous_Chemical_Rules%201989.pdf | 1989 (amended 2000) | 2026-10-31 | Isolated storage; thresholds in schedules | search summary |
| 42 | Hazardous waste committee minutes; utilisation SOP | Punjab Pollution Control Board; TNPCB | https://ppcb.punjab.gov.in/media/documents/37_MeetingRegistrationCommitteeHWM.pdf ; https://tnpcb.gov.in/PDF/Waste_Mngt/HazardousWaste/Guidelines_and_Documents/sops/SOP6.pdf | 2016 rules (documents not dated) | 2026-10-31 | Entry 33.1 drums; Rule 9 permission conditions | search summary |
| 43 | NABL testing manual and introduction | NABL (QCI) | https://nablwp.qci.org.in/assets/Manual/Testing.pdf ; https://nabl-india.org/introduction/ | not shown | 2026-10-31 | Fee categories; amounts not found | search summary |
| 44 | R8161 Winch dyeing booklet | UK government (DFID research output) | https://assets.publishing.service.gov.uk/media/57a08cc9ed915d3cfd0015f6/R8161-WinchDyeing.pdf | not shown | 2026-10-31 | Recipe errors: about 20% re-shaded, 10% re-dyed (estimates) | search summary |
| 45 | Productivity improvement in a dyehouse in the textiles industry | University of Cape Town | https://open.uct.ac.za/handle/11427/8358 | not shown | 2026-10-31 | Human error; rejects rise with workload | search summary |
| 46 | Problems in dyeing and their remedies (Chinta and Dhar) | Fibre2Fashion (mapping uncertain) | https://www.fibre2fashion.com/industry-article/3353/problems-in-dyeing-and-their-remedies | not shown | 2026-10-31 | Unverified claim: 70% of problems from pretreatment | search summary |
| 47 | EP0384771 powdered dye dispensing | European Patent Office | https://data.epo.org/publication-server/rest/v1.2/patents/EP0384771NWB1/document.pdf | about 1990 (from number) | 2026-10-31 | 1% dose deviation gives a visibly different result | search summary |
| 48 | Precision of colour strength determination (Dyes and Pigments, abstract) | ISC index (mapping uncertain) | https://search.isc.ac/Inventory/10/54452.htm | 1999 (per summary) | 2026-10-31 | Statistical treatment of strength precision; no numbers seen | search summary |
| 49 | ISP 1014 Lab to plant correlation in jet dyeing | Cotton Incorporated | https://www.cottoninc.com/wp-content/uploads/2017/12/ISP-1014-Lab-to-Plant-Correlation-in-Jet-Dyeing.pdf | 2017-12 (upload path) | 2026-10-31 | Lab dyeings from production-prepared fabric; pure lab water hurts correlation | search summary |
| 50 | Liquid reactive dye preparation patents US4711642 and US4749380 | Google Patents; USPTO | https://patents.google.com/patent/US4711642 ; https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4749380 | 1987-1988 (from numbers) | 2026-10-31 | Hydrolysis by pH and reactive group; 60% loss at pH 6.5 in 4 weeks at 40 °C | search summary |
| 51 | Optimisation of the disperse dyeing process | Fibre2Fashion | https://www.fibre2fashion.com/industry-article/2094/optimisation-of-the-disperse-dyeing-process | not shown | 2026-10-31 | Online dyebath monitoring failed to commercialise in 1970s-80s | search summary |
| 52 | US6056790 Method for automated dyebath reuse | USPTO | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6056790 | about 2000 (from number) | 2026-10-31 | Lint holds dye, causes errors, clogs lines | search summary |
| 53 | US8925356 Optical readings on packaged textile material during dyeing | USPTO (mapping uncertain) | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8925356 | about 2014 (from number) | 2026-10-31 | Single-dye determination hard at low concentrations | search summary |
| 54 | EDY: automatic dyeing control system, final report summary | CORDIS (European Commission) | https://cordis.europa.eu/project/id/508180/reporting/fr | about 2006 (project period) | 2026-10-31 | Earlier systems analysed after the process; variable path probe | search summary |
| 55 | Delhi High Court suit on defective dyeing | LatestLaws | https://www.latestlaws.com/judgements/delhi-hc/2005/january/2005-latest-caselaw-133-del | 2005-01 | 2026-10-31 | ₹25.4 lakh claim against ₹1.64 lakh charges | search summary (from 05-invent-2 S46; not re-searched) |
| 56 | Colour spectrophotometer listings | Spectra Labtech via IndiaMART | https://m.indiamart.com/spectra-labtech/color-spectrophotometer.html | not shown | 2026-10-31 | ₹1,75,000 entry instrument | search summary (from 05-invent-2 S47; not re-searched) |
| 57 | Lab dyeing machine listings | IndiaMART | https://m.indiamart.com/impcat/lab-dyeing-machine.html | not shown | 2026-10-31 | ₹80,000-2,45,000 | search summary (from 05-invent-2 S48; not re-searched) |
| 58 | Dyestuff dissolving system | TradeIndia | https://www.tradeindia.com/products/dyestuff-dissolving-system-c4736061.html | not shown | 2026-10-31 | ₹2,00,000-5,00,000 | search summary (from 05-invent-2 S49; not re-searched) |
| 59 | Kohl's color review process requirements | Kohl's | https://link.kohls.com/content/dam/klink/pdfs/Kohls-Color-Review-Process-Requirements.pdf | not shown | 2026-10-31 | 0.8 CMC for solid lab dips | search summary (from 05-invent-2 S22; not re-searched) |
| 60 | Conference paper on colour matching in a dyehouse | IEOM Society | https://www.ieomsociety.org/proceedings/kualalumpur2011/165.pdf | 2011 | 2026-10-31 | 1.2 CMC commercial limit | search summary (from 05-invent-2 S29; not re-searched) |
| 61 | Color management in textiles | Datacolor | https://www.datacolor.com/business-solutions/blog/color-management-in-textiles-how-to-deliver-accuracy-and-speed/ | not shown | 2026-10-31 | Visual assessment still essential | search summary (from 05-invent-2 S44; not re-searched) |
| 62 | Insure AI (aiSure) | Munich Re | https://www.munichre.com/en/solutions/for-industry-clients/insure-ai.html | not shown | 2026-10-31 | Insured performance guarantee model | search summary (from 05-invent-2 S17; not re-searched) |
| 63 | Contractors all risk wordings | Tata AIG; Future Generali | https://tataaig.com/s3/contractors_all_risk_insurance_retail_v2_15_01_2025_c30dac4c71.pdf | 2025-01-15 (file name) | 2026-10-31 | Care, custody or control and faulty workmanship exclusions | search summary (from 05-invent-2 S19, S20; not re-searched) |
| 64 | Warranty insurance (retail) customer information sheet | Generali Central Insurance | https://www.generalicentralinsurance.com/downloads/other-insurance/warranty-insurance/customer-information-sheet/warranty-insurance-retail-cis.pdf | not shown | 2026-10-31 | Indian insurers sell warranty insurance | search summary (from 05-invent-2 S38; not re-searched) |
| 65 | Report chapter on HueMetrix Dye-It-Right | P2 InfoHouse | https://p2infohouse.org/ref/08/07014.pdf | not shown (1990s) | 2026-10-31 | Per-dye bath monitor in select plants (mapping uncertain) | search summary (from 05-invent-2 S31; not re-searched) |
| 66 | LTMS product sheet | Ocean Insight | https://www.OceanInsight.com/globalassets/catalog-blocks-and-images/pdfs/ltms-product-sheet_v7.pdf | not shown | 2026-10-31 | Commercial in-line dye-tank monitor | search summary (from 05-invent-2 S34; not re-searched) |
| 67 | Right-First-Time: a necessity not a luxury | Textile Today | https://textiletoday.com.bd/right-first-time-a-necessity-not-a-luxury | not shown | 2026-10-31 | Addition and strip cost ratios (background only) | search summary (from 05-invent-2 S45; not re-searched) |
| 68 | CETPs: an untapped opportunity for energy efficiency | CAG | https://www.cag.org.in/blogs/cetps-untapped-opportunity-energy-efficiency | not shown | 2026-10-31 | CETP clusters of 40-50 units (background) | search summary (from 05-invent-2 S53; not re-searched) |
| 69 | Thies dispensing system; THEN dyehouse network | Textile World; Fong's Europe | https://www.textileworld.com/textile-world/dyeing-printing-finishing-2/2008/05/thies-unveils-new-dispensing-system/ ; https://fongs.eu/site/assets/files/1398/then_dyehouse_network_feu_2021.pdf | 2008-05; 2021 | 2026-10-31 | In-plant central colour kitchens exist | search summary (from 05-invent-2 S7, S8; not re-searched) |
| 70 | US5145484 PVA envelopes for fibre-reactive dyes | Google Patents | https://patents.google.com/patent/US5145484 | about 1991-1992 | 2026-10-31 | Prior art for unit packs | search summary (from 05-invent-2 S9; not re-searched) |
| 71 | US5846265 Closed-loop textile dyeing with metered dosing | USPTO | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5846265 | about 1998 | 2026-10-31 | Prior art for DyeWatch | search summary (from 05-invent-2 S32; not re-searched) |
| 72 | EP0125556 Controlling the dye receptivity of textiles | Google Patents | https://patents.google.com/patent/EP0125556B1/en | about 1984 | 2026-10-31 | Prior art for the cause test | search summary (from 05-invent-2 S26; not re-searched) |
| 73 | Texanlab to set up a lab in Tirupur | Apparel Resources | https://apparelresources.com/business-news/trade/texanlab-to-setup-a-lab-in-tirupur/ | 2017 | 2026-10-31 | DyStar-group lab in Tirupur (neutrality) | search summary (from 05-invent-2 S25; not re-searched) |
| 74 | Reactive dyes listings | IndiaMART | https://m.indiamart.com/impcat/reactive-dyes.html | not shown | 2026-10-31 | Dye prices (background, not used in calculations) | search summary (from 05-invent-2 S35; not re-searched) |
| 75 | 100% cotton greige single jersey listing | Fibre2Fashion | https://www.fibre2fashion.com/fabrics/cotton-fabric-suppliers-1490820 | not shown | 2026-10-31 | ₹280 per kg greige (claim cap in C9b) | search summary (from 05-invent-2 S36; not re-searched) |
