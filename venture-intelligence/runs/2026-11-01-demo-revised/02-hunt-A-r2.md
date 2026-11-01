# Hunt A, round 2: money wasted (Opportunity Hunter, 2026-11-01)

Verdict: no ADVANCE yet. One of the eleven round-1 candidates is now REJECT, ten are INVESTIGATE, and eight new ideas are all INVESTIGATE. The strongest on the numbers is a live-bird transport kit for broiler traders, and the most original is a success-fee desk that recovers wrongly billed container detention.

What changed from round 1: round 1 rejected candidates because evidence was missing or because an incumbent exists. Under the revised rules that is not enough. Rejection now needs contradicting evidence or credible figures that show the approach is impractical.

Separation used throughout: `[S#]` sourced fact, `[I]` and `[A]` estimate, `[H]` hypothesis, and "Not found" for missing information. Economics are in `runs/2026-11-01-demo-revised/econ_A_r2.py` (round 1 script: `payback_A.py`).

Deciding questions, written before the new searches:
- Broilers: who bears the shrinkage, the farmer or the trader, and does any Indian product address it?
- Detention: can a wrongly billed amount be recovered under Indian law, and is the claim big enough to pay a desk?
- Fish: do small boats lack ice access, and what is the highest rent a reusable cold pack could charge?
- Tyres: does a drive-over scanner exist abroad, and is there a place in India where trucks stop anyway?
- Eggs: does a shell coating exist as a product, and what does it cost against what it saves?
- Steam: can a passive label tell a failed trap from a healthy one?
- Spices: is any shared or mobile steriliser offered to small exporters?

## 1. Industries chosen and why

| Industry | Why it might hide an opportunity now |
|---|---|
| Poultry live-haul | Chennai broiler trucks lose 2.36 to 3.01% of weight and 0.43 to 0.53% of birds per trip [S19]. An Indian live-shrink study reports a mean loss of 4.47% and about Rs 2,905 crore a year across the industry [S31]. |
| Port and container logistics | Exporters allege non-transparent detention billing, and DG Shipping met stakeholders on 17 April 2026 [S8]. Courts have ordered refunds where a detention certificate existed [S28]. |
| Marine fisheries | Ice shortages hit small boats first at landing sites [S30]. Measured loss in the traditional sector is 4.30% at landing [S1]. |
| Road freight tyres | Tyres are 10 to 18% of vehicle operating cost by one vendor figure [S12]. Drive-over tyre scanners are sold abroad and none were found in India [S26]. |
| Dairy and egg packaging | A vendor claims a quarter of milk crates are lost a year, unverified [S13]. Egg coating products exist [S27]. |
| Industrial steam | Failed-trap shares of 9.4% managed to 25% unmanaged in a large Japanese dataset [S6]. |
| Spice export compliance | The Spices Board promoted steam sterilisation after the 2024 ethylene oxide scare [S15]. |

## 2. Round-1 candidates, re-sorted

| # | Candidate | Round 1 | Round 2 | Why the change or the hold |
|---|---|---|---|---|
| 1 | Small-boat fish spoilage | Cut | INVESTIGATE | A subsidy on boxes does not remove a need for ice access on small boats [S30]. Loss rate is 4.30% in the traditional sector [S1]. Test: idea I3. |
| 2 | Ice cost on mechanised boats | Cut | REJECT | Ice was Rs 20,000 against about Rs 3 lakh of diesel on one 20-day trip account [S3]. The saving is too small to pay for a product. |
| 3 | Steam trap monitoring | Cut | INVESTIGATE | An incumbent exists [S5], but its price to small plants was not found after 1 search. Test: ask 5 small plants what they last paid for a survey, and idea I8. |
| 4 | Container detention tool | Cut | INVESTIGATE | Software tracking is crowded [S7], but a recovery desk is a different mechanism. See I2. |
| 5 | Truck tyre sensors | Cut | INVESTIGATE (low) | Payback ran 14.5 to 143 months on assumed inputs [A], not on measured ones. See I5 for a different mechanism. |
| 6 | Milk crate loss | Cut | INVESTIGATE (low) | The loss rate is unverified but not contradicted [S13]. See I4. |
| 7 | Egg breakage | Cut | INVESTIGATE (low) | No Indian breakage rate found after 5 searches. See I7. |
| 8 | Broiler transport | Cut | INVESTIGATE | Shrinkage of 2.36 to 3.01% on 2,236 birds a truck is large per trip [S19]. See I1. |
| 9 | Spice sterilisation | Cut | INVESTIGATE (low) | Capital is above Rs 5,00,000 [S17], but a shared or mobile mechanism has not been tried. See I6. |
| 10 | Rice mill yield | Cut | INVESTIGATE (unassessed) | One search only. Rubber-roll mills give 2 to 3% more out-turn than emery mills [S23], and the FCI out-turn rule was not found. Not enough work to judge. Test: read the FCI custom-milling order and ask 3 millers for their head-rice yield. Cost about Rs 1,000 and 2 weeks [H]. |
| 11 | Cutting-fluid recycling | Cut | INVESTIGATE (unassessed) | No India data found after 1 search. Test: ask 5 machine shops what they pay per litre and for disposal. |

Nothing else is REJECT. Reaching REJECT needs a contradicting figure, and none of the others has one.

## 3. Creative phase and ideas kept

Ratings are difference, desirability and plausibility, each high, medium or low. They are judgements, not measurements.

| Idea | Type | Difference | Desirability | Plausibility | Outcome |
|---|---|---|---|---|---|
| I1 Broiler live-haul shrink and heat kit | New capability on an old problem | Medium | High [H] | Medium | INVESTIGATE |
| I2 Detention recovery desk on success fee | Different business model | High | Medium | Medium | INVESTIGATE |
| I3 Rented PCM totes for small boats | Different material | Medium | Medium | Low | INVESTIGATE |
| I4 Crate QR plus UPI deposit | Different mechanism | Medium | Low | Medium | INVESTIGATE |
| I5 Tyre scan at weighbridges | Unserved place, existing tech | High | Low | Low | INVESTIGATE |
| I6 Shared or mobile spice steriliser | Different business model | Low | Medium | Low | INVESTIGATE |
| I7 Egg shell coating at the packer | Known material, new buyer | Low | Low | Medium | INVESTIGATE |
| I8 Passive steam trap indicator labels | Product category that may not exist | High | Medium | Low | INVESTIGATE |

### I1 Broiler live-haul shrink and heat kit (INVESTIGATE)

1. Different: a retrofit for the load, not the truck: in-cage misting or wetting, airflow when stopped, and a loading routine. No Indian retrofit seller was found after 3 searches (queries: "live poultry transport vehicle India startup retrofit", "broiler live bird transport India vehicle design sprinkler", "India live bird trader shrinkage allowance").
2. Desire: the trader or integrator loses weight and birds on every trip. One Chennai study shows 2.36 to 3.01% shrinkage and 0.43 to 0.53% mortality [S19]. The mean live shrink in another Indian study is 4.47% [S31].
3. Buyer: a poultry trader or integrator with daily trucks [H]. A Chennai truck carries about 2,236 birds [S19]. Who blocks: the driver, and the farmer if the farmer is paid on market weight [H].
4. Advantage: against doing nothing, it targets the heat-driven part of shrinkage. Against the free option of wetting birds by hand, which is already practised and more often in summer [S19], it adds control and airflow when the truck is stopped. A patent notes the stopped vehicle is the high-risk moment and that retrofits are expensive [S36].
5. Price and cost: loss per trip is Rs 9,499 to Rs 17,499 at Rs 90 to Rs 130 a kg [I] using 2 kg birds [A] and the price range in [S32]. A kit that recovers only 5% of the loss saves Rs 71,239 to Rs 2,18,737 a year at 150 to 250 trips [I]. A kit cost of Rs 50,000 [H] gives payback of 2.7 to 8.4 months at the 5% recovery [I]. Selling price Rs 50,000 and unit cost Rs 30,000 are both [H].
6. Critical unverified assumption [H]: at least 5% of the shrinkage is heat-driven and avoidable, and the buyer, not the farmer, bears it. A pilot paper puts shrinkage at 0.18 to 0.60% an hour after feed withdrawal and about 0.30% an hour later [S20 via search summary], so part of it is fasting, which a kit will not fix.
7. Cheapest test: weigh 10 truck loads at farm and at market, 5 with a rented mister and 5 without. About Rs 45,000 and 6 weeks [H]. Plus 5 calls to Namakkal, Palladam or Hyderabad traders on who bears shrinkage, free, 1 week.

Existing solutions: not found after 3 searches. A US trailer patent exists [S36]. No Indian product found. A gap with no found competitor is either a real opening or no demand. The loss figures point to the first, but no trader has yet been asked.

### I2 Detention recovery desk on success fee (INVESTIGATE)

1. Different: it sells recovery, not tracking. Courts have ordered refunds of detention collected despite a valid certificate, but a certificate does not give an automatic right, and misdeclaration defeats a claim [S28]. It would keep a dataset of gate-in times and tariff terms. That is the only asset.
2. Desire: exporters said bargaining power is lopsided against global lines [S8].
3. Buyer: an exporter or importer with a large disputed bill, working through a clearing agent [H].
4. Advantage: Cogoport and similar tools warn about free days [S7], they do not argue claims.
5. Price and cost: a bill of Rs 45,000 yields an expected fee of Rs 562 to Rs 1,688, while a Rs 11.2 lakh bill yields Rs 14,000 to Rs 42,000 [I]. Founder time at 6 hours a claim costs Rs 4,500 [A]. So only large bills pay. Success rate and the 25% fee are [H].
6. Critical unverified assumption [H]: enough disputed bills above Rs 5 lakh exist and are winnable without litigation.
7. Cheapest test: collect 10 exporters' detention invoices for 12 months and have a customs lawyer grade 3 of them. About Rs 8,000 and 4 weeks [H].

Existing solutions: carriers' own tariffs, for example Emirates Line, effective 1 October 2025 [S7]. Not found after 2 searches for a contingency recovery service (queries: "wrongly charged detention refund claim exporters India contingency", "detention demurrage management software India").

### I3 Rented PCM totes for small boats (INVESTIGATE, low plausibility)

1. Different: reusable phase-change packs in a tote, rented per trip at the jetty, so a boat needs no ice. Reusable PCM packs sold as ice substitutes exist for coolers [S29].
2. Desire: ice runs short at some landing sites [S30].
3. Buyer: a small-boat owner, or a landing-site cooperative [H].
4. Advantage over ice: no melt water and no dependence on plant power. Against a subsidised box it adds temperature hold. No independent boat trial found [S29].
5. Price ceiling: with half of the 4.3% loss avoidable [S1][A], value per trip is only Rs 32 at a Rs 3 lakh catch and Rs 129 at Rs 12 lakh [I]. A tote costing Rs 4,000 [H] needs many trips, so margin is thin.
6. Critical unverified assumption [H]: packs hold fish near 0 to 4 C through a trip at lower cost per trip than ice.
7. Cheapest test: two commercial packs, a logger, one day on a jetty against ice. About Rs 12,000 and 2 weeks [H].

### I4 Crate QR plus UPI deposit (INVESTIGATE, low desirability)

1. Different: a QR on the crate and an app-based deposit held from the retailer, rather than a hardware tag. The incumbent is a patented tag system [S13].
2. Desire: the dairy loses crates at Rs 225 to Rs 380 each [S14] at an unverified rate [S13].
3. Buyer: a dairy's distribution head [H]. Retailers can block a deposit.
4. Advantage: lower cost than tags [H].
5. Price: value per crate is Rs 3 to Rs 57 a year across loss rates of 5 to 25% [I]. A fee of Rs 6 per crate a year [H] gives Rs 1,20,000 a year from a 20,000-crate dairy [I]. That is thin for a business.
6. Critical unverified assumption [H]: retailers will accept a deposit.
7. Cheapest test: print QR labels on 200 crates on one route and ask 3 distributors. About Rs 6,000 and 6 weeks [H].

### I5 Tyre scan at weighbridges (INVESTIGATE, low)

1. Different: use the place where trucks already stop. Drive-over scanners are sold abroad [S26]. No weighbridge add-on found [S35].
2. Desire: unclear. The payer may be the fleet, the plant or nobody [H].
3. Buyer: weighbridge operator, mine or mill [H].
4. Advantage over in-truck sensors: one reader serves many trucks, and a truck owner buys nothing.
5. Price: hardware Rs 8 lakh [H]. At Rs 20 a scan and 100 scans a day, payback is 13.3 months [I]. At Rs 10 and 50 scans, 53.3 months [I]. Capital above the Rs 5,00,000 default [A].
6. Critical unverified assumption [H]: someone pays per scan.
7. Cheapest test: call 5 weighbridge operators and 5 fleet owners with a price. About Rs 3,000 and 2 weeks [H].

### I6 Shared or mobile spice steriliser (INVESTIGATE, low)

1. Different: a mobile or cooperative-owned steriliser. None found after 1 search (query: "mobile spice processing unit farmers cooperative Kerala"). Fixed public units exist [S34][S16].
2. Desire: small exporters need an ethylene-oxide-free route [S15].
3. Buyer: a small exporter or farmer producer company [H].
4. Advantage: no need to ship to a park. Against the park, it competes on location only.
5. Price and cost: steriliser alone is about Rs 10 to Rs 12 lakh [S17]. With a truck and boiler I assume Rs 19 lakh in total [H]. At a Rs 15 per kg toll [S16, weak] and 60 days a year, payback is 24.5 months [I]. At 20 days it is 108.6 months [I].
6. Critical unverified assumption [H]: utilisation of 60 days or more at Rs 15 a kg.
7. Cheapest test: ask the Spices Board for park toll terms and ask 10 exporters what they pay. About Rs 2,000 and 3 weeks [H].

### I7 Egg shell coating at the packer (INVESTIGATE, low)

1. Different: coat at the packer to cut spoilage in the hot season. Coating is a known practice. A manufacturer claims at least 30 days of extra shelf life [S27]. Reviews disagree on benefit [S27]. A claim that mineral oil coating is prohibited abroad is unverified [S27].
2. Desire: summer shelf life falls to one to two weeks without cold storage [S18].
3. Buyer: a packer or exporter [H].
4. Price: farm eggs sell at Rs 4.30 to Rs 5.40 [S37]. A 1% loss cut is worth Rs 0.043 to Rs 0.054 an egg against a Rs 0.03 to Rs 0.08 coating cost [H]. Margin is thin.
5. Critical unverified assumption [H]: coating cuts breakage or spoilage by 1% or more.
6. Cheapest test: 120 eggs, one litre of oil, 4 weeks. About Rs 3,000 [H].

### I8 Passive steam trap indicator labels (INVESTIGATE, low plausibility)

1. Different: a Rs-per-trap label read by eye. Irreversible heat labels are used on traps [S33]. A single-threshold label detects only high temperature [S33], and a healthy trap on the steam side is also hot [K]. So the label may not separate good from failed.
2. Desire: a leaking trap can lose Rs 90,000 a year across a 50-trap plant at 10% failure, and Rs 45 lakh across a 200-trap plant at 25% [I], using 2 to 5 kg an hour [H] and Rs 1.5 to Rs 3 a kg of steam [A].
3. Buyer: a plant maintenance head.
4. Advantage: price only. Incumbents sell surveys and monitors [S5].
5. Critical unverified assumption [H]: a label on the condensate side correlates with failure.
6. Cheapest test: 50 labels and a borrowed ultrasonic gun at one plant. About Rs 5,000 and 2 weeks [H].

## 4. Which two to take first

- I1 has the largest per-buyer numbers and a measured Indian loss rate [S19][S31]. It is unproven on who bears the loss and how much a kit recovers.
- I2 is the most unusual mechanism and costs the least to test, but pays only on large bills.

## 5. What I did not check

- Whether the shrinkage in I1 is borne by the farmer or the trader. Not found after 2 searches.
- The two primary papers behind [S19] and [S20]. I saw summaries, and pmc.ncbi.nlm.nih.gov did not resolve in this session.
- Scheme guidelines, Spices Board toll terms, FCI out-turn order.
- Any buyer. Demand evidence is L0 to L1 for every idea here.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Post harvest losses in marine fisheries | ICAR-CIFT | https://drs.cift.res.in/bitstreams/ad3a50de-5289-46fc-ae4c-5275f57aca14/download | n/d 2026 | 2026-11-01 | Landing loss rates | search summary |
| 3 | Thoothukudi boats anchored due to ice bar price hike | DT Next | https://www.dtnext.in/news/tamilnadu/thoothukudi-boats-anchored-due-to-ice-bar-price-hike-800262 | n/d 2026 | 2026-11-01 | Ice price, trip cost | search summary |
| 5 | Forbes Marshall Trap Monitoring System | Forbes Marshall | https://www.forbesmarshall.com/BlogDetails/Blog/WirelessSteamTrapMonitoringSystem | n/d 2026 | 2026-11-01 | Incumbent monitoring | search summary |
| 6 | Steam trap failure rate statistics | Reliabilityweb | https://reliamag.com/topics/guides/steam-trap-failure-rate-statistics | n/d 2026 | 2026-11-01 | Failure benchmarks | search summary |
| 7 | Demurrage and detention, how to avoid charges | Cogoport | https://www.cogoport.com/blogs/demurrage-detention-how-to-avoid-charges | n/d 2026 | 2026-11-01 | Tracking tool, vendor rates | search summary |
| 8 | BRFEDF flags systemic issues in shipping line practices | The Week | https://www.theweek.in/wire-updates/business/2026/04/27/brfedf-flags-systemic-issues-in-shipping-line-practices-urges-urgent-policy-intervention-following-dg-shipping-meeting.html | 2026-04-27 | 2026-11-01 | Detention complaints | search summary |
| 12 | Tyre management | Fleetx | https://www.fleetx.io/tyre-management | n/d 2026 | 2026-11-01 | Tyre cost share | search summary |
| 13 | Prompt TrackSure crate management | Prompt Dairytech | https://www.promptdairytech.com/?p=8342 | n/d 2026 | 2026-11-01 | Crate loss claim, incumbent | search summary |
| 14 | Dairy crates listings | IndiaMART (MPH Group) | https://m.indiamart.com/mphgroup/dairy-crates.html | n/d 2026 | 2026-11-01 | Crate prices | search summary |
| 15 | Spices Board guidelines on ETO | Outlook Business | https://www.outlookbusiness.com/news/spices-board-formulates-comprehensive-guidelines-for-exporters-to-prevent-eto-contamination | 2024-05 | 2026-11-01 | Steam route promoted | search summary |
| 16 | Top 5 spice export rejection reasons | Sadbhaav Spices | https://sadbhaavspices.com/top-5-spice-export-rejection-reasons/ | n/d 2026 | 2026-11-01 | Toll rate (weak) | search summary |
| 17 | Spices sterilizing systems listing | TradeIndia | https://www.tradeindia.com/products/spices-sterilizing-systems-c5628001.html | n/d 2026 | 2026-11-01 | Steriliser price | search summary |
| 18 | Researchers raise concerns over egg quality in Hyderabad | The News Minute | https://www.thenewsminute.com/telangana/researchers-raise-concerns-over-egg-quality-in-hyderabad-anganwadis | n/d 2026 | 2026-11-01 | Summer shelf life | search summary |
| 19 | Live weight shrinkage and mortality during broiler transport, Chennai | Krishikosh | https://krishikosh.egranth.ac.in/handle/1/5810213004 | n/d 2026 | 2026-11-01 | Shrinkage, mortality, birds per truck | search summary |
| 20 | Transportation stress in meat-type chickens, Indian scenario | Indian J. Animal Research | https://arccjournals.com/journal/indian-journal-of-animal-research/ARCC089 | 2013 | 2026-11-01 | Hourly shrinkage, mitigation | search summary |
| 23 | Post-harvest operations and value addition | ICAR | https://krishi.icar.gov.in/jspui/bitstream/123456789/44421/1/TB5_Post-harvest%20operations%20and%20value_S%20Priyadarsani.pdf | n/d 2026 | 2026-11-01 | Rubber-roll gain | search summary |
| 26 | Goodyear DrivePoint drive-over tyre inspection | Goodyear | https://www.goodyear.eu/en_ie/truck/tyre-management/drivepoint.html | n/d 2026 | 2026-11-01 | Drive-over scanners abroad | search summary |
| 27 | A novel emulsion coating for eggs; TotalEnergies egg coating oil | LSU repository; TotalEnergies | https://repository.lsu.edu/animalsciences_pubs/627 | n/d 2026 | 2026-11-01 | Coating evidence, claim | search summary |
| 28 | Detention certificate refund case summaries | Indian Kanoon | https://future.indiankanoon.org/doc/55946260/ | n/d 2026 | 2026-11-01 | Refund law | search summary |
| 29 | Arctic Ice cooler pack review; PCM coolbox study | Field and Stream; UEA | https://ueaeprints.uea.ac.uk/id/eprint/100445 | n/d 2026 | 2026-11-01 | PCM packs exist | search summary |
| 30 | Ice shortage hits fishermen; water crisis hits ice plants | Free Press Journal; Deccan Herald | https://www.freepressjournal.in/amp/mumbai/fpj-exclusive-ice-shortage-due-to-power-cuts-hits-fishermen-hard-in-peak-season | n/d 2026 | 2026-11-01 | Ice shortages | search summary |
| 31 | Live shrink loss in broiler marketing | buecher.de listing | https://buecher.de/artikel/buch/live-shrink-loss-in-broiler-marketing/60969419 | n/d 2026 | 2026-11-01 | 4.47% mean, industry loss figure | search summary |
| 32 | Broiler farming profit per bird in India | agrifarming.in | https://www.agrifarming.in/broiler-farming-profit-per-bird | 2026-04 | 2026-11-01 | Live price range | search summary |
| 33 | Steam trap monitor patent; thermochromic labels | Google Patents | https://patents.google.com/patent/US4333339 | 1982 | 2026-11-01 | Passive label limits | search summary |
| 34 | Spice parks and shared facilities | Spices Board | https://indianspices.com/node/63.html | n/d 2026 | 2026-11-01 | Fixed public facilities | search summary |
| 35 | Weighbridges | Avery Weigh-Tronix India | https://www.averyweigh-tronix.com/en-in/weighbridges/ | n/d 2026 | 2026-11-01 | No tyre add-on listed | search summary |
| 36 | Trailer for transporting living fowl | USPTO | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8794187 | n/d 2026 | 2026-11-01 | Stopped-vehicle risk, retrofit cost | search summary |
| 37 | Iran war hits Namakkal, egg price drops | DT Next | https://www.dtnext.in/news/tamilnadu/iran-war-hits-namakkal-egg-price-drops-by-40-paise-in-3-days | 2026 | 2026-11-01 | Egg price | search summary |
