# Hunt A: Money already wasted

Specialist: Opportunity Hunter. Date: 2026-10-31. Lens A: costly inefficiency, workarounds, losses, rework, penalties, middlemen.

Method and limits. I ran 59 web searches. WebFetch failed on the one page I tried (taxguru.in did not resolve in this session), so I opened no pages. Every source below was seen only through search-result summaries and is marked `search summary`. The summaries sometimes did not tie a figure to one exact URL; where that happened, the Sources table says so. I did not contact any buyer. Nothing here is above demand level L1.

Constraints used: founder capital ₹5,00,000 and founder time at ₹750 per hour, both taken from the brief [A]. Currency conversions use ₹88 per USD and ₹0.31 per PKR as of 2026-10-31 [A] (basis: approximate recent levels, not checked in this run; test against the RBI reference rate).

## 1. Industries chosen and why

I chose four operations-heavy industries that share no buyers, inputs, or technology. None is a common startup theme.

**Gold jewellery manufacturing (karigar workshops and the wholesalers who issue them gold)**
- Gold is lost as dust, filings, and sludge at every bench, and the trade already pays for workarounds: a 2-3% loss allowance to karigars [S2] and informal sweepers who buy workshop dust [S15, S19].
- What changed: the price of each lost gram rose about 39% between October 2025 (₹1,24,160 per 10 g [S6]) and January 2026 (MCX near ₹1.72 lakh per 10 g [S7]) [I], and DGFT tightened export loss allowances from 1 January 2025 [S3].

**Textile wet processing (job-work dye houses)**
- Re-dyeing a failed lot adds 70% to 200% to the cost of the first dyeing [S34, S35], and some Indian mills still re-process 8-10% of output for shade [S32].
- What changed: in 2026 dye-house input costs rose sharply. Tirupur dyers raised charges by ₹10-20 per kg in May 2026 [S39], and Surat mills saw imported coal rise about 25% in March 2026 [S48]. Each re-dye now costs more [I].

**Metal casting foundries (small induction-melting foundries)**
- Induction foundries use 700-2,000 kWh per tonne of finished casting [S53], against a CII norm of 620 kWh per tonne of liquid metal [S54, S55]. Excess maximum demand is billed at 150% of the demand charge in Maharashtra [S57].
- What changed: demand charges are rising. Tamil Nadu has a proposal to raise them from ₹350 to ₹600 per kVA per month [S63]. The EU also proposes to extend CBAM to downstream metal goods from 2028 [S79], which would make energy data a sales requirement for exporters [I].

**Container import logistics (detention and demurrage)**
- Container detention costs Indian traders a reported ₹4,200 crore a year (unsourced vendor figure) [S89]. Exporters told DG Shipping in April 2026 that some cumulative charges reach 60-70% of cargo value [S84].
- What changed: DG Shipping held a stakeholder meeting on 17 April 2026 [S84] and issued an advisory against exorbitant charges [S85]. In the US, a billing rule for these charges took effect on 28 May 2024 [S91].

## 2. Raw candidates

| # | Problem | Payer | Signal | Tag |
|---|---|---|---|---|
| J1 | Gold process loss in workshops is not measured and not recovered | Gold-issuing wholesaler or workshop owner | Real loss 0.5-2% vs 5-12% billed [S1]; dust sold to sweepers at 10-40% below value [S19] | [S1, S19] |
| J2 | Karigars divert or abscond with gold issued for job work | Wholesaler or manufacturer | Four Zaveri Bazaar cases from ₹98.07 lakh to ₹2.66 crore, 2025-26 [S10, S11, S12, S13] | [S10, S13] |
| J3 | Gold issue, receipt, and loss tracking stays on paper | Manufacturer | Several ERPs already sell karigar loss modules [S14] | [S14] |
| D1 | Shade failures force strip-and-re-dye in job-work dye houses | Dye-house owner | Shade re-process target of 10.16% cut to 8.0% in a job advert [S32] | [S32] |
| D2 | Incoming dye strength varies and small units cannot test it | Dye-house owner | Small processors may lack QC labs for incoming dyes [S37] | [S37] |
| D3 | Coal and gas cost spikes squeeze Surat processors | Process-house owner | Imported coal up about 25% in days; 2-day weekly closures for about 350 units [S48, S49] | [S48, S49] |
| D4 | ZLD effluent treatment cost per litre | Dye house via CETP | Over ₹150 per m3 treated [S42] | [S42] |
| F1 | Melt-shop electricity waste and excess-demand penalties | Foundry owner | Measured 12.9-21% above the CII norm [S54]; 150% penal demand rate [S57] | [S54, S57] |
| F2 | Casting rejection of 8-27% | Foundry owner | Kolhapur part at 13%, rising to 18% in one month [S72]; 27% cut to 9.79% [S73] | [S72, S73] |
| F3 | CBAM default emission values penalise exporters with no data | Exporting foundry | Default mark-ups of 10% (2026), 20% (2027), 30% (2028) [S78] | [S78] |
| F4 | Waste foundry sand disposal | Foundry owner | Kolhapur cluster spent ₹16 crore and ₹14 crore on reclamation plants [S82] | [S82] |
| L1 | Container detention overbilling and ignored waivers | Importer or exporter | Charges up to 60-70% of cargo value in some cases [S84] | [S84] |
| L2 | CFS overcharging on ground rent and handling | Importer | A CFS agreed to refund overcharges after a 2018 customs committee review [S95] | [S95] |

I investigated J1 (with J2 folded in), D1, F1, F2, F3 and L1 in depth. I kept three.

## 3. Opportunity theses

### Thesis 1: Gold lost in karigar workshops is neither measured nor recovered

**Problem.** Gold handed to karigars for job work comes back as jewellery that weighs less. The gap includes real process loss (dust, filings, polishing sludge, wash water), gold kept by karigars beyond their real loss, and sometimes outright diversion. The owner of the gold cannot tell these three apart, so the gap is paid for without checking.
- The trade pays karigars a loss allowance of about 2-3% of weight [S2]. One jeweller says a well-run workshop's real loss is 0.5-2%, while customers are billed 5-12% "wastage" [S1]. This is one seller's claim, not an audit.
- Keeping gold beyond the real loss is established practice. A West Bengal GST advance ruling treats retained gold as part of the job worker's taxable consideration [S23].
- Export manufacturers face hard limits. DGFT norms from 1 January 2025 allow 2.25% loss for handmade gold jewellery, 0.45% for machine-made, 4% for handmade studded, and 2.8% for machine-made studded [S3]. One summary gives a conflicting 0.90% for machine-made plain [S5]. I trust S3 more because it gives the full schedule with a notice number (30/2024-25), but neither was opened.

**Who pays, who uses, who can block.**
- Economic buyer: the wholesaler or manufacturer who issues gold and pays the loss allowance. Second buyer: the owner of a larger workshop with 10 or more karigars [I, from S2 and S23].
- User: the workshop manager or head karigar who weighs metal in and out [A] (basis: trade practice described in S29; test in interviews).
- Blockers: karigars, who lose retained gold and sweepings income; the contract dust collectors who buy sweepings [S19]; owners who do not want outsiders to see metal flows [S20].

**Current alternatives and what buyers spend on them.**
- Informal recovery. Kolkata has hereditary dust panners ("newaras") who work the sludge from about 2,000 workshops [S15]. An Ahmedabad firm recovered 30 kg of gold from 3 tonnes of sweepings collected over years [S16]. Sweepings are sold to collectors at 10-40% below market value [S19]. A Delhi shop sells a year's dust at ₹1,000-2,000 per sack [S18]. In Peshawar, sweepers pay PKR 5,000-10,000 (about ₹1,550-3,100 [A]) a month for one workshop's dirt [S17]. That someone pays for the dirt shows real gold is in it [I].
- Equipment. A jewellery polishing machine with dust collector is listed at ₹4,72,000 including 18% GST [S26]. A US wash-water gold recovery system sells for USD 6,610 (about ₹5.8 lakh [A]) [S27], and one replacement filter costs USD 440 (about ₹38,700 [A]) [S28].
- Refiner services. Indian refiners advertise recovery from floor dust and setting-tank dust [S30]. In the US, the refiner Pease & Curren sells loss-prevention audits; one audit found a missed maintenance step costing a client USD 8,000-10,000 a year [S25].
- Software. Joolet and other jewellery ERPs track gold issued to karigars, returns, and loss percentages [S14]. No public prices were found [S14].
- Indian refining charges and recovery yields for sweeps: not found after 3 searches (queries: "gold refinery India jewellery manufacturing waste sweeps refining charges percentage recovery Rajkot Mumbai", "goldsmith workshop sweepings sold price per bag India", "gold recovery wash water filter jewellery workshop India system price").

**Frequency and cost of the problem to the buyer.**
- The loss happens every working day at every bench [K].
- Worked example: a workshop handling 2 kg of gold a month [A] (basis: a 10-20 karigar workshop; test by asking 5 owners) with 0.5-2% real loss [S1] loses 10-40 g a month. At ₹14,000 per gram [A] (basis: below the 2026 prices of ₹1,53,540 to ₹1,68,717 per 10 g in S8 and S9; test against IBJA on the day), that is ₹1.4-5.6 lakh a month [I].
- Loss can be cut. A Thai factory audit cut loss in soldering from 3.99% to 3.13% and in stone setting from 2.84% to 1.94% [S24]. If a workshop cuts total loss by 0.3 percentage points [A] (basis: about a third of the gains per stage in S24; test with one pilot), it saves 6 g a month at 2 kg throughput, worth about ₹84,000 a month [I].
- Diversion losses come in larger, rarer amounts. Mumbai police registered cases of ₹98.07 lakh [S10], ₹1.15 crore [S11], ₹1.25 crore [S12] and ₹2.66 crore [S13] in 2025-26.

**Why now.**
- Each gram lost is worth far more than a year ago: ₹1,24,160 per 10 g on 10 October 2025 [S6], against MCX near ₹1.72 lakh on 28 January 2026 [S7]. Later 2026 reports conflict (₹1,53,540 in Bengaluru on 24 April [S8]; ₹1,68,717.60 on a rate page dated 25 May [S9]). I did not find an October 2026 price.
- Export loss allowances were cut from 1 January 2025 [S3], after a sharper cut was proposed in May 2024 and then suspended [S4].
- Only HUID-hallmarked gold jewellery may be sold from 1 April 2023 [S22], which pushes the trade towards per-piece records [I].

**Why unsolved.** Category (d), a trust barrier, with (e), fragmented buyers.
- Owners and karigars both gain from opacity: karigars keep retained gold [S23] and sweepings income [S19]; owners pass "wastage" on to customers [S1] [I].
- Units are closely held family firms that are reluctant to share financial information [S20].
- Diversion risk makes owners wary of any outsider near the metal [I, from S10-S13].
- It is not technically hard. Capture methods (water-filtered dust collectors, wash-water traps) are standard [S27, S29].
- Not reason (a): the money is visible, and people already pay for the dirt [S17, S19].

**Competitors, including failed attempts.**
- Informal sweepers and refiners [S15, S16, S30]; ERP vendors [S14]; equipment sellers [S26, S27].
- Alchemy Recyclers (Bharuch) is listed on a government portal as commercialising a plant that recovers precious metal from e-waste and jeweller waste [S30].
- No Indian firm selling independent loss audits to workshops was found after 3 searches (queries: "gold loss audit jewellery manufacturing consultant metal loss reduction", "jewellery workshop gold dust recovery service India startup", "karigar ghat gold loss allowance job work wholesaler"). No failed attempts were found either. That absence is not evidence of opportunity.

**Barrier for a small new entrant, and the way in.**
- Barriers: trust; liability for handling gold-bearing waste; credible assays; karigar resistance [I].
- Way in: start with no hardware. Sell a fixed-fee monthly metal-balance audit to gold-issuing wholesalers: weigh in, weigh out, sample assays at a hallmarking centre or refiner, and a per-karigar loss report [A] (basis: the wholesaler pays the allowance [S2], so they gain directly; test with 10 wholesalers). Then add capture hardware with a partner refiner on a share of recovered gold [A].
- Test under ₹50,000: one 0.01 g precision balance plus assay fees for one month at two workshops [A] (basis: equipment prices not checked in this run; get quotes).

**Reachable buyer pool (bottom-up).**
- Kolkata has about 2,000 workshops [S15]. A trade article in the same search gave about 6,000 units, but I could not tie that figure to one URL, so I did not use it.
- If 10-20% of Kolkata workshops have 10 or more karigars [A] (basis: NCAER describes mostly small family units [S20]; test by a cluster walk), that is 200-400 units [I]. Mumbai, Coimbatore and Thrissur together are assumed to add about the same number [A] (basis: no count found; test with association rolls). Total: 400-800 reachable units [I].
- Revenue per client at a 15-25% share of a 0.3-point loss cut at 2 kg a month: ₹12,600-21,000 a month [I]. Twenty clients would bring in ₹2.5-4.2 lakh a month [I].
- About 60-65% of Indian jewellery is handmade (World Gold Council estimate, about 2017) [S21]. Handmade work loses more gold [S1], so it is the target segment [I].

**Demand evidence level.** L1, moderate, not strong. Several independent sources show money spent on the problem: dust bought by sweepers [S17, S19], equipment [S26], ERP loss modules [S14], and loss allowances [S2]. But no source shows an Indian buyer paying a third party to reduce loss.

**What would make this large.** Becoming the trusted record of metal flows between gold owners and karigars, which could support loss-based pricing, insurance, or credit [A]. Silver is a next step: HUID became mandatory for hallmarked silver from 1 September 2025 [S99].

**What would kill it.**
- Real loss in target workshops already below 0.5% (common in machine-made work [S1]), leaving little to recover [I].
- Owners refusing outsiders after the 2025-26 fraud cases [S10, S13].
- Karigars leaving for workshops that do not audit [A].
- A sharp fall in the gold price [I].

**Confidence.** Medium that the loss is real and valuable (several independent sources). Low that owners will pay an outsider (no direct evidence).

### Thesis 2: Shade failures force costly re-dyeing in job-work dye houses

**Problem.** When a dyed lot misses the buyer's shade, the dye house strips and re-dyes it, or adds dye and runs again. This repeats the water, steam, dye, chemical, and effluent cost, and uses machine time that could have carried a new lot.
- Re-dyeing adds 170-200% to the first dyeing cost (Bangladesh trade article) [S34]. One summary of an NMIMS study gave 170% [S35]; another summary of the same study gave 70% [S35]. I could not open it, so I use 70% as the conservative case and 170% as the base case.
- Performance varies widely. A Tirupur exporter's own dye house reports 97.4% right-first-time and 1.2% rework [S31] (self-reported, best in class). A Delhi-area employer wants shade re-processing cut from 10.16% to 8.0% [S32]. Another wants internal re-dyeing cut from 1.66% to 0.5%, with a 90% bulk-to-bulk right-first-time target [S33].

**Who pays, who uses, who can block.**
- Payer: the job-work dye-house owner, who usually absorbs re-dye cost [A] (basis: no source found; one search "job work dyeing shade rejection who pays re-dyeing cost" found only a tax case allowing 3% defects; test in interviews).
- User: the dyeing master and lab in-charge [S33].
- Blockers: dyeing masters whose judgement the service would replace [S36]; garment exporters who set the shade standard [A].

**Current alternatives and what buyers spend on them.**
- Spectrophotometers and colour-matching systems are listed at ₹1,75,000-9,00,000 [S44]. Premier Colorscan claims over 3,500 installations and has a Tirupur office [S43].
- Dye dissolving and dispensing automation is listed at ₹2,00,000-5,00,000 [S46]. Enmos, Tecnorama and Color Service sell dye-house automation in India [S47].
- Software vendors such as iFactory market AI for shade consistency [S52] (vendor claims, unverified).
- Most of all, buyers pay with rework itself and with experienced dyeing masters. Job adverts ask for 10 or more years' experience in consistent shade matching [S36].

**Frequency and cost of the problem to the buyer.**
- It happens daily in every running dye house [I, from S32 and S33].
- Worked example: a unit dyeing 3 tonnes a day [A] (basis: the cluster dyes 400-2,800 t a day [S41] across about 450 units [S41], an average of 0.9-6.2 t; test with consent records) that re-processes 8% [S32] re-dyes 240 kg a day. If the variable cost of a first dyeing is ₹60 per kg [A] (basis: older charges of ₹70-120 per kg [S40] plus the 2026 rise of ₹10-20 [S39], minus margin; test with three unit owners), re-dyeing costs ₹42-102 per kg [I]. That is ₹10,080-24,480 a day, or ₹30-73 lakh a year over 300 days [I].
- Cutting re-processing by 2 points saves ₹7.6-18.4 lakh a year [I].
- Each re-dye in Tirupur also passes through ZLD treatment, which costs over ₹150 per m3 [S42] [I].

**Why now.**
- Dyers raised charges by ₹10, ₹15 and ₹20 per kg for light, medium and dark shades in May 2026 [S39] because inputs rose [S39].
- Surat mills raised job-work charges 15% after imported coal rose about 25% [S48], and the processors' association approved 2-day weekly closures affecting about 350 units [S49].
- Higher input cost per kg means each failure costs more [I].
- A coloration skills shortage is reported internationally [S38], which weakens reliance on master dyers [I].

**Why unsolved.** Category (e), fragmented buyers nobody serves well, with some (b), technical difficulty.
- Instruments exist [S43, S44], yet rework persists [S32]. The causes are process variables: dye strength, dispensing errors, chemicals, water [S36]. A device alone does not fix them [I].
- Small processors may lack labs to test incoming dyes [S37], even though Indian test methods exist (IS 7845:2022 for reactive dye strength [S100]).
- Vendors sell equipment, not outcomes [I, from S46 and S47].
- Not reason (a): the rework is paid for daily [S32].

**Competitors, including failed attempts.**
- Instrument and automation vendors [S43, S45, S47]; AI software vendors [S52]; KBCols, a seed-funded Indian colour-science startup [S50]; STCH, which raised USD 7 million in April 2026 for AI-led textile R&D and contract manufacturing (about ₹61.6 crore [A]) [S51].
- Datacolor calls Tirupur, Ludhiana, Surat and Ichalkaranji emerging markets [S45]. That suggests instruments are not yet saturated there [I].
- Failed attempts: none found after 1 search (query: "dyeing shade matching startup India AI dye house software funding OR shut down"). That is thin. It needs more disconfirming search.

**Barrier for a small new entrant, and the way in.**
- Barriers: incumbent instrument makers; dyeing-master resistance; the textile chemistry skill needed for credibility [I].
- Way in: an outcome-priced re-dye reduction service for 5-10 job-work units in one cluster. Log every failed lot's causes (incoming dye strength per IS 7845 [S100], water hardness, dosing, liquor ratio), use the unit's existing instruments, and charge a fixed monthly fee with a bonus tied to measured re-process rate [A] (basis: unmet gap between instruments and outcomes [I]; test with three units for 60 days).
- Test under ₹50,000: lab consumables and travel for a 60-day pilot in Tirupur [A].

**Reachable buyer pool (bottom-up).**
- Tirupur has about 450 dye units linked to 18 ZLD CETPs [S41]. Older counts were 729-733 [S40].
- If 40% are mid-size job-work units open to a pilot [A] (basis: no split found; test with the Dyers Association), that is about 180 units [I].
- At ₹20,000-30,000 a month per unit [A], 15 units bring in ₹3-4.5 lakh a month [I].
- Surat, Ludhiana, Erode and Ichalkaranji add further clusters; no counts were checked [A].

**Demand evidence level.** L1, moderate. Buyers already spend on instruments [S43] and on hiring for right-first-time [S32, S33]. No source shows Indian dye houses paying for an outcome-based service.

**What would make this large.** A cross-unit database of failure causes and dye-lot strengths, sold to dye makers and brands as a supplier quality record [A]. The same approach could extend to yarn dyeing in Surat [S39].

**What would kill it.**
- Mid-size units already above 95% right-first-time, like the exporter in S31 [I].
- Re-dye costs passed on to garment exporters, so dyers do not care [A].
- An instrument vendor bundling a free service [I].
- The 70% cost case: at ₹7.6 lakh a year of savings [I], a ₹3.6 lakh annual fee takes 47% of the gain, which is hard to sell [I].

**Confidence.** Medium that the cost is real. Low on the price buyers will pay, and on whether the founder can earn trust without dyeing credentials.

### Thesis 3: Small induction foundries waste melt-shop electricity and pay demand penalties

**Problem.** Many small induction foundries use more electricity per tonne than good practice needs, and some exceed their contract demand and pay penal rates.
- A study of four foundries measured 700-750 kWh per tonne, 12.9-21% above the CII norm of 620 kWh per tonne of liquid metal [S54, S55].
- BEE puts induction foundries at 700-2,000 kWh per tonne of finished casting [S53].
- The waste comes from daily practice: holding molten metal, open lids, charge density, and unplanned scheduling [K]. One Gujarat foundry paper estimated that lid insulation and covers alone could save about 152,100 kWh a year [S71] (an estimate, not a measurement).

**Who pays, who uses, who can block.**
- Payer: the foundry owner, who pays the electricity bill [K].
- User: the melt-shop supervisor and furnace operators [K].
- Blockers: furnace makers' service teams, operators who resist shift discipline, and DISCOM rules on meter access [A] (basis: not checked; test with two foundries).

**Current alternatives and what buyers spend on them.**
- Maximum demand controllers are listed at roughly ₹9,000-25,000 in Mumbai [S67].
- Energy audits are often subsidised. TERI audited the Rajkot cluster and estimated about 15% energy-cost savings [S56]. MEDA did walk-through audits at more than 40 Kolhapur foundries [S53].
- Digital furnace monitoring is starting. Indofen deployed Siemens Industrial Edge [S68].
- Performance contracting has struggled. About 139 ESCOs were registered, few were active, and dispute resolution was a major barrier [S69]. BEE notes a lack of information on the savings that interventions actually produce [S70].

**Frequency and cost of the problem to the buyer.**
- Electricity is used on every melt, every day [K].
- Worked example: a foundry melting 5-8 t a day [A] (basis: Kolhapur's about 650,000 t a year [S72] over 200 or more units [S53] averages up to about 11 t of castings a day [I]; test with two foundries) that saves 40-80 kWh per tonne [I] (basis: half to all of the 80 kWh gap between 700 and 620 [S54]) over 300 days, at ₹6.70-8.20 per unit [S60, S61], saves ₹4.0-15.7 lakh a year [I]. A July 2025 state comparison cites ₹9.04 for Tamil Nadu and ₹8.98 for Gujarat, on an unclear basis [S62]. So the range may be low for those states [I].
- Demand penalties come on top. Exceeding contract demand by 100 kVA in one month at ₹400 per kVA [S61] billed at 150% [S57] costs ₹60,000, of which ₹20,000 is penalty [I]. Kerala adds 50% on excess demand [S58]. Uttarakhand industries complained that penalties were imposed arbitrarily [S59].

**Why now.**
- Demand charges are rising: a Tamil Nadu proposal goes from ₹350 to ₹600 per kVA per month [S63], and Karnataka moved to higher fixed charges with lower energy charges [S60]. Higher fixed charges make demand control worth more [I].
- The EU Commission proposed on 17 December 2025 to extend CBAM to downstream goods [S79]. The Parliament wants 457 product types and the Council about 200, from 2028 [S79]. If castings are added, exporting foundries will need measured energy data [I].
- Cheap clamp-on power logging and cloud dashboards make continuous monitoring affordable for small units [K].

**Why unsolved.** Category (e), fragmented buyers, with (d), a trust barrier.
- One-off audits produce reports, but the savings depend on daily shop-floor behaviour [K].
- Shared-savings contracts fail on measurement disputes [S69, S70].
- Most of the industry is small: about 90% MSME [S66]. Many Kolhapur foundries turn over ₹10 crore or less [S53].
- Not clearly reason (a). The bills are large, but subsidised audits may have taught owners to expect advice for free [I].

**Competitors, including failed attempts.**
- Demand-controller sellers [S67]; subsidised auditors (TERI, MEDA, BEE) [S53, S56]; Siemens through furnace makers [S68]; ESCOs, mostly inactive [S69].
- Furnace makers' own monitoring: not found after 1 search (query: "induction furnace energy monitoring IoT foundry India startup OR OEM digital melt shop Electrotherm Megatherm Inductotherm").
- Failed ESCO attempts are documented in aggregate [S69], not by name.

**Barrier for a small new entrant, and the way in.**
- Barriers: metallurgical and electrical credibility; safe metering; owners' distrust of savings claims [I].
- Way in: non-invasive clamp-on logging on furnace feeders, plus a weekly melt-practice scorecard (kWh per tonne by shift, holding minutes, demand peaks) for a fixed monthly fee, not shared savings, so there is nothing to dispute [A] (basis: the dispute barrier in S69; test with three foundries).
- Test under ₹50,000: rent or buy one logger, run 30 days at one foundry, and compare against the bills [A] (basis: logger prices not checked; get quotes).

**Reachable buyer pool (bottom-up).**
- India has about 4,500-5,000 foundries [S64, S65]. About 43% of castings come from induction furnaces [S66]. Small foundries mostly use coke-fired cupolas [S66].
- Rajkot has more than 350 foundries [S56] and Kolhapur more than 200 small foundries [S53]. If half are induction units [A] (basis: S66 output share; test with cluster association lists), that is about 275 units in two clusters [I].
- At ₹10,000-20,000 a month [A], 20 clients bring in ₹2-4 lakh a month [I].

**Demand evidence level.** L1, weak to moderate. Foundries buy demand controllers [S67] and take part in audits [S53, S56]. Paid spending on ongoing energy services was not shown.

**What would make this large.** Selling verified energy and emissions data to exporting foundries if CBAM's downstream extension covers castings [S79]. Adding casting-rejection analytics on the same data (see cut F2) [I].

**What would kill it.**
- Real excess below 40 kWh per tonne in target foundries [I].
- Furnace makers bundling free monitoring [A].
- Owners refusing to pay for what audits gave them free [I].
- Power-cut-driven, irregular melting that no practice change can fix [A].

**Confidence.** Low to medium. The physics and the tariffs are solid. Willingness to pay is unproven, and the ESCO history is a warning.

## 4. Cut candidates and reasons

- **J2 karigar diversion.** Folded into Thesis 1. The same buyer, the same measurement, and on its own it is a police and insurance problem [S10, S13].
- **J3 jewellery ERP.** Crowded with Joolet, GehnaERP, SocioLedger, OMGOLD and Auric [S14]. Software alone does not stop physical loss [I].
- **D2 dye strength variation.** Folded into Thesis 2 as a root cause. On its own it is a testing service with public standards [S100].
- **D3 Surat energy price spikes.** An input-price problem, not waste. The fixes are fuel switching and tariffs, outside a small entrant's reach [S48].
- **D4 ZLD treatment cost.** Run collectively through CETPs, capital-heavy and regulated [S41, S42].
- **F2 casting rejection.** A real cost (13-27% rejection in published cases [S72, S73]). Simulation cut one foundry's rejection from 8.5% to 3.5% [S74], and auto OEMs raise quality-reject debit notes on suppliers [S77]. But it is crowded. AutoCAST is sold as affordable for small foundries [S75], Aganita claims hundreds of foundry clients [S76], and Hitachi ADSTEFAN and others sell simulation. It needs deep methoding skill. Kept as a possible extension of Thesis 3.
- **F3 CBAM for castings.** I could not confirm that cast iron or steel articles (CN 7325) are in the current scope after 1 search. The downstream extension is not settled and would start in 2028 at the earliest [S79]. Consultancies already sell CBAM services [S81], and the government may reimburse up to 90% of small steel exporters' certification costs [S80], which would steer buyers to subsidised providers.
- **F4 waste foundry sand.** Needs cluster-scale plants costing ₹14-16 crore [S82], far beyond the founder's capital. Public bodies (CSIR-CRRI with IIF) are already working on reuse in road building [S83].
- **L1 container detention.** Large but crowded. Forwarding platforms and tools already track detention exposure [S89, S97, S98]. Tariffs are set by the lines and paid at release [S86, S87, S88], so importers have little leverage. Carriers employ dedicated D&D invoicing staff [S92]. The volume is large (JNPA alone handled about 7.9 million TEU in 2025 [S93]), but it is not spread across fragmented, unserved buyers. Waivers after customs holds are legal work [S96]. No Indian third-party detention recovery service was found after 2 searches (queries: "freight audit recovery service India importers overcharges shipping line invoices contingency fee D&D recovery", "startup detention demurrage India platform shut down OR raised funding"), so I have no evidence of willingness to pay. The reported ₹4,200 crore figure is unsourced [S89], and the ₹3,500 crore demurrage figure is also a vendor claim [S90].
- **L2 CFS overcharging.** Spread thin, handled through customs committees and courts [S95]. Port-level levy fights in 2026 are between ports and CFS operators [S94], not open to a small entrant.

## 5. Sources

All sources were seen through search-result summaries only. No page was opened. Retrieved means the date of the search.

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Gold wastage vs making charges, Nagpur | Londe Jewellers | https://londejewellers.com/guides/gold-wastage-vs-making-charges-nagpur | not shown | 2026-10-31 | Real loss 0.5-2% vs billed 5-12% (seller claim) | search summary |
| 2 | Manufacturers discuss impact of low labour to artisans | Retail Jeweller India | https://retailjewellerindia.com/manufacturers-discuss-impact-of-low-labour-to-artisans-suggest-measures-to-curb-the-outcome | not shown | 2026-10-31 | 2-3% loss allowance paid to karigars | search summary |
| 3 | Govt revises wastage, input-output norms for gold, silver jewellery exports | Daily Excelsior | https://www.dailyexcelsior.com/?p=1860208 | 2024-11 (approx.) | 2026-10-31 | DGFT PN 30/2024-25 loss norms, effective 2025-01-01 | search summary |
| 4 | Govt puts on hold new wastage norms for gold, silver jewellery exports | Outlook Business | https://www.outlookbusiness.com/news/govt-puts-on-hold-new-wastage-norms-for-gold-silver-jewellery-exports-till-july-31 | 2024 | 2026-10-31 | May 2024 cut and suspension | search summary |
| 5 | DGFT notifies revised wastage limits, input norms for jewelry exports | TaxGuru | https://taxguru.in/dgft/dgft-notifies-revised-wastage-limits-input-norms-jewelry-exports.html | not shown | 2026-10-31 | Conflicting 0.90% figure (page fetch failed) | search summary |
| 6 | Gold prices in India hit record highs on October 10 | Free Press Journal | https://www.freepressjournal.in/business/gold-prices-in-india-hit-record-highs-on-october-10-2025-24k-gold-crosses-12400gram-as-mcx-futures-rise-sharply | 2025-10-10 | 2026-10-31 | ₹1,24,160 per 10 g | search summary |
| 7 | Daily recap 28 Jan 2026 | GoldMeter | https://goldmeter.in/news/recap/daily-recap-28-jan-2026 | 2026-01-28 | 2026-10-31 | MCX gold near ₹1.72 lakh | search summary |
| 8 | Gold rate today April 24, IBJA rate | Oneindia | https://www.oneindia.com/business/gold-rate-today-april-24-ibja-rate-24k-22k-18k-prices-edge-lower-in-bengaluru-8067969.html | 2026-04-24 | 2026-10-31 | ₹1,53,540 per 10 g, Bengaluru | search summary |
| 9 | India gold rate today | Shekhawati Live | https://shekhawatilive.com/india-gold-rate-today | 2026-05-25 (as shown) | 2026-10-31 | ₹1,68,717.60 per 10 g (weak source) | search summary |
| 10 | 2 Zaveri Bazaar gold artisans flee with jewellery worth ₹98.07 lakh | Free Press Journal | https://www.freepressjournal.in/mumbai/mumbai-crime-2-zaveri-bazaar-gold-artisans-flee-with-jewellery-worth-9807-lakh-case-registered | 2026-01 | 2026-10-31 | Diversion case | search summary |
| 11 | 2 gold artisans booked for cheating traders of ₹1.15 crore | Free Press Journal | https://www.freepressjournal.in/mumbai/mumbai-crime-2-gold-artisans-booked-for-cheating-traders-of-115-crore-in-pydhonie-zaveri-bazaar-both-accused-absconding | 2025-12 | 2026-10-31 | Diversion case | search summary |
| 12 | 2 artisans allegedly flee with gold jewellery worth ₹1.25 cr | Free Press Journal | https://www.freepressjournal.in/mumbai/2-artisans-allegedly-flee-away-with-gold-jewellery-worth-125-cr-from-mumbais-zaveri-bazaar-search-operation-launched | 2025-03 | 2026-10-31 | Diversion case | search summary |
| 13 | Goldsmith booked for ₹2.66 crore fraud | Free Press Journal | https://www.freepressjournal.in/mumbai/mumbai-crime-news-goldsmith-booked-for-266-crore-fraud-absconds-with-26kg-of-gold | 2025-08 | 2026-10-31 | Diversion case | search summary |
| 14 | Joolet ERP | Joolet | https://joolet.com/ | not shown | 2026-10-31 | Karigar issue, receipt and loss modules; no public prices | search summary |
| 15 | Kolkata's gold scavengers reap rewards at Diwali | Gulf News | https://gulfnews.com/world/asia/india/kolkatas-gold-scavengers-reap-rewards-at-diwali-1.1402369 | not shown | 2026-10-31 | About 2,000 Kolkata workshops; dust panners | search summary |
| 16 | Gold scavengers | The Tribune | https://tribuneindia.com/2011/20110917/saturday/main3.htm | 2011-09-17 | 2026-10-31 | 30 kg gold from 3 t of sweepings, Ahmedabad | search summary |
| 17 | Workers in Peshawar save gold from going down the drain | Geo TV | https://www.geo.tv/latest/166463-workers-in-peshawar-save-gold-from-going-down-the-drain | not shown | 2026-10-31 | Sweepers pay PKR 5,000-10,000 a month | search summary |
| 18 | Delhi's gold hunters | Hindustan Times via PressReader | https://www.pressreader.com/india/hindustan-times-delhi/20180617/281646780853873 | 2018-06-17 | 2026-10-31 | Dust sold at ₹1,000-2,000 per sack (may be the companion HT page of the same date) | search summary |
| 19 | Sweepers of gold | Gulf News | https://gulfnews.com/general/sweepers-of-gold-1.802734 | not shown | 2026-10-31 | Sweepings sold 10-40% below market; contract collectors (summary did not tie the 10-40% to one URL) | search summary |
| 20 | Cluster Mapping Study of the Gems & Jewellery Sector in India | NCAER | https://ncaer.org/publication/cluster-mapping-study-of-the-gems-amp-jewellery-sector-in-india/ | 2020-10 | 2026-10-31 | Closely held units, reluctant to share financial data | search summary |
| 21 | Jewellers migrate to unorganised sector over new hallmarking rule | Business Standard | https://business-standard.com/amp/article/companies/jewellers-migrate-to-unorganised-sector-over-new-hallmarking-rule-117020600601_1.html | 2017-02 (approx.) | 2026-10-31 | 60-65% handmade (WGC) | search summary |
| 22 | Sale of gold jewellery hallmarked without 6-digit code to be banned after March 31 | The Tribune | https://www.tribuneindia.com/news/business/sale-of-gold-jewellery-hallmarked-without-6-digit-code-to-be-banned-after-march-31-14980 | 2023 (approx.) | 2026-10-31 | HUID-only sales from 2023-04-01 | search summary |
| 23 | 5% GST applicable on value of part of gold retained for job work: West Bengal AAR | LiveLaw | https://www.livelaw.in/amp/news-updates/gst-value-of-part-of-gold-job-work-west-bengal-aar-222433 | not shown | 2026-10-31 | Retained gold treated as consideration | search summary |
| 24 | FMEA thesis on a jewellery plant | Chulalongkorn University | https://digital.car.chula.ac.th/chulaetd/66938 | 2007 | 2026-10-31 | Measured loss reductions by stage | search summary |
| 25 | Pease & Curren offering loss prevention audits to jewelry manufacturers | InStore | https://instoremag.com/pease-curren-offering-loss-prevention-audits-to-jewelry-manufacturers/ | not shown | 2026-10-31 | Refiner-led loss audit precedent | search summary |
| 26 | Jewellery polishing machine with dust collector | TradeIndia | https://www.tradeindia.com/products/jewellery-polishing-machine-with-dust-collector-9405114.html | not shown | 2026-10-31 | ₹4,72,000 incl. GST | search summary |
| 27 | Romanoff gold recovery system | Romanoff | https://romanoff.com/products/romanoff-gold-recovery-system | not shown | 2026-10-31 | USD 6,610 system | search summary |
| 28 | The Goldwasher | Gesswein | https://gesswein.com/cleaning/recovery-refining/the-goldwasher | not shown | 2026-10-31 | USD 440 filter | search summary |
| 29 | Procedures to recover gold from dust | Ganoksin forum | https://orchid.ganoksin.com/t/procedures-to-recover-gold-from-dust/44203 | not shown | 2026-10-31 | Indian workshop missing floor sweeps; random assay of returns | search summary |
| 30 | Integrated plant for recovery of precious metals from e-waste and jeweller waste | India Science and Technology portal | https://www.indiascienceandtechnology.gov.in/technologies/development-integrated-plant-recovery-precious-metals-e-waste-and-jeweller-waste | not shown | 2026-10-31 | Alchemy Recyclers; refiner dust services context | search summary |
| 31 | Anugraha Session 2, GIS 2018 | Global Organic Textile Standard | https://gotslive.global-standard.org/images/events/Anugraha-Session2-GIS18.pdf | 2018 | 2026-10-31 | 97.4% right-first-time, 1.2% rework | search summary |
| 32 | PPC Manager, Textile (job) | Fibre2Fashion | https://www.fibre2fashion.com/jobs/ppc-manager-textile-textile-manufacturing-production-delhi-india-114020.htm | not shown | 2026-10-31 | Shade re-process 10.16% to 8.0% target | search summary |
| 33 | Processing Manager, Textile (job) | Fibre2Fashion | https://www.fibre2fashion.com/jobs/processing-manager-textile-manufacturing-production-delhi-india-114019.htm | not shown | 2026-10-31 | 90% right-first-time; re-dye 1.66% to 0.5% | search summary |
| 34 | Right-First-Time: a necessity not a luxury | Textile Today (Bangladesh) | https://textiletoday.com.bd/right-first-time-a-necessity-not-a-luxury | not shown | 2026-10-31 | Re-dye adds 170-200% | search summary |
| 35 | Study on lab to bulk shade variation | NMIMS Shirpur | https://engineering-shirpur.nmims.edu/docs/study-on-lab-to-bulk-shade-variation.pdf | not shown | 2026-10-31 | 170% or 70% extra (summaries conflict) | search summary |
| 36 | Problems in dyeing and their remedies | Fibre2Fashion | https://www.fibre2fashion.com/industry-article/3353/problems-in-dyeing-and-their-remedies | not shown | 2026-10-31 | Causes of shade mismatch | search summary |
| 37 | Standardisation of dyes | Fibre2Fashion | https://www.fibre2fashion.com/industry-article/7674/standardisation-of-dyes | not shown | 2026-10-31 | Small processors may lack incoming QC labs | search summary |
| 38 | Textile dyeing skills shortage at crisis point | Ecotextile News | https://www.ecotextile.com/2021021527392/dyes-chemicals-news/textile-dyeing-skills-shortage-at-crisis-point.html | 2021-02 | 2026-10-31 | International coloration skills shortage | search summary |
| 39 | Tirupur hit by sharp yarn price surge | Apparel Resources | https://apparelresources.com/business-news/trade-business-news/tirupur-hit-sharp-yarn-price-surge/ | 2026-05 | 2026-10-31 | Dyers raised ₹10/15/20 per kg (may be the near-identical pulse.bot report) | search summary |
| 40 | Dyeing costs shoot up 30% as 700 Tirupur units shut shop | DNA India | https://www.dnaindia.com/business/report-dyeing-costs-shoot-up-30-as-700-tirupur-units-shut-shop-1528343/amp | 2011 (approx.) | 2026-10-31 | Older charges ₹70-120 per kg (stale); unit counts | search summary |
| 41 | Mountain of salt sludge hampers dyehouses | Ecotextile News | https://www.ecotextile.com/2022101029927/dyes-chemicals-news/mountain-of-salt-sludge-hampers-dyehouses.html | 2022-10 | 2026-10-31 | About 450 units, 18 CETPs; output 400-2,800 t a day (conflicting cluster totals) | search summary |
| 42 | Towards zero discharge | Down To Earth | https://www.downtoearth.org.in/environment/towards-zero-discharge-33489 | not shown | 2026-10-31 | ZLD over ₹150 per m3 | search summary |
| 43 | Premier Colorscan Instruments profile | IndiaMART | https://m.indiamart.com/premiercolorscan/profile.html | not shown | 2026-10-31 | Over 3,500 installations; Tirupur office | search summary |
| 44 | Colour spectrophotometer | Spectra Labtech via IndiaMART | https://m.indiamart.com/spectra-labtech/color-spectrophotometer.html | not shown | 2026-10-31 | ₹1,75,000-9,00,000 range (includes other listings) | search summary |
| 45 | We are keen on people using our technology | Textile Excellence | https://textileexcellence.com/single-news/1841/we-are-keen-on-people-using-our-technology-to-enhance-quality-of-their-products | not shown | 2026-10-31 | Datacolor sees Tirupur, Surat as emerging | search summary |
| 46 | Dyestuff dissolving system | TradeIndia | https://www.tradeindia.com/products/dyestuff-dissolving-system-c4736061.html | not shown | 2026-10-31 | ₹2,00,000-5,00,000 | search summary |
| 47 | Enmos dye house automation solutions find favour in India | Indian Textile Magazine | https://www.indiantextilemagazine.in/enmos-dye-house-automation-solutions-find-favour-in-india/ | not shown | 2026-10-31 | Automation vendors | search summary |
| 48 | Surat dyeing and printing mills raise job-work charges | Textile Insights | https://textileinsights.in/?p=22318 | 2026-03-05 | 2026-10-31 | Coal up about 25%, 15% charge rise (may be the companion 2026-03-23 page) | search summary |
| 49 | Surat textile units mull two-day weekly closure | DeshGujarat | https://deshgujarat.com/?p=276884 | 2026 | 2026-10-31 | About 350 units, 2-day closures | search summary |
| 50 | KBCols Science receives seed funding | CIOL | https://www.ciol.com/funding-kbcols-science-receives-seed-funding-chiratae-ventures-axilor-ventures-derbi-foundation | not shown | 2026-10-31 | Colour-science startup | search summary |
| 51 | Textile tech startup STCH raises USD 7M | Pulse | https://www.pulse.bot/ai/deals/textile-tech-startup-stch-raises-7m-in-pre-series-a-round-led-by-omnivore-9ef4e946-32bb-4a38-b751-b4aa142a0ced/ | 2026-04 | 2026-10-31 | Adjacent funded startup | search summary |
| 52 | Re-dyeing cost reduction | iFactory | https://ifactoryapp.com/industries/textile-manufacturing/re-dyeing-cost-reduction-root-cause-prevention-strategy | not shown | 2026-10-31 | Vendor AI competitor (claims unverified) | search summary |
| 53 | Maharashtra's clean industry plan runs into gaps in Kolhapur foundries | Down To Earth | https://www.downtoearth.org.in/amp/story/renewable-energy/maharashtras-clean-industry-plan-runs-into-funding-and-policy-gaps-in-kolhapur-foundries | not shown | 2026-10-31 | BEE 700-2,000 kWh/t; 200+ small units; MEDA audits | search summary |
| 54 | Foundry energy study | CORE | https://core.ac.uk/download/236406221.pdf | not shown | 2026-10-31 | Four foundries 700-750 kWh/t, 12.9-21% above norm (summary did not tie this to one URL; may be S55) | search summary |
| 55 | CII foundry energy paper | Foundry Informatics Centre | https://www.foundryinfo-india.org/tech_section/pdf/57ifctp12.pdf | not shown | 2026-10-31 | 620 kWh/t norm; melting 70-85% of energy | search summary |
| 56 | TERI conducts energy audit for Rajkot foundry cluster | Business Standard | https://www.business-standard.com/amp/article/sme/teri-conducts-energy-audit-for-rajkot-foundry-cluster-115051901530_1.html | 2015-05-19 | 2026-10-31 | 350+ units; about 15% savings | search summary |
| 57 | MSEDCL tariff document, Kolhapur | MSEDCL | https://www.mahadiscom.in/wp-content/uploads/2018/03/Kolhapur8_1521098535575.pdf | 2018-03 | 2026-10-31 | 150% penal rate on excess demand (one of several MSEDCL documents in results) | search summary |
| 58 | HT industrial tariff | KSEB | https://kseb.in/articledetail/eyJpdiI6IitxV3pzSGlkWCtNT2orMjI1azNibnc9PSIsInZhbHVlIjoiQ1d4SlZjV1NFQmN4K080RXUwSlRqQT09IiwibWFjIjoiZDM4ZDE0NjQ1MWIyMDY1OGY5ODIzZTE2NTZlMTBmYTk2ZDEwMTE3NmQ4NTgzYjMxZTNjMTJjM2ZhMzE5ZTQyNCIsInRhZyI6IiJ9 | not shown | 2026-10-31 | 50% extra on excess demand | search summary |
| 59 | Uttarakhand regulator document | Government of Uttarakhand (S3WaaS) | https://cdnbbsr.s3waas.gov.in/s3cf05968255451bdefe3c5bc64d550517/uploads/2025/05/202505031156926351.pdf | 2025-05 | 2026-10-31 | Complaints of arbitrary excess-demand penalties | search summary |
| 60 | Karnataka electricity tariff | The Week (PTI) | https://www.theweek.in/wire-updates/national/2025/03/27/mes21-ka-electricity-tariff.amp.html | 2025-03-27 | 2026-10-31 | ₹365/kVA, ₹6.70/unit (another report says ₹6.60) | search summary |
| 61 | Maharashtra power tariff 2026 | BharatDCIM blog | https://bharatdcim.pages.dev/blog/maharashtra-dc-power-tariff-2026 | 2026 | 2026-10-31 | ₹8.20/kVAh, ₹400/kVA (blog, weak) | search summary |
| 62 | Maharashtra set to offer India's lowest industrial power tariffs | Nagpur Today | https://www.nagpurtoday.in/maharashtra-set-to-offer-indias-lowest-industrial-power-tariffs-fadnavis/ | 2025-07-18 | 2026-10-31 | State tariff comparison (basis unclear) | search summary |
| 63 | Power tariff hike will drive away industries, warns TASMA | DT Next | https://www.dtnext.in/amp/story/news/tamilnadu/power-tariff-hike-will-drive-away-industries-from-state-warns-tasma | not shown | 2026-10-31 | Proposal ₹350 to ₹600 per kVA | search summary |
| 64 | Profile of Indian foundry industry | Institute of Indian Foundrymen | https://www.foundryinfo-india.org/profile_of_indian.aspx | not shown | 2026-10-31 | About 5,000 units | search summary |
| 65 | Indian foundries must raise castings output | Castings SA | https://castingssa.com/indian-foundries-must-raise-castings-output/ | not shown | 2026-10-31 | 4,500 foundries | search summary |
| 66 | Potential for electrifying Indian MSMEs | TERI | https://www.teriin.org/sites/default/files/2021-07/potential-for-electrifying-Indian-msme.pdf | 2021-07 | 2026-10-31 | 43% induction share; cupola common; 90% MSME | search summary |
| 67 | Maximum demand controllers in Mumbai | IndiaMART | https://m.indiamart.com/city/mumbai/maximum-demand-controllers.html | not shown | 2026-10-31 | ₹9,000-25,000 listings | search summary |
| 68 | Indofen uses Siemens Xcelerator to power smart foundries | Construction World | https://www.constructionworld.in/policy-updates-and-economic-news/indofen-uses-siemens-xcelerator-to-power-smart-foundries/76421 | not shown | 2026-10-31 | Digital furnace monitoring | search summary |
| 69 | ESCO financing: opportunities and challenges | SIDBI via SlideShare | https://www.slideshare.net/aspcv/sidbi-presentation | not shown | 2026-10-31 | 139 ESCOs, few active; dispute barrier | search summary |
| 70 | BEE SME programme presentation | IEA | https://iea.blob.core.windows.net/assets/imports/events/131/SameerPandita.pdf | not shown | 2026-10-31 | Lack of information on savings | search summary |
| 71 | Gujarat foundry energy paper | Hrcak | https://hrcak.srce.hr/file/215828 | not shown | 2026-10-31 | About 152,100 kWh/yr from lids (estimate; attribution not certain) | search summary |
| 72 | Kolhapur foundry rejection case study | Zenodo | https://zenodo.org/records/10674982 | 2023-10-30 | 2026-10-31 | 13-18% rejection; Kolhapur 650,000 t/yr | search summary |
| 73 | Gating redesign case study | Inderscience | https://www.inderscience.com/filter.php?aid=112364 | not shown | 2026-10-31 | 27% to 9.79% rejection | search summary |
| 74 | Rejection analysis of casting defect | Academia.edu | https://www.academia.edu/81358368/Rejection_Analysis_of_Casting_Defect_Using_Statical_Quality_Tools | not shown | 2026-10-31 | 8.5% to 3.5% with simulation | search summary |
| 75 | AutoCAST / FLOW+ | CSIR-NIIST | https://www.niist.res.in/ml/node/329 | not shown | 2026-10-31 | Affordable simulation for SMEs | search summary |
| 76 | Aganita Ventures profile | Populer | https://www.populer.com/aganita_ventures_private_limited-3025353/view | not shown | 2026-10-31 | Hundreds of foundry clients (self-claim) | search summary |
| 77 | OEM debit note dispute recovery, India | Terra Insight | https://www.terra-insight.com/insights/oem-debit-note-dispute-recovery-india/ | not shown | 2026-10-31 | Debit-note context (weak) | search summary |
| 78 | EU Commission finalizes CBAM benchmarks, default values | Eurometal | https://eurometal.net/eu-commission-finalizes-cbam-benchmarks-default-values-ahead-of-january-2026-launch/ | 2025 | 2026-10-31 | Mark-ups 10/20/30% | search summary |
| 79 | EU's CBAM downstream extension: the road to trilogue | Mayer Brown | https://www.mayerbrown.com/ja/insights/publications/2026/10/eus-cbam-downstream-extension-and-anti-circumvention-amendments-the-road-to-trilogue | 2026-10 | 2026-10-31 | 17 Dec 2025 proposal; 180/200/457 product types; 2028 start | search summary |
| 80 | Govt may reimburse CBAM certification costs for small steel exporters | Free Press Journal | https://www.freepressjournal.in/business/govt-may-reimburse-cbam-certification-costs-for-small-steel-exporters-under-export-scheme | 2026 | 2026-10-31 | Up to 90% reimbursement; about ₹10 lakh per firm | search summary |
| 81 | CBAM for iron and steel exporters | GreenSutra | https://greensutra.in/services/cbam-steel/ | not shown | 2026-10-31 | Consultancy competitor | search summary |
| 82 | Small foundries to commission plant for sand recycling | Foundry Planet | https://www.foundry-planet.com/d/in-small-foundries-to-commission-plant-for-sand-recycling/ | not shown | 2026-10-31 | ₹16 cr and ₹14 cr reclamation plants (attribution not certain) | search summary |
| 83 | CSIR-CRRI national effort on foundry waste | Devdiscourse | https://www.devdiscourse.com/article/law-order/3852034-csir-crri-leads-national-effort-to-convert-foundry-waste-into-sustainable-highway-infrastructure | not shown | 2026-10-31 | Waste sand context | search summary |
| 84 | BRFEDF flags systemic issues in shipping line practices | The Week | https://www.theweek.in/wire-updates/business/2026/04/27/brfedf-flags-systemic-issues-in-shipping-line-practices-urges-urgent-policy-intervention-following-dg-shipping-meeting.html | 2026-04-27 | 2026-10-31 | DGS meeting 17 Apr 2026; 60-70% of cargo value | search summary |
| 85 | Exporters name liners' opportunistic pricing | India Shipping News | https://indiashippingnews.com/?p=87553 | not shown | 2026-10-31 | DGS advisory of 9 March | search summary |
| 86 | DND charges, India import | RCL | https://rclgroup.com/pdf/Surcharge/DND/DNDCharge-IN-Imp-20241223.pdf | 2024-12-23 | 2026-10-31 | Line-set detention slabs | search summary |
| 87 | Import tariff | PIL via Mellship | https://mellship.com/Tariffs/ixe_import | not shown | 2026-10-31 | Detention slabs | search summary |
| 88 | Detention charges effective April 2026 | Ocean Network Express India | https://in.one-line.com/sites/india/files/2026-04/Detention%20charges%20eff%20Apr%2026.pdf | 2026-04 | 2026-10-31 | Free days and slabs | search summary |
| 89 | Container detention charges in India | Cogoport | https://www.cogoport.com/knowledge-center/resources/shipping-terms/container-detention-charges-equipment-usage-fees-india | not shown | 2026-10-31 | ₹4,200 crore a year (unsourced); competitor | search summary |
| 90 | Detention and demurrage charges explained | Roado | https://www.roado.tech/blog/detention-and-demurrage-charges-explained-causes-costs-and-prevention-strategies/ | not shown | 2026-10-31 | ₹3,500 crore demurrage (vendor claim) | search summary |
| 91 | FMC's new demurrage and detention regulations become effective May 2024 | HFW | https://www.hfw.com/insights/FMCs-New-Demurrage-and-Detention-Regulations-Become-Effective-May-2024 | 2024 | 2026-10-31 | US rule effective 2024-05-28 | search summary |
| 92 | Senior Process Expert, Detention and Demurrage Invoicing (job) | Apna | https://apna.co/job/chennai/process-expert-senior-process-expert-1825147996 | not shown | 2026-10-31 | D&D billing labour at carriers (context only) | search summary |
| 93 | JNPA record 7.9 million TEUs in 2025 | Indian Infrastructure | https://indianinfrastructure.com/2026/01/02/jawaharlal-nehru-port-authority-sets-new-benchmark-with-record-handling-of-7-9-million-teus-in-2025/ | 2026-01-02 | 2026-10-31 | Port volume context | search summary |
| 94 | CFS operators take on APSEZ over new levy at Hazira | India Sea Trade News | https://indiaseatradenews.com/cfs-operators-takes-on-apsez-over-new-extra-levy-at-hazira-port/ | 2026-06-04 | 2026-10-31 | Port vs CFS levy dispute | search summary |
| 95 | PTFC meeting minutes 22-02-2018 | Jawaharlal Nehru Custom House | https://www.jawaharcustoms.gov.in/pdf/ptfc/minutes_of_ptfc_meeting_(i)22_02_2018.pdf | 2018-02-22 | 2026-10-31 | CFS refund of overcharges | search summary |
| 96 | Indian scrap imports from UAE halt after container detention | BigMint | https://bigmint.co/insights/detail/indian-scrap-imports-from-uae-halts-after-container-detention-at-ports-444281 | 2023 (approx.) | 2026-10-31 | Customs-hold detention (attribution not certain) | search summary |
| 97 | What is detention? | GoComet | https://www.gocomet.com/blog/what-is-detention/ | not shown | 2026-10-31 | Competitor presence | search summary |
| 98 | How to streamline detention and demurrage | Fleetx | https://blog.fleetx.io/how-to-streamline-detention-and-demurrage-for-effective-cost-savings | not shown | 2026-10-31 | Competitor presence | search summary |
| 99 | 17 lakh silver jewellery items hallmarked within three months of HUID | Free Press Journal | https://www.freepressjournal.in/business/17-lakh-silver-jewellery-items-hallmarked-within-just-three-months-of-the-government-making-huid-mandatory | 2025 (approx.) | 2026-10-31 | Silver HUID from 2025-09-01 | search summary |
| 100 | IS 7845:2022 reactive dye strength test | Bureau of Indian Standards | https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/Indian_standards/isdetails/Mjc3NTg= | 2022 | 2026-10-31 | Indian test method for dye strength | search summary |
