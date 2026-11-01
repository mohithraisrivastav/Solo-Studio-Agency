# Hunt B: something changed (rules, cheap capability, input costs)

Date: 2026-11-01. Run: demo-revised. Lens B.

**Result: zero theses kept.** Six candidates were investigated. All failed at least one of the buyer's three questions. This is a valid result; the near-misses and the reasons are below.

**Limit on verification.** Every Indian government host I tried (CGWA, CPCB, BIS, MoEFCC, India Code, e-Gazette, NGT, PIB, Sansad) and the vendor pages I tried to open were blocked by the session network. I could not open any rule text. Every rule claim below is from search summaries, so each load-bearing assumption is `UNVERIFIED KILLER` unless stated. Who could answer: the CGWA consolidated guideline (24.09.2020, amended 29.03.2023) and CPCB tyre portal are free to read for anyone with normal internet access; cost is about an hour.

Search count: about 33 of the budget of about 45. I stopped when no candidate passed the buyer questions, rather than spend the rest on prior-art sweeps for theses already failing.

## 1. Industries chosen and why

Deciding questions are written per industry before any scan. A candidate survives only if all are answered "yes".

| Industry | Deciding questions |
|---|---|
| Industrial groundwater (water infrastructure) | Is the rule enforced? Does a small firm earn money against vendors already selling the hardware? |
| Tyre recycling (rubber) | Is the compliant route open to a new entrant? Is output demand real? |
| Footwear and small-factory product testing (BIS Quality Control Orders) | Is the buyer's cheapest rival (subsidised public lab) beaten? |
| Refrigerants (cooling services) | Is there a mandate or price shift that pays for reclaim? |
| Ethanol by-products (distillery feed) | Can a small firm afford the process? Who keeps the savings? |
| Export honey and spices (food testing and processing) | Is the change recent, and does a small firm have a way in? |

Why each might hide something now:

- Groundwater: `[S1]` CGWA notice requires tamper-proof digital flow meters with telemetry on abstraction structures of NOC applicants. Rule is recent enough for hardware to still be rolling out `[I]`.
- Tyres: `[S7]` Waste tyre EPR notified 21 July 2022. Producers must buy certificates from registered recyclers `[S7]`.
- QCO testing: `[S10]` Think-tank GTRI says testing costs squeeze MSMEs. `[S11]` Footwear QCO deadline for non-leather micro and small units moved to 31 July 2027.
- Refrigerants: `[S18]` Official ministry document ties the HFC freeze to 01.01.2028. Price pressure on R22 is plausible `[A]`, basis: HCFC phase-out under way; test by finding a dated India price.
- Ethanol by-products: `[S16]` Rice DDGS export price fell from USD 435 to USD 324 per tonne over 2022 to 2024. `[S17]` Distilleries run at 60 to 70 percent on weak orders per an ethanol body chief.
- Honey and spices: `[S13]` NMR tests mandatory for honey exports since 1 August 2020. `[S15]` Spices Board guidelines after the 2024 EtO findings steer exporters to steam sterilisation.

## 2. Raw candidates

| # | Problem | Payer | Signal | Tag |
|---|---|---|---|---|
| 1 | Industrial NOC holders must fit and calibrate flow meters with telemetry | Factory, hotel, mine, bottler | Listings of CGWA-compliant meters at INR 18,900 to 30,999 per unit | `[S3]` |
| 2 | Annual NABL calibration of installed groundwater meters | Same | Calibration listed at INR 2,800 to 12,000 per meter | `[S4]` |
| 3 | Waste tyres recycled legally | Tyre producers (EPR certificate buyers) | 217 producers and 493 recyclers registered per a 2025 parliamentary reply | `[S8]` |
| 4 | Small footwear makers need BIS tests or in-house lab | Micro and small footwear units | Testing fee relief of 80 percent for micro units (2023, secondary) | `[S10]` |
| 5 | Scrapped AC gas vented instead of reclaimed | AC service firms, chiller owners | Undated forum price of INR 680 to 720 per kg for R22 | `[S19]` |
| 6 | Low-value DDGS from distilleries | Distillery owners | Export price USD 324 per tonne for rice DDGS | `[S16]` |
| 7 | Honey exporters need NMR proof of purity | Honey exporters | Cost INR 15,000 to 25,000 per sample, vendor guide, unverified | `[S13]` |
| 8 | Spice exporters need EtO-free sterilisation | Spice processors | Steam sterilisers already sold to the Indian spice industry (2024) | `[S15]` |
| 9 | Time-of-day tariffs make storage worth buying | Commercial and industrial users above 10 kW | Rule 8A: peak at least 1.2 times normal tariff, solar hours at least 20 percent lower, per one trade report | `[S21]` |

Candidate 9 was dropped after one search: the tariff gap is set state by state `[S21]`, so the value rests on one rule and one season-like price window. Not investigated further.

## 3. Opportunity theses

None kept. The nearest three are written up under section 4 with the numbers that killed them. Payback script: `runs/2026-11-01-demo-revised/01-hunt-B-payback.py`.

## 4. Cut candidates and reasons

### T1 Groundwater flow meter with telemetry and calibration (the near miss)

- Load-bearing assumption: meters with telemetry are mandatory for NOC holders and enforced. Checked via `[S1]` (FAOLEX copy of the CGWA notice, via search summary) and `[S2]` (consolidated guideline, not opened). `UNVERIFIED KILLER`. Sources disagree on notice timing (30 days or 90 days) and one source says the 2019 revision was stayed by the NGT `[S2]`; a later 2020 guideline supersedes earlier ones `[S2]`.
- Demand is real but small: 12,650 NOCs issued to industries in five years `[S5]`, about 2,530 per year `[I]`. CGWA detected 2,833 cases of extraction without a valid NOC or beyond quota up to 15 February 2026 `[S6]`.
- Buyer cost: INR 25,000 per meter `[A]`, basis: middle of listing range `[S3]`; calibration INR 6,500 a year `[A]`, basis: middle of listings `[S4]`. For two structures, capex is INR 50,000 and opex INR 19,000 a year `[I]` (script).
- Buyer payback: the buyer gets no cash return; the benefit is avoided penalty of at least INR 1 lakh `[S6]`. Payback is undefined. Rated weak.
- Prior art (6 searches: "CGWA flow meter telemetry price India", "NOC flow meter vendors", calibration price, NOC holder count, Lok Sabha reply on telemetry, FAOLEX notice): many Indian vendors already sell it, including Flowtech, Vision World Tech, Acorn Controls and IndiaMART/TradeIndia sellers `[S3]`. Other countries and failed entrants: not found after 0 dedicated searches; I did not run the two-country sweep because the thesis failed earlier.
- Cheapest rival: a listed meter at INR 18,900 `[S3]`, bought locally.
- Buyer's three questions: why buy: supported (mandatory, `UNVERIFIED KILLER`); why this one: not supported (commodity hardware, many sellers `[S3]`); why a small firm earns: not supported. At a 2 percent share (about 51 NOCs a year `[I]`) hardware margin is about INR 7.6 lakh and recurring margin INR 3.8 lakh at assumed margins of 30 and 40 percent `[A]`, basis: typical reseller margins, test with two vendor quotes. Founder time at INR 750 per hour and 12 hours per installation `[A]` costs about INR 9.1 lakh `[I]`. A loss on founder time.
- Cut: reason (e), fragmented buyers served by many vendors; no asset a small firm builds that others cannot copy.

### T2 Refrigerant recovery and reclaim

- Load-bearing assumption: a rule or price shift makes reclaimed gas worth more than the cost of collecting it. Not supported. I found no Indian mandate to reclaim and no 2026 India price: the only India price is an undated forum post of INR 680 to 720 per kg `[S19]`. Customs seized 80 tonnes of R22 labelled as R134a, showing illegal supply competes `[S19]`.
- HFC freeze is 01.01.2028 with first cut later `[S18]`, so no gas shortage for HFCs soon `[I]`.
- Recovery machines cost INR 27,000 to 75,000 `[S20]`. Script, with assumed discount of 30 percent to virgin and handling INR 150 per kg `[A]`: margin about INR 340 per kg, about INR 408 per scrapped AC; 85 units repay one machine `[I]`. Looks fine on paper but rests on an unconfirmed price and an unconfirmed supply of recoverable gas.
- Reclaim to a sellable standard needs distillation and testing; some blends cannot be separated `[S22]`. No Indian reclaimer list found after 4 searches (queries: "refrigerant reclamation centre India", "reclaimed R22 India", "ODS rules reclamation 2024", "refrigerant recovery machine price India").
- Cut: reason (a), demand not shown. Would revisit if a dated India R22 price trend or a reclaim mandate is found.

### T3 In-house test kit for footwear QCO

- BIS allows subcontracting tests to recognised labs where in-house equipment is expensive `[S12]`, and micro units get an 80 percent cut in testing charges `[S10]` (2023, secondary).
- Cheapest rival: a subsidised public lab; fee after the cut is INR 2,000 on a INR 10,000 fee `[I]`. Kit price not found; at an assumed INR 10 lakh `[A]` and 10 variants a year `[A]`, payback is 50 years, and 10 years even at full fee `[I]`.
- Cut: reason (a), the buyer already has a cheaper option. Also the deadline moved to 31 July 2027 for non-leather micro and small units `[S11]`, which lowers urgency.

### T4 Waste tyre recycling

- Producers meet EPR targets with certificates from registered recyclers `[S7]`. Registered base is already 493 recyclers `[S8]`. The pyrolysis route draws closure orders: CPCB ordered 270 units to shut `[S9]`.
- Certificate price not found after 2 searches (queries: "EPR certificate price waste tyre per tonne", "waste tyre EPR certificate trade 2025"). Recovered carbon black and pyrolysis oil prices not found.
- Cut: reasons (c) and (d); regulated and polluting process, no price evidence, crowded registered base.

### T5 DDGS upgrading (protein fractionation)

- Distillery owners keep any gain. Price fell USD 435 to USD 324 per tonne for rice DDGS `[S16]`; exports rose from 16,556 tonnes to about 354,110 tonnes `[S16]`.
- A process plant for a distillery is beyond the Rs 5,00,000 capital default `[A]`, basis: brief; no plant cost found. Incumbent equipment makers could add it `[K]`.
- Cut: reason (b) and capital.

### T6 Honey NMR screening and spice steam sterilisation

- Honey NMR has been required since 1 August 2020 `[S13]`; it is not a change from this year. Cost figure is from a vendor guide `[S13]`. Spice steam sterilisers are sold already `[S15]`.
- Cut: not new, incumbents present, and no primary price or capacity data found.

## 5. Top uncertainties

1. CGWA and CPCB texts were not opened; T1 and T4 rest on search summaries.
2. No 2026 India price for R22 or for tyre EPR certificates was found.
3. Founder-time and margin figures in the script are assumptions; two vendor quotes would test T1 in a day.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Notice, CGWA, installation of digital water flow meter | FAOLEX / UNEP | https://leap.unep.org/en/countries/in/national-legislation/notice-central-ground-water-authority-installation-digital-water | n/d | 2026-11-01 | Flow meter requirement | search summary |
| 2 | Consolidated MoJS guidelines to regulate ground water extraction | CGWA | https://cgwa-noc.gov.in/landingpage/Guidlines/ConsolidateGuidline.pdf | 2023 | 2026-11-01 | Guideline text (not opened, host blocked) | search summary |
| 3 | Telemetry flow meter listings | Flowtech, IndiaMART | https://m.indiamart.com/flowtechinstruments/telemetry-flow-meter.html | n/d | 2026-11-01 | Meter prices | search summary |
| 4 | Flow meter calibration listings | IndiaMART | https://dir.indiamart.com/impcat/flow-meter-calibration.html | n/d | 2026-11-01 | Calibration prices | search summary |
| 5 | Lok Sabha unstarred answer AU1333 | Sansad | https://eparlib.sansad.in/bitstream/123456789/1470210/1/AU1333.pdf | n/d | 2026-11-01 | NOC count | search summary |
| 6 | CGWA detects 2,833 illegal extraction cases | Eastern Mirror | https://www.easternmirrornagaland.com/central-ground-water-authority-detects-2833-illegal-groundwater-extraction-cases | 2026 | 2026-11-01 | Enforcement count | search summary |
| 7 | Extended producer responsibility for waste tyre | Mondaq | https://www.mondaq.com/india/waste-management/1231236/extended-producer-responsibility-epr-for-waste-tyre | 2022 | 2026-11-01 | Tyre EPR mechanics | search summary |
| 8 | Rajya Sabha reply PQ 267 | Rajya Sabha | https://rsdebate.nic.in/bitstream/123456789/759350/1/PQ_267_20032025_U2297_p310_p312.pdf | 2025-03-20 | 2026-11-01 | Registered producers and recyclers | search summary |
| 9 | CPCB orders closure of 270 tyre pyrolysis units | Daily Pioneer | https://www.dailypioneer.com/2019/india/cpcb-orders-closure-of-270-tyre-pyrolysis-units.html | 2019 | 2026-11-01 | Pyrolysis closures (stale) | search summary |
| 10 | Govt should cap charges of product testing under QCO: GTRI | Outlook Business | https://www.outlookbusiness.com/economy-and-policy/govt-should-cap-charges-of-product-testing-under-quality-control-order-gtri | 2026 | 2026-11-01 | QCO testing cost, 80 percent cut | search summary |
| 11 | Footwear QCO deadline extension 2027 | EVTL India | https://evtlindia.com/footwear-qco-deadline-extension-2027-business-impact | n/d | 2026-11-01 | Deadline 31 July 2027 | search summary |
| 12 | BIS footwear circular for branch offices | BIS | https://services.bis.gov.in/tmp/footwear_circular_for_BOs_bJF5_2021-02-26.pdf | 2021-02-26 | 2026-11-01 | Subcontract testing allowed | search summary |
| 13 | How to export honey from India | Ximpex | https://ximpex.in/guides/how-to-export-honey-from-india | n/d | 2026-11-01 | NMR cost, mandate date (vendor guide) | search summary |
| 15 | Spices Board guidelines to prevent EtO contamination | Outlook Business | https://www.outlookbusiness.com/news/spices-board-formulates-comprehensive-guidelines-for-exporters-to-prevent-eto-contamination | 2024 | 2026-11-01 | Steam sterilisation guidance | search summary |
| 16 | India witnesses rise in DDGS exports, price decline | Bioenergy Times | https://bioenergytimes.com/india-witnesses-rise-in-exports-of-ethanol-byproduct-ddgs-but-price-decline-poses-challenge-for-industry/ | 2025 | 2026-11-01 | DDGS prices and exports | search summary |
| 17 | Rice from FCI has cut biofuel dependence on maize | Informist | https://informistmedia.com/CommodityWire/39098/Rice-from-FCI-has-cut-biofuel-dependence-on-maize-says-ethanol-body-chief-Jain | n/d | 2026-11-01 | Distillery utilisation | search summary |
| 18 | PARIVESH office memorandum on HFC controls | MoEFCC | https://parivesh.nic.in/publicdocument/UPLOAD_OM_NOTIFICATION/IA_DOCS/1002_07042026062522.pdf | 2026-04-07 | 2026-11-01 | HFC freeze date | search summary |
| 19 | R22 cost thread; customs seizure of R22 | NoBroker forum; Cooling Post | https://www.nobroker.in/forum/what-is-the-cost-of-r22-refrigerant | n/d | 2026-11-01 | R22 price (weak), seizure | search summary |
| 20 | Refrigerant recovery machine listing | TradeIndia | https://therefrigeration.tradeindia.com/value-vrr24l-1hp-refrigerant-recovery-machine-8404893.html | n/d | 2026-11-01 | Recovery machine prices | search summary |
| 21 | Understanding ToD rebates and surcharges | Daily Excelsior | https://www.dailyexcelsior.com/understanding-tod-rebates-and-surcharges-in-jks-new-power-tariff/ | 2026 | 2026-11-01 | ToD rule summary | search summary |
| 22 | The separation equation | ACHR News | https://achrnews.com/articles/107668-the-separation-equation | n/d | 2026-11-01 | Blend separation limit | search summary |
