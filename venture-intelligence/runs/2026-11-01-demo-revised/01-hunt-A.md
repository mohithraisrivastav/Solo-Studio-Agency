# Hunt A: money wasted (Opportunity Hunter, 2026-11-01)

Verdict: zero theses kept. Six candidates were tested and each failed at least one of the buyer's three questions. The near-misses and the evidence that would revive them are listed in section 4.

Deciding questions, written before searching:
- Marine fisheries: Is on-boat spoilage large enough to pay for a fix, is ice a big cost, do subsidies already cover boxes, and who keeps the saving?
- Poultry (eggs, broilers): Is breakage or shrinkage measured in India, and who bears it?
- Port and container logistics: Who pays detention, can the buyer avoid it, and does a tool already exist?
- Industrial steam: Is trap leakage measured, and do equipment makers already sell surveys and monitoring?
- Road freight tyres: Does the loss pay back a sensor on a small fleet, and who already sells one?
- Returnable packaging (milk crates): Is the loss rate independently measured, and is there an incumbent tracker?
- Spice export compliance: Is there a gap that a small firm can fill with a steriliser or toll service?

## 1. Industries chosen and why

Chosen from the money-wasted lens, outside the excluded list. Searches used: about 38 of 45.

| Industry | Why it might hide an opportunity now |
|---|---|
| Marine fisheries post-harvest | Reported national post-harvest loss near 20% of production, inland and marine combined [S1]. The scheme PMMSY funds ice boxes and cold-chain items [S21]. |
| Road freight (truck tyres) | Tyres are 10 to 18% of vehicle operating cost by one vendor's figure [S12]. A 20% underinflation is reported to cut tyre life by 30% [S12]. |
| Port and container logistics | Exporters complained about detention billing in April 2026 and DG Shipping met stakeholders on 17 April 2026 [S8]. |
| Dairy returnable packaging | A vendor claims about a quarter of India's milk crates are lost each year [S13]. |
| Industrial steam | Vendor audits claim 20 to 30% of steam traps waste steam [S5]. |
| Poultry logistics | Transport shrinkage of 2.36 to 3.01% and mortality of 0.43 to 0.53% per broiler truck in Chennai [S19]. |
| Spice export compliance | The ethylene oxide scare of 2024 led the Spices Board to push steam sterilisation [S15]. |

## 2. Raw candidates

| # | Problem | Payer | Signal | Tag |
|---|---|---|---|---|
| 1 | Fish spoilage on small boats and at landing | Boat owner | Traditional-sector loss of 4.30% at landing centres in one pilot [S1] | [S1] |
| 2 | Ice cost on mechanised boats | Boat owner | Ice bar at Rs 140 to Rs 150 and up to Rs 5,000 a day per boat in one report [S3] | [S3] |
| 3 | Steam trap leakage in SME plants | Plant owner | Vendor claim of 20 to 30% failed [S5] | [S5] |
| 4 | Container detention and demurrage | Importer, exporter | Exporters allege non-transparent billing [S8] | [S8] |
| 5 | Underinflated truck tyres | Small fleet owner | 30% life loss at 20% underinflation [S12] | [S12] |
| 6 | Lost milk crates | Dairy | Vendor claim of a quarter lost a year [S13] | [S13] |
| 7 | Egg breakage in transport | Trader | Damaged eggs sold cheap to stalls [S18] | [S18] |
| 8 | Broiler transport shrinkage and death | Trader, integrator | 2.36 to 3.01% shrinkage [S19] | [S19] |
| 9 | Spice sterilisation for small exporters | Exporter | Toll rate of Rs 15 to 25 per kg from an unsourced blog [S16] | [S16] |
| 10 | Rice mill yield loss | Miller | Rubber-roll mills give 2 to 3% more out-turn than emery mills [S23] | [S23] |
| 11 | Cutting-fluid waste in machine shops | Shop owner | No India data found | [A] |

## 3. Opportunity theses

None kept. The tests below show why the best four did not survive. Python output is in `runs/2026-11-01-demo-revised/payback_A.py`.

### 3.1 Truck tyre pressure monitoring for small fleets (physical product): cut

- Load-bearing assumption: a sensor pays back for a 1 to 5 truck owner. Primary source check: not reached. The only tyre-life figure is a vendor-quoted TMC number, which is a proxy for US trucks [S12].
- Existing solutions:

| Product | Maker | Price | Date | Does | Misses |
|---|---|---|---|---|---|
| TREEL sensors | JK Tyre | Not found | n/d | Pressure and temperature, fleet dashboard, pilot with fleet owners [S10] | Price unknown |
| Kawach | Fleeca | Not found | n/d | Rim-mounted pressure, temperature, alignment [S24] | Price unknown |
| Tyremate | Manatec | Rs 14,999 listed | n/d | Solar display, tubeless sensors, 6 sensors per pack [S11] | Seller listing, not a quote |
| Generic 6-sensor kit | Unbranded | Rs 6,090 listed | n/d | Wireless solar monitor [S11] | Quality unknown |

- Prior-art searches: four (queries: "truck TPMS India price small fleet", "Apollo Tyres JK Tyre TPMS fleet solution", "Fleeca Kawach") plus the two tyre-cost searches above. Not run: other countries and government schemes.
- Cheapest rival: a Rs 6,090 imported kit [S11] and a hand gauge with a driver routine [K].
- Buyer payback from the script: with Rs 1,20,000 a year of tyre spend [A], 20% of life run underinflated [A], 70% recovered [A], the value is Rs 5,040 a year [I]. Payback is 14.5 months on a Rs 6,090 kit and 35.7 months on a Rs 14,999 kit [I]. At Rs 60,000 spend and 10% underinflation it is 58 to 143 months [I]. The result swings on assumed tyre spend and driver behaviour, so it is weak.
- Buyer's three questions: why buy, partly supported (loss exists, size unverified); why this one, not supported (tyre makers own the channel and Rs 6,090 kits exist [S10][S11]); why a small firm earns money, not supported (hardware margin on a Rs 6,090 retail item with a distribution fight against tyre makers [I]).
- Verdict: cut. The Apollo TPMS note suggests the largest tyre maker was still seeking a hardware partner at an unknown date, which is the only opening seen [S10], and it is not enough.

### 3.2 Dairy crate tracking (physical product with tag): cut

- Load-bearing assumption: the annual crate loss is near a quarter. Primary source check: failed. The only India figure is from the vendor Prompt Dairytech [S13]. Label: `UNVERIFIED KILLER`. A dairy logistics head could answer in one call.
- Existing solutions: Prompt TrackSure is a patented tag-in-crate system claimed to serve India's largest dairies, with no named customer found [S13]. LEAP India and others pool returnable packaging [S25].
- Prior-art searches: 4 (queries: "milk crates missing dairy India", "milk crate price India", "Aavin Sudha Nandini crates missing", "Prompt Dairy Tech crate management").
- Crate price: Rs 225 to Rs 380 per crate on seller listings [S14].
- Cheapest rival: a deposit or an agent-level count, which no source shows in use in India. Not found after 2 searches (queries: "dairy crate deposit distributor Mother Dairy Amul", "Aavin crates missing").
- Buyer payback from the script: for a 20,000-crate fleet with an assumed Rs 40 tag and Rs 3 lakh of readers [A], payback is 11.6 to 195.6 months depending on loss between 5% and 25% [I]. Only the vendor's 25% claim with a 60% cut and a Rs 380 crate gets under 24 months [I].
- Buyer's three questions: why buy, partly (loss real but unmeasured); why this one, not supported (patented incumbent [S13]); why a small firm earns money, not supported (crate makers earn from replacement [K]).
- Verdict: cut.

### 3.3 Small-boat insulated boxes and ice (physical): cut

- Load-bearing assumption: spoilage on small boats is large and unsubsidised. Primary source check: partial. A pilot study puts mechanised-boat loss at 0.18 to 0.41% and the traditional sector at 4.30% at landing [S1]. The 20% national figure mixes inland and marine fish [S1].
- Subsidy: PMMSY already funds ice boxes, fish holding boxes and vehicles with ice boxes [S21]. State listings show 40% general and 60% for women and SC/ST on those items [S2]. The state listings are secondary and cover transport items, not boat holds. Not verified against the scheme guidelines.
- Ice is a small share of trip cost: Rs 20,000 of ice against about Rs 3 lakh of diesel on one 20-day trip account [S3].
- Commission agents take 5 to 10% of sales, and Kerala caps auction commission at 5% [S4]. The saving would be shared with agents and the boat owner.
- Prior-art searches: 5 (queries: "India marine fishing boats post-harvest loss ice insulated", "PMMSY insulated fish box subsidy", "fishing boat ice consumption cost", "fish landing centre auction commission", "pib PMMSY fishing vessels insulated holds"). Failed attempts not found.
- Cheapest rival: subsidised box at 40 to 60% off [S2].
- Buyer payback from the script: Rs 12,000 box [A], Rs 3 lakh a year catch [A], half the 4.3% loss avoided [A]; 22.3 months unsubsidised, 13.4 months subsidised [I]. Under a subsidy, the entrant sells into a state scheme.
- Buyer's three questions: why buy, partly; why this one, not supported (subsidy and existing box makers [S21]); why a small firm earns money, not supported (state scheme buyers, tender cycles [I]).
- Verdict: cut.

### 3.4 Container detention tracking (service): cut

- Load-bearing assumption: importers and exporters pay avoidable detention that software can prevent. Primary source: the Supreme Court rule as summarised by a law firm says waivers apply only where customs caused the delay by unlawful action [S9]. That limits avoidable cost to the buyer's own delay.
- Existing: Cogoport shows free days, terms and alerts for free-day expiry [S7]. No per-shipment price found after 1 search for pricing.
- Daily rates of Rs 3,000 to Rs 8,000 come from a vendor blog and are not a tariff [S7].
- Prior-art searches: 4 (queries: "container detention charges India importers", "detention demurrage management software India", "customs holds detention waiver", "Emirates Line India detention tariff").
- Why unsolved: category (e) with a policy angle. DG Shipping met stakeholders on 17 April 2026 and I did not verify the outcome [S8].
- Buyer's three questions: why buy, partly; why this one, not supported (Cogoport and forwarders already alert [S7]); why a small firm earns money, not supported (software that forwarders can copy in a product cycle [I]).
- Verdict: cut. This is a service close to consulting and builds no asset.

## 4. Cut candidates and reasons

| # | Candidate | Reason cut |
|---|---|---|
| 1 | Fish spoilage | Subsidised boxes, small measured loss, agent share. See 3.3. |
| 2 | Ice cost | Ice is a small share of trip cost [S3]. |
| 3 | Steam trap monitoring | Forbes Marshall already sells trap monitors and a trap management service [S5]. Spirax, TLV and others sell surveys. Failure-rate figures are vendor-sourced [S6]. |
| 4 | Container detention | See 3.4. |
| 5 | Truck TPMS | See 3.1. |
| 6 | Milk crates | See 3.2. |
| 7 | Egg breakage trays | No Indian breakage rate found after 3 searches (queries: "egg breakage transport India percent", "egg transport damage India trays", "Namakkal breakage allowance"). Cracked eggs resell at a discount [S18], so the loss is partial. Not verified further. |
| 8 | Broiler transport | Shrinkage 2.36 to 3.01% and mortality 0.43 to 0.53% in one Chennai study [S19]. Fixes are low-cost handling advice such as stocking density and pre-feeding [S20]. No product payer. |
| 9 | Spice steam sterilisation | Spice parks already offer steam sterilisation at 500 kg per batch [S16]. Steriliser listings run near Rs 10 to 12 lakh, above the Rs 5,00,000 capital [S17]. EU alerts on Indian foods reportedly fell after mandatory testing began in 2022 [S22]. The toll price is unsourced [S16]. |
| 10 | Rice mill yield | Rubber-roll mills already deliver the gain [S23]. FCI out-turn rule not verified after 1 search, so no saving can be built. |
| 11 | Cutting-fluid recycling | No India disposal cost or rule found after 1 search. Only UK benchmarks seen, not valid for India. |

## 5. What I did not check

- Primary rules for PMMSY vessel holds, FCI out-turn ratio, Spices Board toll terms, and CPCB waste-emulsion rules.
- Prices from Fleeca, JK Tyre and Prompt. Quotes needed.
- Any buyer interview. Demand evidence stays at L0 to L1 for everything here.
- Failed-startup post-mortems for tyre sensors and crate trackers. None found.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Post harvest losses in marine fisheries (CIFT pilot; parliamentary figure) | ICAR-CIFT and others | https://drs.cift.res.in/bitstreams/ad3a50de-5289-46fc-ae4c-5275f57aca14/download | n/d | 2026-11-01 | Boat and landing loss rates | search summary |
| 2 | PMMSY ice box vehicle listings, Gujarat | startup-gujarat mirror | https://startup-gujarat.pages.dev/schemes/pmmsy-three-wheeler-with-ice-box-including-e-rickshaws-for-fish/ | n/d | 2026-11-01 | Subsidy rate on ice-box items | search summary |
| 3 | Thoothukudi boats anchored due to ice bar price hike; trip cost accounts | DT Next; ICSF | https://www.dtnext.in/news/tamilnadu/thoothukudi-boats-anchored-due-to-ice-bar-price-hike-800262 | n/d | 2026-11-01 | Ice price and share of trip cost | search summary |
| 4 | Fish auction commission; Kerala Act 16 of 2021 | MBAI; India Code | https://www.indiacode.nic.in/bitstream/123456789/21056/1/act_16_of_2021-engfinal.pdf | 2021 | 2026-11-01 | Commission 5 to 10%, Kerala cap | search summary |
| 5 | Forbes Marshall Trap Monitoring System | Forbes Marshall | https://www.forbesmarshall.com/BlogDetails/Blog/WirelessSteamTrapMonitoringSystem | n/d | 2026-11-01 | Incumbent steam trap monitoring, 20 to 30% claim | search summary |
| 6 | Steam trap failure rate statistics | Reliabilityweb | https://reliamag.com/topics/guides/steam-trap-failure-rate-statistics | n/d | 2026-11-01 | Failure-rate benchmarks, mostly non-India | search summary |
| 7 | Demurrage and detention, how to avoid charges | Cogoport | https://www.cogoport.com/blogs/demurrage-detention-how-to-avoid-charges | n/d | 2026-11-01 | Existing tracking tool, vendor rates | search summary |
| 8 | BRFEDF flags systemic issues in shipping line practices | The Week | https://www.theweek.in/wire-updates/business/2026/04/27/brfedf-flags-systemic-issues-in-shipping-line-practices-urges-urgent-policy-intervention-following-dg-shipping-meeting.html | 2026-04-27 | 2026-11-01 | Detention complaints, DG Shipping meeting | search summary |
| 9 | Demurrage and detention waiver, fault-based divide | Bhatt and Joshi Associates | https://bhattandjoshiassociates.com/the-fault-based-divide-when-demurrage-and-detention-waiver-under-hccar-2009-scmtr-2018-are-granted-and-when-they-are-refused/ | n/d | 2026-11-01 | Waiver rule | search summary |
| 10 | JK Tyre acquires Treel, launches tyre monitoring sensors; Apollo interview | Autocar Professional | https://www.autocarpro.in/news-national/jk-tyre-acquires-treel--launches-tyre-monitoring-sensors-43773 | n/d | 2026-11-01 | Incumbent TPMS | search summary |
| 11 | Manatec Tyremate TPMS listing; generic 6-sensor kit | IndiaMART; Fruugo | https://m.indiamart.com/proddetail/manatec-tyremate-tpms-for-bus-trucks-solar-display-with-tubeless-tyres-pack-of-6-sensors-2857752662991.html | n/d | 2026-11-01 | TPMS prices | search summary |
| 12 | Tyre management; TMC figure via Fleet Equipment | Fleetx | https://www.fleetx.io/tyre-management | n/d | 2026-11-01 | Tyre share of cost, life loss | search summary |
| 13 | Prompt TrackSure crate management | Prompt Dairytech | https://www.promptdairytech.com/?p=8342 | n/d | 2026-11-01 | Crate loss claim, incumbent | search summary |
| 14 | Dairy crates listings | IndiaMART (MPH Group) | https://m.indiamart.com/mphgroup/dairy-crates.html | n/d | 2026-11-01 | Crate prices | search summary |
| 15 | Spices Board guidelines to prevent ETO contamination | Outlook Business | https://www.outlookbusiness.com/news/spices-board-formulates-comprehensive-guidelines-for-exporters-to-prevent-eto-contamination | 2024-05 | 2026-11-01 | ETO guidelines, steam route | search summary |
| 16 | Top 5 spice export rejection reasons; Spice Park tender | Sadbhaav Spices; Spices Board | https://sadbhaavspices.com/top-5-spice-export-rejection-reasons/ | n/d | 2026-11-01 | Toll rate (weak), spice park steam unit | search summary |
| 17 | Spices sterilizing systems listing | TradeIndia | https://www.tradeindia.com/products/spices-sterilizing-systems-c5628001.html | n/d | 2026-11-01 | Steriliser price | search summary |
| 18 | Researchers raise concerns over egg quality in Hyderabad | The News Minute | https://www.thenewsminute.com/telangana/researchers-raise-concerns-over-egg-quality-in-hyderabad-anganwadis | n/d | 2026-11-01 | Cracked eggs resold | search summary |
| 19 | Live weight shrinkage and mortality during broiler transport, Chennai | Krishikosh | https://krishikosh.egranth.ac.in/handle/1/5810213004 | n/d | 2026-11-01 | Shrinkage and mortality | search summary |
| 20 | Transportation stress in meat-type chickens, Indian scenario | Indian J. Animal Research | https://arccjournals.com/journal/indian-journal-of-animal-research/ARCC089 | 2013 | 2026-11-01 | Mitigation advice | search summary |
| 21 | Parliamentary reply on PMMSY cold chain and ice boxes | Lok Sabha | https://eparlib.sansad.in/bitstream/123456789/2995611/1/AU3865_VGAcy6.pdf | n/d | 2026-11-01 | Scheme coverage | search summary |
| 22 | Ensure compliance with norms, govt tells Everest, MDH | Tribune | https://www.tribuneindia.com/news/india/ensure-compliance-with-norms-govt-tells-everest-mdh-inspects-facilities-623215/amp | 2024-04 | 2026-11-01 | EU alerts fell after 2022 testing | search summary |
| 23 | Post-harvest operations and value addition | ICAR | https://krishi.icar.gov.in/jspui/bitstream/123456789/44421/1/TB5_Post-harvest%20operations%20and%20value_S%20Priyadarsani.pdf | n/d | 2026-11-01 | Rubber-roll out-turn gain | search summary |
| 24 | Fleeca India launches TPMS for heavy commercial vehicles | CarDekho Tyres | https://tyres.cardekho.com/news/fleeca-india-launches-tyre-pressure-monitoring-system-devices-for-heavy-commercial-vehicles | n/d | 2026-11-01 | Incumbent TPMS | search summary |
| 25 | India returnable transport packaging market | Mobility Foresights | https://mobilityforesights.com/product/india-returnable-transport-packaging-market | n/d | 2026-11-01 | Pooling players (LEAP India) | search summary |
