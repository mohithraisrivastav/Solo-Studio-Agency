# Invention 3: Lift safety and AMC accountability for Indian housing societies

Run: 2026-10-31 acceptance test. Role: Inventor. Inputs: Director's framing; `03-market-5-lifts.md` (Market Investigator, best evidence); `01-hunt-C.md` Thesis 3 (unverified; pricing corrected by the Investigator).

Constraints: founder capital Rs 5,00,000; founder time Rs 750 per hour; India first [A] (user-set constraints, not market facts).

## Method and limits

- 37 web searches with my own queries. I did not try WebFetch because the Director said it is blocked. Every source I list was seen only through search-result summaries. I opened no page.
- Facts taken from the Market Investigator's file are cited to the Investigator's sources and marked in the Sources table as "not re-checked by me".
- Currency is INR. GST at 18% on services is assumed [A] (standard rate; confirm with a CA). Prices below exclude GST unless stated.
- Not checked: any buyer's view (evidence stays at L1); the full text of any Act, rule, policy wording or patent claim; IRDAI rules on fees a broker may pay to a non-licensed risk surveyor; Indian patent families of the US patents named; NABCB accreditation cost; per-lift entrapment rates; whether society lifts in India normally have a separate feeder in the society's own panel.

## 1. Problem framing

**The job.** A society managing committee wants four things from its lifts, roughly in this order of felt urgency [A] (basis: the incidents and FIRs below; test in interviews):

1. Not to be the office-bearer named in an FIR after an accident. FIRs have named AOA president, vice president and treasurer in Noida [S1], and a society chairman in Pune [S2].
2. Lifts that run, and fast rescue when someone is trapped. In a July 2026 survey, 46% of respondents said they or family were trapped in a residential lift in the past 12 months [S3].
3. A fair AMC price. Society AMCs found run Rs 48,000-1,25,000 per lift a year [S4][S5][I].
4. Little committee time. Office-bearers are volunteers who change after elections [A].

**Constraints they live with.**
- Spending above a bye-law limit needs the general body. Limits reported range from Rs 10,000 in one Bengaluru association [S6] to Rs 1-3 lakh in Maharashtra model bye-laws (disputed) [S7].
- The contractor holds the technical knowledge, the tools and often the machine-room key [A].
- In Uttar Pradesh the owner must hold a comprehensive AMC from the maker or an authorised service provider [S8].
- State inspection is thin: in Pune only about 26% of 61,521 lifts had the annual inspection in FY 2025-26 [S9][I].

**What they pay today.**

| Item | Amount | Tag |
|---|---|---|
| Passenger-lift AMC | Rs 48,000-1,25,000 per lift a year | [S4][S5][I] |
| Repairs outside the AMC | Rs 15,000-50,000 per incident | [S10] |
| Third-party lift liability insurance | Rs 3 per mille of the annual limit (one insurer, undated) | [S11] |
| Typical cover bought (one institutional tender) | Rs 5 lakh per passenger, Rs 10 lakh in total | [S12] |
| Statutory inspection fee | Rs 1,000 periodic (Haryana); Rs 2,000 (Bhopal) | [S13][S14] |

**Buyer decision criteria** [A] (basis: Investigator's section 8 and the bye-law limits; test in interviews): independence from the contractor; no new budget line, or a price under the committee's own limit; something that protects office-bearers; no fight with the contractor; low effort.

**Measure of "better".**

| Measure | Best current figure | What a winning concept should move |
|---|---|---|
| Entrapments | 46% of respondents trapped in 12 months; no per-lift rate found [S3] | Count every entrapment, then reduce it |
| Rescue time | No society AMC with a rescue-time clause found; public contracts use 30 minutes [S15] | Contracted and measured, 30 minutes or less |
| Downtime | Not measured by societies [A] | Hours per lift per month, measured independently |
| AMC price | Rs 48,000-1,25,000 per lift a year [S4][S5][I] | 5-15% lower for the same or better terms [A] (basis: consultant claims in [S16]) |
| Liability cover against exposure | Rs 10 lakh cover [S12] against a Rs 3.01 crore principal award plus interest [S17] | Cover sized to the exposure |
| Inspection status | About 26% done in Pune [S9][I] | Every lift inspected yearly |

## 2. Inherited assumptions

| # | Assumption every current solution shares | Lever it opens |
|---|---|---|
| 1 | Each society buys its AMC alone, renewal by renewal. | Pool many societies into one tender (Lead 1). |
| 2 | The maintainer reports on its own work. | An independent ledger, inspector or recorder (Leads 1-3). |
| 3 | Seeing the lift needs a device on or in the lift. | Measure at the society's own power supply, or let residents report (Lead 3, wildcard). |
| 4 | The AMC fee is fixed whatever the outcome; the society carries the failure risk. | Results duty with automatic penalties (Lead 1, wildcard). |
| 5 | The committee is the only payer. | Insurers, residents, contractors or builders pay or demand quality (Lead 2, concepts 9 and 15). |
| 6 | Inspection is the state's job and happens rarely. | Private, independent inspection on demand (Lead 2). |
| 7 | Only a comprehensive AMC caps parts risk. | Insurance for sudden failure plus a sinking fund for wear (Lead 2 module). |
| 8 | Lift insurance is a tick-box with a small limit. | Cover sized to the exposure and tied to inspection (Lead 2). |
| 9 | Entrapments are the contractor's and the guard's problem and stay invisible to residents. | Pay the trapped household; residents become the sensor (wildcard). |
| 10 | Lift data belongs to whoever owns the sensor, usually the maker. | Society-owned data (Lead 3). |

## 3. Raw concepts

| # | Concept | Method | One-line mechanism |
|---|---|---|---|
| 1 | Federation pooled AMC tender | Mechanism transfer (UK social-housing purchasing consortia) | 15-30 societies tender together on one contract for volume and terms [A] |
| 2 | Federation model "results-duty" AMC | Mechanism transfer (French UNIS Avantage contract) | A standard contract with automatic penalties that any society can adopt |
| 3 | Shared-savings AMC audit | Business model shift (energy-service shared savings) | Free benchmark; fee only as a share of verified savings |
| 4 | AMC escrow | Inversion (when value arrives) | Monthly AMC held and released only against proven visits and uptime |
| 5 | Inspect-and-insure | Mechanism transfer (Hartford Steam Boiler, 1866) | An independent inspection becomes the basis for an adequate liability policy |
| 6 | Unbundled comprehensive AMC | Inversion (who carries parts risk) | Labour-only AMC plus breakdown insurance plus sinking fund; inspector gatekeeps claims |
| 7 | Office-bearer protection file | Consolidation | One file of AMC, licence, insurance, inspections and escalations to show duty of care |
| 8 | Accredited third-party statutory inspector | Constraint change (who inspects) | Become an approved body when Maharashtra opens third-party lift inspection |
| 9 | Handover lift audit | Constraint change (timing) | Independent audit when the builder hands lifts to the AOA, to claim defects |
| 10 | Shared lift supervisor and rescue readiness | First principles (rescue time depends on who is on site) | One trained supervisor across about 10 societies checks alarms and rescue drills and witnesses contractor visits [A] |
| 11 | Society-side lift recorder | Constraint change (sensing point) plus research application (current signature) | Clip-on current sensors on each lift's feeder in the society's panel log runs, idle time and power events |
| 12 | Phone barometer crowdsensing | Research application (barometer lift-usage detection) | Residents' phones in a society app infer lift rides and stalls; no device on the lift |
| 13 | QR and guard-round ledger | Elimination (of hardware) | QR in each car plus a 2-minute daily guard round builds an uptime and entrapment record [A] |
| 14 | Lift health grade on listings | Mechanism transfer (energy labels, hygiene ratings) | A public grade per society tower shown to buyers and tenants |
| 15 | Contractor-paid verified uptime | Inversion (who pays) | Independent AMC firms pay to have their uptime verified, to win against makers |
| 16 | Entrapment bounty | Inversion (who receives the penalty) | A fixed contractor penalty per verified entrapment is credited to the trapped household |
| 17 | Uptime-guaranteed prime contractor | Business model shift (sell availability) | The firm sells guaranteed uptime and subcontracts maintenance |
| 18 | Modernisation as a service | Business model shift (leasing) | Old lifts replaced with lender finance; society pays monthly with an uptime guarantee |
| 19 | Common-equipment compliance desk | Consolidation | One desk for lifts, fire Form B, DG sets and pumps |

Short notes on each:

1. **Pooled tender.** UK housing consortia run lift maintenance frameworks open to hundreds of members [S18][S19]. A Bengaluru or Pune federation could sponsor the same for societies. Payer: societies.
2. **Model contract.** A French property managers' union launched a standard lift contract in March 2026 that moves maintainers from a best-efforts duty to a results duty, with automatic penalties [S20]. An Indian federation could publish one. Payer: federation or societies; low revenue alone.
3. **Shared savings.** The audit is free; the fee is a share of the savings at renewal. This removes the new-budget-line problem [I] (from the bye-law limits [S6][S7]).
4. **Escrow.** Pay-for-proof. It needs a payment partner and contractor consent; heavy friction [A].
5. **Inspect-and-insure.** Hartford Steam Boiler paired insurance with engineering inspection [S21]; UK insurers still examine lifts [S22]. In India it would size liability cover to the exposure after the July 2026 ruling.
6. **Unbundled AMC.** Comprehensive AMCs cost about 60-70% more than non-comprehensive ones in one home-lift guide [S23]. Breakdown insurance excludes wear and tear [S24], so only sudden failures can move to an insurer.
7. **Protection file.** It answers the FIR fear directly [S1][S2], but alone it is paperwork with no measurement [I].
8. **Accredited inspector.** Maharashtra said in March 2026 it intends a third-party lift inspection system like Mumbai's fire-audit model [S25]. Not yet notified [S25].
9. **Handover audit.** Payer: AOA at handover. Narrow trigger; once per society [A].
10. **Shared supervisor.** Labour-heavy; margins depend on wages [A].
11. **Society-side recorder.** The measuring point sits in the society's electrical room, not in the contractor's domain. Patented methods read operating state from supply-line current [S26].
12. **Phone crowdsensing.** Barometers can identify lift use in wearable data [S27]; an in-car barometer prototype exists [S28]. Mobile background-sensing limits and app distribution make it hard; a society app could copy it easily [A].
13. **QR and guard ledger.** Cheapest measurement; depends on guard discipline [A].
14. **Listing grade.** Turns "knowing creates duty" into "knowing raises resale value" [I]; needs a portal partner and carries defamation risk [A].
15. **Contractor-paid verification.** Hong Kong's regulator already publishes contractor ratings [S29]. A private, contractor-paid version risks the issuer-pays bias [A].
16. **Entrapment bounty.** Developed as the wildcard.
17. **Prime contractor.** Close to WeMaintain, which Otis took a majority stake in during April 2026 [S30], and to India's Rieka [S31]. It carries the failure risk on Rs 5 lakh of capital [I].
18. **Modernisation finance.** Large tickets; needs a lender; slow [A].
19. **Compliance desk.** Mumbai societies already file fire Form B twice a year through licensed agencies [S32]. A good expansion path, not a starting wedge [I].

## 4. Clusters

| Cluster | Core principle | Business model | Concepts |
|---|---|---|---|
| A. Buyer-side procurement and contract design | Change the contract and the buyer's bargaining power | Success fee from savings; admin fee | 1, 2, 3, 4 |
| B. Risk transfer through insurance | A third party that prices risk demands quality | Inspection fee; broker partnership | 5, 6, 7 |
| C. Independent human inspection and supervision | Independent eyes on site | Fee per inspection or per month | 8, 9, 10 |
| D. Contractor-independent measurement | Measure without the contractor | Hardware plus subscription, or app licence | 11, 12, 13 |
| E. Disclosure and ratings | Reputation as the lever | Portal or contractor pays | 14, 15 |
| F. Resident incentives | Residents paid to report | Contract term; admin fee | 16 |
| G. The firm carries the failure risk | Sell availability, not visits | Margin on a guaranteed contract | 17, 18 |
| Expansion only | Same buyer, more equipment | Bundle | 19 |

Merges: 2 and 13 become parts of Lead 1 (the contract and the ledger). 8 becomes the later stage of Lead 2. 6 becomes an optional Lead 2 module. 7 is a deliverable in Leads 2 and 3, not a concept on its own.

Picks: Lead 1 from cluster A, Lead 2 from cluster B (with C), Lead 3 from cluster D. Wildcard from cluster F.

## 5. Three lead concepts

### Lead 1: Society Lift Pool, a federation-run tender for results-based AMCs, paid from savings

**Method.** Mechanism transfer from UK social-housing lift frameworks [S18][S19] and the French UNIS Avantage results-duty contract [S20]; business model shift to shared savings (concept 3); no-hardware ledger (concept 13).

**Core mechanism.** Many societies' AMCs are tendered at once on one standard contract that pays for results (uptime, rescue time, proven visits) and applies penalties automatically. A no-hardware ledger measures the results. The firm is paid only from verified savings plus a small administration fee.

**How it works.**
1. A federation (Bangalore Apartments' Federation has 1,400+ member associations [S33]; Pune and Mumbai cooperative federations [A]) sponsors a buying round. The firm does the work.
2. Free "AMC X-ray" for each society: collect the AMC, invoices and breakdown log; benchmark price per lift, scope (comprehensive or not), exclusions and response terms. About 2 hours per society [A].
3. A standard contract drafted once with a lawyer. Terms: entrapment response within 30 minutes, as in NSW and Covina public contracts [S15][S34]; monthly uptime target per lift [A]; visit proven by check-in photo and guard signature; penalty of a set share of the monthly fee per lift, with 2% per month per lift as an Indian institutional precedent [S35]; non-proprietary alarm and monitoring interfaces, as UNIS requires [S20]; a duty to source spare parts, given that lock-out of independents happens abroad [S36]; exit on repeated breach.
4. Tender in lots by brand and area. Invite makers and registered independent contractors. About 30% of lifts are serviced by third-party contractors nationally [S3]. Score on price and on record.
5. Each society signs its own contract. The firm runs the monthly ledger: QR in each car for residents to report "stuck" or "not working", a 2-minute daily guard round, and the contractor's visit check-in. Output: a one-page scorecard and a penalty credit note.
6. Fee: 30% of first-year verified savings against the current AMC, then Rs 200 per lift a month for administration [A] (basis: below 3% of a mid-range AMC; test in the first round).

**What the buyer experiences.** The committee hands over its AMC papers. Two weeks later it gets a benchmark. It puts a proposal to the AGM that lowers a cost line instead of adding one. Then it gets a monthly scorecard and credit notes, with no hardware.

**Measurable advantage against the best current alternative** (individual renewal with the incumbent):
- Price: 5-15% lower [A] (basis: consultants claim 10-15% for audits and renegotiation [S16]; consultants also cite volume pricing from bundling buildings [S37]; test in round one).
- Terms: a contracted 30-minute rescue time and automatic penalties, where society AMCs found show none [S15][A].
- Reliability: one US hospital that tied vendor pay to time between failures reported one lift bank moving from 9-13 days to 33-116 days between unplanned stops [S38]. A single case, vendor-reported; low confidence.

**Who pays, price logic, frequency.**

| Item | Figure | Tag |
|---|---|---|
| Pool size | 20 societies × 10 lifts = 200 lifts | [A] (10 lifts per society follows the Investigator's estimate from a two-lift, 60-flat Pune example [S5]) |
| AMC spend in pool | 200 × Rs 80,000 = Rs 1.6 crore a year | [I] (mid-range of [S4][S5]) |
| Saving at 10% | Rs 16 lakh a year, Rs 8,000 per lift | [I] |
| Firm revenue, year 1 | Rs 4.8 lakh success fee + Rs 4.8 lakh admin = Rs 9.6 lakh | [I] |
| Founder time, round 1 | About 400 hours × Rs 750 = Rs 3 lakh | [I] (hours [A]: 200 site hours, 200 for contract, tender and meetings) |
| Society net gain, year 1 | Rs 32,000 for a 10-lift society; Rs 56,000 from year 2 | [I] |
| At 5% saving | Rs 4,000 per lift saved; admin fee eats 60% of it | [I] |

Frequency: once per AMC cycle (yearly) plus a monthly fee [A].

**Production or delivery.** Founder plus a part-time retired lift engineer for site checks [A]. Lawyer for the contract and tender rules, about Rs 50,000 [A]. QR stickers and a WhatsApp bot, under Rs 30,000 in total [A]. Capital at risk before the first fee: about Rs 1.5 lakh [A].

**Why makers would not block or copy.** The firm works for the buyer. A maker cannot credibly run a tender against itself [I]. Makers can decline to bid. That matters less where independents hold a large share, as in the Bengaluru survey cut (38% third party) [S40]. In UP the law limits bidders to makers and authorised providers [S8], and only 87 manufacturers and 98 AMC agencies had registered in one count [S39], so start in Bengaluru and Pune.

**What must be true.**
1. At least 3 qualified bidders per lot, including independents who can get parts and software for the brands involved [A].
2. Committees will run renewal through a federation process, and their bye-laws let them sign a cheaper contract without a special general meeting [A].
3. Contractors accept penalties in exchange for volume [A].
4. Savings average at least 7%, or the admin fee is not worth paying [I] (from the 5% row above).

**Biggest risk.** Brand lock-in. If makers withhold parts or service tools, independents cannot bid, and a pooled tender becomes a talk with one maker. This happened abroad: Singapore's competition authority took commitments from a lift parts supplier to supply third-party maintainers [S36]. In India, the Competition Commission fined car makers for restricting parts to independent repairers [S41], which gives a route to complain but not a fast one. Second risk: informal ties between committees and incumbents. I found no report of lift-AMC kickbacks after 1 search, so this is untested.

**Prior-art check** (9 searches).
- Products and services: UK consortium lift frameworks (CHIC, valued at GBP 100 million including VAT, about Rs 1,100 crore at an assumed Rs 110 per GBP [A]; Efficiency East Midlands with 261 member organisations) [S18][S19]. US: lift consultants sold through a purchasing group (VDA via OMNIA Partners) [S16]; a landlord renegotiated contracts across 400 elevators [S37]. France: UNIS Avantage, March 2026, results duty with automatic penalties and non-proprietary telealarms, successor to a 2006 contract [S20]. Singapore's regulator encourages outcome-based lift contracts [S42]. India: independent elevator consultants advise societies [S43]; no federation group-buying of AMCs found after 2 searches ("apartment federation collective tender bulk purchase societies India AMC group buying RWA federation", "elevator consultant India AMC tender housing society lift consultancy fees benchmarking contract review Mumbai Pune").
- Patents (Google Patents via search): maker-side billing and availability tools, e.g. Inventio US8028807 (customer sets an availability standard) and Hitachi US7194415 (maintenance contract support) [S44]. These serve the maintainer, not a buyer pool.
- Papers: no peer-reviewed study of outcome-based lift contracts found after 1 search; New Zealand's Auditor-General judged KPI-linked housing maintenance contracts effective [S45].
- Crowdfunding: none relevant (one elevator crowdfunding search found nothing [S46]).
- Closest existing thing: UNIS Avantage (a standard results contract sponsored by an association) combined with UK frameworks (pooled tender). Real difference: Indian volunteer societies pooled through federations, paid only from savings, measured by a no-hardware ledger. I do not claim novelty.

**First test** [A]: one federation, 10 societies, free X-rays in 4 weeks. Success: at least 6 hand over AMC papers and the median benchmark gap is at least 10%. Cost about Rs 40,000 plus 60 founder hours (Rs 45,000) [I].

Confidence: medium that the mechanism works (proven abroad); low that Indian committees will move as a group.

### Lead 2: Inspect-and-insure, an independent inspection that sizes and unlocks liability cover

**Method.** Mechanism transfer from Hartford Steam Boiler, which paired engineering inspection with insurance from 1866 [S21], and from UK engineering insurers that carry out statutory lift examinations [S22]. Constraint change: who inspects (independent, on demand, instead of a backlogged state). Inversion: the insurer, not the volunteer committee, becomes the party that demands quality.

**Core mechanism.** An independent inspection to a published checklist becomes the underwriting evidence for a lift liability policy sized to the real exposure. A licensed broker places the policy. The report goes to the committee, the insurer and the contractor. Red items must be closed to keep the cover. The committee gets a duty-of-care file as a by-product.

**Why the gap matters.**
- Joint and several liability was confirmed by the Supreme Court on 29 July 2026 [S17][S47].
- The award in that case was Rs 3,01,48,195 plus 9% annual interest from 2003, rising to 12% [S17]. At a simple 9% for 23 years, the total would be about Rs 9.3 crore [I] (simple interest assumed [A]; the 12% period not checked).
- One institutional buyer specified Rs 5 lakh per passenger and Rs 10 lakh in total [S12]. That is about 1% of the exposure above [I].
- At Rs 3 per mille [S11], a Rs 2 crore annual limit costs about Rs 60,000 a year and Rs 1 crore about Rs 30,000 [I]. The rate depends on risk group and limit ratios [S11], so these are rough.
- Sources disagree on who was the maintainer in the case: one gives Otis 70% as maintainer [S17]; another lists Otis at 70% and Military Engineering Services, the maintenance agency, at 25% [S47]. Either way the owner side was held liable too.

**How it works.**
1. Trigger: the Maharashtra Lifts Act comes into force on 1 November 2026 [S48] and requires owners to hold third-party insurance [S49]; Haryana needs insurance for registration [S50]; the ruling [S17].
2. The society books a "Lift Risk Inspection". An engineer checks brakes, ropes, door locks, rescue device, alarm, intercom, pit, machine room, earthing and documents, with the contractor's technician present. The engineer never works on the controller.
3. The report rates each item red, amber or green. The committee sends the red list to the contractor with a deadline. That creates the paper trail office-bearers need [I].
4. A broker partner places liability cover sized to the exposure and gives the insurer the report. Condition of renewal: yearly re-inspection and closure of red items.
5. Optional module, outside UP only: replace a comprehensive AMC with a non-comprehensive AMC plus machinery-breakdown cover plus a sinking fund. The inspector checks every parts claim. For a Rs 80,000 comprehensive AMC, a non-comprehensive one would be about Rs 48,500 if the 65% premium in [S23] holds, a gap of about Rs 31,500 [I]. But breakdown policies exclude wear, gradual deterioration and replaceable parts [S24], so only sudden failures (for example a drive burnt by a surge) move to the insurer. Housing-society package policies already list lifts and a breakdown section [S51].
6. When Maharashtra notifies its third-party lift inspection system [S25], apply for accreditation and become a statutory inspector (concept 8).

**What the buyer experiences.** One visit per lift. A colour-coded report in a week. A renewed policy with a limit that matches the risk. A file that shows the committee acted.

**Measurable advantage against the best current alternative.**
- Against waiting for the state inspector: available on demand, where only about 26% of Pune lifts were inspected in FY 2025-26 [S9][I].
- Against the contractor's own report: independent. France requires its five-yearly lift control to be done by a body with no link to the owner or maintainer [S52]; UK inspection bodies sell their independence [S53].
- Against current cover: sized to the exposure, not Rs 10 lakh [S12][I].

**Who pays, price logic, frequency.**

| Item | Figure | Tag |
|---|---|---|
| Inspection fee to the society | Rs 4,000 per lift a year, plus Rs 1,500 for a mid-year re-check of red items | [A] (basis: above state fees of Rs 1,000-2,000 [S13][S14]; test with 10 committees) |
| 10-lift society | Rs 40,000-55,000 a year, plus premium paid to the insurer | [I] |
| Engineer cost per lift | Rs 50,000 a month salary ÷ (4 lifts a day × 22 days) ≈ Rs 570 | [I] (salary and pace [A]) |
| Founder doing it | 2 hours × Rs 750 = Rs 1,500 per lift | [I] |
| Gross margin | About 60-85% | [I] |
| Maharashtra statutory market if third-party inspection opens | 2.1 lakh lifts [S25] × Rs 2,000-5,000 = Rs 42-105 crore a year | [I] (fee range [A]) |

Precedent for paid independent safety certificates: Maharashtra law requires owners to file fire Form B from a licensed agency twice a year [S32]; one 96-flat Mumbai society paid Rs 1.1 lakh for a one-off fire audit [S54].

The firm cannot take insurance commission itself: a corporate agent needs Rs 50 lakh net worth [S55], ten times the capital. Insurance revenue, if any, would be a fee from a broker for risk reports; whether IRDAI rules allow that was not checked [A].

**Production or delivery.** A qualified lift engineer (founder or first hire). Professional indemnity cover for the firm [A] (price not checked). A checklist built on the state rules and an Indian lift standard [A]. One broker partner. Start-up cash: about Rs 1.5 lakh for indemnity cover, legal terms and tools [A].

**Why makers would not block or copy.** A maker cannot credibly inspect lifts it maintains; France bars exactly that [S52]. A contractor can stall machine-room access. But the owner carries the legal duty under the state Acts [S50][S49], so committees can insist [I]. The real copiers are testing firms such as TÜV SÜD, which already has lift inspection accreditation in India [S56], and insurers' own surveyors.

**What must be true.**
1. At least one insurer or broker will write higher limits for societies and will use the report [A].
2. Committees will pay about Rs 4,000 per lift without a legal mandate, or Maharashtra will mandate third-party inspection [A].
3. The firm can survive a missed defect: indemnity cover and clear contract terms [A].
4. Contractors let the inspector observe with their technician present [A].

**Biggest risk.** The inspector's own liability. After an accident, an inspector who rated a lift green could be named alongside the committee. A second risk: at Rs 3 per mille, premiums are small, so insurers may not care about inspection quality on society policies [I].

**Prior-art check** (10 searches).
- Products and services: HSB's inspect-and-insure model [S21]; UK insurers (HSB, Zurich) carry out lift examinations [S22]; UK block-of-flats insurers sell lift insurance with inspection and breakdown [S57]. China: a monitoring, maintenance and insurance pilot by Taoping's Skyladder with PICC in Tianjin, August 2026, in a city of 160,000+ lifts [S58]; a South China reform added accident-liability insurance and gave insurers a supervisory role [S59]; Shanghai planned commercial insurance for lifts [S60]; Macau dropped a maintainer-insurance requirement [S61]. France: compulsory five-yearly independent lift control [S52].
- Patents (via search): Hartford US8271303 (premium set using monitored risk-reduction technology), MetLife US10762573, and others on sensor-based underwriting [S62]. None is lift-specific.
- Papers: no rigorous study of insurer involvement and lift accidents found after 2 searches; one 2025 paper notes Chinese pilots combining on-demand maintenance with liability insurance but does not measure outcomes [S59].
- Crowdfunding: not relevant to an inspection service; none found [S46].
- Closest existing thing: UK engineering insurers who inspect lifts and insure them. Real difference: in India the inspector is an independent small firm working with a broker, filling a state inspection backlog. I do not claim novelty.

**First test** [A]: 10 Pune or Mumbai committees offered a Rs 4,000-per-lift inspection plus a broker quote for higher cover in November 2026, the month the Act starts. Success: at least 3 pay within 6 weeks and the broker returns quotes from at least 1 insurer.

Confidence: medium on the insurance gap (sourced); low on insurer interest and committee willingness to pay.

### Lead 3: Society-side lift recorder, contractor-proof evidence read from the lift's own power supply

**Method.** Constraint change: move the sensing point from the lift car or controller to the society's own electrical supply. Research application: reading lift state and faults from motor or supply current [S63][S64][S26]. Elimination: the contractor leaves the data path.

**Core mechanism.** A split-core current clamp on one phase of each lift's incoming feeder, plus a voltage tap, sits in the society's panel. It logs every run, idle period, power cut and voltage event. Software turns this into uptime, trips per hour, abnormal run current (for example a dragging brake, which raises motor current [S64]), and slow inspection-speed runs that suggest a maintenance visit happened [A] (test on real lifts). Guards and residents add entrapment reports by QR, as in Lead 1.

**How it works.**
1. The society's own electrician clips the sensors on. No disconnection is needed: the closest patent notes that a galvanically separated sensor can be mounted without interrupting the supply [S26]. One 4-channel logger with a SIM per panel.
2. A two-week learning period sets each lift's normal pattern.
3. Alerts to the estate manager: no runs for more than 30 minutes in busy hours ("possibly out of service") [A]; abnormal run current; voltage outside about ±5% of nominal, the band one source calls tolerable [S65].
4. A monthly duty-of-care report: uptime per lift, outages and restore times, likely visit dates, and power events. The secretary signs it and sends it to the contractor.

**What the buyer experiences.** A small box in the electrical room. WhatsApp alerts. A one-page monthly report. No permission from the contractor, and nothing in the lift.

**Measurable advantage against the best current alternative.**
- Contractor veto: none, because nothing touches the lift [I]. Maker systems send alerts to the maker [S66].
- Cost: about Rs 5,000 per 4-lift panel [A] against one estimate of Rs 1-2 lakh for monitoring a six-storey Bengaluru building [S67] (attribution uncertain in that source).
- Blame-shifting: contractors and buildings attribute stoppages to voltage fluctuation [S68]; repeated lift power-supply burnouts have traced to a building's own board voltage [S69]. A timestamped voltage record settles who pays [I].

**Who pays, price logic, frequency.**

| Item | Figure | Tag |
|---|---|---|
| Kit, 4-lift panel, at cost | Rs 4,000-6,000 one-time | [A] (basis: consumer 3-phase CT meters sell at Rs 4,851-4,999 [S70][S71]) |
| Subscription | Rs 250 per lift a month = Rs 3,000 a year | [A] |
| Share of AMC | 2.4-6.3% | [I] (Rs 3,000 ÷ Rs 1,25,000 and ÷ Rs 48,000 [S4][S5]) |
| 4-lift tower | Rs 12,000 a year, billed Rs 1,000 a month | [I] |
| 500 lifts | Rs 15 lakh a year | [I] |
| Kits the firm could fund itself | Rs 5,00,000 ÷ Rs 4,000-6,000 = 83-125 kits | [I] |

The kit is priced under the lowest committee limit found (Rs 10,000 [S6]), and the fee is billed monthly so it fits routine spending authority [A] (test with committees). Facility management firms are a second channel: they serve many societies and need proof of their own SLAs [A].

**Production or delivery.** Prototype with off-the-shelf CT meters [S70]; then a custom logger with an ESP32-class chip, split-core CTs and a SIM, bill of materials Rs 3,500-6,000 [A]. Software on a cloud database plus WhatsApp. First 10 lifts: about Rs 60,000 of hardware and 80 founder hours (Rs 60,000) [I] (hours [A]).

**Why makers would not block or copy.** Nothing touches their equipment. A maker could offer a free dashboard, but it cannot sell independence from itself [I]. The real copy threat is retrofit IoT firms such as KALA or DATOMS moving to societies [S72][S73].

**What must be true.**
1. A single-phase current trace separates runs, idle, power cuts and inspection mode across drive types (VVVF, older drives, hydraulic) with useful accuracy. Test on 10 lifts of 4 brands [A].
2. Each lift has its own reachable feeder in a panel the society controls [A].
3. Committees act on alerts, so the record helps them and does not just show they knew [A].
4. The patents below do not block use in India. Freedom-to-operate check needed.

**Biggest risk.** The signal is ambiguous. It cannot detect an entrapment by itself, and an idle lift at 3 pm may simply be unused. If false "out of service" alerts are common, committees will ignore them. Second: patent exposure from the US11603286 family, whose assignee I did not see.

**Prior-art check** (6 searches).
- Products: KALA, non-invasive, not connected to lift controllers, sold by subscription in India since 2024 [S72]; LiftEnergy+, which tracks lift energy, trips and reliability [S74]; Owlsome LiFTMiND with trapped-passenger detection [S74]; Hong Kong's EMSD has asked for a non-intrusive current data acquisition device for lift monitoring and lists a non-intrusive sensor device [S75].
- Patents: US11603286B2, which infers lift operating state from the current-time profile on the supply line, built to retrofit [S26]; US11524876 for doors by the same method [S26]; US7350883 (brake drag from motor current) and US5765664 (drive faults from current) [S64]; JP7856408B2, a sensor not connected to the control board [S76].
- Papers: a 2023 Harbin Institute of Technology paper classifies lift condition from traction-machine current and active-power images [S63]; NUS EleTrack (2018), an in-cabin barometer and magnetometer device [S28].
- Crowdfunding: none found after 1 search [S46].
- Closest existing thing: US11603286B2 (the sensing method) and KALA (non-invasive and sold in India). Real difference: placement in the society's own panel, ownership by the society, power-quality evidence, and a price under the committee's limit. The method is not new. I do not claim novelty.

**First test** [A]: 10 lifts across 3 societies for 6 weeks, with guards keeping a paper log as ground truth. Success: at least 90% of outages over 30 minutes detected, and fewer than 1 false alert per lift a week.

Confidence: medium that it works technically for outage and run counting (patented and studied); low on willingness to pay without Lead 1's contract terms.

**How the three fit.** They are separate businesses, but Lead 3's data can feed Lead 1's penalties and Lead 2's insurer [I]. Lead 1 needs no hardware and is paid from savings, so it is the cheapest start [I].

## 6. Wildcard: the entrapment bounty

**Method.** Inversion: the trapped household, not the society, receives the penalty. Mechanism transfer from automatic parametric payouts (AXA's flight-delay product paid automatically once a flight was more than 2 hours late [S77]) and from public-sector liquidated damages in lift contracts [S15][S34].

**Mechanism.** The AMC sets a fixed penalty per verified entrapment, for example Rs 2,000 if longer than 10 minutes and Rs 5,000 if longer than 30 minutes [A]. It is paid to the society and credited to the trapped household's next maintenance bill. Residents report by QR or WhatsApp during the event; the guard and CCTV timestamp confirm it. Because each report earns money, residents report every entrapment. The society gets a complete record at no hardware cost, and the contractor faces a priced cost per failure.

**Why it might work.**
- It turns the 46% self-reported entrapment rate [S3] into a number the contractor pays for [I].
- At an assumed 4 entrapments per lift a year [A] (no per-lift rate found), Rs 2,000 each is Rs 8,000 a lift, about 10% of an Rs 80,000 AMC [I]. That is a real incentive.
- Residents see the guarantee directly, which builds support for the committee at the AGM [A].
- A confident contractor can offer it to stand out from makers [A].

**Why it is risky.**
- Contractors may refuse or load the price [A].
- Fake or staged entrapments, and disputes over minutes [A].
- AXA stopped selling its automatic-payout product for low demand and weak distribution [S77].
- If the firm funded payouts itself, that would be insurance business needing an IRDAI licence [I] (from the licensing rules in [S55]). It must stay a contract term between society and contractor.

Prior art: Hong Kong publishes lift contractor performance ratings and failure records [S29]; US and Australian public contracts set entrapment response times and per-day damages [S15][S34]. No contract paying trapped residents directly was found after 1 search.

## 7. Sources

All rows retrieved 2026-10-31. I opened no page. Rows marked "not re-checked by me" are the Market Investigator's sources, used as reported in `03-market-5-lifts.md`.

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Woman's death in lift: Noida police lodges FIR against society's maintenance firm, office-bearers, lift maker | Deccan Herald | https://www.deccanherald.com/india/womans-death-in-lift-noida-police-lodges-fir-against-societys-maintenance-firm-office-bearers-lift-maker-1243725.html | 2023-08 (approx.) | 2026-10-31 | FIR on AOA office-bearers | search summary (Investigator S12; not re-checked by me) |
| 2 | Pune: man dies after lift crash in Talegaon, case filed against society chairman and 11 others | Free Press Journal | https://www.freepressjournal.in/amp/pune/pune-man-dies-after-lift-crash-in-talegaon-case-filed-against-society-chairman-11-others | 2026-03 | 2026-10-31 | Case against society chairman | search summary (Investigator S13; not re-checked by me) |
| 3 | Got a lift in your apartment? Survey says 46% residents were trapped at least once last year | Business Today (LocalCircles) | https://www.businesstoday.in/amp/india/story/got-a-lift-in-your-apartment-survey-says-46-residents-were-trapped-at-least-once-last-year-546526-2026-07-31 | 2026-07-31 | 2026-10-31 | Entrapment rate; who maintains lifts | search summary (Investigator S1; also seen in my search) |
| 4 | Society maintenance charges in Navi Mumbai 2026 | navimumbai.com | https://navimumbai.com/?p=5471 | 2026 | 2026-10-31 | Per-lift AMC | search summary (Investigator S33; not re-checked by me) |
| 5 | Pune property maintenance charges guide 2026 | Pune Reality Hub | https://punerealityhub.pages.dev/blog/pune-property-maintenance-charges-guide-2026 | 2026 | 2026-10-31 | Per-lift AMC; lifts per flats | search summary (Investigator S34; not re-checked by me) |
| 6 | Dispute with apartment association, Bengaluru | Vidhikarya | https://www.vidhikarya.com/FreeLegalAdvice/43211/dispute-with-apartment-association-bengaluru-bangalore | not shown; retrieved 2026 | 2026-10-31 | Rs 10,000 approval threshold | search summary (Investigator S60; not re-checked by me) |
| 7 | Model bye-laws of cooperative housing society: maintenance accounts | MySocietyClub | https://mysocietyclub.com/bye-laws/maharashtra-cooperative-housing-society-bye-laws/maintenance-accounts | not shown; retrieved 2026 | 2026-10-31 | Committee spending limit | search summary (Investigator S57; not re-checked by me) |
| 8 | Uttar Pradesh Lifts and Escalators Act, 2024 | TeamLease RegTech | https://www.teamleaseregtech.com/updates/article/32469/uttar-pradesh-lifts-and-escalators-act-2024 | 2024 | 2026-10-31 | Comprehensive AMC from OEM or authorised provider; agency registration (attribution among results uncertain) | search summary |
| 9 | Sinhagad Road lift tragedy puts spotlight on delayed safety audits | Punekar News | https://www.punekarnews.in/?p=235806 | 2026-05 | 2026-10-31 | Pune inspection backlog | search summary (Investigator S7; not re-checked by me) |
| 10 | Elevator maintenance checklist | NoBrokerHood | https://www.nobrokerhood.com/blog/elevator-maintenance-checklist/ | not shown; retrieved 2026 | 2026-10-31 | Out-of-AMC repair cost | search summary (Investigator S71; not re-checked by me) |
| 11 | Terms and conditions for Lift Insurance Policy (Liability Cover) | indiacustomercare.com (reproducing New India Assurance terms) | https://www.indiacustomercare.com/terms-conditions-lift-insurance-policy-liability-cover | undated | 2026-10-31 | Rs 3 per mille of annual limit (attribution between this and the site's public liability page uncertain) | search summary |
| 12 | Tender for insurance including passenger lift third-party cover | IIM Kozhikode | https://iimk.ac.in/uploads/tenders/_601103641.pdf | not shown; retrieved 2026 | 2026-10-31 | Rs 5 lakh per passenger, Rs 10 lakh total | search summary |
| 13 | CEI Haryana fees page | Chief Electrical Inspector, Haryana | https://ceiharyana.com/StaticPage1.aspx | not shown; retrieved 2026 | 2026-10-31 | Periodic inspection fee | search summary (Investigator S23; not re-checked by me) |
| 14 | BMC conducts safety audit of only 400 lifts in Bhopal high-rise buildings | Free Press Journal | https://www.freepressjournal.in/amp/bhopal/bmc-conducts-safety-audit-of-only-400-lifts-in-bhopal-high-rise-buildings | not shown; retrieved 2026 | 2026-10-31 | Rs 2,000 electrical safety fee | search summary |
| 15 | TK Elevator Australia lift maintenance contract (redacted) | NSW Department of Planning | https://www.dpie.nsw.gov.au/__data/assets/pdf_file/0007/624796/TK-Elevator-Australia-Pty-Ltd-Lift-Maintenance-Contract_Redactedv4.pdf | not shown; retrieved 2026 | 2026-10-31 | 30-minute entrapment response; also LA Metro and Hawaii damages in same search | search summary |
| 16 | VDA supplier page (nonprofit) | OMNIA Partners | https://www.omniapartners.com/suppliers/vda/nonprofit | not shown; retrieved 2026 | 2026-10-31 | Claimed 10-15% maintenance cost reduction; consultant sold via purchasing group | search summary |
| 17 | M/s Otis Elevator Co (India) Ltd v Rashmi Handa & Others, 2026 INSC 756 | Verdictum | https://www.verdictum.in/supreme-court/ms-otis-elevator-co-india-ltd-v-rashmi-handa-others-2026-insc-756-1618809 | 2026-07-29 | 2026-10-31 | Joint liability; award and interest; apportionment | search summary (Investigator S9; not re-checked by me) |
| 18 | CHIC Lifts & Mobility Aids Framework 2025-29 | Find a Tender (UK) | https://www.find-tender.service.gov.uk/procurement/ocds-h6vhtk-052585 | 2025 | 2026-10-31 | Pooled lift framework; GBP 100 million lot value | search summary |
| 19 | Lifts Install, Refurbishment and Maintenance (Efficiency East Midlands) | Bidstats | https://bidstats.uk/tenders/2021/W43/761659743 | 2021 | 2026-10-31 | 261 member organisations | search summary |
| 20 | Contrat UNIS Avantage ascenseurs (press release) | UNIS Marseille Provence Corse | https://www.unis-immo.fr/app/uploads/2026/04/2026.03.09-CP-UNIS-MPC-Contrat-UNIS-Avantage-ascenseurs.pdf | 2026-03-09 | 2026-10-31 | Results duty, automatic penalties, non-proprietary telealarm, 2006 predecessor (also Monimmeuble coverage, https://monimmeuble.com/?p=106140) | search summary |
| 21 | The history of Hartford Steam Boiler | Munich Re HSB | https://munichre.com/hsbeil/en/about-us/hsb-engineering-insurance/history.html | not shown; retrieved 2026 | 2026-10-31 | Inspection paired with insurance from 1866 | search summary |
| 22 | LOLER inspection of lifting equipment | Munich Re HSB Engineering Insurance | https://www.munichre.com/hsbeil/en/services/engineering-inspection-services/uk/LOLER-inspection-lifting-equipment.html | not shown; retrieved 2026 | 2026-10-31 | Insurers' engineers examine lifts (also Zurich, https://www.zurich.co.uk/engineering/inspection/lifts-and-lifting-equipment) | search summary |
| 23 | Lift AMC evaluation guide India | Studio Matrx | https://www.studiomatrx.org/guides/lift-amc-evaluation-guide-india | 2026 | 2026-10-31 | Comprehensive about 60-70% above non-comprehensive (home lifts) | search summary |
| 24 | Machinery Breakdown Insurance Policy Wording (Commercial) | Zurich Kotak | https://cms.zurichkotak.com/uploads/32_Machinery_Breakdown_Insurance_Policy_Wording_Commercial_78baabcd5f.pdf | not shown; retrieved 2026 | 2026-10-31 | Exclusion of gradual deterioration; also New India and Bajaj wear-and-tear exclusions in same search | search summary |
| 25 | Maha to strengthen lift inspection system, 519 posts to be created | Lokmat Times | https://www.lokmattimes.com/national/maha-to-strengthen-lift-inspection-system-519-posts-to-be-created-cm-fadnavis | 2026-03-04 | 2026-10-31 | Planned third-party inspection; 2.1 lakh lifts | search summary |
| 26 | US11603286B2 Method and device for determining an operating state of an elevator system | Google Patents | https://patents.google.com/patent/US11603286 | application published 2018 (US20180215578); grant date not shown | 2026-10-31 | Supply-line current profile; retrofit; family US11524876 | search summary |
| 27 | Raising the Bar(ometer): identifying a user's stair and lift usage through wearable sensor data | AITopics (arXiv record) | https://aitopics.org/doc/arxivorg:C3F07693 | not shown; retrieved 2026 | 2026-10-31 | Barometer lift detection | search summary |
| 28 | EleTrack (EWSN 2018) | National University of Singapore | https://www.comp.nus.edu.sg/%7Echanmc/papers-by-year/2018-ewsn-eletrack.pdf | 2018 | 2026-10-31 | In-cabin barometer and magnetometer prototype | search summary |
| 29 | EMSD releases lift and escalator contractors' latest performance ratings | Hong Kong Government | https://www.info.gov.hk/gia/general/202507/17/P2025071700473p.htm | 2025-07-17 | 2026-10-31 | Public ratings, convictions and failure records; April 2026 release also seen | search summary |
| 30 | Otis Worldwide to buy majority stake in WeMaintain | Nasdaq | https://www.nasdaq.com/articles/otis-worldwide-buy-majority-stake-wemaintain | 2026-04 | 2026-10-31 | Independent maintainer absorbed | search summary (Investigator S50; not re-checked by me) |
| 31 | Rieka Elevator and Escalators startup listing | Startup in UP portal | https://www.startinup.up.gov.in/crm/Welcome/startup_user_details/NDE3MDY= | not shown; retrieved 2026 | 2026-10-31 | Indian smart-AMC rival | search summary (Investigator S44; not re-checked by me) |
| 32 | Mumbai Fire Safety Week: Form B mandatory for all buildings | Free Press Journal | https://www.freepressjournal.in/amp/mumbai/mumbai-fire-safety-week-begins-form-b-mandatory-for-all-structures | not shown; retrieved 2026 | 2026-10-31 | Licensed-agency Form B twice a year | search summary |
| 33 | BAF urges govt to table, implement Karnataka Apartment Ownership Act | Newsdrum (IANS) | https://www.newsdrum.in/national/baf-urges-govt-to-table-implement-karnataka-apartment-ownership-act-10866157 | 2025-12 | 2026-10-31 | BAF 1,400+ member associations | search summary (Investigator S65; not re-checked by me) |
| 34 | RFP Elevator Maintenance and Repair Services | City of Covina | https://covinaca.gov/wp-content/uploads/2024/03/RFP-Elevator-Maintenance-and-Repair-Services.pdf | 2024-03 | 2026-10-31 | 30-minute entrapment response | search summary |
| 35 | Notice inviting tender, lift AMC | Nalanda University | https://nalandauniv.edu.in/wp-content/uploads/2026/03/NIT.pdf | 2026-03 | 2026-10-31 | 2% per month per lift penalty | search summary (Investigator S37; not re-checked by me) |
| 36 | Investigation into lift spare parts suppliers: commitments | Competition and Consumer Commission of Singapore | https://www.ccs.gov.sg/case-register/public-register/commitments-and-remedies/investigation-into-lift-spare-parts-suppliers--bnf- | not shown; retrieved 2026 | 2026-10-31 | Parts withheld from a third-party maintainer; commitments | search summary |
| 37 | Behringer Harvard vertical transportation case | consultant site (squarespace) | https://boca-draft.squarespace.com/behringer-harvard | not shown; retrieved 2026 | 2026-10-31 | Renegotiation across 400 elevators; volume pricing by bundling buildings (same search) | search summary |
| 38 | Delivering elevator reliability in healthcare | Reliabilityweb | https://reliabilityweb.com/amp/elevator-reliability-2674310676 | not shown; retrieved 2026 | 2026-10-31 | MTBF change after results-linked contract | search summary |
| 39 | Lift and Escalator Act, 2024: Noida dominates registration drive across Uttar Pradesh | The Realty Today | https://therealtytoday.com/news/trending/lift-and-escalator-act-2024-noida-dominates-registration-drive-across-uttar-pradesh | not shown (after Oct 2024) | 2026-10-31 | 87 manufacturers and 98 AMC agencies registered in UP | search summary |
| 40 | Four in 10 Bengalureans dread stepping into a lift: survey | Deccan Herald | https://deccanherald.com/india/karnataka/bengaluru/four-in-10-bengalureans-dread-stepping-into-a-lift-survey-4098155 | 2026-08 | 2026-10-31 | Bengaluru maker vs third-party split (as reported by the Hunter; not re-checked by me) | search summary |
| 41 | CCI imposes Rs 2,544 crore fine on 14 car manufacturers | Bar & Bench | https://www.barandbench.com/news/cci-imposes-rs-2544-crore-fine-14-car-manufacturers | 2014 | 2026-10-31 | Indian precedent on spare-parts restriction | search summary |
| 42 | Periodic maintenance requirements (lifts) | Building and Construction Authority, Singapore | https://www1.bca.gov.sg/safety-and-standards/lifts-escalators-and-mechanised-car-parking-systems/fixed-installations-legislations/periodic-maintenance-requirements/ | not shown; retrieved 2026 | 2026-10-31 | Regulator encourages outcome-based lift contracts | search summary |
| 43 | How housing societies can control elevator expenses for their buildings | Free Press Journal | https://www.freepressjournal.in/amp/business/how-housing-societies-can-control-elevator-expenses-for-their-buildings | not shown; retrieved 2026 | 2026-10-31 | Independent consultants for societies | search summary |
| 44 | US8028807B2 Remote recording of maintenance operations | Google Patents | https://patents.google.com/patent/US8028807 | 2011 | 2026-10-31 | Availability standard offered to customer; Hitachi US7194415 (https://patents.google.com/patent/US7194415) in same search | search summary |
| 45 | State housing: managing maintenance work | Office of the Auditor-General, New Zealand | https://oag.parliament.nz/2008/state-housing/part3.htm | 2008 | 2026-10-31 | KPI-linked maintenance contracts judged effective | search summary |
| 46 | IoT-Intelligent Elevator Movement Surveillance Device (i-EMSD), returned by a crowdfunding search that found no campaigns | EMSD Innovation (Hong Kong) | https://inno.emsd.gov.hk/en/inno-catalogue/details/index_id_49.html | not shown; retrieved 2026 | 2026-10-31 | No Kickstarter or Indiegogo campaign found | search summary |
| 47 | No more shifting blame: Supreme Court rules building owners, makers jointly liable for lift accidents | WION | https://www.wionews.com/india-news/no-more-shifting-blame-supreme-court-rules-building-owners-makers-jointly-liable-for-lift-accidents-1785387070126 | 2026-07 | 2026-10-31 | Joint liability; 70/25/5 split naming MES as maintenance agency | search summary |
| 48 | Maharashtra brings Lift and Escalator Safety Regime into force from 1 November | SCC Online | https://www.scconline.com/blog/?p=399876 | 2026-10 | 2026-10-31 | Act in force 1 Nov 2026, notified 22 Oct 2026 | search summary |
| 49 | Great move toward safety | Elevator World | https://elevatorworld.com/?p=49622 | not shown (c. 2018) | 2026-10-31 | Maharashtra third-party insurance duty | search summary |
| 50 | Checklist for registration and inspection of lifts and escalators | Chief Electrical Inspector, Haryana | https://ceiharyana.com/Procedure_For_Registration_Lift_Exclator.aspx | not shown; retrieved 2026 | 2026-10-31 | AMC and insurance needed for registration | search summary (Investigator S21; not re-checked by me) |
| 51 | Housing Society Package Plus Policy prospectus | Zurich Kotak | https://cms.zurichkotak.com/uploads/36_HOUSING_SOCIETY_PACKAGE_PLUS_POLICY_PROSPECTUS_b5e0834fdc.pdf | not shown; retrieved 2026 | 2026-10-31 | Lifts in common areas; breakdown section | search summary |
| 52 | Contrôle technique quinquennal des ascenseurs (FAQ) | French Ministry of Ecology | https://www.ecologie.gouv.fr/sites/default/files/documents/Questions%20r%C3%A9ponses%20addititif%20n%C2%B01%20concernant%20les%20contr%C3%B4les%20techniques%20quinquennaux%20-%20mars%202014.pdf | 2014-03 | 2026-10-31 | Five-yearly independent control; independence rules (also Monimmeuble, https://monimmeuble.com/?p=56440) | search summary |
| 53 | Lifting equipment inspections and testing (LOLER) | Bureau Veritas UK | https://bureauveritas.co.uk/engineering-inspections/loler-testing | not shown; retrieved 2026 | 2026-10-31 | Independence as a selling point | search summary |
| 54 | Case study: fire safety audit of residential building | Elion | https://elion.co.in/case-study-fire-safety-audit-of-residential-building/ | 2024-02-17 | 2026-10-31 | Rs 1.1 lakh one-off audit, 96 units | search summary |
| 55 | Requirements for registering as a corporate agent | IRDAI policyholder portal | https://policyholder.gov.in/web/guest/requirements-for-license-as-a-corporate-agent | not shown; retrieved 2026 | 2026-10-31 | Rs 50 lakh capital and net worth | search summary |
| 56 | Independent third-party lift inspections tailored for India | TÜV SÜD (PresseBox) | https://www.pressebox.com/pressrelease/tuev-sued-ag/independent-third-party-lift-inspections-tailored-for-india/boxid/1277681 | not shown; retrieved 2026 | 2026-10-31 | Incumbent inspection firm | search summary (Investigator S56; not re-checked by me) |
| 57 | Lift insurance and inspection | London Flats Insurance | https://www.londonflatsinsurance.co.uk/blocks-of-flats-insurance/lift-insurance-and-inspection/ | not shown; retrieved 2026 | 2026-10-31 | Insurance bundled with inspection for blocks of flats | search summary |
| 58 | Taoping launches new smart elevator insurance pilot program | Barchart (PR Newswire) | https://www.barchart.com/story/news/3754817/taoping-launches-new-smart-elevator-insurance-pilot-program | 2026-08-10 | 2026-10-31 | Tianjin monitoring, maintenance and insurance pilot | search summary |
| 59 | Innovation in elevator safety management in South China | Elevator World | https://elevatorworld.com/?p=38924 | not shown; retrieved 2026 | 2026-10-31 | Accident-liability insurance; insurers as supervisors; MDPI 2025 paper on pilots (https://www.mdpi.com/2076-3417/15/15/8644/htm) in same search | search summary |
| 60 | Plan calls for elevator insurance | Shanghai Daily | https://archive.shine.cn/metro/Plan-calls-for-elevator-insurance/shdaily.shtml | not shown; retrieved 2026 | 2026-10-31 | Shanghai plan | search summary |
| 61 | Macau government nixes VT maintenance insurance requirement | Elevator World | https://elevatorworld.com/news/daily-news/macau-government-nixes-vt-maintenance-insurance-requirement | not shown; retrieved 2026 | 2026-10-31 | Requirement dropped | search summary |
| 62 | US8271303B2 (Hartford) and related sensor-underwriting patents | Google Patents | https://patents.google.com/patent/US8271303B2/en | 2012 | 2026-10-31 | Premium based on monitored risk-reduction technology; MetLife US10762573 in same search | search summary |
| 63 | Two-dimensional images of current and active power signals for elevator condition recognition | Journal of Harbin Institute of Technology (New Series) | https://hit.ijournals.cn/jhit_cn/article/html/20230204 | 2023 | 2026-10-31 | Condition from current and power | search summary |
| 64 | US7350883B2 Detecting elevator brake and other dragging by monitoring motor current | Google Patents | https://patents.google.com/patent/US7350883 | 2008 | 2026-10-31 | Brake drag from current; US5765664 (https://patents.google.com/patent/US5765664) in same search | search summary |
| 65 | Managing the menace of high voltage | Electrical India | https://www.electricalindia.in/?p=16312 | not shown; retrieved 2026 | 2026-10-31 | ±5% tolerable band | search summary |
| 66 | Johnson Lifts launches IoT-based feature named WATCH | ThePrint (ANI) | https://theprint.in/ani-press-releases/johnson-lifts-launches-an-iot-based-technological-feature-in-its-lifts-named-watch/1137423 | 2022 | 2026-10-31 | Trap alerts go to the maker | search summary (Investigator S40; not re-checked by me) |
| 67 | Lift installation cost India residential 2026 | Aecord | https://aecord.com/blog/lift-installation-cost-india-residential-2026 | 2026 | 2026-10-31 | Rs 1-2 lakh IoT estimate (attribution uncertain) | search summary (Investigator S45; not re-checked by me) |
| 68 | Indian court order noting lifts stopping due to voltage fluctuation | Indian Kanoon | https://future.indiankanoon.org/doc/73160522/ | not shown; retrieved 2026 | 2026-10-31 | Voltage blamed for stoppages | search summary |
| 69 | Investigating repeated lift panel power supply failures in an office building | newpages.asia | https://mail.newpages.asia/ph/zh/news/175752 | not shown; retrieved 2026 | 2026-10-31 | Burnouts traced to local board voltage | search summary |
| 70 | 200A three-phase power meter with inbuilt CT | IndiaMART | https://m.indiamart.com/proddetail/three-phase-meter-power-meter-with-inbuilt-ct-2855874857348.html | not shown; retrieved 2026 | 2026-10-31 | Rs 4,851 per piece | search summary |
| 71 | XPR3SS 100A 3-phase bi-directional energy meter price history | pricehistory.app | https://pricehistory.app/p/xpr3ss-100a-3-phase-bi-directional-energy-CotD7Ace | 2026-03-20 | 2026-10-31 | Rs 4,999 | search summary |
| 72 | PAPL, Ardelisys launch IoT-based elevator monitoring system at SLM World in India | Elevator World | https://elevatorworld.com/news/daily-news/papl-ardelisys-launch-iot-based-elevator-monitoring-system-at-slm-world-in-india | 2024-03 | 2026-10-31 | KALA non-invasive, subscription | search summary |
| 73 | Connected IoT elevators | DATOMS | https://datoms.io/elevator-escalator-monitoring/ | not shown; retrieved 2026 | 2026-10-31 | Retrofit IoT aimed at makers | search summary (Investigator S42; not re-checked by me) |
| 74 | Smart Lifts: LiftEnergy+ case study | Indeema | https://indeema.com/portfolio/smart-lifts | not shown; retrieved 2026 | 2026-10-31 | Energy, trips, reliability; Owlsome LiFTMiND (https://info.exosite.com/owlsome_lift) in same search | search summary |
| 75 | Research, design and installation of a non-intrusive current data acquisition device for lift monitoring | EMSD Innovation (Hong Kong) | https://inno.emsd.gov.hk/en/it-wish-list/index_id_172.html | not shown; retrieved 2026 | 2026-10-31 | Regulator wants non-intrusive current sensing; also index_id_958 solution page | search summary |
| 76 | JP7856408B2 remote monitoring support device | Goveda | https://www.goveda.com/patent/JP-7856408-B2 | not shown; retrieved 2026 | 2026-10-31 | Sensor not connected to control board | search summary |
| 77 | AXA stops selling blockchain flight delay product | Post Online | https://www.postonline.co.uk/personal/4461796/axa-stops-selling-blockchain-flight-delay-product | 2019 | 2026-10-31 | Automatic payout after 2 hours; closed for low demand and weak distribution | search summary |
