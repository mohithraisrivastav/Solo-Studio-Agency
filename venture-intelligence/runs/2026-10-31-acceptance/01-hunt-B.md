# 01 Hunt B: Something changed

Specialist: Opportunity Hunter. Lens B: new rules, newly cheap capabilities, input cost shifts, behaviour shifts.
Date: 2026-10-31. Brief: `runs/2026-10-31-acceptance/00-brief.md`.

**Method and limits.**
- About 60 web searches. WebFetch failed on the one site tried (DNS block), so every source below was seen only through search-result summaries. No page was opened.
- No buyer was contacted. All demand evidence is desk evidence, so L1 at most.
- Search summaries sometimes merged several results. Where I could not tell which outlet a figure came from, I say so or leave the figure out.
- Constraints used: founder capital ₹5,00,000 and founder time at ₹750 per hour [A] (basis: the brief's stated defaults). Currency rates used: USD 1 = ₹88 and EUR 1 = ₹100 [A] (rates assumed for 2026-10-31, not checked; test against the RBI reference rate).

## 1. Industries chosen and why

I chose five industries. They do not share buyers, channels or technology. None is a common startup theme. Two are unglamorous B2B niches (construction waste compliance and hospital gas-plant upkeep).

**1. Engineering metal exports (steel and aluminium products made by MSMEs).**
- The EU Carbon Border Adjustment Mechanism (CBAM) moved from reporting only to its definitive phase on 1 January 2026. Exporters now need verified emissions data [S1].
- India's steel and aluminium exports to the EU fell 24.4% in FY25 before any certificate was paid [S3]. A CEEW analysis found about 30% of metal-sector MSMEs lack the digital systems to track emissions [S15].

**2. Building construction (projects with 20,000 sq m built-up area or more).**
- New Construction and Demolition (C&D) Waste Management Rules took effect on 1 April 2026. Large projects must recycle, use recycled material, and file returns on a CPCB portal [S24, S25, S27].
- Recycling supply is thin and badly used. CSE found most of the 16 plants it assessed underused or unviable [S29]. One commentary says capacity covers under 2% of the waste, sits in big cities, and debris does not travel economically between cities [S32].

**3. MSME pharmaceutical manufacturing.**
- The revised Schedule M (GMP) deadline for MSMEs, 31 December 2025, passed. Only about 1,700 of an estimated 6,500 MSME units required to comply, about 26%, had filed upgrade plans [S42].
- Industry quotes ₹3 crore to ₹10 crore to upgrade a running unit [S44]. 144 MSME units in Himachal Pradesh were reported closed [S43].

**4. Bioenergy co-products and feedstocks (DDGS, used cooking oil).**
- Grain-based distilleries supplied 624 of 895 crore litres of ethanol by August-end in the 2025-26 supply year [S51]. Their by-product, DDGS, has flooded feed markets and now makes up 30–40% of the protein-feed segment [S52].
- India has sustainable aviation fuel (SAF) blending targets of 1% by 2027 and 5% by 2030 [S64]. Yet only about 6% of an estimated 1.8–2.6 million tonnes of used cooking oil (UCO) is formally collected [S61].

**5. Public-hospital medical-gas infrastructure (PSA oxygen plants).**
- About 4,135 pressure swing adsorption (PSA) oxygen plants were installed during the pandemic [S70]. Of 3,005 plants that reported status, only 53% were working [S69].
- On centrally procured plants, warranties ran 3 years, and routine operation and maintenance was always left to hospitals and states [S77]. That large installed base is now past warranty with no clear payer for upkeep [S69].

## 2. Raw candidates

| # | Problem | Payer | Signal | Tag |
|---|---|---|---|---|
| R1 | MSME steel and aluminium exporters cannot produce verified, plant-level emissions data that EU buyers and verifiers accept | MSME exporter, possibly reimbursed by government | Industry puts reporting compliance at ₹15–20 lakh per unit; government says it will cover certification costs for micro and small firms | [S7, S9, S10] |
| R2 | Downstream fabricators cannot get precursor emissions data from the steel mills that supply them | Fabricator or exporter | A "data access gap" for MSMEs that buy inputs from large producers | [S1] |
| R3 | Large building projects in tier-2 cities must meet new C&D recycling and recycled-content duties, but no local recycler or certificate supply exists | Developer or EPC contractor | Rules in force from 1 April 2026; recycled content 5% from 2026-27; capacity concentrated in metros | [S25, S27, S32] |
| R4 | Builders and road contractors distrust recycled aggregate quality, so recycled products do not sell | Builder, road contractor | Down To Earth calls for testing and standards; Delhi plant output under-used | [S28, S33] |
| R5 | MSME pharma units must qualify and validate HVAC, water and equipment to revised Schedule M before inspection | MSME pharma unit | 74% of MSME units had not filed upgrade plans; risk-based inspections began | [S42, S48] |
| R6 | Brand owners whose contract manufacturers shut down need compliant replacement capacity fast | Pharma marketing company | Closures in Himachal Pradesh; Gujarat body warns 4,000–5,000 units could close | [S43, S49] |
| R7 | Micro pharma units run quality systems on paper and cannot show compliant records | MSME pharma unit | Revised Schedule M adds a pharmaceutical quality system and quality risk management | [S42] |
| R8 | Feed mills receive DDGS of unknown and variable protein, fat and aflatoxin | Cattle, poultry and fish feed mills | NDDB guidance (Feb 2026) on QC at DDGS procurement; BIS draft standard (Aug 2025) | [S54, S55] |
| R9 | Distilleries cannot export DDGS at full value because of aflatoxin | Grain distilleries | Traders say aflatoxin keeps Indian DDGS from competing with US product | [S53] |
| R10 | SAF and biodiesel makers cannot get traceable used cooking oil; most is diverted back into food | SAF and biodiesel producers, exporters | 6% formally collected; 95% diversion claim; aggregators ask for EPR | [S61, S62] |
| R11 | Hospital PSA oxygen plants sit idle for lack of maintenance and spare parts | State health departments, hospitals | 53% functional; one-year CAMC tender worth ₹34.96 lakh in Srinagar | [S69, S74] |

## 3. Opportunity theses

Investigated in depth: R1, R3, R8, R10, R11, plus R5 to R7 more lightly (the pharma group). Kept: R3, R1, R11. Ranked by my judgement of strength.

### Thesis 1 (R3): C&D waste compliance and recycled-material supply for large building projects in tier-2 cities

**Problem.**
- Since 1 April 2026, projects with 20,000 sq m or more of built-up area count as "producers". They must register on a CPCB portal and file a waste management plan approved by the local authority [S25, S27].
- They must use recycled C&D material: at least 5% of construction materials in 2026-27, rising to 25% by 2030-31 [S25].
- Demolition and reconstruction projects carry recycling targets: 25% in 2025-26, rising to 100% from 2028-29 [S25]. A project that falls short must buy EPR certificates from registered recyclers [S26, S27].
- In most tier-2 cities there is no working recycler to buy material or certificates from [S32] [I].

**Who pays, who uses, who can block.**
- Pays: the developer or EPC contractor of each covered project. The likely signer is the project head or the liaison or compliance head [A] (basis: who handles environmental clearance today; test in 10 developer calls).
- Uses: site engineers and liaison staff [A].
- Can block:
  - the local authority that approves the plan [S25];
  - the state pollution control board;
  - city contractors with exclusive debris rights, such as Bengaluru's single-agency debris contract [S40];
  - structural consultants who refuse recycled aggregate because standards and testing are weak [S28].

**Current alternatives and what buyers spend.**
- Builders already pay to have debris lifted:
  - Nashik charges ₹800 per tonne, and fines non-compliance at ten times that [S38];
  - Pune charges ₹1,250 per tonne for smaller quantities [S39];
  - Mumbai charges ₹1,425 per tonne (₹1,415 in the western suburbs) for loads over 500 kg [S37].
- Cities also pay processors. Bengaluru pays a contractor a tipping fee of about ₹967 per tonne [S40].
- EPR certificate prices: not found after 2 searches (queries: "C&D waste EPR certificate portal CPCB recyclers registered 2026 price per tonne", "C&D waste EPR certificate first trade price developers buying certificates"). The rules let CPCB set a price band at 30% to 100% of the environmental compensation for missed targets [S26]. The compensation rate itself was not found.

**Frequency and cost of the problem to the buyer.**
- The duty runs for the whole life of each project and is reported every year [S25] [I].
- A rough size: assume 1.5–2.5 tonnes of material per sq m of built-up area [A] (basis: RCC frame with masonry; test against one quantity surveyor's bill of quantities). Then a 20,000 sq m project uses about 30,000–50,000 tonnes, and the 5% recycled share in 2026-27 is about 1,500–2,500 tonnes [I] (20,000 × 1.5–2.5 × 5%).
- Delivering that from a city with no recycler means trucking from another city. One commentary says that is not economic [S32].

**Why now.** The rules took effect on 1 April 2026 [S27]. 2026-27 is the first year of the recycled-content target [S25]. In August 2025 the Supreme Court's Vanashakti ruling struck down an exemption, so some large buildings that had been exempt now need prior environmental clearance again [S35]. More projects are therefore on regulators' lists [I].

**Why unsolved.**
- Category (f), newly created, and (e), fragmented buyers. The duty is six months old [S27]. Tier-2 projects are spread out, and the processors who exist sit in metros [S32].
- Risk of (a), weak demand:
  - Unmet EPR duties can be carried forward for up to three years, which lets builders delay [S27].
  - Recycled products have struggled to sell. CSE found most assessed plants underused or unviable [S29]. Delhi's Jahangirpuri plant slowed for lack of demand and the site became a landfill [S33].
  - Private buyers make up about 67% of recycled C&D demand and government only about 14% [S30]. Public offtake does not carry the market.
- 2026 enforcement data (registrations, returns filed, penalties): not found after 3 searches (queries: "C&D waste rules 2025 implementation builders registration portal delay CREDAI", "CPCB C&D waste EPR portal launched 2026 registration", "C&D waste management rules amendment 2026 deferred").

**Competitors, including failed attempts.**
- Large operators run city plants under public-private partnerships. Ramky (Re Sustainability) runs Hyderabad's plant with GHMC [S89].
- Cities keep tendering new plants: a 50 TPD plant in Navsari (₹10 crore+), a combined plant and landfill in Nadiad (₹23.94 crore), and a 100 TPD plant in Meerut with 10 years of operation [S34]. CSE counted over 34 operating plants [S31].
- Mobile crusher makers (Keestrack, Terex, MB Crusher, Schwing Stetter) sell equipment, not compliance [S90].
- Compliance law firms publish guidance on the rules [S25, S27].
- Failed attempts: no C&D-specific startup shutdown found after 2 searches (queries: "C&D waste startup India debris collection recycling aggregator funding shut down", "mobile C&D waste crusher on-site recycling service India builders"). The Delhi plant slowdown is the nearest failure signal [S33].

**Barrier for a small new entrant, and the way in.**
- Capital: a crusher bucket costs about ₹20–35 lakh [S36], above the ₹5 lakh budget [I]. On-site mobile crushing was rare in India as of 2016 [S41].
- Only registered recyclers can issue certificates [S27], so the entrant needs a recycler partner.
- Way in, asset-light, in one tier-2 city with no working recycler:
  - Sell a yearly compliance retainer: registration, waste plan, returns, and site segregation.
  - Arrange recycled-content supply and certificates through a partner, such as a local stone crusher or a machine owner who registers as recycler.
  - Take a margin on material moved [A] (basis: the model of the debris-lifting charges above; test whether a local crusher owner will register).
- Big operators bid for city-scale tenders [S34]. Project-level service in small cities is below their threshold [I].

**Reachable buyer pool (bottom-up).**
- Maharashtra alone had about 700 projects pending before its state clearance authority while the court's stay was in force [S35]. The stay ran from February to August 2025 [S35].
- If that backlog equals about six months of inflow, Maharashtra sees roughly 1,400 covered projects a year [I] (700 × 2) [A] (basis: backlog ≈ inflow during the stay; test against PARIVESH EC grant data).
- If Maharashtra is 20–30% of the national total [A] (basis: share of urban construction; test against PARIVESH), India has about 4,700–7,000 new covered projects a year [I] (1,400 ÷ 0.30 to 0.20).
- One tier-2 city may have 20–60 live covered projects [A] (test: PARIVESH EC list for one district). Winning 10–15 retainers at ₹1.5–4 lakh a year gives ₹15–60 lakh revenue [I] (10 × 1.5 to 15 × 4), before any material margin.
- The number of building ECs granted each year nationally was not found after 2 searches (queries: "number of building construction projects environmental clearance granted per year India", "Supreme Court Vanashakti 2025 ... number of projects affected").

**Demand evidence level.** L1, weak to moderate. Builders already pay ₹800–1,425 per tonne to get rid of debris in several cities [S37, S38, S39]. Cities spend crores on plants [S34]. No evidence that any builder has yet bought certificates or recycled content under the new rules.

**What would make this large.**
- Targets rise to 25% recycled content and 100% demolition recycling [S25].
- A trading module would let a trusted local intermediary aggregate certificates across many projects [S27] [I].
- The same desk could sell to roads and airports, which have their own targets [S26].

**What would kill it.**
- CPCB and state boards do not enforce, or the three-year carry-forward becomes a standing deferral [S27].
- Cities grant exclusive debris rights to one contractor [S40].
- Engineers keep refusing recycled aggregate [S28].
- A large operator offers a cheap national compliance product.

**Confidence.** Medium-low. The regulation is real and in force. Enforcement and willingness to pay in 2026-27 are untested.

### Thesis 2 (R1): Verification-ready CBAM emissions data for MSME steel and aluminium exporters, cluster by cluster

**Problem.**
- From 2026, EU importers must declare embedded emissions for steel and aluminium goods, using verified installation data or default values [S1, S2].
- Default values are set high. A vendor page in the results gives Indian hot-rolled coil a default of about 4.27 t CO2 per tonne. It puts the theoretical full-phase exposure near €220 per tonne, about ₹22,000 at the assumed rate [S21] [A] (vendor estimate; the exact source page was not clear in the summary).
- MSME producers lack the metering, records and verified reports to beat the defaults [S15]. They lose orders or cut prices. GTRI says many may need to cut prices 15–22% [S3].

**Who pays, who uses, who can block.**
- Pays: the MSME owner or director [A]. The minister has said the Export Promotion Mission will cover certification costs for micro and small exporters [S10]. A separate report says up to 90% reimbursement is being considered, with export promotion councils filing claims [S9]. Neither guideline text was found.
- Uses: plant manager, accounts and quality staff [A].
- Can block:
  - the EU importer, which can switch suppliers or accept defaults;
  - the EU-accredited verifier, which is scarce. One guide says no CBAM verifier was accredited as of 11 July 2026 [S13];
  - the upstream mill that will not share precursor data [S1].

**Current alternatives and what buyers spend.**
- Indian sustainability software and consultancies (GreenSutra, The Sustainability Cloud, Bevolve) [S17, S18, S21].
- Testing and certification majors seeking verifier status (TÜV NORD) [S19]. EU platforms such as CBAMBOO [S20].
- Industry estimates put reporting compliance at ₹15–20 lakh per unit before any levy [S7]. Published package prices: not found after 2 searches (queries: "CBAM verification fee India exporter consultant price", "CBAM compliance service India MSME package price ₹ per quarter").

**Frequency and cost of the problem to the buyer.**
- Data is gathered all year. The first annual declaration, for 2026 imports, is due by 30 September 2027 [S2].
- The share of the full charge that is payable is small now: 2.5% in 2026, rising to 100% by 2034 [S2].
- So 2026-27 cost is mostly lost orders and price pressure, not the levy [I].

**Why now.**
- The definitive period began on 1 January 2026 [S1].
- The first verification needs a physical site visit [S13].
- The EU has proposed adding about 180 downstream steel and aluminium products [S14].
- Reimbursement statements in 2026 lower the buyer's net cost [S9, S10].

**Why unsolved.**
- Category (f), new, and (e), fragmented MSMEs without systems [S15].
- It is not a case of weak demand: Ch. 72 iron and steel exports to the EU fell from $4.69 billion to $3.05 billion, a 35.1% fall [S4]. Mongabay found export growth fell for most MSMEs in 20 of 27 EU states in 2024-25 [S5].
- The EU's 50-tonne exemption takes about 90% of importers out but keeps about 99% of emissions in scope [S11, S12]. So the large buyers that matter still ask suppliers for data [I].
- Disconfirming: Sandbag says the CBAM cost for Indian steel is likely overstated [S16].

**Competitors, including failed attempts.** Crowded and growing (above) [S17, S18, S19, S20, S21]. Failed or exited CBAM vendors: not found after 1 search (query: "CBAM compliance service India MSME package price").

**Barrier for a small new entrant, and the way in.**
- The barriers are credibility and access to verifiers, not capital [I].
- Way in: pick one product cluster. Candidates are secondary-steel units in Raipur or Kolhapur [S5] and fastener makers, if CN 7318 coverage is confirmed. A low-authority tariff site says CN 7318 15 bolts are in scope since 2026 [S23].
- Offer a fixed-fee, on-site, local-language "verification-ready file": monitoring plan, meter log, precursor data request, and default-versus-actual comparison.
- Price it inside the reimbursement rules [S9]. Batch site visits so one verifier trip serves several units [A] (basis: verifier scarcity [S13]; test with one verifier).

**Reachable buyer pool (bottom-up).**
- Assume MSMEs ship 30–50% of the $3.05 billion Ch. 72 exports to the EU [S4] [A] (basis: reports that "a large share" comes from MSMEs; test with EEPC or DGFT exporter data).
- Assume an average of $2–5 million a year per MSME exporter [A]. That gives about 180–760 MSME exporters in Ch. 72 alone [I] (3,050 × 0.3 ÷ 5 to 3,050 × 0.5 ÷ 2, in $ million).
- Ch. 73 and aluminium would add more. No count was found.
- One cluster might hold 40–120 of them [A]. Twenty clients at ₹2–6 lakh a year gives ₹40–120 lakh revenue [I].
- Founder time: at 40–60 hours per client a year [A], that is ₹30,000–45,000 per client [I] (40–60 × ₹750).
- A firm count of affected MSME exporters was not found after 1 search (query: "how many Indian MSME exporters affected CBAM number of firms").

**Demand evidence level.** L1, moderate. The export fall, buyer data requests [S15], a vendor market that has formed, and government money set aside all show spend pressure. No buyer price was seen.

**What would make this large.**
- The downstream expansion [S14].
- A UK CBAM. Indian verification bodies are seeking both EU and UK accreditation [S91].
- Reuse of the same data for buyers' Scope 3 reporting [A].

**What would kill it.**
- Reimbursement pays only accredited verifiers and not data preparation [S9].
- A free government tool appears.
- An India-EU deal on carbon pricing or verifier recognition makes the problem simple.
- A price war among the many vendors.
- The cost turns out lower than feared [S16].

**Confidence.** Low-medium. The spend is real but the field is crowded. The difference would come from delivery (on-site, cluster-based, local-language), which is easy to copy.

### Thesis 3 (R11): Multi-brand upkeep for idle and ageing hospital PSA oxygen plants

**Problem.**
- Many oxygen plants installed in 2020-22 have stopped working. Of 3,005 plants that reported, 53% worked [S69]. In West Bengal, 32 of 75 PSA plants worked as of December 2023 [S71]. In Kota, 4 of 24 [S72].
- Hospitals fall back on bought-in oxygen. Faridabad's 1,000 LPM plant has been down about two years and the hospital buys outsourced oxygen [S73].

**Who pays, who uses, who can block.**
- Pays: state health departments, medical colleges, and public works mechanical divisions that issue repair and CAMC tenders [S74, S75]. Private hospitals with their own plants are a possible second payer (not checked).
- Uses: hospital biomedical and mechanical staff [A].
- Can block:
  - finance approvals. Faridabad's estimated ₹5 lakh a year for maintenance was never sanctioned [S73];
  - the original manufacturer, which holds warranty, CAMC and spare parts [S77, S83];
  - safety licensing. One directory says PESO approval is mandatory; this claim is unverified [S82].

**Current alternatives and what buyers spend.**
- Repair and CAMC tenders:
  - a one-year CAMC of oxygen plants for a Srinagar government hospital, valued at ₹34.96 lakh [S74];
  - a repair tender in Rayagada, with bids due 5 March 2026 [S75];
  - quotations sought in Kandhamal [S75].
- A peer-reviewed cost study puts yearly comprehensive maintenance at about 5–7% of plant cost, with ₹3,50,000 for a 100 LPM plant [S76].
- Manufacturers sell their own AMCs (PSA Nitrogen, MVS Engineering) [S80, S81].

**Frequency and cost of the problem to the buyer.**
- Upkeep is continuous.
- An idle plant wastes capital of about ₹1 crore per PM CARES plant [S70]. Nurpur's ₹2 crore plant has sat idle about two years [S85]. Kerala's ₹1 crore Neyyattinkara plant was reported rusting in October 2026 [S78].
- An Assam House panel found failures across government hospitals [S79].

**Why now.**
- The base has aged past warranty. Centrally procured plants carried a 3-year warranty, and routine operation and maintenance was left to hospitals and states [S77].
- Plants installed in 2021 are out of warranty since about 2024 [I]. For the 162 CMSS plants, a 7-year CAMC was bought (₹64.25 crore of ₹201.58 crore) [S77]. The rest of the roughly 4,135 plants [S70] have no such contract on record [I].
- Failures and repair tenders keep appearing in 2026 [S75, S78].

**Why unsolved.**
- Category (d), trust and procurement barriers, and (e), fragmented brands and sites. Over 195 suppliers are claimed in one directory [S82].
- Serious risk of (a): the user needs the plant but the payer often does not budget. Examples:
  - Faridabad [S73];
  - Jawali, where transformer and generator funds were not sanctioned [S86];
  - Neyyattinkara, where funds were held back [S78].
- States may have believed the Centre would pay operator wages and maintenance; this was never stated [S69].
- Spare parts often must come from the original installer, and imported parts are unavailable [S83]. There is also a technician shortage [S87].
- Mock-drill results on plant status are not public [S69]. Buyers cannot see the size of the problem [I].

**Competitors, including failed attempts.**
- Manufacturers' service arms [S80, S81].
- Local mechanical contractors who answer repair tenders [S75] [I].
- Failed multi-brand service firms: not found after 1 search (query: "PSA oxygen plant AMC service provider India multi-brand maintenance company").

**Barrier for a small new entrant, and the way in.**
- Barriers:
  - tender eligibility (turnover and past work) [A];
  - access to parts;
  - payment delays of 90–180 days from public buyers [A] (basis: common public-sector practice; test with two past bidders).
- Tool kit: oxygen purity analyser, dew-point meter, flow meters [A]. It probably fits within ₹2–4 lakh [A] (test with three supplier quotes).
- Way in:
  - Start with private and trust hospitals that run their own plants and pay faster.
  - Subcontract to manufacturers or winning bidders on government CAMCs.
  - Build a multi-brand parts list and low-cost remote purity and uptime logging. A 2021 PM review asked for IoT tracking of these plants [S88].

**Reachable buyer pool (bottom-up).**
- About 4,135 plants installed [S70]. Of the 3,005 that reported, 47% were not working [S69], so at least about 1,400 non-working plants [I] (3,005 × 0.47).
- A three-state region may hold 250–400 public-facility plants [A] (basis: about 4,135 plants spread over 36 states and UTs; test via state NHM lists).
- Winning 15–25 plants at ₹2.5–5 lakh a year gives ₹37.5–125 lakh revenue [I] (15 × 2.5 to 25 × 5), using the cost-study and Faridabad benchmarks [S76, S73].
- Spares and travel cut margins. Time at 80–120 hours per plant a year [A] costs ₹60,000–90,000 [I] (× ₹750).
- Private-hospital plant counts: not checked.

**Demand evidence level.** L1, moderate. Several independent tender notices show public buyers paying for PSA upkeep [S74, S75]. Many other facilities show the opposite: no budget.

**What would make this large.**
- A state-level O&M contract.
- Extending to other idle pandemic equipment such as ventilators [S71].
- Similar markets abroad that show the same failure pattern (Nepal [S83]).

**What would kill it.**
- States will not fund upkeep.
- Manufacturers lock up parts.
- Lowest-price bidding drives fees down.
- Plants are written off.
- Liability for an oxygen purity failure.

**Confidence.** Low-medium. The pain is clear and partly funded. Whether payers pay reliably is the open question.

## 4. Cut candidates and reasons

| # | Candidate | Why cut | Tag |
|---|---|---|---|
| R2 | Precursor emissions data exchange | Depends on large mills that hold the data and have little reason to share it. Folded into Thesis 2 as one task | [S1] |
| R4 | Recycled aggregate testing and certification | Lab testing is a commodity service, a lab costs more than the budget [A], and demand depends on Thesis 1 working first. Folded into Thesis 1 | [S28] |
| R5 | Schedule M qualification and validation services | Crowded with local validation vendors (an IndiaMART listing shows HVAC cleanroom service at ₹5,000 per day). Close to consulting. Customer base shrinking as units close | [S50, S43] |
| R6 | Matchmaking for replacement contract manufacturing | No evidence of buyer spend found; the space is full of directory and IndiaMART listings. Not found after 1 search | [S49] |
| R7 | Low-cost quality-system software for micro pharma | Existing tools (GMPPro from ₹25,000 per user; QEdge from $79 per user). Buyers must first find ₹3–10 crore of capex | [S46, S47, S44] |
| R8 | DDGS quality grading at feed mills | Feed plants already run QC under NDDB guidance. AgNext ($21 million Series A) already offers rapid feed testing. Lab aflatoxin tests cost ₹2,750 per sample at NIFTEM. No evidence buyers would pay a third party more | [S54, S57, S58] |
| R9 | Low-aflatoxin export DDGS | Technically hard: the moisture problem starts at grain intake. A commodity at about $230 per tonne (about ₹20,240 at the assumed rate) with thin margins | [S53] [A] |
| R10 | Traceable used cooking oil collection | Commodity aggregation. Informal buyers sometimes pay more than virgin oil. Funded rivals exist (Ecoil Energy, $2.5 million Series A). EPR not yet notified. Reported refiner margins of ₹6–12 per kg come from a report with blank fields | [S67, S65, S61, S68] |

Pharma as a whole was cut. Every route for a small firm is consulting, crowded software, or capex the buyers cannot yet fund [S44, S45].

## 5. Sources

All sources were seen only as search-result summaries. None was opened. "Published" is the date shown in the result or URL. "not shown" means the summary did not give one.

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | EU's Carbon Tax Hits Indian Steel Exports From January 1 | Free Press Journal | https://www.freepressjournal.in/business/eus-carbon-tax-hits-indian-steel-exports-from-january-1 | not shown | 2026-10-31 | Definitive phase from 1 Jan 2026; verifier need; data-access gap | search summary |
| 2 | CBAM in 2026: All You Need to Know | GreenSutra (vendor) | https://greensutra.in/?p=236766 | not shown | 2026-10-31 | Phase-in coefficients; declaration date 30 Sep 2027 | search summary |
| 3 | CBAM may force steel, aluminium firms cut prices: GTRI | Business Standard | https://www.business-standard.com/amp/industry/news/cbam-may-force-steel-aluminium-firms-cut-prices-gtri-125123101012_1.html | 2025-12-31 | 2026-10-31 | 24.4% FY25 export fall; 15–22% price cuts | search summary |
| 4 | India's Metal Exports to EU Plunge 24% as CBAM Reporting Hits MSMEs | Basis Point Insight | https://www.basispointinsight.com/Story/-india-s-metal-exports-to-eu-plunge-24--as-cbam-reporting-hits-msmes-_30e1360663c9.html | not shown | 2026-10-31 | Ch. 72 exports $4.69bn to $3.05bn | search summary |
| 5 | European Union border tax tests India's small iron and steel businesses | Mongabay India | https://india.mongabay.com/2026/06/european-union-border-tax-tests-indias-small-iron-and-steel-businesses/ | 2026-06 | 2026-10-31 | MSME export growth fell in 20 of 27 EU states; Raipur, Kolhapur clusters | search summary |
| 7 | EU's CBAM poses major compliance challenge for Indian MSMEs | Tribune India | https://www.tribuneindia.com/news/business/eus-cbam-poses-major-compliance-challenge-for-indian-msmes-experts-seek-urgent-government-support/ | 2026-07 (mirror dated 4 Jul 2026) | 2026-10-31 | ₹15–20 lakh per unit compliance estimate (summary merged several outlets) | search summary |
| 9 | Govt May Reimburse CBAM Certification Costs For Small Steel Exporters | Free Press Journal | https://www.freepressjournal.in/business/govt-may-reimburse-cbam-certification-costs-for-small-steel-exporters-under-export-scheme | 2026-07 | 2026-10-31 | Up to 90% reimbursement proposal; EPC claims | search summary |
| 10 | Centre to bear full certification cost for micro, small exporters under EPM, says Goyal | Swarajya | https://swarajyamag.com/news-brief/centre-to-bear-full-certification-cost-for-micro-small-exporters-under-export-promotion-mission-says-goyal | not shown (2026) | 2026-10-31 | Minister's statement on cost cover | search summary |
| 11 | CBAM: Deal with Council to simplify EU carbon leakage instrument | European Parliament | https://www.europarl.europa.eu/news/es/press-room/20250613IPR28918/cbam-deal-with-council-to-simplify-eu-carbon-leakage-instrument | 2025-06-13 | 2026-10-31 | 50-tonne de minimis; about 90% importers exempt, 99% emissions kept | search summary |
| 12 | Officially published: simplifications to CBAM | European Commission | https://taxation-customs.ec.europa.eu/news/officially-published-simplifications-carbon-border-adjustment-mechanism-cbam-2025-10-20_en | 2025-10-20 | 2026-10-31 | Simplification in force | search summary |
| 13 | Accredited CBAM Verifiers: Country-by-Country Accreditation Status (July 2026) | CBAM Guide | https://cbamguide.com/compliance/accredited-verifiers/ | 2026-07 | 2026-10-31 | Zero accredited verifiers as of 11 Jul 2026; site visit rule | search summary |
| 14 | EU plans to expand carbon tax to 180 more steel, aluminium products | Business Today | https://www.businesstoday.in/industry/story/fresh-export-challenge-for-msmes-eu-plans-to-expand-carbon-tax-to-180-more-steel-aluminium-products-526508-2026-04-20 | 2026-04-20 | 2026-10-31 | Downstream expansion | search summary |
| 15 | How the EU's carbon border tax is reshaping Indian MSMEs | The Wire | https://thewire.in/environment/how-the-eus-carbon-border-tax-is-reshaping-indian-msmes | not shown | 2026-10-31 | CEEW: about 30% of metal MSMEs lack digital systems; EU buyers asking for data | search summary |
| 16 | Interview: Sandbag says EU CBAM cost for Indian steel likely overstated | S&P Global | https://www.spglobal.com/energy/en/news-research/latest-news/metals/081026-interview-sandbag-says-eu-cbam-cost-for-indian-steel-likely-overstated | 2026-08-10 | 2026-10-31 | Disconfirming view on cost | search summary |
| 17 | Best CBAM Software in India 2026 | The Sustainability Cloud | https://www.thesustainabilitycloud.com/blog/cbam-software-in-india/ | 2026 | 2026-10-31 | Competitor | search summary |
| 18 | CBAM Made Simple: What Indian Exporters Need to Know | Bevolve | https://bevolve.ai/cbam-compliance-indian-exporters-iron-steel/ | not shown | 2026-10-31 | Competitor | search summary |
| 19 | CBAM verification | TÜV NORD India | https://www.tuv-nord.com/in/en/our-services/system-certification/sustainability-esg-energy-water-carbon-ghg/carbon-border-adjustment-mechanism-cbam-verification/ | not shown | 2026-10-31 | Competitor (verification) | search summary |
| 20 | Get on top of CBAM with the CBAMBOO platform | Fastener + Fixing | https://fastenerandfixing.com/management-systems/get-on-top-of-cbam-with-the-cbamboo-platform | not shown | 2026-10-31 | Competitor (EU platform) | search summary |
| 21 | CBAM Cost Calculator | GreenSutra (vendor) | https://greensutra.in/?p=236509 | not shown | 2026-10-31 | Default value about 4.27 tCO2/t, about €220/t exposure (attribution in summary unclear); competitor | search summary |
| 23 | Customs tariff 7318 15 | celna24.pl | https://celna24.pl/customs-tariff/731815 | not shown | 2026-10-31 | CN 7318 15 in CBAM scope (low authority) | search summary |
| 24 | New construction waste rules push for producers' accountability and recycling | Mongabay India | https://india.mongabay.com/2025/05/new-construction-waste-rules-push-for-producers-accountability-and-recycling/ | 2025-05 | 2026-10-31 | Bulk generator definition | search summary |
| 25 | Construction & Demolition Waste Management Rules 2025 | Lawrbit | https://www.lawrbit.com/article/construction-demolition-waste-management-rules-2025/ | 2025 | 2026-10-31 | Targets, recycled content, waste plan, portal | search summary |
| 26 | Transfer of EPR certificates under C&D Waste Rules 2025 | Lawrbit | https://www.lawrbit.com/ehs/transfer-epr-certificates-cd-waste-rules-2025/ | not shown | 2026-10-31 | Price band 30–100% of environmental compensation; certificate purchase; roads and airports | search summary |
| 27 | Navigating the New Landscape: India's C&D Waste Management Rules, 2025 | IndiaLaw LLP | https://www.indialaw.in/blog/civil/construction-and-demolition-waste-management/ | 2025 | 2026-10-31 | Effective 1 Apr 2026; portal; registered recyclers issue certificates; three-year carry-forward (law-firm summaries, not checked against Gazette) | search summary |
| 28 | C&D waste rules 2025 welcome move, but codes need an update now more than ever | Down To Earth | https://www.downtoearth.org.in/waste/cd-waste-rules-2025-welcome-move-but-codes-need-an-update-now-more-than-ever | 2025 | 2026-10-31 | Need for testing and standards of recycled products | search summary |
| 29 | Manage C&D waste better to fight air pollution, says new CSE assessment | Centre for Science and Environment | https://cseindia.org/manage-construction-and-demolition-c-d-waste-better-to-fight-air-pollution-says-new-cse-assessment-12474 | not shown | 2026-10-31 | 16 plants assessed, most underused or unviable | search summary |
| 30 | Repurposing Waste: Utilising recycled C&D materials in urban infrastructure | Indian Infrastructure | https://indianinfrastructure.com/2026/05/06/repurposing-waste-utilising-recycled-cd-materials-in-urban-infrastructure-development/ | 2026-05-06 | 2026-10-31 | Private 67%, government 14% of recycled demand | search summary |
| 31 | Rubble Recast: Navigating the Road to Efficient C&D Waste Recycling | Centre for Science and Environment | https://www.cseindia.org/rubble-recast-navigating-the-road-to-efficient-c-d-waste-recycling-12386 | not shown | 2026-10-31 | Over 34 operating plants | search summary |
| 32 | Transforming C&D waste management | Waste Recycling Magazine | https://www.wasterecyclingmag.com/news/transforming-c-d-waste-management | not shown | 2026-10-31 | Capacity under 2%, metro-clustered; inter-city transport uneconomic (opinion) | search summary |
| 33 | Jahangirpuri C&D plant report | Delhi Greens | https://delhigreens.org/?p=16142 | not shown | 2026-10-31 | Plant slowed for low demand; site became landfill | search summary |
| 34 | Selection of operator for C&D facility (Navsari) and similar tenders | InfraLens tenders | https://tenders.infralens.in/tender/selection-of-operator-for-establishment-of-construction-and-demolition-2026-nnmee-1148058-1 | 2026 | 2026-10-31 | Navsari, Nadiad, Meerut tender values | search summary |
| 35 | Vanashakti v. Union of India, 2025 INSC 961 | Casemine | https://www.casemine.com/judgement/in/68a2ac73099cb54b4d4823a9 | 2025-08 | 2026-10-31 | Exemption struck down; stay from Feb 2025; 700 Maharashtra projects pending | search summary |
| 36 | Bucket crusher listings | IndiaMART | https://m.indiamart.com/impcat/bucket-crusher.html | not shown | 2026-10-31 | Crusher bucket ₹20–35 lakh | search summary |
| 37 | BMC collects over 12,000 MT construction waste in 6 months | Free Press Journal | https://www.freepressjournal.in/mumbai/mumbai-news-bmc-collects-over-12000-mt-construction-waste-in-6-months-post-relaunch-of-debris-on-call-service-new-rules-to-kick-in-from-2026 | not shown | 2026-10-31 | Mumbai ₹1,415–1,425 per tonne | search summary |
| 38 | Nashik municipal commissioner takes tough stance on construction waste | PropNewsTime | https://propnewstime.com/latestnewsstories/MzQ0Nw==/nashik-s-municipal-commissioner-takes-tough-stance-on-improper-construction-waste-disposal | not shown | 2026-10-31 | Nashik ₹800 per tonne; tenfold fine | search summary |
| 39 | Pune municipality's construction debris transport service poised for expansion | PropNewsTime | https://propnewstime.com/latestnewsstories/MjYxMQ==/pune-municipality-s-construction-debris-transport-service-poised-for-expansion | not shown | 2026-10-31 | Pune ₹1,250 per tonne | search summary |
| 40 | Single firm awarded debris contract in Bengaluru | Deccan Herald | https://www.deccanherald.com/amp/story/india%2Fkarnataka%2Fbengaluru%2Fsingle-firm-awarded-rs-1714-crore-contract-to-handle-debris-in-bengaluru-3865063 | not shown | 2026-10-31 | About ₹967 per tonne tipping fee; single-agency model | search summary |
| 41 | Greening the Brown: Mobile Crushing Technologies | Development Alternatives | https://devalt.org/newsletter/jul16/of_1.htm | 2016-07 | 2026-10-31 | Mobile crushing uncommon in India (dated) | search summary |
| 42 | Schedule M extension for MSME pharma firms unlikely | Business Standard | https://www.business-standard.com/industry/news/schedule-m-extension-for-msme-pharma-firms-unlikely-125122901058_1.html | 2025-12-29 | 2026-10-31 | About 8,500 MSME units; 1,700 of 6,500 (26%) filed; inspections from Jan 2026; PQS and QRM requirements | search summary |
| 43 | Unable to upgrade, 144 pharma units in state close operations | Tribune India | https://www.tribuneindia.com/news/himachal/unable-to-upgrade-144-pharma-units-in-state-close-operations-640531 | not shown | 2026-10-31 | 144 closures in Himachal Pradesh | search summary |
| 44 | Solan: Unable to upgrade to GMP norms, 410 MSMEs seek exit road map | Tribune India | https://tribuneindia.com/news/unable-to-upgrade-to-gmp-norms-410-msmes-seek-exit-road-map-606362 | not shown | 2026-10-31 | ₹3–10 crore upgrade cost | search summary |
| 45 | Guidelines PTUAS | Department of Pharmaceuticals | https://www.pharma-dept.gov.in/sites/default/files/Guidelines%20PTUAS_0.pdf | not shown | 2026-10-31 | 20% and 15% capex subsidy | search summary |
| 46 | GMPPro | Capterra India | https://www.capterra.in/software/135640/gmppro | not shown | 2026-10-31 | From ₹25,000 per user | search summary |
| 47 | QEdge | Capterra India | https://www.capterra.in/software/134220/qedge | not shown | 2026-10-31 | From $79 per user | search summary |
| 48 | CDSCO reports risk-based inspections of pharmaceutical manufacturing units | CliniExperts | https://cliniexperts.com/regulatory-update/cdsco-reports-risk-based-inspections-of-pharmaceutical-manufacturing-units/ | not shown | 2026-10-31 | Inspections and regulatory actions | search summary |
| 49 | DMMA warns regulatory burden threatening Gujarat's pharma MSMEs | BioSpectrum India | https://www.biospectrumindia.com/news/16/26724/dmma-warns-regulatory-burden-threatening-gujarats-pharma-msmes.html | not shown | 2026-10-31 | 4,000–5,000 units could close | search summary |
| 50 | HVAC services listing | IndiaMART (Filtech Solutions) | https://m.indiamart.com/filtech-solutions/hvac-services.html | not shown | 2026-10-31 | ₹5,000 per day HVAC cleanroom service | search summary |
| 51 | India ethanol supplies reach 895 crore litres by August-end | Autocar Pro | https://www.autocarpro.in/news/india-ethanol-supplies-reach-895-crore-litres-by-august-end-134667 | 2026 | 2026-10-31 | Grain-based 624 crore litres | search summary |
| 52 | DDGS supply lowers protein feed prices in India | UkrAgroConsult | https://ukragroconsult.com/en/news/ddgs-supply-lowers-protein-feed-prices-in-india-boosting-feed-mill-profits | 2025-10 | 2026-10-31 | DDGS 30–40% of protein-feed segment | search summary |
| 53 | India likely to emerge as key DDGS supplier amid ethanol industry expansion | S&P Global | https://www.spglobal.com/commodity-insights/en/news-research/latest-news/agriculture/061125-india-likely-to-emerge-as-key-ddgs-supplier-amid-ethanol-industry-expansion | 2025-06-11 | 2026-10-31 | Aflatoxin barrier; about $230/t CFR | search summary |
| 54 | Guidelines for quality DDGS | National Dairy Development Board | https://www.nddb.coop/sites/default/files/pdfs/Guidlines_DDGS_24_2_26.pdf | 2026-02-24 | 2026-10-31 | QC at cattle-feed plant procurement; aflatoxin section | search summary |
| 55 | Draft specification for DDGS as livestock feed ingredient | Bureau of Indian Standards | https://www.services.bis.gov.in/tmp/WCFAD27627476_05082025_2.pdf | 2025-08-05 | 2026-10-31 | Draft standard | search summary |
| 57 | AgNext raises US$21 million in Series A | FoodTechBiz | https://www.foodtechbiz.com/business-updates/agnext-raises-us-21-million-in-the-largest-series-a-financing-in-agri-tech | not shown | 2026-10-31 | Funded competitor covering feed | search summary |
| 58 | FSQT test charges | NIFTEM Thanjavur | https://niftem-t.ac.in/docs/fsqt-test-charges.pdf | not shown | 2026-10-31 | Aflatoxin test ₹2,750 per sample | search summary |
| 61 | UCO aggregators seek EPR enforcement to unlock India SAF feedstock potential | S&P Global | https://www.spglobal.com/energy/en/news-research/latest-news/agriculture/093026-uco-aggregators-seek-epr-enforcement-to-unlock-india-saf-feedstock-potential | 2026-09-30 | 2026-10-31 | 1.8–2.6 Mt generated; about 6% collected; EPR not in place | search summary |
| 62 | India UCO needs globally linked, traceable pricing: M11 Energy | S&P Global | https://www.spglobal.com/energy/en/news-research/latest-news/agriculture/100226-india-uco-needs-globally-linked-traceable-pricing-to-unlock-saf-supply-m11-energy | 2026-10-02 | 2026-10-31 | 95% diversion claim | search summary |
| 64 | SAF Association urges India to capitalise on UCO supply | QCIntel | https://www.qcintel.com/biofuels/article/saf-association-urges-india-to-capitalise-on-uco-supply-reports-60748.html | not shown | 2026-10-31 | SAF targets 1% by 2027, 5% by 2030 | search summary |
| 65 | Ecoil Energy lands $2.5M Series A for Indian UCO supply chain platform | Biofuels Digest | https://biofuelsdigest.com/ecoil-energy-lands-2-5m-series-a-for-indian-uco-supply-chain-platform/ | not shown | 2026-10-31 | Funded competitor | search summary |
| 67 | Used cooking oil and SAF in India (Bloomberg report) | Daily Sun | https://www.daily-sun.com/business/905746 | 2026-10 | 2026-10-31 | UCO sometimes priced above virgin oil | search summary |
| 68 | India Used Cooking Oil (UCO) Market | MarketResearch.com (StatLedger) | https://www.marketresearch.com/StatLedger-Market-Research-Consulting-v4317/India-Cooking-Oil-UCO-Trend-43046125 | not shown | 2026-10-31 | Refiner margins ₹6–12/kg (report has blank fields; weak) | search summary |
| 69 | Why India must keep Covid-era oxygen plants running | IndiaSpend | https://indiaspend.com/health/why-india-must-keep-covid-era-oxygen-plants-running-932840 | 2024 | 2026-10-31 | 3,005 reported, 53% functional; mock drills not public; O&M payer unclear | search summary |
| 70 | Why India must keep Covid-era oxygen plants running (reprint) | Moneylife | https://moneylife.in/article/why-india-must-keep-covidera-oxygen-plants-running/75759.html | 2024-12 | 2026-10-31 | 4,135 plants installed; 1,225 PM CARES plants at about ₹1 crore each | search summary |
| 71 | CAG flags non-functional PM CARES oxygen plants, idle ventilators in Bengal hospitals | ThePrint | https://theprint.in/india/cag-flags-non-functional-pm-cares-oxygen-plants-idle-ventilators-in-bengal-hospitals-during-covid/2997176/ | not shown | 2026-10-31 | 32 of 75 working (Dec 2023); idle ventilators | search summary |
| 72 | Many oxygen plants in Kota medical college hospitals non-operational | ETV Bharat | https://etvbharat.com/en/!state/many-oxygen-plants-in-kota-medical-college-hospitals-are-non-operational-enn24092502278 | 2024-09-25 | 2026-10-31 | 4 of 24 operational | search summary |
| 73 | Amid plant failure, Faridabad civil hospital relies on outsourced oxygen | Tribune India | https://www.tribuneindia.com/news/haryana/amid-plant-failure-faridabad-civil-hospital-relies-on-outsourced-oxygen | not shown | 2026-10-31 | 1,000 LPM plant down about 2 years; no AMC; ₹5 lakh/yr not sanctioned | search summary |
| 74 | CAMC of oxygen plants and allied equipment (Srinagar) | InfraLens tenders | https://tenders.infralens.in/tender/camc-of-oxygen-plants-and-allied-equipments-for-a-2026-pwdjk-313145-4 | 2026 | 2026-10-31 | ₹34.96 lakh one-year CAMC | search summary |
| 75 | Short tender call: breakdown repair and maintenance of PSA plant, DHH Rayagada | Rayagada district administration | https://rayagada.odisha.gov.in/en/node/107701 | 2026-02 | 2026-10-31 | Repair tender, bids due 5 Mar 2026; Kandhamal quotations | search summary |
| 76 | Cost analysis of different medical oxygen sources for a healthcare facility in India | Indian Journal of Anaesthesia via PMC | https://pmc.ncbi.nlm.nih.gov/articles/PMC10993950/ | 2024-01 | 2026-10-31 | CMC 5–7% of plant cost; ₹3,50,000 for 100 LPM | search summary |
| 77 | PM CARES allocates Rs 201.58 crore for 162 PSA plants | Press Information Bureau | https://pib.gov.in/PressReleasePage.aspx?PRID=1686271 | 2021-01 | 2026-10-31 | 3-yr warranty, 7-yr CAMC, ₹64.25 crore CAMC; routine O&M by hospitals and states | search summary |
| 78 | Oxygen plant left gasping at Neyyattinkara hospital | Onmanorama | https://www.onmanorama.com/news/kerala/2026/10/02/neyyattinkara-general-hospital-rs-1-crore-oxygen-plant-decays-lies-unused.html | 2026-10-02 | 2026-10-31 | ₹1 crore plant decaying; funds withheld | search summary |
| 79 | Assam House panel flags widespread failures in oxygen plants at government hospitals | The Sentinel Assam | https://www.sentinelassam.com/topheadlines/assam-house-panel-flags-widespread-failures-in-oxygen-plants-at-government-hospitals-warns-of-risk-to-critical-care | not shown | 2026-10-31 | Widespread failures | search summary |
| 80 | PSA Nitrogen Limited: Delivering Success | Construction World | https://www.constructionworld.in/latest-construction-technology/PSA-Nitrogen-Limited-Delivering-Success-/12278 | not shown | 2026-10-31 | OEM AMC offering | search summary |
| 81 | MVS Engineering company profile | MVS Engineering | https://www.mvsengg.com/wp-content/uploads/2021/05/103_MVS_Company-Profile.pdf | 2021-05 | 2026-10-31 | OEM AMC offering | search summary |
| 82 | Medical gas plant and oxygen concentrator suppliers | Trade4Asia | https://www.trade4asia.com/suppliers/medical-gas-plants-oxygen-concentrators | not shown | 2026-10-31 | 195+ suppliers claim; PESO claim (unverified) | search summary |
| 83 | Oxygen plant closed for lack of maintenance (Nepal) | INSEC Online | https://inseconline.org/en/main_news/138536/ | not shown | 2026-10-31 | Parts only from installer; imported parts unavailable | search summary |
| 85 | Two years of silence: Nurpur hospital's Rs 2 crore oxygen plant lies defunct | Tribune India | https://www.tribuneindia.com/news/himachal/two-years-of-silence-nurpur-hospitals-rs-2-crore-oxygen-plant-lies-defunct | not shown | 2026-10-31 | Idle about 2 years; repair funds requested | search summary |
| 86 | Sans power supply, Rs 1.5 cr O2 plant lies non-operational at Jawali hospital | Tribune India | https://www.tribuneindia.com/news/himachal/sans-power-supply-1-5-cr-o2-plant-lies-non-operational-at-jawali-hospital | not shown | 2026-10-31 | Transformer and generator funds not sanctioned | search summary |
| 87 | First India lacked oxygen plants in hospitals, now it lacks technicians to operate them | Scroll | https://scroll.in/article/1007579/first-india-lacked-oxygen-plants-in-hospitals-now-it-lacks-technicians-to-operate-them | not shown (c. 2021) | 2026-10-31 | Technician shortage | search summary |
| 88 | PM chairs high-level meeting to review oxygen supply | narendramodi.in | https://www.narendramodi.in/prime-minister-narendra-modi-chairs-high-level-meeting-to-review-ramping-up-of-oxygen-supply-across-the-country-556086 | 2021 | 2026-10-31 | IoT tracking and training directive | search summary |
| 89 | Ramky Enviro launches Hyderabad C&D waste recycling plant with GHMC | Infrastructure Today | https://infrastructuretoday.co.in/ramky-enviro-launches-hyderabad-cd-waste-recycling-plant-in-partnership-with-ghmc/ | not shown | 2026-10-31 | Large PPP operator | search summary |
| 90 | Keestrack India: jaw crushers, screens and stackers to recycle C&D waste | NBM&CW | https://www.nbmcw.com/article-report/infrastructure-construction/construction-demolition/keestrack-india-jaw-crushers-screens-stackers-to-recycle-c-d-waste.html | not shown | 2026-10-31 | Equipment sellers | search summary |
| 91 | Indian verification bodies seek EU and UK CBAM accreditation | NewsBytes | https://www.newsbytesapp.com/news/business/indian-verification-bodies-seek-eu-and-uk-cbam-accreditation/tldr | not shown | 2026-10-31 | UK CBAM reference; Indian verifiers seeking accreditation | search summary |
