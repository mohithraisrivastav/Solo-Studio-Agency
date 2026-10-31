# Hunt C: Underserved and premium

Run: 2026-10-31 acceptance test. Role: Opportunity Hunter. Lens C: specialised buyers nobody serves well, poor experiences people still pay for, unmet premium demand.

Constraints applied, as given in runs/2026-10-31-acceptance/00-brief.md: founder capital Rs 5,00,000, founder time valued at Rs 750 per hour, India first [A] (user-set constraints, not market facts).

## Method and limits

- About 75 web searches across five industries. WebFetch failed for every host I tried (medicaldialogues.in and businesstoday.in did not resolve in this session). Every source below was seen only through search-result summaries and is marked "search summary". I opened no web page.
- Currency: Rs (INR) unless stated. Conversions use USD 1 = Rs 88 and AED 1 = Rs 24, both assumed for 2026-10-31 and not checked [A]. Prices are ex-GST unless stated. Where GST applies to a service, I assume 18% [A] (standard rate for most services; confirm with a CA).
- Not checked: whether Indian drug inspectors accept shared or third-party supplier audits; any buyer's willingness to pay (no buyer contact, so demand evidence stops at L1); current prices of Qualifyze, Intertek, DATOMS or KALA in India; RWA budgets; NRI case volumes; the full text of any regulation or judgment.

## 1. Industries chosen and why

I chose five industries that do not depend on each other and avoid common startup themes. The pharma one is the unglamorous business-to-business niche.

**A. Small-scale pharmaceutical manufacturing (business-to-business, industrial)**
- Revised Schedule M became binding on all units from 1 January 2026, and the health ministry was unlikely to extend the deadline for small firms [S1]. Only about 1 in 4 small units had filed upgrade plans before the deadline [S2], so thousands of plants must change how they buy and control inputs [I].
- After the Coldrif deaths, CDSCO in October 2026 told states to make manufacturers test high-risk excipients such as propylene glycol and glycerin [S10], and an August 2026 circular asked for robust vendor qualification systems [S16]. New compulsory work for buyers with little quality staff is a spending shift that opens niches [I].

**B. Bereavement and estate administration**
- 86.6 lakh deaths were registered in 2023 [S44]. When the government launched a recovery drive in October 2025, about Rs 1.84 lakh crore sat unclaimed in banks, insurance, mutual funds and dividends [S38].
- RBI's 2025 Directions give banks a 15-day window and compensation for delay on deceased-customer claims, with implementation by 31 March 2026 [S36][S37]. Up to four nominees are allowed from 1 November 2025 [S53]. The rules are being standardised in one place while families still face scattered processes everywhere else [I].

**C. Residential lifts (building maintenance)**
- A LocalCircles survey (11,229 respondents, July 2026) found 46% of lift users or their family were trapped at least once in the past year, and 21% said their building had no proper maintenance contract (AMC) [S65].
- On 29 July 2026 the Supreme Court held OTIS liable as maker and comprehensive maintenance contractor [S68]. One report says maker, maintenance operator and premises owner can all be jointly liable [S69]. Uttar Pradesh's 2024 Act makes lift registration and a comprehensive AMC compulsory [S70][S71].

**D. Luxury goods aftercare (watches, leather goods)**
- Swiss watch exports to India reached about CHF 274 million in 2024, up roughly 25% [S89]. TEPA, in force from 1 October 2025, phases out India's roughly 22% duty on Swiss watches over seven years [S90].
- India's pre-owned luxury watch market was put at about USD 405 million in 2023 and projected at USD 862 million by 2030 [S91]. Major Louis Vuitton repairs go to the brand's care centre in France and can take one to three months [S97].

**E. Indian classical performing-arts supply for the diaspora**
- A US arangetram (a Bharatanatyam debut) was reported at about USD 30,000 with four musicians flown in from India [S102]. That is premium spending on a supply chain based in India [I].
- Buyers abroad report poor setup, shipping damage and disappointment with bargain sitars bought online [S99][S100]. A harmonium brand that is tuned in the US sells at USD 1,199 [S105], which suggests buyers pay for quality assurance [I].

## 2. Raw candidates

| # | Problem | Payer | Signal | Tag |
|---|---|---|---|---|
| 1 | Small drug makers must audit and approve their raw-material suppliers, especially of high-risk excipients, but cannot afford one audit per supplier | Owner of the small plant | Revised Schedule M requires supplier audits before approval; weak vendor qualification is a common inspection finding; abroad, shared audits cut the cost to USD 800-2,000 per sponsor | [S9][S15][S18] |
| 2 | Small plants need cleanroom, HVAC and storage-area validation | Plant owner | IndiaMART listings at Rs 3,000-3,500 per day | [S28] |
| 3 | Small plants lack a working quality system (quality procedures, documents, quality software) | Plant owner | About 1 in 4 filed upgrade plans; quality software from USD 79 per user; many freelancers | [S2][S31][S29] |
| 4 | Heirs, especially those abroad, cannot efficiently settle a dead parent's bank, demat, insurance and property claims | Legal heirs, often non-resident Indian (NRI) children | Rs 1.84 lakh crore unclaimed; banks demanded succession certificates inconsistently; court fee up to 3% of asset value | [S38][S37][S42] |
| 5 | City funerals are opaque and families get overcharged | Bereaved family | Bengaluru families charged Rs 3,000-5,000 for a Rs 250 civic cremation | [S58] |
| 6 | Bringing bodies home from the Gulf is slow and confusing | Employer, insurer or family | 7,096 bodies repatriated in 2024; air cargo AED 1,800-2,500 | [S61][S62] |
| 7 | Shares and dividends stuck with the investor protection fund (IEPF) | Investor or heir | One firm claims 117 crore shares worth Rs 40,000-50,000 crore lie unclaimed | [S63] |
| 8 | Housing societies pay for lift AMCs but cannot check the upkeep, and they now carry liability | Society owners' association (RWA or AOA) | 46% trapped in a year; 21% with no proper AMC; Supreme Court joint liability | [S65][S69] |
| 9 | Buyers of pre-owned luxury watches cannot check authenticity or get trusted, affordable servicing | Collector | Pre-owned market about USD 405 million; at one dealer, Rolex fakes are half of all knockoffs | [S91][S94] |
| 10 | Brand repairs of luxury leather goods take months | Owner | Major Louis Vuitton repairs go to France and take 1-3 months | [S97] |
| 11 | Students abroad cannot get a properly set-up, warrantied Indian classical instrument | Student or parent abroad | Forum complaints; US-tuned harmonium at USD 1,199 | [S99][S100][S105] |
| 12 | Diaspora families struggle to coordinate costumes, jewellery and musicians from India for an arangetram | Parents abroad | Budgets near USD 30,000 | [S102] |

I investigated candidates 1, 4, 5, 6, 8, 9 and 11 further (4 or more extra searches each). I kept 1, 4 and 8.

## 3. Opportunity theses

### Thesis 1: Shared supplier audits for small Indian drug makers (candidate 1)

**Problem.** Revised Schedule M says a manufacturer must set up a process for approving suppliers of starting and packaging materials, judge them on history and GMP compliance, and audit them before approval [S9]. Commentary describes an approved-vendor list with audit and re-qualification cycles for critical suppliers [S9]. Most small plants cannot afford, staff or schedule one audit per supplier [I] (a 2-day site visit per supplier [S21] multiplied across many suppliers, set against Baddi senior QA officer salaries of Rs 2.7-6.5 lakh a year [S30]). Inspectors list weak vendor qualification among the most common findings of risk-based inspections [S15]. Coldrif showed the cost of failure. The propylene glycol was bought from two local distributors that held no licence for pharma-grade material [S12]. It was never tested for DEG [S12], and Tamil Nadu then found 39 critical and 325 major non-compliances at the plant [S13]. In Himachal, a trader was arrested for relabelling low-grade material as a known excipient maker's product and selling it to drug firms [S14].

**Who pays, who uses, who can block.**
- Economic buyer: the owner or managing director of a small formulation plant [A] (in small firms the owner usually approves spending; test with 10 calls).
- User: the QA head or QA officer.
- Can block: suppliers and traders who refuse audits or refuse to let reports be shared; state drug inspectors, if they reject third-party audit reports (not checked); the plant's existing consultant.

**Current alternatives and what buyers spend.**
- Paper qualification using a supplier questionnaire and certificate of analysis. I assume this is the most common practice, which is why vendor qualification shows up as an inspection finding [A, basis S15].
- Own audit by plant staff. Indian sites usually allow two days on site [S21].
- Local consultants. One IndiaMART listing offers GMP lead-auditor services at Rs 29,000 a month [S27]. A freelance pharma QA writer charges USD 20 an hour, about Rs 1,760 at the assumed rate [S29].
- Global shared audits. Rx-360 put a standalone audit at USD 7,000-10,000 and a shared one at USD 800-2,000 per sponsor [S18], about Rs 70,400 to Rs 1,76,000 per sponsor [I]. That article's date was not shown and describes the programme just after its pilot, so the price is old and stale [I]. Qualifyze, Intertek, Eurofins and Diapharm sell shared audits or ready reports, priced on request [S20][S25][S24][S22]. Pharmaoffer estimates one supplier audit costs about USD 24,000 all-in for a Western buyer [S21].
- A domestic price per audit was not found after 3 searches (queries: "vendor audit charges India pharma third party auditor per day fee API supplier audit cost INR", "vendor audit service pharma India charges per audit rupees consultant supplier GMP audit excipient manufacturer Gujarat", "Qualifyze India distributors directory audit library price per report").

**Frequency and cost of the problem to the buyer.**
- Frequency: suppliers must be approved before first use and re-qualified on a cycle [S9]. In 2023 CDSCO planned audits of raw-material and packaging suppliers "at least once a year" [S17]. I found no final notification of that annual rule after 1 search.
- Cost of failure: regulators have issued show-cause notices, stop-production orders, and licence suspensions or cancellations (over 200 actions in one 2024 count) [S111]. One 2024 report says 36% of about 400 inspected plants were shut [S34]. Upgrades cost an estimated Rs 50 lakh to Rs 2.5 crore per unit [S2]. A plant that has spent that much cannot afford to fail on supplier paperwork [I].

**Why now.**
- Schedule M has been binding since 1 January 2026, and the government was unlikely to grant small firms another extension [S1]. DCGI told states in November 2025 to act strictly against non-compliant units [S110].
- In October 2026 CDSCO told states to make manufacturers test raw materials and finished products, naming excipients such as propylene glycol, glycerol and sorbitol [S10]. A CDSCO circular dated 5 August 2026 asks states to make manufacturers follow robust vendor qualification systems [S16]. The Indian Pharmacopoeia reportedly added DEG/EG testing for all oral liquids [S11].
- In Himachal, only a small share of units were found fully compliant in January 2026, and about 80 got notices [S8].

**Why unsolved.** Category (e): fragmented buyers nobody serves well, plus (f): the task only recently became compulsory. Shared-audit firms exist and cover India [S20][S25], but they serve Western buyers auditing Indian makers of active ingredients for export [S35][S20], and their pricing is in USD or on request [S18][S20] [I]. Small Indian plants buy through local distributors and traders [S12][S14], and I found no service aimed at that segment. No domestic audit-sharing service was found after 2 searches (queries: "India pharma vendor audit report marketplace startup audit sharing platform domestic manufacturers", "supplier audit fatigue excipient manufacturer India customer audits per year shared audit benefit suppliers").

**Competitors, including failed attempts.**
- Qualifyze (Germany) raised about USD 12 million in 2023 while tracking toward USD 10 million+ annual recurring revenue [S19]. It runs shared audits and lists Indian manufacturers in its audit library [S20], and partnered with the distributor Brenntag [S26].
- Others: Rx-360 joint audits [S18]; Intertek shared audits, which now cover India [S25]; Eurofins [S24]; Diapharm, with 500+ GMP audit reports [S22]; the Pharmaoffer audit-report library [S112]; Mendel Genetics, which audits Indian suppliers for North American buyers [S35]; local consultants [S27].
- Failed attempts: none found after 2 searches (same queries as above).
- Suppliers have their own reason to want shared audits. Large API makers can face up to 100 customer audit requests a year [S22], and excipient makers often host 10+ direct-customer audits a year [S23]. Eurofins says a typical shared audit has 5-10 buyers [S24] (all vendor claims).

**Barrier for a small new entrant, and the way in.**
- Barriers: auditor credibility (the founder needs GMP audit experience or a partner who has it) [A]; getting suppliers to consent; liability if an audited supplier later ships bad material; uncertainty over whether regulators accept shared reports.
- Way in: start with the high-risk excipients CDSCO named (glycerin, propylene glycol, sorbitol, maltitol, certain PEGs) [S10] and the traders and distributors serving one cluster. Baddi in Himachal is a candidate: it had about 400 small units before 144 closed [S6]. Offer suppliers "be audited once and share with all your customers" (Qualifyze runs an auditee programme on the same logic [S113]). Pre-sell each audit to 4 or more buyers before booking it.
- Capital: per-audit cash cost of about Rs 60,000 [A] (2 auditor-days at Rs 20,000 a day, about Rs 15,000 travel and Rs 5,000 report writing; the day rate sits above the Rs 1,760-per-hour freelance rate [S29]). Templates, agreements and a website fit well inside Rs 5,00,000 [A].
- Rough economics: at Rs 20,000 per shared report [A] (about a third of the low end of Rx-360's shared price [S18]; test with 10 QA heads), an audit breaks even at 3 buyers, makes a 50% gross margin at 6 buyers and 62.5% at 8 [I]. Reselling an existing report before it expires is almost pure margin [I].

**Reachable buyer pool (bottom-up).**
- Unit counts disagree. One count gives about 8,500 small units out of about 10,500 plants [S4][S5]. Another gives 6,500 small firms, of which 1,400 (21.53%) filed plans [S3]. The health ministry is quoted as saying about 10,000 [S32]. I use 8,500 as the middle figure.
- Assume half survive into 2027 [A] (Himachal lost 144 of about 400 small units, 36% [S6]; a Gujarat industry body warns 4,000-5,000 are at risk nationally [S7]): about 4,250 units [I].
- Assume each buys about 4 shared reports a year [A] (8-15 critical suppliers, each re-qualified every 2-3 years; test with QA heads). At Rs 20,000 a report, the serviceable market is about Rs 34 crore a year [I].
- First cluster: about 256 small units left in Himachal (400 minus 144) [I] (from [S6]). Gujarat had 684 WHO-GMP certified makers in 2019 [S33]. A year-2 target of 60 paying units buying 4 reports each at Rs 20,000 gives about Rs 48 lakh a year [I].

**Demand evidence level.** L1. Regulation, inspection findings and enforcement show a compulsory task that is going undone [S9][S15][S16]. Buyers abroad already pay for shared audits [S18][S19]. I found no evidence that small Indian plants pay for shared audits today, so this is not strong L1.

**What would make this large.** Becoming the default domestic supplier-qualification database for Schedule M plants; adding certification paid for by suppliers; extending to Ayush, cosmetics and nutraceutical makers; licensing the data to distributors and state regulators [A].

**What would kill it.** Inspectors refuse to treat a shared report as the manufacturer's own supplier audit (not checked). Plants keep passing inspections with questionnaires and certificates of analysis. Suppliers refuse access. Qualifyze or Intertek cut prices for India. A contamination event is traced to a supplier you audited.

**Confidence: medium.** The regulatory and inspection evidence is recent, consistent and from several sources. Willingness to pay at Rs 20,000 per report [A] and regulator acceptance are both untested.

### Thesis 2: Done-for-you estate settlement for heirs living abroad (candidate 4)

**Problem.** When a parent dies in India, heirs must settle bank deposits, lockers, demat accounts, insurance, provident fund and property one institution at a time. Banks have followed divergent practices and often demanded succession certificates or court orders even where nominations existed [S37]. Without a nominee, heirs generally need a succession certificate or probate [S40]. Court fees run 1-3% of asset value in some states, with Maharashtra capped at Rs 75,000 [S42]. A certificate takes 45-90 days by one source and 6-12 months by another [S42][S43]. Heirs abroad also need apostilled documents and a power of attorney [S40]. About Rs 1.84 lakh crore lies unclaimed [S38], which shows how often families give up [I].

**Who pays, who uses, who can block.**
- Payer and user: the heir abroad who acts as executor [A].
- Can block: co-heirs who dispute the split; bank or share-registry staff; lawyers who see the work as theirs; relatives in India who handle it informally.

**Current alternatives and what buyers spend.**
- Do it yourself with relatives in India; lawyers or CAs per task. Their fees were not found after 2 searches (queries: "NRI parent death India bank claim succession certificate transmission shares difficulty agent fees", "Kustodian.life fee model percentage recovered OR Belong NRI inheritance service price OR Assetly NRI succession fee").
- Paid services:
  - FamEase charges fixed fees, never a percentage. One search summary showed an entry tier "from Rs 35,000" and a second summary of the same listing showed no standard prices, so I give that figure low trust [S49].
  - Kustodian.life recovers money stuck in provident fund, insurance and bank accounts [S50].
  - PropResolve offers fixed-fee inheritance handling (press release) [S51].
  - LegacyNext [S55]; Share Samadhan quotes fees by proposal [S52].
- Some CAs have helped families for free [S54].
- Court fee as above [S42].

**Frequency and cost of the problem to the buyer.** Each death triggers one settlement, so the same family rarely buys twice [I] (from [S44]). Cost: court fees up to Rs 75,000 in Maharashtra [S42], flights home (not priced) and months of delay [S43].

**Why now.**
- RBI Directions dated 26 September 2025, to be implemented by 31 March 2026, with a 15-day window and compensation for delay [S36][S37].
- Up to four nominees per account from 1 November 2025 [S53].
- The "Your Money Your Right" drive had returned Rs 5,777 crore by March 2026, with over Rs 73,000 crore still unclaimed [S39].
- SEBI lets demat holdings up to Rs 5 lakh per depository participant be transmitted without a succession certificate [S41].
- Abroad, Empathy raised a USD 72 million Series C in 2025 [S47]. It reaches families through life insurers and employers, and insurers are among its investors [S48]. That shows bereavement administration is a paid category with institutional channels [I].

**Why unsolved.**
- (d) Trust barrier: families must hand over documents and authority at a vulnerable time [A].
- (e) Fragmentation: each institution runs its own process [S37].
- Partly (c): court petitions need an enrolled advocate [A] (my reading of the Advocates Act, to be confirmed with a lawyer).
- New rules are fixing the bank-deposit part [S36], which shrinks the problem [I].

**Competitors, including failed attempts.** FamEase, Kustodian.life, PropResolve and LegacyNext all appear to be recent [S49][S50][S51][S55], so the category is young and filling up [I]. Unclaimed-share firms such as Share Samadhan, InvestorLink and Shares Claim Dost serve part of the need [S52][S63][S64]. Failed attempts: none found after 2 searches (queries: "India startup help families after death paperwork bank insurance transmission service fee", "funeral startup India shut down OR failed OR pivot deathcare startup").

**Barrier for a small new entrant, and the way in.**
- Barriers: trust, the cost of finding each customer, and long case cycles.
- Way in: one diaspora corridor, such as Gulf-based Keralites or US-based Telugu families [A]. Partner with bank NRI desks and with funeral providers, who already get requests from relatives abroad [S114]. Sell fixed-fee packages and use a paralegal in India for field visits.
- Rough economics: a fee of Rs 60,000 (about USD 682) per complex estate [A] (priced above FamEase's reported entry tier [S49]). Founder time of 25 hours at Rs 750 is Rs 18,750 [I], plus Rs 8,000 for a field agent [A], leaving Rs 33,250 before acquisition cost [I]. Acquisition cost is unknown [A] (test with 2 partner channels).

**Reachable buyer pool (bottom-up).** There are 1.71-1.78 crore NRIs [S45][S46]. I assume 40% have a living parent in India, 1.5 NRI siblings per parent pair and 3% annual parental mortality [A]. That gives about 2.8 lakh NRI-linked parent deaths a year [I]. If 30% of these involve assets across several institutions above the simplified thresholds [A], that is about 84,000 complex estates a year [I]. A 0.5% share is 420 cases, about Rs 2.52 crore a year at Rs 60,000 each [I].

**Demand evidence level.** L1. Several firms already charge for this [S49][S50][S51][S52], and the unclaimed total is large [S38]. I found no direct evidence of what heirs abroad will pay.

**What would make this large.** Distribution deals with insurers, employers or banks, as Empathy has in the US [S47]. Moving upstream into nomination clean-up while parents are alive. Property mutation and sale.

**What would kill it.** RBI and nominee reforms make bank claims easy enough to do yourself [S36][S53]. Better-funded rivals. Family disputes and liability. Cases that take 6-12 months and choke cash flow [S43].

**Confidence: low to medium.** The pain is well documented from several sources, but the bank part is being fixed by regulation, rivals appeared in 2025-26, and acquisition cost is unknown.

### Thesis 3: Independent lift uptime and maintenance accountability for housing societies (candidate 8)

**Problem.** Housing societies pay annual maintenance contracts (AMCs) for lifts but cannot see whether contractors keep them safe and running. Residents get trapped, and committees now carry legal risk. In the July 2026 survey, 46% of lift users or family were trapped at least once in a year, 15% of respondents 6-9 times, and 33% had no confidence in their lift's safety [S65].

**Who pays, who uses, who can block.**
- Payer: the society's managing committee (RWA or AOA), usually volunteers [A].
- Users: residents, the facility manager and security staff.
- Can block: the AMC contractor or lift maker, who controls access to the lift controller and may raise warranty objections; the builder before handover; residents who resist higher maintenance charges.

**Current alternatives and what buyers spend.**
- AMC prices:
  - Rs 12,000-18,000 a year for a basic contract on a two-floor home lift [S76].
  - Rs 15,000-40,000 a year for 2-4 person residential lifts [S75]. These come from vendor blogs and probably understate society lifts [A].
  - A 2012 Delhi thread cited third-party AMC near Rs 2,500 per lift per month. That price is stale [S77].
- Who maintains the lift: nationally, 49% by the maker under an AMC, 30% by third-party contractors, 11% by society staff and 10% by calling technicians only when it breaks [S65]. The Bengaluru cut shows 33% maker and 38% third party [S66]. An older LocalCircles release shows 46% and 42% [S67]. The sources disagree. I trust the July 2026 national figure for scale but not for the split.
- Monitoring products: makers' own IoT (KONE runs 24x7 in India) [S83]; DATOMS, priced per connected machine [S81]; the PAPL-Ardelisys KALA non-invasive subscription [S82]; Bosch retrofit sensing [S87]; the startup Rieka [S88]. Prices were not found after 1 search (query: "DATOMS elevator monitoring price per elevator subscription OR KALA lift monitoring subscription price India").

**Frequency and cost of the problem to the buyer.**
- Entrapments are frequent, as above [S65].
- After the Supreme Court ruling, an owner can share liability. In that case the award carried 9% annual interest from the accident date [S68].
- In Uttar Pradesh, an unregistered lift can draw fines up to Rs 10,000 and suspension [S73].

**Why now.**
- Supreme Court judgment of 29 July 2026 [S68][S69].
- UP Act of 2024: rules in July 2024, Rs 5,000 registration per lift, and a copy of the comprehensive AMC to be filed every year [S71][S72]. Compliance lags: 12,600 registrations covering about 16,000 lifts, with only 87 manufacturers and 98 AMC agencies registered [S72]. A May 2026 Amar Ujala headline reports only 1,475 registrations in 18 months in Noida [S74]. I could not open it, and it may conflict with S72.
- 76% of people want mandatory maintenance standards [S86].

**Why unsolved.**
- (d) Distribution and trust: makers and contractors control the controllers and have no reason to expose their own performance [A].
- (e) Fragmented buyers: volunteer committees decide slowly [A].
- Partly (b): sensing must work across many lift brands.
- Monitoring vendors mainly court makers and contractors (DATOMS has a page aimed at elevator companies [S80]), so societies have no independent referee [I].

**Competitors, including failed attempts.** Listed above [S80][S82][S83][S87][S88]. Failed attempts: none found after 2 searches (queries: "elevator IoT remote monitoring retrofit India startup RWA lift uptime sensor", "DATOMS elevator monitoring price per elevator subscription OR KALA lift monitoring subscription price India").

**Barrier for a small new entrant, and the way in.**
- Barriers: hardware cost and installation, liability, pushback from makers, and slow committee sales.
- Way in: white-label a non-invasive sensor kit or buy hardware at about Rs 10,000 per lift [A]. Charge societies a one-time installation fee to protect capital. Sell "AMC accountability": a monthly uptime and entrapment report, an SLA score for the contractor, UP registration paperwork, and help re-tendering the AMC each year. Start with Bangalore Apartments' Federation member societies and Noida high-rises.
- Rough economics: Rs 500 per lift per month, i.e. Rs 6,000 a year [A], is 15-40% of the Rs 15,000-40,000 AMC range [I] (from [S75]). If the founder paid for hardware, Rs 5,00,000 would fund only about 50 devices [I], so the installation fee is essential.

**Reachable buyer pool (bottom-up).**
- The Bangalore Apartments' Federation has 1,400+ member associations [S84]. At an assumed 6 lifts each [A], that is about 8,400 lifts [I].
- UP registrations cover about 16,000 lifts [S72].
- Together the two clusters hold about 24,400 lifts [I]. A 3% share is about 732 lifts, or about Rs 44 lakh a year at Rs 6,000 per lift [I].
- National installed base: about 6 lakh units in 2025 by one estimate and over 7 lakh in 2022 by another [S78][S79]. These disagree, so I do not rely on them.

**Demand evidence level.** L1. Survey, court and regulatory evidence show the pain [S65][S68][S70]. Today's spending goes on AMCs, not monitoring, and I found no evidence that societies pay for independent monitoring.

**What would make this large.** Becoming the standard tool societies use for lift compliance across states; tie-ups with insurers (the UP Act has an insurance section [S70]); adding other equipment the same committee buys, such as DG sets and fire and water pumps [A].

**What would kill it.** Societies will not pay. Makers bundle free monitoring. Contractors refuse devices on their lifts. A missed fault draws you into liability. DATOMS or KALA start selling directly to societies.

**Confidence: low to medium.** The pain and the reason it is open now are strong and recent. Willingness to pay, hardware economics and maker resistance are untested.

### Ranking for the Director

1. Thesis 1 (pharma shared audits): clearest compulsory spend, a cost structure incumbents priced for Western buyers cannot easily match, and low capital.
2. Thesis 3 (lift accountability): strong "why now" and recurring revenue, but payer budgets and hardware capital are unproven.
3. Thesis 2 (estate settlement): real pain, but rivals are arriving and regulation is shrinking part of it.

## 4. Cut candidates and reasons

| # | Candidate | Why cut | Tag |
|---|---|---|---|
| 2 | Validation services for small plants | Commodity pricing (Rs 3,000-3,500 a day on IndiaMART), and the instruments needed (particle counters, aerosol photometers) would likely exceed Rs 5,00,000 | [S28][A] |
| 3 | Quality system or quality software for small plants | Generic consulting: crowded with freelancers and low-priced software (from USD 79 per user), and plants are spending their cash on Rs 50 lakh to 2.5 crore upgrades | [S29][S31][S2] |
| 5 | City funeral management | Crowded (Last Journey, Swargayatraa, Mokshshil, Anthyesti), low tickets (Rs 12,000-50,000 packages), and operations-heavy in each city | [S56][S57][S59][S60] |
| 6 | Gulf body repatriation | Small (about 6,000-7,000 cases a year); employers or insurers must pay; consulates and volunteers already help | [S61][S62] |
| 7 | Recovering unclaimed shares from the investor protection fund | Crowded with recovery firms, and the government is pushing free self-service portals | [S63][S64][S38] |
| 9 | Pre-owned luxury watch checks and independent servicing | Swiss brands may lawfully refuse parts to independents; Ethos's pre-owned arm Second Movement draws on Ethos's service network; needs a skilled watchmaker; independents such as POGU (base price Rs 20,000 in a 2023 report, now stale) already exist | [S92][S91][S93] |
| 10 | Luxury leather restoration | The Restory (UK) went into proposed liquidation in 2023 after raising USD 8 million, with unit economics cited; Indian demand not found after 1 search ("luxury handbag repair restoration India Louis Vuitton boutique repair sent to Europe months customers") | [S95][S96] |
| 11 | Set-up, warrantied classical instruments for students abroad | Tiny market: Indian exports of string instruments put at Rs 33.7-75 crore by two disagreeing sources; curated sellers already exist; buyers rarely repurchase | [S106][S107][S105] |
| 12 | Arangetram production packages | Vendors already ship worldwide with video fittings and book orchestras; no count of arangetrams per year found after 1 search ("number of arangetrams per year United States Bharatanatyam students diaspora dance schools count"); visa and event risk | [S103][S104][S115] |

The visa point in row 12 rests on a US P-3 petition filing fee of USD 460 [S115].

## 5. Sources

All entries were seen only through search-result summaries. Retrieved 2026-10-31 for all. "n.s." means the publication date was not shown.

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Schedule M extension for MSME pharma firms unlikely | Business Standard | https://www.business-standard.com/industry/news/schedule-m-extension-for-msme-pharma-firms-unlikely-125122901058_1.html | 2025-12-29 | 2026-10-31 | No extension; binding from 2026 | search summary |
| 2 | Just 1 in 4 MSME pharma units set for GMP transition | Vision IAS (summary of Business Standard) | https://visionias.in/current-affairs/upsc-daily-news-summary/article/2025-12-26/business-standard/science-and-technology/just-1-in-4-msme-pharma-units-set-for-gmp-transition-as-deadline-nears | 2025-12-26 | 2026-10-31 | 1 in 4 ready; upgrade cost | search summary |
| 3 | Over 60% of pharma MSMEs yet to comply | inkl | https://www.inkl.com/news/over-60-of-pharma-msmes-yet-to-comply-with-updated-manufacturing-norms | n.s. (2025) | 2026-10-31 | 6,500 firms, 1,400 plans | search summary |
| 4 | Over 60% of small pharma units may face closure | Outlook Business | https://www.outlookbusiness.com/corporate/over-60-per-cent-of-small-pharma-units-may-face-closure-over-new-compliance-norms | n.s. (2025) | 2026-10-31 | 8,500 of 10,500 units | search summary |
| 5 | Only 2k out of 10,500 pharma firms comply with WHO-GMP | Nagpur Today | https://www.nagpurtoday.in/only-2k-out-of-10500-pharma-firms-comply-with-who-gmp-standards-in-india-3-from-nagpur/08071649 | 2023-08-07 | 2026-10-31 | Unit count | search summary |
| 6 | Unable to upgrade, 144 pharma units in state close operations | Tribune India | https://www.tribuneindia.com/news/himachal/unable-to-upgrade-144-pharma-units-in-state-close-operations-640531 | n.s. (likely 2025) | 2026-10-31 | Himachal closures | search summary |
| 7 | DMMA warns regulatory burden threatening Gujarat's pharma MSMEs | BioSpectrum India | https://www.biospectrumindia.com/news/16/26724/dmma-warns-regulatory-burden-threatening-gujarats-pharma-msmes.html | n.s. (2025-26) | 2026-10-31 | 4,000-5,000 at risk | search summary |
| 8 | Schedule M shock in Himachal: only 11% units fully compliant | Medical Dialogues | https://medicaldialogues.in/amp/news/industry/pharma/schedule-m-shock-in-himachal-only-11-pharma-units-fully-gmp-compliant-162892 | 2026-01 | 2026-10-31 | Himachal compliance, notices | search summary |
| 9 | Key notes on revised Schedule M: materials (Haryana drugs controller compilation) | The Health Master | https://thehealthmaster.com/?p=64418 | 2025-03-15 | 2026-10-31 | Supplier approval and audit rules | search summary |
| 10 | CDSCO asks states to mandate raw material and finished formulation testing | Business Standard | https://www.business-standard.com/s/2gA9FwC | 2026-10-28 | 2026-10-31 | Excipient testing directive | search summary |
| 11 | DEG/EG position paper | IPEC Europe | https://www.ipec-europe.org/uploads/publications/20260427-deg-eg-pp-final-1777975682.pdf | 2026-04-27 | 2026-10-31 | IP amendment on DEG/EG tests | search summary |
| 12 | Indian officials probe whether safety lapses led to children dying from cough syrup (Reuters) | CP24 | https://www.cp24.com/news/world/2025/11/21/indian-officials-probe-whether-safety-lapses-led-to-children-dying-from-cough-syrup/ | 2025-11-21 | 2026-10-31 | Coldrif supply chain | search summary |
| 13 | Inspection finds 364 violations at Kanchipuram Coldrif facility | The South First | https://thesouthfirst.com/health/leaking-equipment-and-non-pharma-materials-inspection-finds-364-violations-at-kanchipuram-coldrif-facility | 2025-10 | 2026-10-31 | Non-compliance counts | search summary |
| 14 | Another arrest in spurious pharma raw material case | Tribune India | https://www.tribuneindia.com/news/himachal/another-arrest-in-spurious-pharma-raw-material-case-508756/amp | n.s. (2023) | 2026-10-31 | Relabelled excipients in Baddi | search summary |
| 15 | India finds multiple deficiencies among drugmakers following inspections | Medical Dialogues | https://medicaldialogues.in/news/industry/pharma/india-finds-multiple-deficiencies-among-drugmakers-following-inspections-across-industry-115319 | 2023 | 2026-10-31 | Vendor qualification a common finding | search summary |
| 16 | Strict compliance with Drugs Rules for testing of raw materials | CliniExperts | https://cliniexperts.com/regulatory-update/strict-compliance-with-the-drugs-rules-1945-for-testing-of-raw-materials-and-finished-formulations/ | 2026 (circular 2026-08-05) | 2026-10-31 | Robust vendor qualification circular | search summary |
| 17 | India to mandate annual audit of pharma suppliers by drugmakers | Medical Dialogues | https://medicaldialogues.in/news/industry/pharma/india-to-mandate-annual-audit-of-pharma-suppliers-by-drugmakers-117723 | 2023-09 | 2026-10-31 | Annual audit proposal | search summary |
| 18 | Rx-360 goes live with joint audit programme | SecuringIndustry | https://securingindustry.com/pharmaceuticals/rx-360-goes-live-with-joint-audit-programme/s40/a1211 | n.s. (old; stale) | 2026-10-31 | Standalone and shared audit cost | search summary |
| 19 | Qualifyze raises EUR 11 million | EU-Startups | https://www.eu-startups.com/2023/08/frankfurt-based-qualifyze-raises-e11-million-to-transform-supply-chain-compliance-in-pharma/ | 2023-08 | 2026-10-31 | Funding, revenue scale | search summary |
| 20 | Qualifyze shared audits | CHEManager | https://chemanager-online.com/en/node/427268 | n.s. | 2026-10-31 | Shared audits, India coverage | search summary |
| 21 | Mastering pharma audits | Pharmaoffer | https://pharmaoffer.com/blog/mastering-pharma-audits-everything-you-need-to-know/ | n.s. | 2026-10-31 | USD 24,000 per audit; 2 days in India | search summary |
| 22 | Diapharm now provides over 500 GMP audit reports | Diapharm | https://diapharm.com/en/news/diapharm-now-provides-over-500-gmp-audit-reports | n.s. | 2026-10-31 | Audit volume per supplier | search summary |
| 23 | Supplier qualification | PharmTech | https://www.pharmtech.com/view/supplier-qualification | n.s. | 2026-10-31 | Excipient makers' audit load | search summary |
| 24 | The power of GxP shared audits | Eurofins | https://www.eurofins.com/assurance/resources/articles/the-power-of-gxp-shared-audits-in-the-pharmaceutical-industry/ | n.s. | 2026-10-31 | 5-10 buyers per shared audit | search summary |
| 25 | Shared audits | Intertek | https://www.intertek.com/pharmaceutical/auditing/shared-audits/ | n.s. | 2026-10-31 | Shared audits expanded to India | search summary |
| 26 | Brenntag partners with Qualifyze | Indian Pharma Post | https://www.indianpharmapost.com/news/lite/brenntag-partners-with-qualifyze-to-enhance-pharma-audit-offering-14504 | 2023 | 2026-10-31 | Distributor partnership | search summary |
| 27 | Pharmexcel services | IndiaMART | https://m.indiamart.com/pharmexcel/services.html | n.s. | 2026-10-31 | GMP lead auditor monthly rate | search summary |
| 28 | Cleanroom validation solution | IndiaMART | https://m.indiamart.com/cleanroom-validation-solution | n.s. | 2026-10-31 | Validation day rates | search summary |
| 29 | Pharma QA writer profile | Kolabtree | https://www.kolabtree.com/find-an-expert/manisha-l.99480 | n.s. | 2026-10-31 | Freelance hourly rate | search summary |
| 30 | Senior Officer QA salary, Baddi | AmbitionBox | https://ambitionbox.com/profile/senior-officer-qa-salary/baddi-location | 2025 | 2026-10-31 | QA salaries | search summary |
| 31 | QEdge | Capterra India | https://www.capterra.in/software/134220/qedge | n.s. | 2026-10-31 | Quality software price | search summary |
| 32 | RPTUAS gets Rs 105 crore to support MSMEs | KNN India | https://knnindia.co.in/news/newsdetails/msme/pharmaceutical-tech-upgradation-scheme-rptuas-gets-rs-105-crore-to-support-msmes | 2025-03 | 2026-10-31 | Subsidy scheme; ministry unit count | search summary |
| 33 | CDSCO releases updated list of 2006 WHO GMP certified drug manufacturers | Medical Dialogues Business | https://business.medicaldialogues.in/cdsco-releases-updated-list-of-2006-who-gmp-certified-drug-manufacturers-details | 2019 | 2026-10-31 | Gujarat count | search summary |
| 34 | DCGI inspections trigger closure of 36% pharma plants | PharmaNow | https://www.pharmanow.live/latest-news/cdsco-enhances-drug-quality-in-pharma | 2024 | 2026-10-31 | Enforcement outcome | search summary |
| 35 | Mendel Genetics | Mendel Genetics | https://sites.google.com/view/mendelgenetics/home | n.s. | 2026-10-31 | Audits of Indian suppliers for export buyers | search summary |
| 36 | RBI notifies new rules for settlement of deceased customers' accounts | Moneylife | https://moneylife.in/article/rbi-notifies-new-rules-for-settlement-of-deceased-customers-accounts-banks-to-face-penalties-for-delays/78430.html | 2025 | 2026-10-31 | RBI Directions 2025 | search summary |
| 37 | RBI issues directions on settlement of deceased claims | IndiaLaw | https://www.indialaw.in/blog/banking-and-finance/rbi-issues-directions-on-settlement-of-deceased-claims/ | 2025 | 2026-10-31 | Divergent bank practice; dates | search summary |
| 38 | FM launches Your Money Your Right drive | Free Press Journal | https://www.freepressjournal.in/amp/business/fm-nirmala-sitharaman-launches-your-money-your-right-drive-184-lakh-crore-unclaimed-funds-to-be-returned-via-portal | 2025-10 | 2026-10-31 | Rs 1.84 lakh crore unclaimed | search summary |
| 39 | Rs 5,777 crore returned under Your Money Your Right | Angel One | https://www.angelone.in/news/market-updates/5-777-crore-returned-under-your-money-your-right-campaign-unclaimed-funds-still-cross-73-000-crore | 2026-03 | 2026-10-31 | Recovery progress | search summary |
| 40 | Documents NRIs need to claim inherited assets in India | Belong | https://getbelong.com/blog/documents-nris-need-to-claim-inherited-assets-in-india/ | n.s. | 2026-10-31 | Claim process for heirs abroad | search summary |
| 41 | Transferring inherited Indian shares to an NRI, 2026 guide | NRI Information | https://nriinformation.com/nri-info/transfer-inherited-shares | 2026 | 2026-10-31 | SEBI Rs 5 lakh threshold | search summary |
| 42 | Succession certificate court fees in India | Lawtendo | https://lawtendo.com/blogs/succession-certificate-court-fees-india | 2024-11-28 | 2026-10-31 | Court fees; timing | search summary |
| 43 | Apply for succession certificate 2026 | RTI Wiki | https://righttoinformation.wiki/apply-succession-certificate-2026 | 2026 | 2026-10-31 | 6-12 months timing | search summary |
| 44 | CRS report shows rise in mortality figures in 2023 | The Statesman | https://www.thestatesman.com/india/crs-report-shows-decline-in-birth-registrations-and-rise-in-mortality-figures-in-2023-1503499921.html | 2025 | 2026-10-31 | Deaths registered | search summary |
| 45 | Population of overseas Indians | Ministry of External Affairs | https://www.mea.gov.in/population-of-overseas-indians | n.s. | 2026-10-31 | NRI count (1.78 crore) | search summary |
| 46 | Over 3.5 crore overseas Indians | Kashmir Life | https://kashmirlife.net/indias-global-family-over-3-5-crore-overseas-indians-canada-tops-the-list-402379/ | 2025 | 2026-10-31 | NRI count (1.71 crore) | search summary |
| 47 | Empathy lands USD 72m | Infor Capital | https://inforcapital.com/news/empathy-lands-72m-to-enhance-grief-and-legacy-solutions/ | 2025-05 | 2026-10-31 | US analogue funding | search summary |
| 48 | Empathy announces USD 47M Series B | II Reporter | https://iireporter.com/empathy-announces-47m-series-b-funding-round-led-by-index-ventures/ | 2024 | 2026-10-31 | Insurer investors and channel | search summary |
| 49 | FamEase Android listing | Chrome-Stats | https://chrome-stats.com/d/com.famease.main | n.s. (2026) | 2026-10-31 | Fixed-fee rival | search summary |
| 50 | Kustodian.life helps families unlock money stuck in EPF, insurance | YourStory | https://yourstory.com/2025/09/kustodianlife-unlock-money-stuck-in-insurance-epf-insurance | 2025-09 | 2026-10-31 | Rival | search summary |
| 51 | PropResolve launches fixed-fee solution for property inheritance | OneIndia (partner content) | https://www.oneindia.com/partner-content/propresolve-launches-fixed-fee-solution-indian-property-inheritance-legal-matters-012-8092393.html | 2026-05 | 2026-10-31 | Rival | search summary |
| 52 | NRI Samadhan services | Share Samadhan | https://sharesamadhan.com/nri-samadhan-services | n.s. | 2026-10-31 | Rival | search summary |
| 53 | Banking Laws Amendment allows up to four nominees from 1 Nov 2025 | Taxmann | https://www.taxmann.com/post/blog/banking-laws-amendment-allows-up-to-four-nominees/ | 2025 | 2026-10-31 | Nominee reform | search summary |
| 54 | CA helps for free with financial documents after a death | The Better India | https://thebetterindia.com/259324/how-to-take-care-of-financial-documents-after-a-loved-ones-death-ca-helps-for-free | 2021 | 2026-10-31 | Free alternative | search summary |
| 55 | LegacyNext | Dealroom | https://datacommons.dealroom.co/companies/legacynext | n.s. | 2026-10-31 | Rival | search summary |
| 56 | What is the cost of cremation in Delhi | Last Journey | https://www.lastjourney.in/blog/what-is-the-cost-of-cremation-in-delhi | n.s. | 2026-10-31 | Funeral package prices | search summary |
| 57 | Funeral services Bengaluru | Swargayatraa | https://swargayatraa.com/?p=16800 | 2026 | 2026-10-31 | Funeral package prices | search summary |
| 58 | Families charged up to Rs 5,000 for cremation service in Bengaluru | The News Minute | https://www.thenewsminute.com/karnataka/families-charged-up-to-rs-5000-for-cremation-service-bengaluru-police-begin-probe | n.s. (2025-26) | 2026-10-31 | Overcharging | search summary |
| 59 | The rise of private entities in India's funeral services | Entrepreneur India | https://india.entrepreneur.com/news-and-trends/the-rise-of-private-entities-in-indias-funeral-services/445838 | 2023-02 | 2026-10-31 | Funeral rivals | search summary |
| 60 | Swargadwara funeral services | YourStory | https://yourstory.com/2019/05/startup-bharat-odisha-swargadwara-funeral-services | 2019-05 | 2026-10-31 | Funeral rivals | search summary |
| 61 | Mortal remains of 54,511 Indians brought back 2016-2025 | Morung Express | https://morungexpress.com/mortal-remains-of-54511-indian-nationals-brought-back-between-2016-2025-eam-jaishankar | 2025-12 | 2026-10-31 | Repatriation volumes | search summary |
| 62 | Indian consulate in Dubai: employers must bear repatriation costs | Gulf Today | https://www.gulftoday.ae/news/2025/08/21/indian-consulate-in-dubai-warns-against-fraud-confirms-employers-must-bear-repatriation-costs | 2025-08-21 | 2026-10-31 | Repatriation costs and payer | search summary |
| 63 | InvestorLink unclaimed shares recovery | The Quint (brand studio) | https://www.thequint.com/brandstudio/investorlink-unclaimed-shares-recovery-iepf-india | n.s. | 2026-10-31 | IEPF scale; rival | search summary |
| 64 | Shares Claim Dost simplifies IEPF claims | Tribune India | https://www.tribuneindia.com/news/business/shares-claim-dost-simplifies-iepf-claim-refund-and-share-recovery-process-for-investors/ | n.s. | 2026-10-31 | Rival | search summary |
| 65 | Survey: 46% residents trapped in a lift at least once last year | Business Today | https://www.businesstoday.in/india/story/got-a-lift-in-your-apartment-survey-says-46-residents-were-trapped-at-least-once-last-year-546526-2026-07-31 | 2026-07-31 | 2026-10-31 | Lift survey | search summary |
| 66 | Four in 10 Bengalureans dread stepping into a lift | Deccan Herald | https://deccanherald.com/india/karnataka/bengaluru/four-in-10-bengalureans-dread-stepping-into-a-lift-survey-4098155 | 2026-08 | 2026-10-31 | Bengaluru split | search summary |
| 67 | Lift problems survey | LocalCircles | https://m-www.localcircles.com/a/press/page/lift-problems-survey | n.s. (older) | 2026-10-31 | Older maintenance split | search summary |
| 68 | Elevator makers can be held primarily liable for passenger death | CourtBook | https://courtbook.in/posts/elevator-manufacturers-can-be-held-primarily-liable-for-passenger-death-in-lift-accident-supreme-court-rules | 2026-07 | 2026-10-31 | Supreme Court ruling | search summary |
| 69 | Supreme Court landmark order on lift safety | News24 | https://news24online.com/india/supreme-court-landmark-order-on-lift-safety-operators-builders-and-makers-are-all-liable-now-for-passenger-accidents/895110/ | 2026-07 | 2026-10-31 | Joint liability | search summary |
| 70 | Uttar Pradesh Lifts and Escalators Act, 2024 | India Code | https://www.indiacode.nic.in/bitstream/123456789/19956/1/act_lift_eng.pdf | 2024 | 2026-10-31 | Act sections incl. insurance | search summary |
| 71 | Uttar Pradesh Lifts and Escalators Act, 2024 | TeamLease RegTech | https://www.teamleaseregtech.com/updates/article/32469/uttar-pradesh-lifts-and-escalators-act-2024 | 2024-02 | 2026-10-31 | Act date; AMC rule | search summary |
| 72 | Lift and Escalator Act: Noida dominates registration drive | The Realty Today | https://therealtytoday.com/news/trending/lift-and-escalator-act-2024-noida-dominates-registration-drive-across-uttar-pradesh | 2025 | 2026-10-31 | Registrations, fee, rules | search summary |
| 73 | Noida DM makes lift registration mandatory within 6 months | Homzcare | https://homzcare.in/?p=19055 | 2024 | 2026-10-31 | Fines and suspension | search summary |
| 74 | Lift Act: only 1,475 registrations in one and a half years | Amar Ujala | https://www.amarujala.com/delhi-ncr/noida/lift-act-only-1475-registration-in-one-and-a-half-years-noida-news-c-23-1-lko1064-94589-2026-05-12 | 2026-05-12 | 2026-10-31 | Compliance gap (headline only) | search summary |
| 75 | Lift price by capacity | Nibav Lifts | https://www.nibavlifts.com/blog/lift-price-by-capacity | n.s. | 2026-10-31 | AMC price range | search summary |
| 76 | Home elevator AMC guide | Home Elevator Chennai | https://www.homeelevatorchennai.com/blog/home-elevator-amc-guide/ | n.s. | 2026-10-31 | Basic AMC price | search summary |
| 77 | Info request: OTIS lift AMC | Dwarka residents Google Group | https://groups.google.com/g/dwarka-residents/c/EIce9AlzmhQ | 2012 | 2026-10-31 | Old third-party AMC price (stale) | search summary |
| 78 | Inside the India elevator and escalator market reset | Next Move Strategy Consulting | https://www.nextmsc.com/blogs/inside-the-india-elevator-and-escalator-market-reset | 2025 | 2026-10-31 | Installed base estimate | search summary |
| 79 | The Indian elevator market flyer | MCG | https://consultmcg.com/blog/comments/feed/The-Indian-Elevator-Market-Flyer-MCG-Sep2022.pdf | 2022-09 | 2026-10-31 | Installed base estimate | search summary |
| 80 | Connected IoT elevators | DATOMS | https://datoms.io/elevator-escalator-monitoring/ | n.s. | 2026-10-31 | Rival | search summary |
| 81 | DATOMS profile | Software Advice | https://www.softwareadvice.com/iot/datoms-profile/ | n.s. | 2026-10-31 | Pricing model | search summary |
| 82 | PAPL, Ardelisys launch IoT-based elevator monitoring | Elevator World | https://elevatorworld.com/news/daily-news/papl-ardelisys-launch-iot-based-elevator-monitoring-system-at-slm-world-in-india | n.s. | 2026-10-31 | Rival | search summary |
| 83 | KONE cruises ahead with 24x7 IoT platform in India | NBM&CW | https://www.nbmcw.com/news/kone-cruises-ahead-with-24x7-iot-platform-in-india.html | n.s. | 2026-10-31 | Maker IoT | search summary |
| 84 | Bangalore Apartments' Federation | Citizen Matters | https://citizenmatters.in/section/bangalore-apartments-federation/ | 2025-12 | 2026-10-31 | 1,400+ member associations | search summary |
| 86 | 76% want mandatory standards for lift maintenance | Sentinel Assam | https://www.sentinelassam.com/amp/story/topheadlines/76percent-of-people-want-mandatory-standards-for-lift-maintenance-report-661414 | n.s. (2026) | 2026-10-31 | Public demand for standards | search summary |
| 87 | Robert Bosch Engineering retrofit monitoring | CIO Tech Outlook | https://hp.ciotechoutlook.com/news/robert-bosch-engineering-and-business-solutions-pvt-ltd-nid-5085-cid-64.html | n.s. | 2026-10-31 | Rival | search summary |
| 88 | Rieka Elevator startup listing | Startup in UP portal | https://www.startinup.up.gov.in/crm/Welcome/startup_user_details/MTI3MDE= | n.s. | 2026-10-31 | Rival | search summary |
| 89 | India becomes fastest growing market for Swiss watch exports | Luxury Tribune | https://www.luxurytribune.com/en/india-becomes-fastest-growing-market-for-swiss-watch-exports | 2025 | 2026-10-31 | Swiss exports to India | search summary |
| 90 | TEPA overview | PwC Switzerland | https://www.pwc.ch/en/insights/custom-ised/tepa-free-trade-agreement-india.html | 2025 | 2026-10-31 | Duty phase-out | search summary |
| 91 | Luxury watch brands in India | Second Movement | https://smless.secondmovement.com/the-journal/luxury-watch-brands-india | n.s. | 2026-10-31 | Pre-owned market size; Ethos link | search summary |
| 92 | Swiss watchmakers permitted to refuse to supply independent repairers | CMS Law | https://cms.law/en/deu/legal-updates/swiss-watchmakers-permitted-to-refuse-to-supply-independent-watch-repairers | 2017 | 2026-10-31 | Parts restrictions | search summary |
| 93 | POGU watch service center in Mumbai | The Hour Markers | https://thehourmarkers.com/articles/pogu-watch-service-center-in-mumbai | 2023 | 2026-10-31 | Independent service price (stale) | search summary |
| 94 | Half of fake watches are Rolex replicas | Mint via Magzter | https://magzter.com/ja/stories/newspaper/Mint-Mumbai/HALF-OF-FAKE-WATCHES-ARE-ROLEX-REPLICAS | n.s. | 2026-10-31 | Fakes | search summary |
| 95 | The Restory put into proposed liquidation | FashionUnited | https://fashionunited.uk/news/business/the-restory-put-into-proposed-liquidation-after-co-founders-exit/2023022868150 | 2023-02-28 | 2026-10-31 | Failed rival | search summary |
| 96 | Unraveling The Restory, and what's next for repair | Yahoo (WWD) | https://sg.style.yahoo.com/unraveling-restory-next-repair-200231950.html | 2023 | 2026-10-31 | Failure causes; USD 8m raised | search summary |
| 97 | Louis Vuitton repair policy | The Vintage Bar | https://it.thevintagebar.com/the-archive/louis-vuitton-repair-policy | n.s. | 2026-10-31 | Repair route and time | search summary |
| 99 | r/Sitar purchasing wiki (mirror) | Reddit | https://reddit.birdcat.cafe/r/Sitar/wiki/purchasing | n.s. | 2026-10-31 | Buyer complaints | search summary |
| 100 | r/Sitar cheap sitars thread (pro luthier moderator, mirror) | Reddit | https://reddit.birdcat.cafe/r/Sitar/comments/6d222b/cheap_sitars | 2017-05-24 | 2026-10-31 | Buyer complaints | search summary |
| 102 | Arangetram cost feature | Saratoga Falcon | https://saratogafalcon.org/?p=10479 | n.s. | 2026-10-31 | Arangetram budget | search summary |
| 103 | Arangetram costume packages shipped to USA | Shanthi Tailors | https://shanthitailor.com/pages/arangetram-costumes-usa | n.s. | 2026-10-31 | Existing vendor | search summary |
| 104 | Arangetram orchestra FAQs | Dance Costumes and Jewelry | https://www.dancecostumesandjewelry.com/pages.php?pageid=85 | n.s. | 2026-10-31 | Existing vendor | search summary |
| 105 | Bhava classic kirtan harmonium listing | Desertcart | https://www.desertcart.pl/products/384887465-bhava-classic-kirtan-harmonium-standard-edition-professionally-tuned-shipped-from | n.s. | 2026-10-31 | Premium price point | search summary |
| 106 | HSN chapter 92 | Busy.in | https://busy.in/hsn/chapter-92.md | FY2024-25 | 2026-10-31 | Instrument exports | search summary |
| 107 | Musical instruments trade dataset | Dataful | https://dataful.in/datasets/1741 | 2024 | 2026-10-31 | Instrument exports | search summary |
| 110 | DCGI orders inspections of pharma units (PTI) | The Week | https://www.theweek.in/wire-updates/national/2025/11/10/des91-health-dcgi-inspection.html | 2025-11-10 | 2026-10-31 | Strict action instruction | search summary |
| 111 | Pharma companies step up corrective action plans after crackdown | Business Standard | https://www.business-standard.com/industry/news/pharma-companies-step-up-corrective-action-plans-after-crackdown-by-govt-124022800928_1.html | 2024-02-28 | 2026-10-31 | Over 200 regulatory actions | search summary |
| 112 | Audit library | Pharmaoffer | https://pharmaoffer.com/audit-reports | n.s. | 2026-10-31 | Rival | search summary |
| 113 | Get audited by Qualifyze | Qualifyze | https://www.qualifyze.com/auditee/ | n.s. | 2026-10-31 | Auditee programme | search summary |
| 114 | Funeral services step in for final rites as curbs keep families away | Hindustan Times via PressReader | https://www.pressreader.com/india/hindustan-times-delhi/20210427/281651077956302 | 2021-04-27 | 2026-10-31 | Requests from relatives abroad | search summary |
| 115 | P-3 culturally unique artist visa | SimpleCitizen | https://start.simplecitizen.com/visa-index/p-3-visa/ | n.s. | 2026-10-31 | P-3 filing fee | search summary |
