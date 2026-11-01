# Hunt B (lens: something changed). Opportunity Hunter, 2026-11-01

Defaults used: capital Rs 5,00,000; founder time Rs 750 an hour; 160 hours a month available [A: brief default plus a full-time month]. All arithmetic is in `runs/2026-11-01-controlled/01-hunt-B-calc.py` (run output quoted below as [I] with the script section letter).

Method note. The search tool returned summaries, not pages. I opened no page. Every source is marked "search summary". Where one summary joined several pages, I say the mapping of figure to page is uncertain. The one page I tried to open (OpIndia) did not resolve, so it is used only through its search summary.

**Result in one line: nothing exceptional yet.** Of 4 evidence-backed theses and 6 exploratory bets, all are REJECT. The closest to alive is the DDGS lot-grading service, which fails on Defensible and on founder hours at 100 customers, not on demand.

## 1. Industries chosen and why

The brief fixed six industries. I added none.

1. Groundwater and industrial water under new compliance rules.
   - CGWA requires tamper-proof digital flow meters with telemetry on every abstraction structure of an NOC holder, and a CGWA technical specification exists [S1, S2].
   - Vendor pages list GSM meters from Rs 15,000 to Rs 32,500 and sizes up to 500 mm, so the hardware is already sold by many firms [S3, S4, S5].
2. Refrigerants and cooling equipment.
   - India plans an HFC production freeze from 1 January 2028 and no new HFC capacity clearances after 2027, per an April 2026 report [S6].
   - News and a state-level report describe unlabelled or counterfeit cylinders, and disposable cylinders are banned in India [S26, S27].
3. Footwear and leather goods quality regulation.
   - Micro and small units making non-leather footwear got until 31 July 2027 to obtain BIS certification [S15].
   - Testing capacity is described as a bottleneck, with 2 BIS labs, 2 FDDI labs, CLRI and 11 private labs recognised in an earlier report [S15].
4. End-of-life tyres and rubber.
   - EPR for waste tyres is in force and producers buy certificates from recyclers on the CPCB portal [S21].
   - NITI Aayog proposed national standards for tyre pyrolysis oil and recovered carbon black because none exist [S22].
5. Food authenticity (honey, spices, edible oils). Honey is the only one I worked deeply.
   - NMR is required for exported honey but not for domestic sale, and FSSAI called NMR of limited utility in 2020 [S7, S8].
   - A 2020 CSE test found 22 samples from 13 brands, with 77% adulterated [S47].
6. Animal feed byproducts.
   - Grain ethanol supplied 67% of India's ethanol in ESY 2025-26 to June, with maize the largest feedstock [S14, S13].
   - Feed mills now replace 10-15% of protein needs with DDGS [S9].

Spices and edible oils were scanned only through the honey and FSSAI results. I did not run spice or oil searches. That is a gap in this hunt.

## 2. Raw candidates

| # | Problem | Payer | Signal | Tag |
|---|---|---|---|---|
| 1 | Aflatoxin and variable quality in DDGS sold to feed mills | Feed mill or distillery | Maize DDGS often 100-200 ppb aflatoxin against a 20 ppb limit; TN farmers ask BIS for benchmarks [S12, S10, S11] | thesis T1 |
| 2 | MSE footwear makers need BIS test capacity before July 2027 | Footwear MSE | Testing bottleneck; BIS allows subcontracting [S15, S68] | thesis T2 |
| 3 | No grade standard for recovered carbon black | Pyrolysis recycler | NITI Aayog notes the gap; ASTM D8632 now exists [S22, S23] | thesis T3 |
| 4 | Meter and telemetry compliance for borewell NOC holders | Industrial water user | Many vendors at Rs 15,000-32,500 [S3, S4, S5] | thesis T4 |
| 5 | Customer cannot verify gas added in AC top-up | Service platform | Scam coverage; arrests in Margao [S36, S37] | bet A |
| 6 | Syrup in honey passes tests | Packer or exporter | CSE finding; novel syrups since late 2024 [S47, S48] | bet B, bet C |
| 7 | Aflatoxin-rejected DDGS has low value | Distillery | 100-200 ppb figure [S12] | bet D |
| 8 | Unlabelled or fake refrigerant cylinders | Service firm, technician | Canada found R40 in cylinders labelled R410A [S28] | bet E (cut) |
| 9 | Groundwater draw unmetered or bypassed | Regulator | Energy-based estimates exist [S58] | cut |
| 10 | Spice and edible oil adulteration screening | Exporter, packer | Not searched | not assessed |

## 3. Evidence-backed theses

### T1. Third-party lot grading of DDGS at the distillery gate (service plus test kit)

**Not claimed original.** Search queries run: "DDGS India surplus ethanol distillers grain price poultry feed 2025 mycotoxin"; "rice DDGS India quality variability aflatoxin fibre feed mills complaint grain ethanol plants"; "Evonik AMINONIR DDGS near infrared feed mill service India OR Foss OR Perten DDGS calibration handheld NIR price"; "aflatoxin rapid test kit price Neogen Reveal Romer AflaCheck strips reader cost per test India lab charge"; "mycotoxin binder price India Rs per kg feed mills Mycofix Toxfin Biomin DDGS aflatoxin 20 ppb limit FSSAI feed standard"; "DDGS price per tonne India Rs maize DDGS rice DDGS 2026 soymeal price feed mill"; "number of grain based ethanol distilleries India operational 2025 DDGS production million tonnes ISMA". Patents, trademarks, crowdfunding and closed ventures were not searched for this thesis. Because I do not claim originality, the full 8-query rule is not triggered, but the gap is listed.

**1. Original.** Nearest neighbours:
- Neogen Reveal Q+ Max, FSSAI-listed for aflatoxin in nuts and cereal products, distributed in India by Neogen India, Kochi [S62]. Price not found.
- Abbexa total aflatoxin rapid kit, USD 203 for 20 tests (about USD 10 a test) [S60]; a TradeIndia listing shows Rs 20,300 a pack, pack size not stated [S61].
- Foss NIR at an Indian cattle feed plant, vendor case study; handheld NIR (Thermo microPHAZIR AG) exists; prices not found [S70-search summary, see note below].
- Mycotoxin binders sold to feed mills: Indian listings Rs 25-160 a kg, dosed 1-5 kg a tonne of feed [S59]. Branded Biomin and Mycofix prices not found.
- Commercial NABL labs: aflatoxin per-sample fee not found.
Difference: a trusted independent lot certificate. A buyer would notice a certificate, but it is a service, not a technology. Not original.
Note on S70: the Foss and Thermo items came from one search summary without a usable URL; the Sources table lists the search, not a page.

**2. Desired.** Payer: the feed mill, which bears a failed batch, or the distillery, which gains a price premium. Beneficiary: the poultry or dairy farmer whose animals eat the feed. Budget line: raw material quality assurance (mill) or sales realisation (distillery) [H: no source names the line]. Behaviour seen: TN farmers asked the centre to monitor DDGS and have BIS set benchmarks [S10]; mills already substitute 10-15% of protein with DDGS [S9]; mills already buy binders [S59]. Prices: rice DDGS about Rs 30 a kg, maize DDGS about Rs 24-24.5 a kg, soya DOC Rs 43-44 a kg, February 2026 [S12]. Contrary: the aflatoxin limit is 20 ppb in one consultant article and "15 mg/kg" on a supplier page, so the threshold is unsettled [S11]. Demand level: L1, indirect.

**3. Feasible.** Aflatoxin strip plus reader at each lot; moisture meter; sampling probe. The method is established. Calibrated NIR for rice DDGS is the unknown: a consultant article gives rice DDGS crude fibre from 1.23% to 5.33%, a spread of 53% [S11], which a single calibration may not handle. Experiment: 30 lots against a lab reference.

**4. Profitable.** Script section A [I]. Inputs: strip Rs 950 a test [A: from USD 10 at Rs 88 per USD, S60, and Rs 1,015 from S61], lot 25 t [A: one truck], technician 0.75 hours at Rs 200 an hour [A], plant of 200 KLPD at 0.55 kg DDGS per litre [A: 0.55-0.79 from US yields, K], fee Rs 60 a tonne [H].
- At fee Rs 60 a tonne: margin per lot Rs 400, about 5.8 lakh a plant a year, 2.2 lakh after one on-site technician [I] [A].
- At fee Rs 30 a tonne: minus 8.7 lakh a plant a year after the technician [I] [A].
- The buyer's own cheapest alternative is the same strip: about Rs 44 a tonne [I] [A]. So the fee buys trust and avoided disputes, not a saving.
**Unknown. Driven by the fee per tonne.** Halving it flips the verdict, and no source gives what a mill or distillery would pay.

**5. Reachable.** The AIDA count is over 380 dedicated distilleries operating, with 33 more coming, but the grain-based share is not stated [S13]. Grain ethanol was 480 crore litres, 67% of supply [S14]. So the buyer pool is a named list I could obtain from AIDA or ISMA, size unknown, below 380 [I]. First 10: AIDA directory, cold approach to distillery sales heads. First 100: not possible if grain plants number below 100 [A]. Sale cycle: unknown.

**6. Defensible.** If a certificate becomes accepted, switching cost is acceptance by buyers. But SGS, Intertek and similar firms run Indian food labs and could add DDGS in under a year [K: they operate commodity inspection; not checked for DDGS]. A distillery can also buy strips itself.

**7. Large enough, within means.** Script section A [I]. 100 plants need 100 readers at an assumed Rs 2 lakh each, which is 200 lakh against 5 lakh capital [A]. Founder hours at 4 hours a plant a month are 400 a month against 160 [A]. Even at 30 plants the work is on-site and labour-heavy.

**Doubt most likely to kill it:** whether anyone pays Rs 60 a tonne for an independent certificate when a strip costs about Rs 44 a tonne. **First test:** five calls to feed mill procurement heads and three to distillery sales heads asking what they pay today and what a dispute costs. **Even-if-true:** assume the fee is Rs 100 a tonne [H]. Margin per plant rises to 20.3 lakh before the technician [I-A], but Defensible still fails (a global testing major can copy) and hours at 100 plants fail. **Outcome: REJECT.**

### T2. Footwear MSE in-house test lab or bench-test kit (physical product)

**Not claimed original.** Queries: "footwear quality control order BIS India 2025 MSME testing labs withdrawn"; "BIS licence footwear in-house laboratory equipment required small manufacturers Agra cost lakh testing facility QCO"; "shared common testing facility footwear cluster BIS testing lab Agra Kanpur Chennai CFC"; "footwear tester price flex tester abrasion tester SATRA Gotech Prime Test India price". Patents, trademarks, closed ventures not searched.

**1. Original.** Near neighbours: Indian instrument makers list a De-Mattia flex tester at Rs 68,000-85,000, a Bennewart flex tester Rs 80,000-1,17,000, a Scott-type crease-flex abrasion tester Rs 1,32,000, a Ross flex tester Rs 2,45,000, a slip-resistance tester listed at Rs 11,00,001 [S19]. Government and shared labs: FDDI International Testing Centres at Noida and Chennai, with Jodhpur and Rohtak planned [S17]; an upgraded National Test House shoe lab at Ghaziabad opened in May 2026 [S18]; SGS Chennai got BIS recognition in 2024 [S18-search summary]. Nothing new in the product.

**2. Desired.** Payer: the MSE footwear maker. Beneficiary: the same, plus the consumer. Budget line: licence cost and testing, which BIS lets a firm outsource to a recognised lab [S68, S16]. BIS even relaxed the in-house testing facility rule after industry complained about equipment cost [S16]. Behaviour: makers sought and got a one-year extension to July 2027 [S15].

**3. Feasible.** Technically trivial; instruments exist. A bench kit is an assembly of third-party testers.

**4. Profitable.** Script section B [I]. Core lab: flex Rs 1,17,000 and Scott Rs 1,32,000 from listings [S19]; abrasion Rs 1,50,000, tensile Rs 4,00,000, oven and bath Rs 50,000 are my assumptions [A: no listing found]. Total Rs 8,49,000 [I-B]. BIS basic test fee per category Rs 15,540 to Rs 22,140 [S20]. Payback of an own lab against outsourcing: 9.6 to 27 years at 2-4 rounds a year; 4.8 years only at 8 rounds at the high fee [I-B]. Halving equipment cost gives 4.8 years at 4 rounds [I-B]. So most MSEs rationally outsource. The verdict does not flip on one input, except the unsourced tensile price, which when halved moves payback but not the ranking against outsourcing at low round counts.

**5. Reachable.** Not counted. No register of footwear MSEs was found in these searches. Not found after 4 searches.

**6. Defensible.** Nothing accumulates. Resellers of the same Indian testers exist.

**7. Large enough, within means.** Lab sale of Rs 8.5 lakh against 5 lakh capital for one customer's equipment on stock [I]. No margin figure is available [A].

**Doubt that kills it:** demand for owned labs is weak because outsourcing is permitted. **Even-if-true:** if every MSE wanted a lab, Defensible still fails (instrument resellers). **Outcome: REJECT.** Rule 13 note: this is the physical-product thesis; the evidence rules out a kept one in these industries because buyers have a cheaper alternative (outsourcing) and the tools are commodity.

### T3. Recovered carbon black (rCB) grading and assay for Indian pyrolysis units

**Not claimed original.** Queries: "India waste tyre EPR pyrolysis oil recycled carbon black certificates price 2025"; "tyre pyrolysis recovered carbon black testing laboratory India grading BET ash toluene extract buyers rCB standard NITI Aayog"; "number of registered tyre recyclers CPCB EPR portal pyrolysis units".

- Original: ASTM D8474 (thermogravimetric analysis of organic residue, fixed carbon and ash) and ASTM D8632 (rCB classification for tyre use) exist [S23]. Operators already run about 10 ASTM controls before shipment [S23].
- Desired: payer is the pyrolysis operator wanting a saleable grade. rCB can be sold only to manufacturers [S21]. Price evidence conflicts: Rs 30-70 a kg against Rs 95-130 for virgin black [S24] versus Rs 5-10 a kg [S25]. I trust neither.
- Feasible: ASTM D8474 needs a thermogravimetric analyser. Price not found. [A: lakhs, not checked].
- Profitable: no fee benchmark. Not computed.
- Reachable: 517 recycling units and 200 pyrolysis units on the portal in one report [S21], against an industry head's figure of about 800 recyclers, 650 of them making pyrolysis oil [S21]. Sources disagree and one claims pyrolysis is banned in most states by pollution boards [S23, interview claim]. Unverified.
- Defensible: weak; a standard-owner such as BIS or NABL labs would own the grade.
- Large enough: a TGA is likely beyond Rs 5 lakh [A].
**Doubt that kills it:** standards unfinished, pyrolysis legality unclear. **Even-if-true:** with a final standard, NABL labs take the work. **Outcome: REJECT.**

### T4. CGWA flow meter and telemetry compliance service for industrial borewells

**Not claimed original.** Queries: "CGWA groundwater guidelines industries digital flow meter telemetry mandatory NOC 2025"; "electromagnetic flow meter with GSM telemetry CGWA compliant price Rs borewell 2 inch 3 inch indiamart".
- Original: at least 5 sellers (Accumax, Vision World Tech, Itechflow, Dhaara Smart, Vishal Borewell) already sell compliant meters at Rs 15,000-30,999 [S3, S4, S5].
- Desired: payer is the NOC holder; beneficiary the regulator. Telemetry within 90 days of NOC is stated only by vendors and I could not confirm it against the official text [S1].
- Profitable: no margin data; sellers compete on price.
- Reachable: NOC holder register not found.
- Defensible: none. A calibration service needs NABL status [S4].
**Outcome: REJECT** (crowded, commodity, no moat). Reason (e) fragmented buyers with many vendors, not unserved.

## 4. Exploratory bets (marked as bets; judged by what each would be if it worked)

### Bet A. Signed weigh-in receipt for AC refrigerant top-ups (drop the assumption that the technician's word is the only record of gas added)
Method: drop an industry assumption (the amount of gas added is known only to the technician).
- If it worked: a scale logs cylinder weight before and after; the customer sees the kilograms on their phone. Buyer: AC service platforms. Margin Rs 3,370 a unit at an assumed Rs 5,500 price [I] [H].
- Evidence of the pain: Rs 650 service fee against nearly Rs 3,500 for an unneeded top-up in Margao [S37]; consumer guides on false "low gas" [S36]. Urban Company already sells a "90 day guarantee" and Rs 10,000 damage cover per AC serviced, so it spends on trust [S39].
- **Novelty search (queries):** "patent refrigerant charging record tamper-proof weight scale customer verification receipt air conditioner service"; "AC service app India verified gas refill digital scale proof startup Urban Company"; "homeowner refrigerant charge report app shows customer how much refrigerant added weight verified HVAC contractor"; "wireless refrigerant scale Bluetooth app logs refrigerant charge job report Testo 560i Fieldpiece"; "refrigerant leak log software F-gas record keeping app"; "HVACVerify OR refrigerant receipt OR gas weight proof trademark kickstarter"; "AC technician fraud verification startup shut down home services India"; "UK OR Australia refrigerant charge customer certificate digital log tamper evident scale".
- Near neighbours: CPS Compute-A-Charge scale with app storing job, invoice and customer [S34]; Testo 560i USD 345.95-407, kit USD 542-638 [S33]; Fieldpiece SR47 USD 357-420, NAVAC NRS2A USD 259-369 [S33]; Indian scales Rs 7,500-10,500 for 50-100 kg [S32]; HVACVerify (US, homeowner report with charge weight, per its own site, which on a second look documents micron and nitrogen hold; weight not confirmed) [S35]; Trakref Pro, GoCanvas refrigerant logs, Parasense [S65, S42]; a 1980s weight-monitored charging station patent [S66]; Refrigerant Reclaim Australia data app [S63]; F-gas register custom builds at EUR 25,000-55,000 [S43]. Closed: Housejoy shut services in 7 cities in 2017 [S64], not for this reason.
- Verdict on originality: no India product found; globally the log-with-customer-report pattern exists. Treat as not original.
- **Even-if-true:** assume a platform wants it. A platform can pair a commercial Bluetooth scale with its own app, so Defensible fails. Buyer pool is about 5-10 platforms [A], so Reachable at 100 customers is impossible; at 5 platforms x 500 technicians stock cash is 53.2 lakh against 5 lakh [I-C].
- Single experiment (if ever run): ask 3 platform operations heads whether a customer-visible weight record has been tried and why it was dropped.
- **Outcome: REJECT as a bet** (fails even-if-true on Defensible and Reachable).

### Bet B. Hive-scale telemetry as provenance evidence for honey (borrow from precision beekeeping and audit trails)
- If it worked: weight traces flag syrup feeding; exporters and packers buy hive-season records; beneficiary is the honest beekeeper whose price fell from Rs 150 to Rs 60-70 a kg [S47]. BOM Rs 2,700 a unit [A, I-D]; 100 hives cost 2.7 lakh [I-D].
- **Novelty queries:** "hive scale weight data detect sugar syrup feeding honey authenticity traceability beekeeper provenance verification"; "BroodMinder hive scale price Arnia hive monitoring BeeHero India beekeeping IoT startup"; "EU honey directive 2024 revised origin labelling traceability"; "honey adulteration India where does it happen processors blend syrup after extraction".
- Near neighbours: BroodMinder monitors USD 64.99 to 76.99, cell hub USD 544.99 [S51]; Arnia (old forum price USD 1,625) [S51]; Intertek honey traceability offering [S49]; EU Honey Directive 2024/1438 with a Honey Platform to advise on traceability [S49].
- Contrary evidence: vendors say a scale "does not inherently distinguish" brood gain from honey storage [S50]. Syrup is described as coming from manufacturers and importers, 10,000 MT a year of Chinese syrup, not from hives [S47].
- **Even-if-true:** hive data would cover only the minority of fraud that occurs at the hive; fraud downstream of extraction is untouched. Large enough fails.
- **Outcome: REJECT as a bet.** Single experiment, not run: 10 scaled hives with a deliberate syrup feed, to see whether the trace separates feeding from flow.

### Bet C. Cheap gate screen for honey syrup (borrow multispectral sensing)
- If it worked: a Rs few-thousand handheld at collection centres. Neighbours: CSIR-CEERI handheld, patent application IN202411019851, 8% detection limit, not a product [S44]; Thai AS7263 multispectral study, 0.91-0.98 accuracy [S46]; Dabur mobile honey lab, 2017 [S45]; academic impedance spectroscopy work [S46-search summary].
- **Novelty queries:** "honey authenticity handheld rapid test impedance spectroscopy sensor syrup adulteration portable device"; "honey adulteration detection startup portable device India beekeepers collection centre"; "handheld honey analyzer commercial product spectrometer detects syrup adulteration price"; "honey NMR test price India per sample lab". Already exists in research and patents. No commercial product with a price was found.
- Contrary: Indian tests passed 25% and 50% adulterated samples; syrups were engineered to pass [S47]. Intertek: new syrups appeared at the end of 2024 [S48].
- **Outcome: REJECT** (not original: patent and research prior art; even-if-true the screen misses designed syrups).

### Bet D. Black soldier fly bioconversion of aflatoxin-failed DDGS (borrow from waste biology)
- If it worked: turn off-spec DDGS into larvae meal listed at Rs 195-500 a kg [S56, S57]. Evidence against: a 2024 study recovered about 50% of aflatoxin B1 with larvae and 60% without, so the larvae add little [S53]; a 2019 study converted about 60% to aflatoxicol and aflatoxin P1, with recovery under 20% [S52].
- **Novelty queries:** "black soldier fly larvae aflatoxin B1 contaminated substrate DDGS"; "black soldier fly India company insect meal price per kg"; "Ynsect liquidation 2025 insect farming closures"; "patent black soldier fly distillery byproduct stillage DDGS". Prior art: the Enviroflight patent US 8,733,284 describes BSF on DDGS [S54]. Closed venture: Ynsect, judicial liquidation 1 December 2025 after raising nearly USD 600 million [S55].
- **Outcome: REJECT** (exists; benefit not shown; capital far over Rs 5 lakh [A]).

### Bet E. Cheap refrigerant identifier (cut after search)
Neutronics identifiers cost about USD 1,723-3,481 in different currencies [S30, S31], which is about Rs 1.5-2.7 lakh [I-E]. A technician-owned recovery machine lists at Rs 33,500 [S32]. No rule makes technicians buy one. Payer unclear. Even-if-true a Rs 6,000 device needs about 22 times cost reduction [I-E] and still has no mandated payer. **REJECT** (fails Reachable: no payer with a budget line).

### Bet F. Groundwater draw from pump electricity (drop the assumption that flow must be measured at the pipe)
Energy-based estimation of abstraction already exists, with R2 about 0.92 for alluvial and about 0.69 for hard-rock aquifers in Gujarat [S58]. CGWA wants tamper-proof flow meters, so a clamp would not be accepted for compliance [S2]. **REJECT** (exists; no accepted payer). One search only; not a full novelty search.

## 5. Cut candidates and reasons

- T4 CGWA meters: crowded commodity.
- Spices and edible oils: not searched, so not assessed. Not found after 0 searches.
- HFC reclaim or refrigerant production: capital-heavy; I did not run searches on reclaim. The regulatory change is real [S6] but no entrant route was tested.
- Leather chemical (chromium VI) testing: not searched.

## 6. Hunt summary

| Idea | Outcome | Deciding reason |
|---|---|---|
| T1 DDGS lot grading | REJECT | Defensible and founder hours at 100 customers |
| T2 Footwear lab or kit | REJECT | Outsourcing is cheaper; commodity tools |
| T3 rCB grading | REJECT | Standards unfinished; TGA capital |
| T4 CGWA meters | REJECT | Crowded |
| Bet A weigh-in receipt | REJECT | Platform can self-build; few buyers |
| Bet B hive scale | REJECT | Fraud is downstream |
| Bet C honey screen | REJECT | Prior art; designed syrups |
| Bet D BSF on DDGS | REJECT | Exists; no toxin benefit |
| Bet E refrigerant identifier | REJECT | No payer |
| Bet F pump-power inference | REJECT | Exists; not accepted for compliance |

**Most original finding:** the Indian AC top-up "gas weight receipt" (Bet A). Novelty evidence: 8 queries, no Indian product found, but the global pattern exists (CPS app, HVACVerify) [S34, S35]. It is not original and fails even-if-true.

**Not checked:** spice and edible-oil testing demand; official CGWA text on deadlines; Indian DDGS tonnage; footwear MSE register; any aflatoxin lab fee; Indian rCB lab capability; trademark and crowdfunding databases for T1 to T4; the OpIndia page.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Digital Water Flowmeter with Telemetry for Groundwater Compliance | The Sustainability Cloud (vendor) | https://www.thesustainabilitycloud.com/digital-flowmeter-telemetry-system/ | n/d | 2026-11-01 | CGWA telemetry rule, deadlines (unverified) | search summary |
| 2 | Final Specification of Digital Water Flow meter with Telemetry System | CGWA | https://cgwa-noc.gov.in/landingpage/UserAssistance/Final%20Specification%20of%20Digital%20Water%20Flow%20meter%20with%20Telemetry%20System.pdf | n/d | 2026-11-01 | Tamper-proof telemetry specification | search summary |
| 3 | Digital Flow Meter With Telemetry listings | IndiaMART | https://m.indiamart.com/impcat/flow-meter-with-telemetry.html | n/d | 2026-11-01 | Meter prices | search summary |
| 4 | CGWA based flow meter with telemetry | Vision World Tech | https://visionworldtech.com/?p=8990 | n/d | 2026-11-01 | Price from Rs 18,999; NABL calibration | search summary |
| 5 | Electronic flow meter listing | Accumax, IndiaMART | https://m.indiamart.com/accumaxinstruments/electronic-flow-meter.html | n/d | 2026-11-01 | GSM meter about Rs 15,000 | search summary |
| 6 | No new clearances for production of refrigerant gases after 2027 | Vision IAS citing Indian Express | https://visionias.in/current-affairs/upsc-daily-news-summary/article/2026-04-09/the-indian-express/environment/no-new-clearances-for-production-of-refrigerant-gases-after-2027-centre | 2026-04-09 | 2026-11-01 | HFC freeze 2028 | search summary |
| 7 | FSSAI clarifies on CSE claims | Business Today | https://businesstoday.in/amp/latest/corporate/story/fssai-clarifies-on-cse-claims-regarding-adulteration-in-honey-samples-280379-2020-12-03 | 2020-12-03 | 2026-11-01 | FSSAI view on NMR | search summary |
| 8 | Govt wants NMR testing mandatory for honey exported | Business Insider India | https://www.businessinsider.in/business/news/govt-wants-nmr-testing-mandatory-for-honey-exported-from-india/articleshow/72212477.cms | 2019-11 | 2026-11-01 | Export NMR requirement | search summary |
| 9 | DDGS supply lowers protein feed prices in India | Tridge | https://www.tridge.com/news/ddgs-supply-lowers-protein-feed-prices-in-in-eiirdi | 2025-10 | 2026-11-01 | Mills replace 10-15% protein with DDGS | search summary |
| 10 | Monitor DDGS inclusion, TN farmers urge Centre | DT Next | https://www.dtnext.in/news/tamilnadu/monitor-ddgs-inclusion-to-ensure-animal-feed-safety-tn-farmers-urge-centre-829166 | n/d | 2026-11-01 | Farmers ask BIS for DDGS benchmarks | search summary |
| 11 | Optimizing Poultry Feed with Rice DDGS | SR Publication (consultant article) | https://www.srpublication.com/?p=18736 | n/d | 2026-11-01 | Fibre range, aflatoxin limit conflict | search summary |
| 12 | DDGS prices and aflatoxin figures | DairyNews7x7 (mapping of figure to page uncertain) | https://dairynews7x7.com/news/ddgs-sorghum-imports-impact-on-feed-and-maize-prices | 2026-02 | 2026-11-01 | Rice and maize DDGS prices; 100-200 ppb | search summary |
| 13 | Maize becomes India's No. 1 ethanol feedstock (AIDA) | Bioenergy Times | https://bioenergytimes.com/maize-becomes-indias-no-1-ethanol-feedstock-as-grain-based-supply-hits-record-high-aida/ | 2026-08 | 2026-11-01 | 380 distilleries; 480 crore litres | search summary |
| 14 | Grain-based ethanol 67 percent of supplies ESY 2025-26 till June | Autocar Pro | https://www.autocarpro.in/news/grain-based-ethanol-accounts-for-67-percent-of-indias-supplies-in-esy-2025-26-till-june-133486 | 2026 | 2026-11-01 | Grain share | search summary |
| 15 | MSEs in non-leather footwear get one more year | Outlook Business | https://www.outlookbusiness.com/news/mses-in-non-leather-footwear-sector-get-one-more-year-to-meet-quality-control-norm | n/d | 2026-11-01 | July 2027 deadline; lab bottleneck | search summary |
| 16 | What is next for the footwear industry | Mondaq / ELP Law | https://www.mondaq.com/india/economic-analysis/1367106/what-is-next-for-the-footwear-industry-navigating-the-bis-quality-control-order-on-footwear | 2023-11 | 2026-11-01 | BIS relaxation of lab rule | search summary |
| 17 | Complete Service Compendium 2026 | FDDI | https://fddiindia.com/pdf/COMPLETE-SERVICE-COMPENDIUM2026.pdf | 2026 | 2026-11-01 | FDDI labs | search summary |
| 18 | NTH establishes advanced shoe testing laboratory in Ghaziabad | All India Radio | https://newsonair.gov.in/national-test-house-establishes-advanced-shoe-testing-laboratory-in-ghaziabad/ | 2026-05-17 | 2026-11-01 | Ghaziabad lab; SGS Chennai recognition via separate SGS result | search summary |
| 19 | Flexing tester listings | TradeIndia | https://www.tradeindia.com/manufacturers/flexing-tester.html | n/d | 2026-11-01 | Tester prices | search summary |
| 20 | BIS notice (test fees) | BIS | https://services.bis.gov.in/tmp/NROL_24052018.pdf | 2018 | 2026-11-01 | Basic test fee Rs 15,540-22,140 (2018, stale over 18 months) | search summary |
| 21 | CSE report on waste tyres | CSE | https://www.cseindia.org/content/downloadreports/12796 | n/d | 2026-11-01 | 517 units, 200 pyrolysis units, EPR rules | search summary |
| 22 | NITI Aayog proposes standards for TPO and rCB | Down To Earth | https://www.downtoearth.org.in/waste/waste-tyre-management-overhaul-niti-aayog-proposes-new-standards-for-tyre-pyrolysis-oil-and-recovered-carbon-black | n/d | 2026-11-01 | Standards gap | search summary |
| 23 | ASTM approves rCB classification | Tyrepress | https://www.tyrepress.com/2026/02/astm-approves-tyre-orientated-recovered-carbon-black-classification/ | 2026-02 | 2026-11-01 | ASTM D8474, D8632; operator controls | search summary |
| 24 | Lead Reclaim intimation | NSE archives | https://nsearchives.nseindia.com/corporate/LEAD_18052026105152_Intimation.pdf | 2026-05-18 | 2026-11-01 | rCB price comparison | search summary |
| 25 | Industry Analysis | Export Experts Global | https://exportexpertsglobal.com/wp-content/uploads/2026/01/Industry-Analysis.pdf | 2026-01 | 2026-11-01 | Conflicting rCB price | search summary |
| 26 | Hyderabad fake refrigerants major threat in summer | Telangana Today | https://telanganatoday.com/hyderabad-fake-refrigerants-major-threat-in-summer | n/d | 2026-11-01 | Unlabelled cylinders (date uncertain) | search summary |
| 27 | Counterfeit refrigerant gases and AC fire incidents | OpIndia | https://www.opindia.com/2026/06/explained-how-counterfeit-refrigerant-gases-illegal-refilling-practices-and-import-dependence-could-be-contributing-to-a-rise-in-deadly-ac-fire-incidents-across-india/ | 2026-06 | 2026-11-01 | Disposable cylinder ban; weak source | search summary |
| 28 | Canada warns of counterfeit R410A | Cooling Post | https://www.coolingpost.com/world-news/canada-warns-of-potentially-lethal-counterfeit-r410a | n/d | 2026-11-01 | R40 in cylinders | search summary |
| 29 | Counterfeit refrigerants | UNIDO | https://UNIDO.org/sites/default/files/unido-publications/2023-02/COUNTERFEIT-REFRIGERANTS-en.pdf | 2023-02 | 2026-11-01 | Background | search summary |
| 30 | Mini ID R-1234yf Refrigerant Identifier | Bacharach | https://www.mybacharach.com/product/mini-id-r-1234yf-refrigerant-identifier/ | n/d | 2026-11-01 | Identifier price (CAD via other retailer) | search summary |
| 31 | Neutronics Mini ID R134a | HVAC Trade Supply (AU) | https://www.hvactradesupply.com.au/products/neutronics-refrigerant-identifier-r134a-mini-id | n/d | 2026-11-01 | Identifier price | search summary |
| 32 | Refrigerant Scales | IndiaMART | https://m.indiamart.com/impcat/refrigerant-scales.html | n/d | 2026-11-01 | Indian scale and recovery machine prices | search summary |
| 33 | Testo 560i | Test Equipment Depot | https://www.testequipmentdepot.com/testo-0564-1560-01-refrigerant-scale-with-bag.html | n/d | 2026-11-01 | Connected scale prices | search summary |
| 34 | CPS Compute-A-Charge CC220EW | SupplyHouse | https://www.supplyhouse.com/CPS-CC220EW-Compute-A-Charge-Enhanced-Wireless-Refrigerant-Charging-Scale | n/d | 2026-11-01 | App with job and customer data | search summary |
| 35 | HVACVerify contractors page | HVACVerify | https://hvacverify.pages.dev/contractors | n/d | 2026-11-01 | Nearest homeowner report | search summary |
| 36 | The Rs 1,500 AC scam in India | Business Today | https://www.businesstoday.in/visualstories/news/the-1500-ac-scam-in-india-are-your-paying-for-gas-that-was-never-leaking-242464-16-06-2025 | 2025-06-16 | 2026-11-01 | Top-up scam | search summary |
| 37 | Fake AC mechanics caught in Margao | Herald Goa | https://www.heraldgoa.in/?p=455737 | n/d | 2026-11-01 | Rs 650 vs Rs 3,500 case | search summary |
| 38 | AC gas refill, Bangalore | Urban Company | https://www.urbancompany.com/bangalore-ac-service-repair/ac-gas-refill-near-me | n/d | 2026-11-01 | Gas by weight or back pressure | search summary |
| 39 | AC service Hyderabad | Urban Company | https://urbancompany.com/hyderabad-ac-service-repair | n/d | 2026-11-01 | 90-day guarantee, Rs 10,000 cover | search summary |
| 40 | Skill development initiative | Tribune India | https://m.tribuneindia.com/article/skill-development-initiative/633744 | n/d | 2026-11-01 | About 200,000 RAC technicians (date unclear) | search summary |
| 41 | AC technician demand and sustainability | CEEW | https://www.ceew.in/publications/air-conditioner-technician-demand-and-Sustainability | 2025-11-03 | 2026-11-01 | Certification context | search summary |
| 42 | Refrigerant tracking and compliance software | AWE International | https://awe.international/article/1939374/news | n/d | 2026-11-01 | Parasense and other software | search summary |
| 43 | F-gas register software | Kolonell | https://kolonell.com/en/blog/f-gas-register-compliance-software-refrigeration-engineers-2026 | 2026 | 2026-11-01 | Custom build EUR 25,000-55,000 | search summary |
| 44 | Handheld honey adulteration detection system, IN202411019851 | CSIR Technology Portal | https://techindiacsir.anusandhan.net/online/handheld-non-destructive-honey-adulteration-detection-system-and-method-IN202411019851-patent.htm | 2025-09 | 2026-11-01 | Prior art, 8% limit | search summary |
| 45 | Dabur launches mobile honey testing lab | Exchange4media | https://www.exchange4media.com/marketing-news/dabur-india-launches-country's-first-mobile-honey-testing-lab-68041.html | 2017-03 | 2026-11-01 | Prior art (stale) | search summary |
| 46 | Low-cost multispectral device for honey adulteration | KMITL | https://dspace.kmitl.ac.th/handle/123456789/20317 | n/d | 2026-11-01 | Prior art, accuracy 0.91-0.98 | search summary |
| 47 | CSE honey investigation | Tribune India | https://www.tribuneindia.com/news/nation/honeytrap-cse-investigations-claim-nefarious-adulteration-business-of-honey-designed-to-bypass-purity-tests-178930 | 2020-12 | 2026-11-01 | 77% adulterated; syrup source; price fall | search summary |
| 48 | Honey fraud and novel syrups | Intertek | https://www.intertek.com/blog/2025/12-18-honey-fraud-novel-syrups-2025/ | 2025-12-18 | 2026-11-01 | New syrups end of 2024 | search summary |
| 49 | Honey | European Commission | https://agriculture.ec.europa.eu/food-farming-fisheries/animals-and-animal-products/animal-products/honey_en | n/d | 2026-11-01 | Directive 2024/1438 | search summary |
| 50 | Hive scale FAQ | HonestBee (vendor) | https://honestbeeltd.com/faqs/how-does-the-use-of-high-precision-electronic-scales-facilitate-the-accurate-measurement-of-bee-feed-consumption | n/d | 2026-11-01 | Scale limits | search summary |
| 51 | BroodMinder TH2SM | Worker and Hive | https://workerandhive.com/products/broodminder-th2sm | n/d | 2026-11-01 | Hive monitor prices | search summary |
| 52 | Aflatoxin B1 conversion by BSF larval enzyme extracts | PMC | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6784232/ | 2019 | 2026-11-01 | Low recovery of AFB1 | search summary |
| 53 | BSFL and AFB1, Ecotoxicology and Environmental Safety | DOAJ | https://doaj.org/article/5580cf251caa45c9a6d3439ddb51b1db | 2024-07 | 2026-11-01 | AFB1 loss similar without larvae | search summary |
| 54 | US8733284B2 Method and apparatus for breeding flying insects | Google Patents | https://patents.google.com/patent/US8733284 | n/d | 2026-11-01 | Prior art on BSF and DDGS | search summary |
| 55 | Judicial liquidation for Ynsect | AgFunderNews | https://agfundernews.com/judicial-liquidation-for-ynsect-as-insect-farming-sector-struggles-to-become-competitive | 2025-12 | 2026-11-01 | Closed venture | search summary |
| 56 | Premium insect meal 60 protein | IndiaMART | https://www.indiamart.com/proddetail/premium-insect-meal-60-protein-bsf-meal-2854163144088.html | n/d | 2026-11-01 | BSF meal Rs 195 a kg | search summary |
| 57 | Waterline Exports feed | IndiaMART | https://m.indiamart.com/waterlineexports/feed.html | n/d | 2026-11-01 | BSF meal Rs 500 a kg | search summary |
| 58 | Energy-based groundwater abstraction estimate | AgEcon Search | https://ageconsearch.umn.edu/record/344328?ln=en | 2023 | 2026-11-01 | Prior art, R2 values | search summary |
| 59 | Toxin binder listings | IndiaMART | https://m.indiamart.com/impcat/toxin-binder.html | n/d | 2026-11-01 | Binder prices and dosage | search summary |
| 60 | Total aflatoxin rapid test kit | Abbexa | https://www.abbexa.com/aflatoxin-rapid-test-kit-colloidal-gold | n/d | 2026-11-01 | USD 203 for 20 tests | search summary |
| 61 | Test kits listing | TradeIndia | https://www.tradeindia.com/delhi/test-kits-city-228067.html | n/d | 2026-11-01 | Rs 20,300 a pack | search summary |
| 62 | Suggestive list of approved RAFT kits | FSSAI | https://fssai.gov.in/upload/uploadfiles/files/Suggestive%20list%20of%20approved%20RAFT%20Kits%20for%20FSW-E-3468.pdf | n/d | 2026-11-01 | Neogen Reveal Q+ Max registered in India | search summary |
| 63 | New refrigerant app out of Australia | Refrigerant HQ | https://refrigeranthq.com/new-refrigerant-app-australia/ | n/d | 2026-11-01 | Reclaim data app | search summary |
| 64 | Housejoy shuts services in 7 cities | Medianama | https://www.medianama.com/2017/05/223-housejoy-shuts-services-in-7-cities/ | 2017-05 | 2026-11-01 | Closed home-services venture (stale) | search summary |
| 65 | Trakref Pro | Apple App Store | https://apps.apple.com/bt/app/trakref-pro/id1470153760 | n/d | 2026-11-01 | Refrigerant tracking app | search summary |
| 66 | USRE32451E Weight-monitored air-conditioner charging station | Google Patents | https://patents.google.com/patent/USRE32451 | 1980s | 2026-11-01 | Old patent prior art | search summary |
| 68 | Note on QCOs for footwear industry | Leather India | https://leatherindia.org/wp-content/uploads/2023/05/Note-on-QCOs-for-Footwear-Industry-May-2023Internal.pdf | 2023-05 | 2026-11-01 | Option to subcontract tests | search summary |
| 70 | Mobile and hand-held NIR in feed evaluation | ILRI / CGSpace | https://cgspace.cgiar.org/items/f9b89a25-86da-4891-9895-695f110f9451 | 2019 | 2026-11-01 | Handheld NIR feed work; Foss and Thermo items from same result set | search summary |
