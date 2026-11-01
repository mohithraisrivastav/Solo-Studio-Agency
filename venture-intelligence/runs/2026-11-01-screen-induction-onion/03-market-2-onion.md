# Market investigation 2: onion storage ventilation retrofit (thesis T2)

Date: 2026-11-01. Investigator: Buyer and Market Investigator. Scope: decide whether the lead deserves any further investment. All sources below were seen as search summaries only. WebFetch failed on every host I tried (icar.org.in, rsdebate.nic.in, freshplaza.com, seedfund.venturecenter.co.in: "host not resolvable in this session"). I opened no page. About 19 searches used; I stopped early because the deciding questions (A1, A2, B6, C7) returned a clear picture. The model is in `03-onion-model.py` and `econ-in.json` / `econ-in-45k.json` / `econ-out.txt` in this folder.

## 1. Claims tested

| # | Claim (hunter, unverified) | Result | Tags |
|---|---|---|---|
| 1 | Onion storage losses are about 30 percent in 2026 | Partly. Losses of 30-46% over 4 months are normal in ordinary structures; ICAR reports 42% for a low-cost structure and 46% for bottom and side ventilated over four months [S1]. The 2026 "30%" is a news figure I did not re-check [K, from hunter file]. | [S1] |
| 2 | Forced ventilation trial results are mixed | Supported. Lower rot but more weight loss in a one-month Indian trial (9% vs 7% weight loss) [S8]; lower weight loss in a 90-day abstract (about 25% vs 34-35%) [S9]; Egyptian trial favoured natural ventilation on net return [S10]. | [S8][S9][S10] |
| 3 | No retrofit kit exists | Contradicted in part. Godaam retrofits warehouses and improves ventilation and installs sensors, reported at about 1,000 locations (vendor-sourced) [S7]. No fan-and-humidity-controller kit with a published price was found. | [S7] |
| 4 | Buyer keeps the saving | Partly. Owner keeps weight saved, but onion price swings (Rs 550 to Rs 5,100 per quintal inside 2026) decide whether storage pays at all [S16]. | [S16] |
| 5 | Subsidy rules do not block a retrofit | Unknown. Subsidy covers a prescribed structure at Rs 10,000/MT, 50% [S2][S3]. I did not find whether add-on equipment qualifies. | [S2][S3] |
| 6 | A founder can profit with Rs 5,00,000 | Not supported at kit prices the buyer's value allows (section 7). | [I] |

## 2. Buyer segments

- Farmers who store rabi onion 4-8 months in their own kanda chawl or shed, typically 5-25 t [S6][S2]. A 25 MT unit is the subsidy unit [S2]. Count of such farmers: not found after 3 searches (queries: "farmers store rabi onion percentage Maharashtra survey", "how many farmers store onions chawl", "onion storage adoption farmers number") [A]. Maharashtra built 42,282 low-cost structures totalling 9.65 lakh tonnes, an average of about 23 t per structure [S19][I].
- Maharashtra held 21 lakh MT of about 50 lakh MT rabi stored nationally in one NHB report [S25] (2018, stale, via search summary).
- FPOs: often lack storage and processing facilities [S20]; farmers allege the FPO procurement model is flawed [S20]. Not a verified paying segment.
- Traders and exporters: use warehouses and cold stores, not farm sheds [K]. Not investigated further.
- Government agencies (NAFED, NCCF, CWC) hold buffer stock; onions rotted at a CWC godown in Lasalgaon in 2026 [S24]. They buy through tenders, not kits [I].

## 3. Buying process and trigger

- Trigger: a bad season with rot in storage (rain in 2026) [S24]. Decision to build or retrofit comes before the March-April harvest [K]. Decider and payer are the same person, the farmer [I].
- Subsidy applications run on a state calendar: West Bengal MIDH 2026-27 window 06/08/2026 to 31/08/2026 [S4]. That channel funnels farmers to the standard structure, not a retrofit [I].
- Trust: farmers copy neighbours, KVK and DOGR advice [K, not checked]. Not tested.

## 4. Current alternatives and their prices

A1. Technologies tested by research bodies (all via search summary):

| Technology | Who | Loss measured | Scale | Note |
|---|---|---|---|---|
| Low-cost thatched bamboo structure | ICAR-DOGR | up to 42% in 4 months | not stated | [S1] |
| Bottom and side ventilated structure | ICAR-DOGR | up to 46% in 4 months | not stated | [S1] |
| Ventilated storage, no control | ICAR table | 54.89% total | not stated | [S1] |
| Bulk storage, Rajgurunagar | ICAR table | 54.64% | not stated | [S1] |
| DOGR cold storage | ICAR table | 7.14% | not stated | [S1] |
| 0 deg C cold storage | ICAR table | 5.00% | not stated | [S1] |
| Kanda chawl | literature | 40-42% in 4 months | 5-10 t | [S6] |
| NHRDF racking model | NHRDF, tested at a KVK | 40.94% over 180 days (hanging: 38.37%) | room 50 q | [S6] |
| Knock-down steel-pipe store | ICAR journal paper | 8-10% claimed | 30 t, about Rs 50,000 | [S13] |
| Evaporative-cooled on-farm store | 2026 paper (source attribution uncertain) | net profit Rs 6,021/t vs Rs 2,553/t, May-Sept | not stated | [S12] |
| Integrated curing and storage structure | IIT Bombay RuTAG | goal 80-90% loss cut; no data | not stated | [S11] |

I could not see original DOGR, NHRDF or IIT Bombay reports. The dates, trial scale and validators of the ICAR table are not shown in the summary. The ICAR page is a secondary summary [S1]. Confidence in these loss numbers: low to medium. I did not find sprout suppressant (maleic hydrazide), irradiation or solar-powered results in this run (not checked).

A2. Products sold in India:

| Product | Maker | Price | Date | Status |
|---|---|---|---|---|
| Godaam Sense (IoT sensors) plus ventilation retrofit | Godaam Innovations, Nashik | not found | claims to 2025-26 | active; reports 15-20% average loss cut, 25-30% in hard conditions, about 1,000 sites (vendor claims) [S7] |
| Agronest smart warehouse | Tata Steel Nest-In | not found | 2020 launch (hunter file) | status unknown |
| Standard low-cost 25 MT chawl, subsidised | Farmer-built under MIDH | cost norm Rs 10,000/MT (Rs 2.5 lakh per 25 MT), 50% subsidy = Rs 1.25 lakh [S2][S3] | Feb 2025 | active; 2026-27 notices issued [S4] |
| 2000 MT onion cold store | Ahata Industries listing | Rs 1,51,32,657 (about Rs 7,566/t capacity) [S14][I] | undated | listing |
| Solar cold storage promotion | Maharashtra government | no figures | Aug 2025 | promoted [S15] |
| Ergos (grain, farm-gate warehouses) | Ergos | n/a | Series B about US$10M | active, not onion-specific [S18] |

Disconfirming search for shutdowns (Godaam, Agronest, Ergos): no closure found in 1 search, but coverage is old [S18]. Not found after 3 searches: a priced fan-and-controller retrofit kit for chawls (queries: "onion storage ventilation fan controller India startup", "onion storage solution India retrofit chawl kit aeration price", "Godaam Sense price"). A student-grade IoT design with DHT22 and ESP32 exists, aiming for 15-20% spoilage vs 40-45% [S22]; it is a paper, not a product.

## 5. Competitor map, including failed and closed entrants

- Direct: Godaam (sensors plus ventilation retrofit, pilot with DOGR in 2018, funded Rs 3 lakh by DOGR centre) [S7]. Founded 2018, raised about US$100,000 [S18]. After 8 years it reports about 1,000 sites [S7]; that is roughly 125 per year if true [I]. That is the closest existing entrant and the number is a ceiling for what a small team sells.
- Government standard structure (free-ish, subsidised) [S2].
- Substitutes: cold storage (about 5-7% loss) but rent is high [S1][S13].
- Failed or closed entrants: none found. Gap noted.

## 6. Willingness-to-pay signals

- Farmers already pay for structures: 42,282 subsidised structures in Maharashtra [S19]. Weak L1 for storage spend.
- Spend on retrofit or control: none found beyond Godaam's installed-base claim (unverified, price unknown) [S7].
- Storage often loses money: spring 2026 average about Rs 1,250/q against cost about Rs 1,800/q [S16]. Net profit of storage in a 2026 paper was Rs 2,553/t for a traditional store [S12]. Per quintal that is Rs 255.

## 7. Bottom-up market size and economics (C7)

Size by terms: buyers x frequency x price.
- Buyers: about 43,000 subsidised structures in Maharashtra [S19] is an upper bound for active sheds [A: some are unused or rebuilt]. A reachable share in 3 years of 1-3% [A, no source].
- Frequency: one purchase per shed, a single season per year [K].
- Price: Rs 25,000-45,000 incl. GST [A].
- Result: 400-1,300 kits over 3 years, Rs 1-6 crore total revenue [I]. Not computed against any sourced adoption rate, because none exists.

Buyer value per season (25 t shed [S2], `03-onion-model.py`). Assumptions: loss cut of 3, 5 or 10 points [A, from mixed trials: S8 shows more weight loss, S9 shows about 9 points less, so any value from negative to 10 is plausible]; price at sale Rs 1,000, 2,000 or 4,000 per quintal [S16 range: Rs 550-5,100 inside 2026].

| Loss cut [A] | Rs 1,000/q [A] | Rs 2,000/q [A] | Rs 4,000/q [A] |
|---|---|---|---|
| 3 points | 7,500 | 15,000 | 30,000 |
| 5 points | 12,500 | 25,000 | 50,000 |
| 10 points | 25,000 | 50,000 | 100,000 |

(Rs per season [I].) Simple payback at Rs 25,000 kit: 0.2 to 3.3 seasons; at Rs 40,000: 0.4 to 5.3 seasons [I]. To pay back in one season at Rs 30,000, a farmer needs a cut of 12 points at Rs 1,000/q, 6 at Rs 2,000, 3 at Rs 4,000 [I]. A real, measured cut in India is 5-10 points at best [A]; Godaam's own average claim is 15-20% [S7] and it relies on sensors and retrofits, not fans alone.

Seller economics (`econ-in.json`, all inputs [A]): kit price Rs 30,000 incl. 18% GST (Rs 25,424 ex-GST [I]); materials Rs 14,000, install transport Rs 2,500, warranty reserve Rs 2,000; 10% channel fee; CAC Rs 3,000; 12 founder hours per unit; one-time Rs 1.2 lakh for a prototype and paired-bay trial. Result at 8 units a month: contribution Rs 146 per unit; founder earns about -Rs 36 per hour; peak cash Rs 7.4 lakh, above the Rs 5 lakh; no cash payback in 24 months [I]. At Rs 45,000 (`econ-in-45k.json`): contribution Rs 10,969 per unit, founder earns about Rs 601 per hour at 8 units/month, peak cash Rs 4.6 lakh [I]. But 8 units a month for 12 months is 96 kits a year, and this market sells in one pre-harvest window [K], so the model overstates sales rhythm; and at Rs 45,000 the buyer payback is 1.8 seasons at 5 points and Rs 2,000/q, 3.6 seasons at Rs 1,000/q [I]. The two requirements do not meet: the price a seller needs is more than a farmer's value supports in a normal year.

Policy and price risk: export ban Dec 2023 to May 2024; ban lifted with duty and minimum price; 20% duty removed 1 April 2025 [S17]. Government procurement and buffer sales also cap price. Year-on-year WPI for onion fell 66% in October 2025 and 42% in March 2026 [S16]. A one-season-per-year product with a payback tied to such a price is unfinanceable for small farmers [I]. I found no 2026 stock-limit rule; not checked.

## 8. Reasons buyers would not switch

- The subsidised standard structure is free to half-free: the farmer pays Rs 1.25 lakh on a 25 t structure and gets 50% back [S2][I]. Subsidy is for the prescribed structure; whether a fan add-on qualifies: not found [unknown]. A kit sold outside the subsidy is an extra cost on top.
- Mixed trial results: forced air can raise weight loss [S8][S10], so the buyer risk is real [I].
- Curing and pre-harvest practice cut rot and raised profit 40-50% in a West Bengal study [S23], at near-zero cost [I]. That is a cheaper alternative with the same objective.
- Godaam already occupies the "tech for onion shed" space with DOGR links [S7].
- Credit, after-sales service across dispersed villages, and one sales window per year [I, no source on credit or service found].
- Price crash years: farmers sell at or below cost and storage itself loses money [S16].

## 9. Demand verdict

(a) Problem spend: weak L1. Farmers do spend on storage structures (42,282 in Maharashtra [S19]), and losses are large [S1]. Confidence medium.
(b) Solution-type demand for a retrofit fan-and-humidity kit: unknown, leaning weak. Only Godaam shows paid sensor/retrofit demand, unpriced and vendor-claimed [S7]. No measured benefit from a controlled fan system in an Indian chawl. Confidence low.

## 10. Cheapest credible demand test

Not recommended, because the verdict is reject. If the Director overrides [A]: ask Godaam's published contact for a price list (not a purchase), ask one KVK/DOGR scientist whether a MIDH subsidy covers add-on ventilation, and ask 10 Nashik farmers who store 20+ t what they would pay for a guaranteed 5-point cut. Success: 6 of 10 say they would pay Rs 25,000 or more before they hear the price [A]. Cost: about Rs 5,000 travel, 3 days [A]. I do not contact anyone.

## Existing solutions comparison

| Solution | Cost per t capacity | Loss measured | Install | Power | Skill | Adoption |
|---|---|---|---|---|---|---|
| Kanda chawl (traditional) | about Rs 6,000-10,000 [S2][S5] | 40-42% in 4 months [S6] | farm build | none | low | most farms [I] |
| MIDH 25 MT low-cost structure | Rs 10,000 norm; farmer net Rs 5,000 after subsidy [S2][I] | 42-46% (ICAR) [S1] | farm build | none | low | 42,282 in Maharashtra [S19] |
| ICAR knock-down steel-pipe | about Rs 1,667 (Rs 50,000 / 30 t) [S13][I] | 8-10% claimed [S13] | farm assemble | none | low | not found |
| NHRDF racking room | Rs 100/q (Rs 50,000 / 50 q) [S6][I] | 40.94% (180 days) [S6] | farm build | none | low | not found |
| Forced-air fans plus controller (proposed) | Rs 1,000-1,800 per t if Rs 25,000-45,000 / 25 t [A] | unproven in India: mixed [S8][S9][S10] | on-site | 130 W solar fans [hunter file, not re-checked] | medium | none |
| Godaam sensors plus retrofit | not found | 15-20% avg, vendor claim [S7] | on-site | low | low for user | about 1,000 sites, vendor claim [S7] |
| Cold storage | about Rs 7,566 (Ahata listing) [S14][I] | 5-7% [S1] | large | grid | high | big traders [I] |

## Buyer's three questions

1. WHY would a farmer, FPO or trader buy this? Partly supported. Losses of 40%+ are documented [S1][S6] and the farmer keeps the saving on own stock [I]. But the saving depends on price and on an unproven loss cut [S8][S9][S16]. Tags: [S1][S8][S16][I].
2. WHY this over existing options, including the free or subsidised shed? Not supported. The subsidised structure costs the farmer about Rs 1.25 lakh net [S2][I]; curing practice is cheaper [S23]; Godaam is already present [S7]. No evidence a controlled-fan kit beats natural ventilation in an Indian chawl [S8][S10]. Tags: [S2][S7][S23].
3. WHY financially attractive for a founder with Rs 5,00,000 and Rs 750/hour? Not supported. At a price the buyer's value supports (Rs 30,000) the founder earns negative per hour and needs Rs 7.4 lakh [I]. At Rs 45,000 the buyer payback is 1.8 to 3.6 seasons at modest loss cuts [I]. One season a year, volatile prices and policy risk [S16][S17]. Tags: [I][A].

## Verdict

Reject. Rationale: (1) a priced competitor with DOGR ties already sells sensor-plus-ventilation retrofits [S7]; (2) forced ventilation results are mixed, so the benefit is unproven [S8][S9][S10]; (3) the only price at which the seller earns near Rs 750/hour makes buyer payback 2-4 seasons in a market where onion has traded at Rs 550-5,100 per quintal within a year [S16][I]. Hold reopens only if a primary source shows a controlled-fan retrofit cutting loss by 10+ points in a real Indian chawl and the subsidy covers it. Confidence: medium on the reject; low on the underlying loss numbers (secondary summaries).

Not checked: sprout suppressants, irradiation, solar options beyond one news item, current stock-limit rules, original DOGR/NHRDF/IIT Bombay reports, MIDH operational guideline text, Godaam price.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Onion Cold Storage - Potential to Stabilize Price Fluctuation | ICAR | https://icar.org.in/en/node/4701 | not shown | 2026-11-01 | DOGR loss table | search summary |
| 2 | Parliamentary answers on MIDH low-cost onion storage (Feb 2025 Lok Sabha; Rs 10,000/MT, 50%, 25 MT) | Lok Sabha / Rajya Sabha | https://eparlib.sansad.in/bitstream/123456789/2988653/1/AS115_nHs2eW.pdf | 2025-02 | 2026-11-01 | subsidy norm (exact document carrying the Rs 10,000 quote not confirmed; also Rs 1.75 lakh older norm) | search summary |
| 3 | 50 percent subsidy for onion warehouses | CMV360 | https://www.cmv360.com/news/50-percent-subsidy-for-onion-warehouses-apply-now-for-benefits | 2025-02 | 2026-11-01 | revised unit cost | search summary |
| 4 | Notice: MIDH 2026-27 low cost onion garlic storage 25 MT | Murshidabad district | https://murshidabad.gov.in/notice/advertisement-regarding-online-application-for-construction-of-low-cost-onion-garlic-storage-structure-25-mt-under-midh-2026-27-in-the-district-website-of-murshidabad/ | 2026-08 | 2026-11-01 | scheme active, window | search summary |
| 5 | WB directorate cost table (Rs 8,000/MT, 50%) | WB FPI&H directorate | https://wbfpih.wb.gov.in/assets/user_uploads/directorate_fpi/1334278438_1784265925.pdf | not shown | 2026-11-01 | state cost norm | search summary |
| 6 | On-farm storage of onion for enhancing income; 180-day storage study | KVK (kiran.nic.in); serialsjournals | https://kiran.nic.in/Enchancing_income.html ; https://serialsjournals.com/abstract/39902_32.pdf | not shown | 2026-11-01 | NHRDF racking, kanda chawl losses | search summary |
| 7 | Godaam Innovations coverage (Better India; CMB IoT cuts onion storage losses; Freshplaza sponsored) | various | https://www.thebetterindia.com/240698/onion-price-rise-costly-warehouse-storage-research-iot-sensors-woman-entrepreneur-nashik-ros174/amp/ ; https://commodity-board.com/iot-cuts-onion-storage-losses-as-indian-prices-edge-higher | 2020-2026 | 2026-11-01 | competitor, claims, 1,000 sites | search summary |
| 8 | Vigyan Ashram forced vs natural ventilation trial | Google Doc export | https://docs.google.com/document/d/1zsQ4sItuTJs_iNV6AXHfDVlCDtoDRQRT/export?format=pdf | not shown | 2026-11-01 | 9% vs 7% weight loss | search summary |
| 9 | Forced vs natural ventilation 90-day study abstract | Scinapse | https://www.scinapse.io/papers/4298008407 | not shown | 2026-11-01 | 25% vs 34-35% | search summary |
| 10 | Effect of storage conditions on onion bulbs (Egypt); Korean study | Mansoura J. Agric. Eng.; Korea Scholar | https://mjae.journals.ekb.eg/article_98928.html ; https://db.koreascholar.com/Article/Detail/40835 | not shown | 2026-11-01 | natural ventilation better net return; rot rates | search summary |
| 11 | Integrated curing and storage structure for onions | IIT Bombay RuTAG / India S&T portal | https://www.indiascienceandtechnology.gov.in/technologies/design-and-development-integrated-curing-and-storage-structure-onions | not shown | 2026-11-01 | goal only | search summary |
| 12 | Evaporative-cooled onion store net profit (source attribution uncertain, one of the results of the IIT Bombay query) | ijabe / other | https://ijabe.org/index.php/ijabe/article/view/10215 | 2026 per summary | 2026-11-01 | Rs 6,021 vs 2,553 per t | search summary |
| 13 | Knock-down steel-pipe onion store; Indian J. Horticulture | ICAR e-pubs | https://epubs.icar.org.in/index.php/IndHort/article/download/126543/51056/472746 | not shown | 2026-11-01 | Rs 50,000, 8-10% | search summary |
| 14 | 2000 MT onion cold storage listing | Ahata Industries | https://ahata.aajjo.com/product/mushroom-cold-storage-plant-5-chamber-35-bags-35-40-ton | undated | 2026-11-01 | Rs 1.51 crore listing | search summary |
| 15 | Solar-powered cold storage for Nashik onion farmers | Free Press Journal | https://www.freepressjournal.in/pune/nashik-solar-powered-cold-storage-offers-new-hope-for-onion-farmers | 2025-08 | 2026-11-01 | promotion, no cost | search summary |
| 24 | Rotten onions at Lasalgaon CWC godown | Free Press Journal | https://www.freepressjournal.in/pune/nashik-rotten-onions-worms-and-maggots-found-at-lasalgaon-cwc-godown-questions-raised-over-storage | 2026 | 2026-11-01 | state storage failure | search summary |
| 16 | Onion prices crash below cost (Rural Voice, Apr 2026); price reports (FPJ) | Rural Voice; Free Press Journal | https://eng.ruralvoice.in/onion-prices-crash-below-cost-amid-export-disruptions-farmers-seek-subsidy-boost-govt-support ; https://www.freepressjournal.in/pune/nashik-onion-rotting-in-storage-sheds-as-rainfall-hits-quality-lasalgaon-prices-touch-4051quintal | 2026 | 2026-11-01 | price range, WPI falls, cost | search summary |
| 17 | Onion export duty cut to nil 1 Apr 2025; export ban lifted | worldtradescanner; Freshplaza | https://worldtradescanner.com/Ntfn%2019-22.03.2025.htm ; https://www.freshplaza.com/asia/article/9623603/onion-export-ban-lifted-in-india-amid-elections/ | 2024-2025 | 2026-11-01 | policy timeline | search summary |
| 18 | Ergos funding; Godaam funding | Inc42; trysignalbase | https://inc42.com/?p=416786 ; https://www.trysignalbase.com/news/funding/empowering-farmers-and-reducing-crop-wastage-godaam-innovations-secures-100k-in-pre-seed-funding-for-agritech-solutions | not shown | 2026-11-01 | active status, funding | search summary |
| 19 | Stabilising onion price (42,282 structures, 9.65 lakh t) | Shankar IAS Parliament | https://www.shankariasparliament.com/blogs/pdf/stabilising-onion-price | not shown | 2026-11-01 | adoption count | search summary |
| 25 | Monthly onion reports | NHB | https://www.nhb.gov.in/statistics/Reports/OnionJune2018.pdf | 2018 | 2026-11-01 | state share stored (stale, over 18 months) | search summary |
| 20 | Too many onions, too little value; FPO procurement complaint | Business India; Free Press Journal | https://businessindia.co/magazine/focus/too-many-onions-too-little-value | not shown | 2026-11-01 | FPO storage gap | search summary |
| 22 | Low-cost ESP32 IoT onion storage system | arXiv 2601.10745 | https://arxiv.org/abs/2601.10745 | 2026-01 | 2026-11-01 | academic design only | search summary |
| 23 | Pre-harvest and curing study, West Bengal; Ahmednagar storage study | serialsjournals / journal.jsure | https://journal.jsure.org.in/index.php/jas/article/download/680/553 | not shown | 2026-11-01 | curing alternative, 40-50% profit | search summary |
