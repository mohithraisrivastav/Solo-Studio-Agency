# Hunt B round 2: re-sort and create

Date: 2026-11-01. Lens B. Supersedes the verdict in `01-hunt-B.md` (left unchanged). Economics script: `runs/2026-11-01-demo-revised/02-hunt-B-r2-econ.py`.

**Result: 0 ADVANCE, 9 INVESTIGATE, 4 REJECT (of the round-1 routes).** Nothing here has buyer contact, so nothing reaches ADVANCE. Several ideas are cheap to test; the first tests cost INR 0 to 5,000 `[A]`, basis: phone calls and two quotes.

**What I could not do.** Indian government hosts (CGWA, CPCB, BIS, MoEFCC, Sansad, NGT) and vendor pages did not open in this session, so rule claims come from search summaries. Missing information is listed in section 5. It is not treated as evidence against any idea.

## 1. Industries (unchanged from round 1)

Groundwater and water infrastructure; tyre and rubber recycling; footwear and small-factory product testing; refrigerants and cooling; ethanol by-products and animal feed; export honey and spices; cold chain and time-of-day tariffs. Reasons are in `01-hunt-B.md`.

## 2. Re-sort of every round-1 candidate

| Round-1 candidate | Round 1 | Round 2 | Why it changed (or did not) |
|---|---|---|---|
| Groundwater flow meter + telemetry resale | Cut | INVESTIGATE, reshaped (I1, I2, I9) | Round 1 judged resale of a INR 19,000 to 31,000 meter `[S3]`, which stays weak. Round 1 also asked for a cash return, but a mandatory purchase has none. The rule creates a captive buyer, a recurring calibration need `[S4]` and a live data stream; those support new models. Test is two vendor quotes. |
| Refrigerant reclaim as a compliance business | Cut | REJECT that form; INVESTIGATE a value-driven form (I4) | CEEW states India has no mandate to recover, reclaim or destroy refrigerant `[S10]`, which contradicts a compliance-led model. The same source says informal handlers vent gas because it has little resale value `[S10]`. That is a gap a payment mechanism could close. |
| Footwear QCO in-house test kit | Cut (50-year payback) | INVESTIGATE, low priority (I8) | Round 1 assumed a INR 10 lakh kit `[A]`. Listings show testers at INR 55,000 to 2.45 lakh each `[S9]`; four of them total about INR 4.9 lakh `[I]`. Payback is 1 to 24 years depending on test fee and volume `[I]`, and the fee data is weak. |
| Waste tyre pyrolysis or EPR recycler | Cut | REJECT pyrolysis; INVESTIGATE mechanical crumb product (I3) | CPCB ordered 270 pyrolysis units to close `[S28]`: strong contradicting evidence for that route. Crumb sells at INR 18 to 38 per kg `[S14]`, so a finished product from it is open. |
| DDGS protein fractionation plant | Cut | REJECT the plant; INVESTIGATE cleaned lots (I6) | A distillery-scale plant is impractical at INR 5,00,000 capital `[A]`, basis: brief; no plant price found. Handling and testing lots needs little capital. |
| Honey NMR screening | Cut (not new) | INVESTIGATE (I5) | "Not new" is not a contradiction. The NMR mandate dates from 1 August 2020 `[S16]`, but I found no beekeeper-facing screener on sale (see I5). |
| Spice steam sterilisation | Cut (incumbents) | INVESTIGATE as shared tolling (I7) | Equipment is sold `[S22]`. Tolling rates not found, so the shared-service model is untested, not disproved. |
| Time-of-day storage retrofit | Dropped | INVESTIGATE, low priority, not developed | Inficold already sells ice-bank retrofits and raised USD 900,000 `[S24]`. Low difference. No contradicting evidence on the rule. |

## 3. Ideas

Ratings: difference, desirability, plausibility, each High / Medium / Low, all judgement `[H]` unless stated. "Cheapest rival" is the do-nothing or simple option.

### I1 Groundwater meter as a rental service (new business model for a known need)

1. **Different:** the factory pays a monthly fee that bundles meter, annual calibration, SIM, installation and the monthly reading report; no capital outlay `[H]`.
2. **Desire:** buyer must otherwise find a vendor, buy at INR 18,900 to 30,999 `[S3]`, and book calibration at INR 2,800 to 12,000 `[S4]` every year `[H]`, basis: renewal needs a valid NABL certificate per one seller `[S3]`. Annual calibration is not confirmed in the rule text (missing information).
3. **Buyers:** industrial NOC holders. 12,650 NOCs were issued in five years `[S5]`, about 2,530 a year `[I]`. Who blocks: the CGWA, which must accept the meter model and telemetry format `[S1]`.
4. **Advantage:** one invoice and no calibration chasing. Cheapest rival is buying a listed meter and calling a calibration lab; its five-year cost per meter is about INR 75,500 including install `[I]` (script, SIM and install are `[A]`).
5. **Price and cost:** at INR 2,000 a month per meter `[H]`, five-year margin is about INR 44,500 (37%) `[I]`; at INR 1,500 it is 16% `[I]`. Cash tied up is about INR 28,000 per meter `[I]`, so INR 5,00,000 funds about 17 meters `[I]`. Business works only if fee is above about INR 1,700 a month `[I]` and fewer than a few units fail.
6. **Critical unverified assumption:** a factory prefers renting to buying `[H]`, and the rule lets a third party own the meter `[H]`.
7. **Cheapest test:** two vendor quotes for wholesale meter plus calibration, and five calls to NOC holders asking what they paid. Cost under INR 5,000 `[A]`, about 1 week `[A]`.

Ratings: difference Medium, desirability Medium, plausibility Medium. Outcome: **INVESTIGATE**.

Existing solutions: Flowtech, Vision World Tech, Acorn Controls and IndiaMART sellers sell CGWA-compliant meters outright, INR 18,900 to 30,999, dates not shown `[S3]`. Rental or service bundle: not found after 2 searches (queries: "CGWA flow meter telemetry price India", "flow meter calibration NABL cost India"); two other countries and failed entrants not searched.

### I2 Pump-health and energy add-on on the mandated meter (new capability on an existing data stream)

1. **Different:** the compliance meter already reports pump working hours and flow `[S3]`; add alerts for dry run, falling flow and idle pumping, sold as a saving `[H]`.
2. **Desire:** borewell pumps are a running cost; a 7.5 kW pump at 4,800 hours uses about INR 2.9 lakh of energy a year `[I]` (hours, kW and INR 8 per kWh are `[A]`; the tariff band of INR 7 to 9 per kWh is `[S25]`).
3. **Buyers:** the same factories. 
4. **Advantage:** zero added hardware; rival is a standalone pump monitor or doing nothing `[H]`.
5. **Price and cost:** a 5% energy saving is about INR 14,400 a year per pump `[I]` (5% is `[H]`). A fee near INR 3,000 a year is plausible `[H]`.
6. **Critical unverified assumption:** the data is rich enough to detect faults and the savings are real `[H]`.
7. **Cheapest test:** ask three vendors for sample data fields and read one day of data from a pilot factory. Cost INR 0 to 3,000 `[A]`, 2 weeks `[A]`.

Ratings: difference High, desirability Low to Medium, plausibility Low. Outcome: **INVESTIGATE (low priority)**; depends on I1 giving access to the data.

### I3 Cow-comfort mats from tyre crumb (different material for a known need)

1. **Different:** a mat made largely of crumb rubber from scrap tyres, which adds a use for a tyre output other than burning `[H]`.
2. **Desire:** dairy farms buy mats; a 4 by 6 ft mat sells at INR 1,500 to 2,800 `[S13]`, about 40 kg `[S13]`.
3. **Buyers:** commercial dairy farms and farm suppliers. Blockers: dealers who stock natural-rubber mats. 
4. **Advantage over rivals:** the rival is existing mats from rubber makers; listings do not state recycled content `[S13]`, so a "recycled" claim may already exist (unchecked).
5. **Price and cost:** crumb costs INR 17.8 to 38 per kg `[S14]`. With assumed 15% binder at three times the per-kg price `[A]`, unit cost ranges INR 1,252 to 2,472 `[I]`. At INR 2,100 price, margin ranges from 40% to a loss of 18% `[I]`. It works only at the low-cost end.
6. **Critical unverified assumption:** a binder system and mould that gives a durable mat at under INR 1,500 to 1,900 per piece `[H]`.
7. **Cheapest test:** one binder quote and a 5-piece hand-pressed sample; ask five farms their price. About INR 15,000 `[A]`, 3 weeks `[A]`.

Ratings: difference Low to Medium, desirability Medium, plausibility Medium. Outcome: **INVESTIGATE**. Prior art: mats from rubber makers are widely listed `[S13]`; crumb-rubber mats and failed entrants not searched.

### I4 Pay-per-kilogram gas bounty for scrap-dealer AC dismantling (different mechanism)

1. **Different:** pay informal dismantlers for each recovered kilogram, with a loaned recovery machine and cylinder, because informal handlers vent gas that has little resale value to them `[S10]`.
2. **Desire:** the dealer gains cash for work they already do; the sponsor resells gas.
3. **Buyers of the gas:** owners of old R22 plant. Not identified. 
4. **Advantage:** removes the time-and-effort disincentive CEEW names `[S10]`. Rival: do nothing, which is what happens now `[S10]`.
5. **Price and cost:** undated forum price for R22 is INR 680 to 720 per kg `[S11]`, weak. A recovery machine is INR 27,000 to 75,000 `[S12]`. At 1.2 kg per AC, a 30% discount to virgin gas and 35% of sale value paid out `[A]`, margin is about INR 262 per AC `[I]`.
6. **Critical unverified assumption:** a current India price for R22 and a buyer who will take recovered, tested gas. Grade is a risk: customs seized 80 tonnes of R22 labelled as R134a `[S11]`.
7. **Cheapest test:** call five AC servicing firms and two chiller owners for price and whether they accept recovered gas; ask one scrap yard how many ACs a month. INR 0 to 2,000 `[A]`, 1 to 2 weeks `[A]`.

Ratings: difference High, desirability Medium, plausibility Low to Medium. Outcome: **INVESTIGATE**. Reclamation to a sellable standard needs distillation and some blends cannot be separated `[S29]`.

### I5 Honey pre-screen at the collection point (a buyer nobody serves with this technology)

1. **Different:** a low-cost screening reader placed with beekeepers or collection centres so syrup-adulterated lots are caught before export testing `[H]`.
2. **Desire:** an exporter or aggregator wants to know before buying a lot. NMR testing is mandatory for exports since 1 August 2020 `[S16]`.
3. **Buyers:** honey aggregators, FPOs and exporters. India exported about USD 206 million of natural honey in 2024-25 `[S16]`.
4. **Prior art:** CSIR-CEERI has a patent application for a handheld honey adulteration detector, with a detection limit of 8% `[S15]`; Dabur ran a mobile lab for beekeepers in 2017 `[S18]`. I found no startup selling a screener to beekeepers (1 search; incomplete).
5. **Price and cost:** the NMR cost is in conflict: INR 15,000 to 25,000 per sample in a vendor guide `[S16]`, and "a few hundred rupees" in an unattributed blog claim `[A]`. At INR 15,000 and a 5% failure rate, screening at INR 300 a lot avoids about INR 775 per lot `[I]`. At INR 500 NMR it does not pay on test cost alone `[I]`. A rejected export lot is the real prize and its value is missing information.
6. **Critical unverified assumption:** the true NMR fee, and that a cheap reader detects syrup at an 8% limit (the patent's limit) well enough to matter `[H]`.
7. **Cheapest test:** ask two labs for NMR fee quotes and turnaround, and ask three exporters about their last failed lot. INR 0, 1 week `[A]`. Technology feasibility needs a CSIR licensing enquiry, INR 0 `[A]`.

Ratings: difference High, desirability Medium, plausibility Low to Medium. Outcome: **INVESTIGATE**.

### I6 Cleaned, aflatoxin-tested DDGS lots for small feed mills and dairy FPOs (unserved buyer)

1. **Different:** sieved, tested DDGS in 1-tonne bags with a certificate, from surplus distilleries `[H]`.
2. **Desire:** DDGS lists at INR 17 to 30 per kg `[S19]`; export unit values were USD 225 a tonne against USD 416 for soybean meal in March 2025 `[S20]`, a gap of about INR 16.8 per kg `[I]` (INR 88 per USD is `[A]`). Distilleries run at 60 to 70% on weak orders `[S21]`.
3. **Buyers:** small feed mills, dairy FPOs. Blockers: aflatoxin and fibre quality; no limits found.
4. **Advantage:** reliability for buyers who cannot assess lots. Rival: buying directly from distilleries or traders listed on IndiaMART `[S19]`.
5. **Price and cost:** a premium of INR 2 per kg on 50 tonnes a month would give about INR 1 lakh gross a month, less about INR 7,500 of testing `[I]` (premium, volume and test cost are `[H]`, `[A]`).
6. **Critical unverified assumption:** buyers pay a premium for tested, sieved lots `[H]`. Thin trader margins are the risk.
7. **Cheapest test:** ask five small feed mills what they pay and what they reject; one lab quote. INR 2,000 `[A]`, 1 week `[A]`.

Ratings: difference Low to Medium, desirability Medium, plausibility Medium. Outcome: **INVESTIGATE**. Closest to a trading margin; no asset moat `[I]`.

### I7 Shared steam sterilisation for small spice processors (a different business model)

1. **Different:** a tolling plant that sterilises per kilogram, so a small processor needs no machine.
2. **Desire:** Spices Board guidance steers exporters away from ethylene oxide to steam or irradiation `[S23]`.
3. **Buyers:** small spice processors and exporters.
4. **Advantage:** no capital outlay. Rival: buy a machine; listings show a general-purpose 500 kg/hr unit at INR 10 lakh and a batch sterilizer of 250 to 1,500 kg `[S22]`.
5. **Price and cost:** tolling rate not found; at INR 5 per kg `[H]` a 250 kg/hr unit at 50% use gives about INR 66,000 a month contribution, 15-month machine payback `[I]` (steam and labour INR 1.5 per kg is `[A]`; excludes building and boiler). At INR 3 per kg payback is 36 months `[I]`.
6. **Critical unverified assumption:** the tolling price and that buyers will ship product to a third party `[H]`.
7. **Cheapest test:** ask five processors what they pay now or would pay, and one equipment quote. INR 0 to 3,000 `[A]`, 2 weeks `[A]`.

Ratings: difference Low to Medium, desirability Medium, plausibility Medium. Outcome: **INVESTIGATE**. Capital above the INR 5,00,000 default `[I]`.

### I8 Footwear test rig for micro units (low priority)

Kit total is about INR 4.9 lakh `[I]` from listed prices `[S9]`. Against a lab spend of INR 20,000 to 4 lakh a year `[A]`, payback is 1.2 to 24 years `[I]`. Fee data is secondary and mixes certification with test fees `[S7]`. BIS allows subcontracting tests to recognised labs `[S8]`. Critical assumption: what micro units actually pay per test `[H]`. Test: ask three Agra or Kolkata-type units. INR 0, 1 week `[A]`. Ratings: difference Low, desirability Low to Medium, plausibility Low. Outcome: **INVESTIGATE (low)**.

### I9 Verified abstraction ledger as a data product (new category)

1. **Different:** monthly metered abstraction data packaged for insurers, lenders and sustainability reports `[H]`.
2. **Desire:** unknown. 3. **Buyers:** not identified. 4. **Advantage:** none shown. 5. **Price:** none. 
6. **Critical assumption:** any buyer values it `[H]`.
7. **Test:** five calls to sustainability or insurance buyers, INR 0, 2 weeks `[A]`.

Ratings: difference High, desirability Low, plausibility Low. Outcome: **INVESTIGATE (lowest priority)**. Do not treat as a winner; it has no evidence.

## 4. Rejected, with the strong evidence

- Compliance-led refrigerant reclaim: no Indian mandate to recover or reclaim `[S10]`.
- Tyre pyrolysis: 270 units ordered closed by CPCB `[S28]`; also contested in the NGT. Date of that order is not clear (2019 article).
- DDGS fractionation plant: beyond the INR 5,00,000 default `[A]`.
- Resale of groundwater meters as a trading business: INR 19,000 to 31,000 listings from many sellers `[S3]`; at a 2% share, founder time (about INR 9.1 lakh `[I]`) exceeds margin on assumed margins `[A]` (see `01-hunt-B-payback.py`).

## 5. Missing information (not evidence of no demand)

- Rule texts: CGWA guideline (annual calibration, third-party ownership, approved meter list), CPCB tyre EPR schedule. Not opened.
- Price: current India R22; tyre EPR certificate; honey NMR fee; spice tolling; binder and mould cost.
- Demand: any buyer response to any idea. Demand evidence is L0 to L1 for all.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Notice on digital water flow meter installation | FAOLEX / UNEP | https://leap.unep.org/en/countries/in/national-legislation/notice-central-ground-water-authority-installation-digital-water | n/d | 2026-11-01 | Meter and telemetry requirement | search summary |
| 3 | Telemetry flow meter listings | Flowtech, IndiaMART | https://m.indiamart.com/flowtechinstruments/telemetry-flow-meter.html | n/d | 2026-11-01 | Meter prices, data fields | search summary |
| 4 | Flow meter calibration listings | IndiaMART | https://dir.indiamart.com/impcat/flow-meter-calibration.html | n/d | 2026-11-01 | Calibration prices | search summary |
| 5 | Lok Sabha answer AU1333 | Sansad | https://eparlib.sansad.in/bitstream/123456789/1470210/1/AU1333.pdf | n/d | 2026-11-01 | NOC count | search summary |
| 7 | Govt should cap charges of product testing: GTRI | Outlook Business | https://www.outlookbusiness.com/economy-and-policy/govt-should-cap-charges-of-product-testing-under-quality-control-order-gtri | 2026 | 2026-11-01 | QCO testing fees | search summary |
| 8 | BIS footwear circular | BIS | https://services.bis.gov.in/tmp/footwear_circular_for_BOs_bJF5_2021-02-26.pdf | 2021-02-26 | 2026-11-01 | Subcontract testing allowed | search summary |
| 9 | Footwear testing equipment listings | IndiaMART, TradeIndia | https://m.indiamart.com/advancetecho/footwear-testing.html | n/d | 2026-11-01 | Tester prices | search summary |
| 10 | Status and barriers in refrigerant management | CEEW | https://www.ceew.in/publications/status-barriers-in-refrigerant-management-activating-circular-economy-for-sustainable-cooling | 2023 | 2026-11-01 | No mandate; informal venting | search summary |
| 11 | R22 cost thread; customs seizure of R22 | NoBroker forum; Cooling Post | https://www.nobroker.in/forum/what-is-the-cost-of-r22-refrigerant | n/d | 2026-11-01 | R22 price (weak), seizure | search summary |
| 12 | Refrigerant recovery machine listing | TradeIndia | https://therefrigeration.tradeindia.com/value-vrr24l-1hp-refrigerant-recovery-machine-8404893.html | n/d | 2026-11-01 | Machine prices | search summary |
| 13 | Rubber stable mat listings | ExportersIndia, Aajjo | https://www.exportersindia.com/pune/rubber-stable-mats.htm | n/d | 2026-11-01 | Cow mat price and weight | search summary |
| 14 | Crumb rubber and tyre scrap listings | IndiaMART | https://m.indiamart.com/greenvitect-revolution | n/d | 2026-11-01 | Crumb prices | search summary |
| 15 | Handheld honey adulteration detection system (patent) | CSIR Technology Portal | https://techindiacsir.anusandhan.net/online/handheld-non-destructive-honey-adulteration-detection-system-and-method-IN202411019851-patent.htm | 2024 | 2026-11-01 | Prior art, 8% limit | search summary |
| 16 | How to export honey from India | Ximpex | https://ximpex.in/guides/how-to-export-honey-from-india | 2025 | 2026-11-01 | NMR mandate, cost, export value | search summary |
| 18 | Dabur launches mobile honey testing lab | Exchange4media | https://www.exchange4media.com/marketing-news/dabur-india-launches-country's-first-mobile-honey-testing-lab-68041.html | 2017 | 2026-11-01 | Prior art | search summary |
| 19 | Rice DDGS listings | IndiaMART | https://m.indiamart.com/impcat/rice-ddgs.html | n/d | 2026-11-01 | DDGS prices | search summary |
| 20 | India's soybean meal demand pressured by DDGS | CropGPT | https://cropgpt.ai/indias-soybean-meal-demand-pressured-by-rising-ddgs-output | 2025 | 2026-11-01 | Export unit values | search summary |
| 21 | Rice from FCI has cut biofuel dependence on maize | Informist | https://informistmedia.com/CommodityWire/39098/Rice-from-FCI-has-cut-biofuel-dependence-on-maize-says-ethanol-body-chief-Jain | n/d | 2026-11-01 | Distillery utilisation | search summary |
| 22 | Spice and steam sterilizer listings | TradeIndia, Aajjo | https://www.tradeindia.com/products/semi-continuous-steam-sterilizer-5895910.html | n/d | 2026-11-01 | Equipment prices and sizes | search summary |
| 23 | Spices Board EtO guidelines | Outlook Business | https://www.outlookbusiness.com/news/spices-board-formulates-comprehensive-guidelines-for-exporters-to-prevent-eto-contamination | 2024 | 2026-11-01 | Steam sterilisation guidance | search summary |
| 24 | Thermal storage firm receives USD 900,000 | Cooling Post | https://coolingpost.com/world-news/thermal-storage-firm-receives-900000-funding | n/d | 2026-11-01 | Inficold funding | search summary |
| 25 | Solar for cold storage ROI | Heaven Green Energy | https://www.heavengreenenergy.com/blog/solar-for-cold-storage-roi | n/d | 2026-11-01 | Blended HT tariff INR 7 to 9 per kWh (vendor blog) | search summary |
| 28 | CPCB orders closure of 270 tyre pyrolysis units | Daily Pioneer | https://www.dailypioneer.com/2019/india/cpcb-orders-closure-of-270-tyre-pyrolysis-units.html | 2019 | 2026-11-01 | Pyrolysis closures (stale) | search summary |
| 29 | The separation equation | ACHR News | https://achrnews.com/articles/107668-the-separation-equation | n/d | 2026-11-01 | Blend separation limit | search summary |
