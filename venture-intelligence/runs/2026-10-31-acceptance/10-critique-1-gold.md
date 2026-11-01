# Critique 1: Witnessed waste sale for gold jewellery workshops (Lead 1, "waste mandi")

Specialist: Independent Critic. Date: 2026-11-01.

Constraints from the brief: founder capital ₹5,00,000 and founder time at ₹750 per hour [A] (basis: brief; test: none needed). Primary market India.

Method and limits.
- Inputs read: 05-invent-1-gold.md (Lead 1), 06-expert-1-gold.md, 07-business-1-gold.md, 03-market-1-gold-loss.md. Nothing else in the run folder. All their claims treated as unverified.
- I ran 30 web searches with my own keywords, in English and Hindi. I did not try WebFetch (the brief says it is blocked). I opened no pages. Every source is marked `search summary`.
- Queries, by deciding question:
  - Q1 (existing equivalents): "Augmont refinery jewellers manufacturing waste sweeps polishing dust refining service"; "MMTC-PAMP jewellers scrap refining B2B manufacturers karigar waste assay"; "gold dust refinery India jewellers sweeping assay certificate fire assay payout percentage"; "Gujarat Gold Centre Ahmedabad refining jewellery waste dust sweeping charges"; "Rajkot gold refinery dust OR sweeping OR polishing waste jewellers recovery service"; "Kolkata Bowbazar gold dust refining jhalai OR sweepings refinery karigar"; "Raw Gold Waste Management Rajkot"; "IndiaMART gold dust refining service jewellery waste per kg OR recovery"; "Alex Stewart International precious metal sweeps refinery supervision"; "jewellery sweeps auction refiners bid platform independent assay"; "startup India jewellers gold scrap B2B platform refiners competitive bids"; "Augmont Sell Old Gold jewellers B2B scrap melting XRF fire assay"; "Bangalore Refinery manufacturing wastage recovery sweeps"; "MSTC e-auction gold bearing sweepings ash India Government Mint"; "RefiningLots.com online marketplace refiners bid"; "India refinery jewellery manufacturing waste OR lemel OR filings recovery service"; "Sabin Metal representation customer witness lot processing".
  - Q2 (what owners realise): a Hindi query on nyariyas buying goldsmith-shop soil; a follow-up Hindi query on the Patrika Bihar story; "goldsmith workshop dust sold to refiner India percentage of value"; "Coimbatore OR Thrissur goldsmith polish dust sold collectors"; "gold refining charges per gram, jewellers, 2026, India"; "tunch refinery karigar dust refining out-turn charges"; "Kolkata gold workshop owner sells dust kadaiwala pays rupees month".
  - Q3 (assay cost): "fire assay gold ore sample price India laboratory NABL"; "fire assay testing charges per sample gold bar bullion lab Zaveri Bazaar OR Rajkot".
  - Q4 (legal and behavioural): "PMLA dealers in precious metals KYC purchase from unregistered seller"; "GST purchase of gold scrap from unregistered person reverse charge"; "section 40A(3) cash payment purchase gold scrap 269ST"; "jewellery karigars job workers unregistered GST informal cash"; "job work waste scrap belongs to principal section 143(5) jewellery".
- Economics: I built my own inputs and ran `python3 tools/econ.py` (input saved as 10-critique-1-gold.json) plus a sweep over lot size, witness hours and volume. All business arithmetic below comes from the script [I].
- Gold price: I did not check it myself. I use ₹14,100 per gram as base [A] (basis: 06 cites IBJA ₹14,108 on 27 October 2026; 05 and 07 use ₹14,300; test against IBJA on the day). Favourable case ₹15,200 [A] (basis: 07's IBJA figure of ₹15,211 on 27 September; a Gujarat Gold Centre page title showed a "live rate" of ₹15,850.86 per gram on 1 November 2026, basis unknown, possibly with tax [S5]).
- USD converted at ₹88 per USD [A] (basis: the specialists' working rate; not checked).
- I contacted no one. Nothing here is above demand level L1.

## 1. Steelman

Indian jewellery workshops generate gold-bearing waste and sell it today to collectors or refiners who also weigh and value it, so the seller has no independent check on the price [S19, S22, S23]. A neutral firm that seals the lot, gets an independent assay, and makes licensed refiners compete could lift the owner's take by several points on lots worth lakhs, paid from a sale the owner already makes, while the firm never holds gold [I] (a 30 g lot is worth ₹4,23,000 at ₹14,100 per gram and one point of realisation is ₹4,230 [I]). High gold prices magnify each point, and cash-limit rules already push large sales towards bank settlement [S28].

## 2. Claims checked

| # | Claim | Source file | My finding | Status | Tag |
|---|---|---|---|---|---|
| 1 | No close match exists for a neutral witness plus split assay plus competing refiner terms | 05 | Multi-refiner bidding on small Indian lots: still not found after 17 searches aimed at equivalents. But the parts exist. Abroad, a refiner invites the customer or a third-party representative to witness weighing, processing and sampling, with customer, umpire and reserve samples [S10]; an inspection firm supervises refinery sampling and lists jewellery scrap and refinery sweeps among its materials [S11]. In India, refiners already toll-refine workshop dust and return metal [S1, S2, S3]. | Partly holds | [S1, S2, S3, S10, S11] |
| 2 | Augmont and MMTC-PAMP already market transparent testing and melting | 07 | Supported. Augmont's 2022 retail service uses touchstone, XRF and melting [S9]; MMTC-PAMP says it melts in front of customers at its centres [S8]. Both target consumer old gold. Neither showed a sweeps service in my searches. MMTC-PAMP's refinery does take jewellery-industry scrap and runs a NABL lab [S7]. | Holds | [S7, S8, S9] |
| 3 | An independent assay costs about ₹5,400 a sample | 06 | Supported. Government lab, from 1 April 2026: gold by fire assay and AAS at ₹4,583, ₹5,408 and ₹5,400 in three unlabelled columns; preparation ₹351-414 a sample [S16]. The 2025 schedule was ₹4,365-5,200 [S17]. A US lab charges USD 30-40 [S18], about ₹2,640-3,520 [A]. No Indian private price found after 2 searches. | Holds | [S16, S17, S18] [A] |
| 4 | Lots under about 25 g of contained gold are uneconomic | 06 | Holds, and is optimistic at 07's 3% fee. With the sourced assay price and 6 founder hours a lot, a lot needs about 48-50 g contained for the founder to earn ₹750 an hour; with a ₹3,000 assay and 4 hours, about 21 g (section 3, M3) | Holds (tightened) | [I] |
| 5 | Refiners often settle small lots on out-turn | 06 | Supported. A refiners' forum says floor and polishing sweeps are usually too small to assay unless the seller is a large producer [S13]; a US refiner sets a USD 200 minimum [S14]; refiners need a minimum batch size [S15]. Indian listings price dust refining per kilogram, a toll model [S1]. | Holds (medium) | [S1, S13, S14, S15] |
| 6 | Base revenue about ₹44,610 per workshop a year, contribution ₹22,210 | 07 | The arithmetic matches 07's inputs, but its base assay of ₹1,500 a lot is an assumption below the only sourced price [S16]. Replacing it with ₹5,822 (assay plus preparation) cuts contribution to ₹4,922 a year; with 6 witness hours instead of 4, to minus ₹1,078 [I] | Does not hold as a base | [S16] [I] |
| 7 | The concept depends on owners realising 80% or less of contained value today | 07 | Agree. Add: owners who already toll-refine pay a processing charge of ₹1,150-2,000 per kg in Mumbai listings [S1], so they probably realise much more than 80% unless the refiner under-reports [I]. Unmeasured. | Holds; condition likely fails for the formal segment | [S1] [I] |
| 8 | Owners realise 60-85% of contained value today | 05 | Unsupported. The basis mixes a quote that small artisans recover only 25-30% of lost gold (a capture problem, which a sale service cannot fix) with a 10-40% sale discount that 05 could not tie to one URL. My 7 searches on Indian realisation found no measurement (queries in Method). | Unsupported (L0) | [I] |
| 9 | Waste is already sold, often for cash, and stored for years | 05, 03 | Supported. A Bihar report says a box of shop "nyara" averages about ₹1 lakh and buyers come from other states [S19]; a 2011 report says some jewellers store dust for years and sell for lakhs [S23]; an Ahmedabad workshop owner buys bags of gold-flecked dirt [S22]. | Holds | [S19, S22, S23] |
| 10 | A cash sale of a normal lot is already unlawful (₹2 lakh limit) | 07 | Supported. Section 269ST bars cash receipts of ₹2 lakh or more, with a penalty equal to the amount on the receiver [S28]; Section 40A(3) disallows a buyer's cash payments above ₹10,000 a day per person [S28]. But informality persists in the trade: a 2018 GFMS survey reported cash deals with only making charges billed [S33]. | Holds in law; weak in practice | [S28, S33] |
| 11 | The firm is probably not a PMLA reporting entity; refiners must report cash of ₹10 lakh or more | 06 | Supported. G.S.R. 799(E) of 28 December 2020 covers dealers' cash transactions of ₹10 lakh or more [S26]; KYC is not mandatory for purchases under ₹2 lakh [S27]. Bank-settled sales fall outside the cash trigger [I]. | Holds | [S26, S27] [I] |
| 12 | Job-work waste may belong to the gold-issuing principal | 07 | Supported by more commentary: waste belongs to the principal unless agreed otherwise; a registered job worker may sell it on payment of tax under Section 143(5), otherwise the principal supplies it [S31]. Secondary sources only. | Holds (medium) | [S31] |
| 13 | 4 founder hours per lot | 05, 07 | 06 says 6-10 hours. No direct evidence found. My sweep: at 30 g lots and favourable costs, the founder clears ₹750 an hour only below about 8 hours a lot [I] | Open | [I] |
| 14 | Refiners want documented supply from small sellers | 07 | Not re-checked directly. A trade report says one large Ahmedabad family left refining in 2019 after 28 years, and that refining earns 0.1-0.2% of scrap value [S6]. Thin margins could make refiners keen on volume, or unwilling to bear small-lot assay costs [I]. | Unclear | [S6] [I] |

## 3. Objections

### Fatal

None proven. Objection M4 below comes close: the owners with the biggest price gap are probably the cash sellers least willing to invoice. It stays major because a cheap test can settle it.

### Major

**M1. A close substitute already exists for the owners most likely to formalise.**
- Indian refiners list dust refining at ₹1,150-2,000 per kg, including polishing dust, hand-wash dust, floor dust and ETP sludge [S1]; a Mumbai refiner advertises casting-scrap dust and floor-dust recovery [S2]; Bangalore Refinery collects scrap and sweeps and returns pure metal [S3, S4]; Gujarat Gold Centre describes assaying and refining scrap on a process charge [S5].
- An owner who toll-refines keeps his own metal and pays a charge. If the ₹1,150-2,000 is per kg of dust holding 20-50 g of gold, the charge is ₹23-100 per gram of gold, while a 3% fee is ₹423 a gram, 4-18 times more [I] (the listing unit is unclear; test with 2 quotes).
- What is left of the difference: refiner competition and a neutral check on out-turn. The neutral check alone can be had more cheaply (section 6) [I].
- To resolve: in the field test, record each owner's last sale route (collector for cash, toll refiner, refiner purchase) and terms. If most owners already toll-refine at 85% or more of contained value, kill [A] (basis: 07's pessimistic case, where an owner already at 85% gains about 3 points, too little to change habits).

**M2. The realisation gap is unmeasured, and 05's basis is circular.**
- No Indian figure for what owners get as a share of contained gold was found after 7 searches (queries in Method) [I].
- 05's 60-85% range rests on a recovery quote (25-30% of lost gold) and an untied discount claim; recovery and sale price are different things [I].
- The only hard Indian values are lot values: a Bihar shop's box sells for about ₹1 lakh on average [S19]. At 75-85% realisation that is about 8-10 g of contained gold [I], well below the lot sizes the economics need (M3).
- To resolve: the split-assay test on 5-10 real lots (06's design) [I].

**M3. The economics pass only in a favourable case, and the deciding inputs are unmeasured.**

My inputs (unit: one witnessed lot; fee charged plus 18% GST [A], basis: services rate; CA to confirm):

| Input | Conservative | Base | Favourable | Tag |
|---|---|---|---|---|
| Contained gold per lot | 15 g | 30 g | 40 g | [A] (basis: 07's 120 g a year over 4 lots; 05's 7.5-20 g a month; Bihar lot values [S19] point lower) |
| Gold price | ₹14,100 | ₹14,100 | ₹15,200 | [A] (Method) |
| Fee and share of lots where it is due | 3%, 50% | 3%, 75% | 3%, 90% | [A] (07's design) |
| Assay, preparation, umpire reserve per lot | ₹6,904 | ₹6,362 | ₹3,300 | [S16] base; [A] favourable (basis: US lab USD 30-40 [S18]) |
| Seals and travel per lot | ₹2,300 | ₹1,500 | ₹900 | [A] (07's ₹300-1,000 lines plus refiner travel) |
| Founder hours per lot | 10 | 6 | 4 | [A] (06: 6-10; 07: 2.5-5) |
| Cash CAC, lots per customer | ₹12,000, 3 | ₹6,000, 6 | ₹3,000, 8 | [A] (07: ₹2,000-7,000 cash for the first 10; agent ₹3,333-16,000 per customer) |
| Fixed cash per month | ₹11,667 | ₹11,667 | ₹11,667 | [A] (07: ₹10,000 overhead; ₹20,000 a year insurance) |
| One-time | ₹1,95,856 | ₹1,95,856 | ₹1,95,856 | [A] (kit ₹1,25,000 and legal ₹25,000 from 07; field test ₹45,856 from 06) |
| Lots a month aimed for | 16.7 | 33.3 | 40 | [A] (07: 100 customers at 4 lots a year by month 24) |

"Favourable plus agent" adds a ₹25,000-a-month field agent who witnesses (07's salary range [A]), leaving the founder 1 hour a lot, at 50 lots a month [A]. "Ceiling" is 60 g, a 4% fee due on every lot, 3 hours a lot [A].

Results from tools/econ.py:

| Metric | Conservative | Base | Favourable | Favourable plus agent | Ceiling | Tag |
|---|---|---|---|---|---|---|
| Fee per lot, ex GST | ₹3,172 | ₹9,518 | ₹16,416 | ₹16,416 | ₹36,480 | [I] |
| Contribution per lot before founder time | minus ₹10,032 | ₹656 | ₹11,841 | ₹11,841 | ₹31,905 | [I] |
| Lots a month reached (founder capacity cap) | 12.0 | 20.0 | 32.5 | 50 | 40 | [I] |
| Founder earnings per hour | minus ₹825 | ₹9 | ₹2,332 | ₹6,942 | ₹8,430 | [I] |
| Peak cash need | ₹21,51,150 | ₹4,81,404 | ₹2,69,441 | ₹4,04,646 | ₹2,69,441 | [I] |
| Cash payback month | none | none | 9 | 10 | 8 | [I] |

- The favourable case clears ₹750 an hour by a wide margin; the base case does not [I].
- Sweep (from the script): with the sourced assay price and 6 hours a lot, the founder reaches ₹750 an hour only at about 48-50 g contained per lot (₹604 at 45 g, ₹802 at 50 g) [I]. With a ₹3,000 assay and 4 hours, about 21 g (₹665 at 20 g, ₹1,082 at 25 g) [I]. At 30 g and favourable costs, witness time must stay under about 8 hours (₹713 at 8 h) [I].
- Assay cost is the swing item: ₹5,822 is 46% of the 3% fee on a 30 g lot and 69% on a 20 g lot [I].
- "Reachable in 24 months": the favourable case needs about 98 active workshops at 4 lots a year by month 16, sold in 30 founder hours a month [I]. That is aggressive for a closed trade [A] (basis: 03's reasons buyers would not switch; test: close rate on the first 10).
- The "ceiling" case (60 g, 4% fee, fee always due) shows the upside, not a forecast [I].
- To resolve: a minimum lot rule (pool to 30 g or more), a costed cheaper assay route, and timing 3 real witnessed lots.

**M4. Informality, title and visibility work against the people with the biggest gap.**
- The largest gap is plausibly in cash sales to collectors [S19, S22, S23]. Those sellers lose the most from paper: an invoiced sale at 3% GST (06's source, not re-checked) and recorded income [I].
- Job-work owners (Segment B in 03) may not own the waste: commentary says it belongs to the principal unless the contract says otherwise [S31]. Gold a job worker retains has been ruled taxable job-work consideration at 5% (AAR, reported in 03 and 07, not re-checked) [I]. An invoiced sale documents the gap between allowance and real loss, which a principal could use to cut the allowance [I].
- Cash rules exist [S28], but trade cash practice continues [S33, S34].
- To resolve: ask 15 owners how they were paid for their last lot, who owns the waste under their job-work terms, and whether they would accept a bank-settled invoiced sale. Target owners who own their gold (in-house manufacturers, own-gold workshops) first.

**M5. Refiners may not bid assay-based terms on small lots.**
- Small sweeps lots are often not assayed [S13]; minimums apply [S14, S15]. No Indian refiner's sweeps terms were found by 06, 07 or me [I].
- To resolve: written terms from at least 3 refiners for a 30 g lot with an umpire clause, before pitching owners (07's own plan).

**M6. Copy risk is high and fast.**
- The witness ritual is already sold: open witnessing at a foreign refiner [S10]; third-party supervision [S11, S12]; online lot and assay tracking for refiner clients [S37]; melting in front of the customer by Augmont and MMTC-PAMP [S8, S9].
- Any Indian refiner can adopt an open-witness policy within months; the auction is the only part a single refiner cannot copy [I]. Moat: low.
- To resolve: not by desk evidence. Accept a small, cluster-scale business, or show that lot-history data has a buyer.

**M7. Solo capacity caps the business.**
- At 4-6 hours a lot, one person witnesses 20-32.5 lots a month [I], which is 60-98 workshops at 4 lots a year [I]. Growth beyond that needs a trusted witness on payroll in a trade where karigar dishonesty is the largest jewellers' block claims category for one broker (reported in 06, not re-checked) [I].

### Minor

- m1. GST on the fee: 18% assumed by 05-07 [A] (basis: services rate; CA to confirm).
- m2. Reverse charge on purchases from unregistered sellers: a 2017 press release and later commentary conflict [S29, S30]. Refiners will want a clear view.
- m3. Hazardous-waste transport, Legal Metrology verification of the balance, and state e-way bill rules: not checked by me.
- m4. Gold price moves every rupee figure; the fee scales with it [I].
- m5. One possible local player: a Rajkot company named Raw Gold Waste Management, incorporated in January 2020, activity unknown [S39].

## 4. What holds up

- No gold custody and low capital: peak cash ₹2.6-4.8 lakh in the base and favourable cases, within ₹5,00,000 [I].
- Sampling, split, umpire and witness practice is standard abroad and documented [S10, S11, S12].
- Problem spend exists: owners already sell waste or pay to refine it [S1, S19, S23]. That is L1 for spending on the problem, not for this service.
- Cash limits favour bank settlement for any lot of ₹2 lakh or more [S28]; PMLA reporting is triggered by cash of ₹10 lakh or more, so bank-settled lots avoid it [S26] [I].
- The favourable case pays well: ₹2,332 an hour at 32.5 lots a month [I].
- A decisive test costs under ₹50,000 (06 estimates ₹45,856) [I].

## 5. Disagreements with specialists

- **07, base assay cost.** 07 uses ₹1,500 a lot [A] and cites a ₹200 consumer fire assay. 06 shows cupellation covers 100-999.5 parts per thousand, so raw sweeps need an ore-type assay at about ₹5,408 [S16]. On 07's own inputs with the sourced price, contribution falls from ₹22,210 to ₹4,922 a workshop a year, and below zero at 6 hours a lot [I]. I trust 06 here: sourced price and a stated method.
- **07, fee trigger.** 07 charges the fee when the owner nets 85% or more of contained value. That tests the panel's payout, not the owner's gain: an owner who already got 88% from a toll refiner would pay 3% for a 2-point gain [I]. Charge on the gain above a documented last realisation, or a flat fee.
- **05, realisation basis.** 05 builds 60-85% realisation from a recovery quote and an untied discount claim. Recovery of lost gold and the price of sold waste are different quantities [I].
- **05, revenue range.** 05's ₹38,600-1,37,300 per workshop a year applies the fee to every lot and assumes 4 hours a lot [I]; 06's 6-10 hours and 07's fee-due share both lower it.
- **06, lot threshold.** 06's 17-25 g break-even is at a 4% fee and covers costs only. At 07's 3% fee, with the fee due on 75% of lots, the founder needs about 48-50 g to earn ₹750 an hour at the sourced assay price [I]. A tightening, not a contradiction.
- **03.** No disagreement. Its finding that no Indian buyer pays an outsider to measure loss still stands after my searches [I].

## 6. Simpler alternatives

1. **Owner-run check.** The owner asks his toll refiner to melt the whole lot to a button in front of him and has the button assayed at a hallmarking centre. 06 calls this Route B. BIS centres advertise consumer fire assay from ₹200 (07's source, not re-checked) [I]. This gives most of the trust value without an intermediary; it misses gold left in slag [I].
2. **Flat-fee witness only.** ₹6,000 a lot plus GST, owner pays the assay, no auction. econ.py gives ₹887 an hour at 32.5 lots a month, peak cash ₹2,59,967 [I]. Marginal, but it does not depend on lot size.
3. **Association tender.** A cluster association pools members' lots once or twice a year and invites sealed refiner bids, with an inspection firm as witness [S11] [A] (basis: no Indian example found; test with the Rajkot association).
4. **Refiner open-witness policy.** Refiners copy the Sabin practice as marketing [S10]. This is the likely incumbent response [I].

## 7. Verdict

**Revise, then run the field test. Do not build.** Confidence: medium on the verdict; low on the realisation gap, which decides everything.

Gate view: G1a weak L1 (03). G1b not shown in India; abroad, third-party supervision is sold, but for large industrial lots [S11]. G2 partial: the auction is new, but the trust parts are common (M1, M6). G4 fails in the base case and passes in the favourable case. G5 plausible (06).

Required changes before the test:
1. Benchmark against toll refining as well as collectors. The test must record each owner's sale route and terms.
2. Set a minimum lot of 30 g contained gold. Pool lots by quarter or across small units.
3. Cost an assay route at ₹3,000 a lot or less [A] (basis: US lab price [S18]): whole-lot melt to button, button assay, slag assay only on large lots. Get 2 Indian private quotes.
4. Batch witnessing so founder time stays at 5 hours a lot or less [A] (basis: sweep in M3). Time 3 real lots.
5. Charge on measured gain above a documented last realisation, or a flat fee per lot. Do not charge on contained value.
6. Start with owners who own the waste (own-gold workshops, in-house manufacturers) or have the principal's written consent. Get a CA opinion before lot 1.
7. Get written terms from 3 refiners accepting assay and umpire settlement on a 30 g lot before pitching owners.

Field test (06's 5-lot design plus 15 owner interviews; cash about ₹46,000-50,000 [A], basis: 06's ₹45,856 plus interview travel). Kill if any of these:
- median realisation today, across all sale routes, is 85% or more of assayed contained value [A];
- median lot is under 20 g contained gold [A];
- fewer than 3 of 10 owners accept a bank-settled, invoiced sale [A];
- no refiner signs assay and umpire terms;
- witnessing takes more than 8 hours a lot [I] (sweep in M3).

Not checked: Indian private assay prices; whether a hallmarking centre will assay a waste button; Indian refiners' small-lot terms; current gold price; Rajkot unit and association counts; hazardous-waste transport rules; Legal Metrology; whether Gujarat Gold Centre still refines (sources conflict [S5, S6]); what Raw Gold Waste Management does [S39]; Alex Stewart's Indian services for jewellers; the Patrika article's date and full text [S19].

## 8. Sources

All sources seen only through search-result summaries. No page was opened. "Tie uncertain" means the summary did not tie the point firmly to that URL.

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Gold Refining (category listings) | IndiaMART | https://m.indiamart.com/impcat/gold-refining.html | not shown, 2025-2026 (approx.) | 2026-11-01 | Dust refining ₹2,000/kg (polishing, hand-wash, floor dust, ETP sludge); KGN ₹1,150/kg; AJS ₹1,600/kg gold powder; Gwalior ₹20,000/kg (units unclear; tie uncertain per seller) | search summary |
| 2 | Atharva Jewellery Refinary | IndiaMART | https://m.indiamart.com/rnzjrefinery | not shown, 2025-2026 (approx.) | 2026-11-01 | Casting-scrap dust and floor-dust recovery, Goregaon | search summary |
| 3 | Bangalore Refinery brochure | Bangalore Refinery | https://cdn.shopify.com/s/files/1/0048/7722/1988/files/Brochure.pdf?3966 | not shown | 2026-11-01 | Recovers from manufacturing wastage; collection service for scrap and sweeps; returns pure metal | search summary |
| 4 | Metal refining and recovery | Bangalore Refinery | https://bangalorerefinery.com/pages/metal-refining-and-recovery | not shown, 2025-2026 (approx.) | 2026-11-01 | Accepts meltable scrap and non-meltable powder and paste residues | search summary |
| 5 | Gujarat Gold Centre refining and why-us pages | Gujarat Gold Centre | https://gujaratgoldcentre.com/refining | not shown, 2026 (live rate in title) | 2026-11-01 | Assaying and refining scrap on process charge; page title live rate ₹15,850.86/g (basis unknown) | search summary |
| 6 | RJ Market Watch (refining business) | Retail Jeweller India | https://retailjewellerindia.com/?p=18175 | not shown, 2019 or later | 2026-11-01 | Ahmedabad family exited refining in 2019 after 28 years; refining earns 0.1-0.2% of scrap value (also cited in 07) | search summary |
| 7 | Products and services | MMTC-PAMP | https://www.mmtcpamp.com/products-services | not shown, 2025-2026 (approx.) | 2026-11-01 | Takes jewellery-industry scrap; NABL-accredited assay lab | search summary |
| 8 | Sell old gold | MMTC-PAMP | https://mmtcpamp.com/sell-old-gold | not shown, 2025-2026 (approx.) | 2026-11-01 | Melts gold in front of customers after weighing and testing | search summary |
| 9 | Augmont launches Sell Old Gold services | GJEPC Solitaire | https://gjepc.org/solitaire/?p=17257 | 2022-09 (approx.) | 2026-11-01 | Touchstone, XRF and melting; Zaveri Bazaar outlet; retail-facing | search summary |
| 10 | Representation; sampling | Sabin Metal Corporation | https://sabinmetal.com/knowledge-center/representation | not shown | 2026-11-01 | Customer or third-party representative may witness weighing, processing, sampling; customer, umpire and reserve samples (sampling point tie uncertain) | search summary |
| 11 | Introducing Alex Stewart International (60 seconds in platinum Q&A) | World Platinum Investment Council | https://platinuminvestment.com/files/sixtysecs/WPIC_60SIP__Introducing_Alex_Stewart_International_QA_08_05_2026.pdf | 2026-08-05 | 2026-11-01 | Inspectors witness weighing and sampling at refineries; materials include jewellery scrap and refinery sweeps (company's own description) | search summary |
| 12 | Spotlight on North American gold and silver refining, chapter 4 | LBMA | https://www.lbma.org.uk/publications/spotlight-on-north-american-gold-silver-refining/chapter-4-sampling-and-assaying | not shown, 2020-2026 (approx.) | 2026-11-01 | Supervision kept independent of sampling | search summary |
| 13 | How to assay sweeps (thread) | Gold Refining Forum | https://goldrefiningforum.com/threads/how-to-assay-sweeps.35859/page-2 | not shown | 2026-11-01 | Small polishing and floor sweeps usually too small to assay unless a large producer (tie uncertain between two threads) | search summary |
| 14 | Sweeps, buffings, polishings refining schedule | Midstates Recycling | https://midstatesrecycling.com/refining_schedule/sweeps-buffings-polishings | not shown, 2024-2026 (approx.) | 2026-11-01 | USD 2 per lb, USD 200 minimum, 4-6 weeks (also in 03) | search summary |
| 15 | Toll refining rate (post) | Gold Refining Forum | https://goldrefiningforum.com/goto/post?id=341548 | not shown | 2026-11-01 | Refiners need a minimum batch size | search summary |
| 16 | Schedule of charges, Mineral Processing Division, from 1 April 2026 | Indian Bureau of Mines | https://ibm.gov.in/writereaddata/files/177504605969cd0dab877ccSOC_MPD_wef_01042026.pdf | 2026-04-01 | 2026-11-01 | Gold fire assay with AAS ₹4,583 / ₹5,408 / ₹5,400; gold and silver ₹6,112 / ₹7,212 / ₹7,200; preparation ₹351 / ₹414 / ₹400 | search summary |
| 17 | Revised schedule of charges from 1 April 2025 | Indian Bureau of Mines | https://ibm.gov.in/writereaddata/files/174375231667ef8c7c52797IBM_Revised_Schedule_of_charges_MPD_w.e.f_01.04.2025.pdf | 2025-04-01 | 2026-11-01 | Gold fire assay ₹4,365 / ₹5,151 / ₹5,200 | search summary |
| 18 | Precious metals / fire assaying | Hazen Research | https://www.hazenresearch.com/node/28 | not shown, 2020-2026 (approx.) | 2026-11-01 | Gold by fire assay USD 30, USD 40 with AA finish | search summary |
| 19 | Garbage sold in Bihar worth lakhs | Patrika | https://www.patrika.com/national-news/ajab-gajab-garbage-is-being-sold-in-bihar-whose-cost-is-in-lakhs-19112079 | unclear (page header 2026-07-27) | 2026-11-01 | Shop "nyara" box averages about ₹1 lakh; buyers from other states; about 500 shops (date and details tie uncertain) | search summary |
| 20 | Nayariyas of Peshawar extract 60 tolas of gold from dirt every month | ProPakistani | https://propakistani.pk/2017/11/08/nayariyas-peshawar-extract-60-tolas-gold-dirt-every-month/ | 2017-11-08 | 2026-11-01 | Collectors pay PKR 5,000-10,000 for workshop soil (also in 07) | search summary |
| 21 | Dreams turn into dust for India's gold scavengers | Dawn (Reuters) | https://www.dawn.com/news/275095 | not shown, 2007 (approx.) | 2026-11-01 | Kadaiwallahs about 1 g after hours of work, up to ₹6,000 a month (stale) | search summary |
| 22 | Sweepers of gold | Gulf News | https://gulfnews.com/general/sweepers-of-gold-1.802734 | not shown | 2026-11-01 | Ahmedabad workshop owner buys bags of gold-flecked dirt | search summary |
| 23 | Gold scavengers | The Tribune | https://tribuneindia.com/2011/20110917/saturday/main3.htm | 2011-09-17 | 2026-11-01 | Jewellers store dust for years and sell to wholesale buyers for lakhs | search summary |
| 24 | Recycling of gold increases in Ahmedabad, 70 kg every day | Vibes of India | https://www.vibesofindia.com/?p=220720 | 2022-07 | 2026-11-01 | Background: recycling volume (stale) | search summary |
| 25 | Attero's MetalMandi crosses 2 lakh+ downloads | pv magazine India | https://www.pv-magazine-india.com/?p=14945 | 2025-2026 (approx.) | 2026-11-01 | B2B scrap marketplace exists; not gold sweeps | search summary |
| 26 | Record of cash transactions in gems and jewellery over ₹10 lakh under PMLA | RSM India | https://www.rsm.global/india/sites/default/files/media/RSM%20India/Publications/2021/rsm_india_newsflash_-_record_of_cash_transactions_in_gems_jewellery_over_and_above_rs._10_lakhs_mandatory_under_pmla.pdf | 2021 | 2026-11-01 | G.S.R. 799(E), 28 December 2020; cash of ₹10 lakh or more | search summary |
| 27 | Only purchase of jewellery above ₹2 lakh needs mandatory KYC | Business Today | https://businesstoday.in/current/economy-politics/only-purchase-of-jewellery-above-rs-2-lakh-needs-mandatory-kyc-clarifies-govt/story/427523.html | 2021-01 | 2026-11-01 | No mandatory PAN or Aadhaar under ₹2 lakh | search summary |
| 28 | Cash transaction limits under income tax: 269SS, 269T, 269ST and 40A(3) | CalcGuru | https://calcguru.in/?p=8213 | not shown, 2025-2026 (approx.) | 2026-11-01 | 40A(3) cash above ₹10,000 a day disallowed; 269ST ₹2 lakh receipt limit, penalty equal to amount (secondary) | search summary |
| 29 | Press release on reverse charge | CBIC | https://cbic-gst.gov.in/pdf/press-release/Press-Release-Reverse-Charge.pdf | 2017 | 2026-11-01 | Old gold from individuals not under reverse charge; unregistered supplier of ornaments to registered buyer under reverse charge (2017 position) | search summary |
| 30 | Forum issue on reverse charge after 2019 | TaxTMI | https://www.taxtmi.com/forum/issue?id=118582 | not shown, 2019 or later | 2026-11-01 | Section 9(4) narrowed from 1 February 2019; forum opinion (tie uncertain) | search summary |
| 31 | Article on job-work waste and scrap | TaxTMI | https://www.taxtmi.com/article/detailed?id=13410 | not shown | 2026-11-01 | Waste belongs to principal unless agreed; 143(5) sale by registered job worker on payment of tax (secondary; tie uncertain across TaxTMI and ICMAI items) | search summary |
| 32 | IGPC-funded project final report on karigars | IIM Ahmedabad | https://www.iima.ac.in/sites/default/files/2024-04/IGPC%20funded%20project%20BVIIMAJKJXLRI-%20Final%20Report%20June2023%20%281%29.pdf | 2023-06 | 2026-11-01 | Karigar sector informal; figures not seen | search summary |
| 33 | GST makes for more cash deals, consolidation in jewellery sector | Business Standard (PressReader) | https://www.pressreader.com/india/business-standard/20180510/282046212734255 | 2018-05-10 | 2026-11-01 | GFMS survey: cash deals, only making charges billed | search summary |
| 34 | Golden rule: always take GST receipt for gold purchases | Outlook Money | https://www.outlookmoney.com/gold/golden-rule-always-take-gst-receipt-for-gold-purchases-heres-why | not shown, 2024-2026 (approx.) | 2026-11-01 | About 14% of recent buyers took no GST receipt (LocalCircles) | search summary |
| 35 | Low-grade sweeps refining | Elemetal | https://elemetal.com/refining/low-grade-sweeps | not shown, 2024-2026 (approx.) | 2026-11-01 | Background: refiners abroad take sweeps at many locations | search summary |
| 36 | Augmont launches Buyer Bazar | SME Street | https://smestreet.in/infocus/augmont-launches-buyer-bazar-indias-1st-dedicated-jewellers-buyer-seller-networking-hub | 2022 | 2026-11-01 | Refiner-led jewellers' hub (also in 07) | search summary |
| 37 | FizTrade / FizRefinery | Dillon Gage | https://classic.fiztrade.com | not shown, 2024-2026 (approx.) | 2026-11-01 | Refining clients track lots and view assay results online | search summary |
| 38 | Kalkata Gold about us | Kalkata Jewels | https://sites.google.com/view/kalkatajewels/about-us | 2021 (launch stated) | 2026-11-01 | Online B2B jewellery platform; no refiner bidding seen | search summary |
| 39 | Raw Gold Waste Management Private Limited | Tofler | https://www.tofler.in/raw-gold-waste-management-private-limited/company/U90000GJ2020PTC112087 | 2020-01-14 (incorporation) | 2026-11-01 | Rajkot company; activity unknown | search summary |
