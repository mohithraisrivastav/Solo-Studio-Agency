# Expert assessment 6: Feasibility of the lift concepts (Leads 1-3 and the wildcard)

Run: 2026-10-31 acceptance test. Role: Multidisciplinary Expert. Inputs: `05-invent-3-lifts.md` (Inventor; claims treated as unverified) and `03-market-5-lifts.md` (Market Investigator; background). No other run files read.

Constraints: founder capital Rs 5,00,000; founder time Rs 750 per hour; India first [A] (user-set constraints, not facts).

## Method and limits

- 37 web searches. WebFetch is blocked, so I opened no page. Every source is marked "search summary". Several summaries merged results; where I could not tie a statement to one page I say "attribution uncertain".
- I set 14 deciding questions first (table below) and spent searches on them in order of how much they decide.
- Sources the Inventor or Investigator found and I rely on without re-searching are marked "not re-checked by me" in the Sources table.
- Currency INR. GST on services assumed 18% [A] (standard rate; confirm with a CA).
- This is not legal advice. Every legal reading below is a desk reading of secondary summaries. A lawyer must confirm the points listed in each section 11.
- Not checked: the full text of any Act, Rule, regulation or judgment; Maharashtra rules under section 37 of the 2017 Act (not found); Karnataka and Haryana fee schedules; current insurer rates (the only rate found is an old tariff); MTCTE test cost; any Indian patent register entry; KALA's sensing method; joint-purchasing treatment under the Competition Act (background knowledge only); any buyer, contractor, insurer or broker view (no contact made).

## Deciding questions

| # | Question | Concepts | Answer found | Tag |
|---|---|---|---|---|
| Q1 | Who may maintain lifts in Maharashtra, Karnataka and UP? | 1, 2, W | Only licensed or registered contractors; in UP a comprehensive AMC must come from the maker or (apparently) its authorised provider | [S3][S7][S10][S11] |
| Q2 | Who may inspect or test lifts, and can a private firm be a statutory inspector? | 2 | State inspectorates; Maharashtra's third-party scheme is announced, not notified; "testing" is a licensed activity in Maharashtra | [S3][S6][S7] |
| Q3 | Is the Maharashtra Act really in force from 1 Nov 2026? | 1, 2 | Yes, notified 22 Oct 2026; rules not seen | [S1][S2] |
| Q4 | Are automatic AMC penalties enforceable? | 1, W | Only as "reasonable compensation" under section 74; courts split on proof of loss | [S18][S19][S20] |
| Q5 | Are penalty credits taxed under GST? | 1, W | Generally not, if purely compensatory (Circular 178/10/2022) | [S21] |
| Q6 | Can a small firm earn insurance money legally? | 2 | Not commission or referral fees (section 40); IMF or corporate agent licences need more net worth than the capital; broker-paid risk work is a narrow route | [S13][S15][S16][S57] |
| Q7 | What does lift liability cover cost, and what limits exist? | 2 | Old tariff: Rs 3 per mille of annual limit plus 10% lift loading; limit ratio cap 1:4 | [S43] |
| Q8 | Will makers starve independents of parts and tools? | 1, 2 | Proven abroad (Italy, Singapore); no Indian lift case found; Indian signs of obsolescence pressure | [S22][S23][S25][S26] |
| Q9 | Can a sensor sit on the lift's feeder in the society's panel, and who may fit it? | 3 | Lift supply must be on separate circuits from the main switch room; work needs a licensed electrical contractor | [S27][S28] |
| Q10 | What device approvals apply to a cellular logger? | 3 | Cellular IoT devices are on the TEC (MTCTE) list | [S30] |
| Q11 | Does a patent block the society-side recorder? | 3 | US11603286 is Inventio AG's; no Indian counterpart found | [S32][S33] |
| Q12 | Who carries liability after an accident? | all | Maker, operator and owner jointly and severally; lifts are common carriers | [S36][S37] |
| Q13 | Are fast, paid rescues safe? | W | Only trained lift staff should release passengers; the leading case death happened during a manual brake release | [S38][S40][S41] |
| Q14 | Do Maharashtra society rules let a committee sign a pooled AMC alone? | 1 | Above a membership-based limit, tenders go to the general body first | [S45] |

## Shared baseline: state lift law, licences and liability

**Maharashtra.**
- The Maharashtra Lifts, Escalators and Moving Walks Act, 2017 comes into force on 1 November 2026, by a notification of 22 October 2026, replacing the 1939 Act [S1][S2].
- An "approved contractor" holds a licence for erection, maintenance or testing issued by the Chief Electrical Inspector [S3]. Section 18 requires every owner to contract with an approved contractor for maintenance [S3].
- Section 23 requires the owner to "ensure third-party insurance" for passengers [S3][S4].
- Secondary summaries say the Act needs yearly periodic inspection, accident reporting and logbooks; section numbers not confirmed [S2].
- Rules under section 37 were not found. A 2026 amending bill changing sections 29, 35 and 37 passed both houses in March 2026; its contents and commencement were not found [S5].
- A state third-party inspection system was announced in March 2026; no notification or accreditation criteria found after 2 searches [S6].
- One procedure page says a lift maintenance licence needs an engineering degree or diploma and an existing electrical contractor licence; tender notices ask for both licences [S54]. Secondary source; verify with the Chief Electrical Inspector.

**Karnataka.** The Karnataka Lifts, Escalators and Passenger Conveyors Act, 2012 (Act 9 of 2013) bars anyone from running a business of erection, installation, periodic testing or maintenance without registration (section 6) [S7]. The owner needs a licence to use a lift, and electricity may not be supplied without it (section 4) [S7]. A 2025 amendment bill would replace "Chief Inspector" with "authorised officer"; enactment not confirmed [S8]. One government AMC tender required registration under the Act and qualified engineers [S9].

**Uttar Pradesh.** The owner must hold a comprehensive AMC from the maker or an authorised service provider [S10]. The official English text's AMC definition is garbled but reads "...his authorized service provider" [S11]. I read "his" as the maker's authorised provider [I] (one OCR fragment; confidence low until the Gazette text is read). AMC agencies register with the Director of Electrical Safety; one count found 87 makers and 98 AMC agencies registered [S12].

**Haryana.** Registration and renewal need a current AMC and insurance [S56].

**Who may inspect.** Statutory inspection sits with state inspectorates (Chief Electrical Inspector in Maharashtra [S3][S71]; Chief Inspector in Karnataka [S7]). A private firm can sell an advisory "risk inspection", but it cannot issue a statutory certificate [I] (from the authority provisions above). In Maharashtra, "testing" is a licensed activity [S3], so a private inspector should observe tests done by the licensed contractor and not perform brake, governor or safety-gear tests itself unless licensed [I]. TÜV SÜD holds NABCB accreditation for lift inspection to IS 17900 (December 2025) [S48].

**Standards.** IS 17900 Part 7/Section 7 covers inspection and maintenance of lifts [S49]; IS 17900 Part 11 covers risk assessment of existing lifts [S50]. I did not see the texts.

**Liability.** In *Otis Elevator Co (India) Ltd v Rashmi Handa*, 2026 INSC 756, decided 29 July 2026, the Supreme Court held an elevator to be a common carrier owing the highest care, and makers, operators and premises owners jointly and severally liable [S36][S37]. It upheld a 70% (Otis), 25% (MES), 5% (RAW) split [S36]. MES relied on a maintenance-contract clause putting accident liability on Otis, and the Court noted Otis's failure to produce maintenance records [S36][S38]. Reports say the technical report put the immediate cause on a manual brake release during a rescue [S38] (attribution among the three reports uncertain). This settles the Inventor's open question: Otis was the maintenance contractor and MES the operating agency [I]. Criminal negligence arrests followed a 2023 Noida lift crash [S39].

## Lead 1: Society Lift Pool (federation tender for results-based AMCs, paid from savings)

### 1. Disciplines and deciding questions

| Discipline | Governing principle | Deciding question |
|---|---|---|
| Contract law | Section 74 Contract Act: stated sums are capped at reasonable compensation | Will automatic penalties survive a challenge? (Q4) |
| Lift regulation | Only licensed or registered contractors may maintain | Are there 3 or more qualified bidders per brand lot in each state? (Q1) |
| Competition and supply chain | Parts and tools access decides whether independents can compete | Will makers supply parts and diagnostic tools to independents? (Q8) |
| Society governance | Bye-law spending limits and tender rules | Can committees sign without a general-body meeting? (Q14) |
| Data protection | DPDP Act for resident reports | What notice and consent apply to QR reports? |
| Service operations | Measurement must be cheap and hard to game | Can a no-hardware ledger measure uptime well enough to trigger penalties? |

### 2. Findings by discipline

**Contract law.**
- Section 74 lets a court award only reasonable compensation up to the stated sum, not the sum itself [S18][S19].
- *Saw Pipes* (2003) held that no proof of loss is needed for a genuine pre-estimate. *Kailash Nath* (2015) is read by some as needing proof unless loss is hard to quantify [S19][S18].
- A Bombay High Court ruling halved a liquidated-damages award, from Rs 6,01,000 to Rs 3,00,000, because actual loss was not proved [S20]. So an "automatic" penalty is automatic only while the contractor does not contest it [I].
- Safer drafting: write the monthly fee as a price for a measured level of service, with service credits that reduce the price. Then the contractor is not "paying damages" but is paid less for less service [K]. A lawyer must confirm this survives section 74 in Indian practice.
- GST: Circular 178/10/2022 treats purely compensatory liquidated damages as outside "supply"; payments for agreeing to tolerate a breach can be taxable; notices still issue [S21]. Service credits that reduce the invoice avoid the question [K].
- Maker standard terms resist results duties. A Schindler AMC form excludes loss of use and consequential losses [S51]. A small Indian maintainer lists missing 3-phase power with earthing and power shortage as force majeure [S52]. Results clauses will be negotiated against these standard terms [I].

**Society governance.** Under the 2014 Maharashtra model bye-laws (bye-law 157 as reproduced), repair spending above a membership-based limit needs prior general-body sanction; the committee invites tenders, places them before the general body, then signs [S45]. Limits reported range from Rs 1 lakh to Rs 5 lakh under amended rules (unverified) [S45]. A draft 2026 model bye-law revision was published in August 2026 [S46]. A 10-lift society's AMC is about Rs 8,00,000 a year [I] (10 × Rs 80,000, mid-range of [S63][S64]), above every limit reported. So general-body approval is likely, whether AMCs count as "repairs" or not [I]. The Inventor's condition "sign without a special general meeting" (What must be true 2) is likely false in Maharashtra [I]. The upside: a federation tender produces exactly the papers bye-law 157 asks for [I].

**Lift regulation (who may bid).**
- Maharashtra: only approved (licensed) contractors [S3].
- Karnataka: only registered contractors [S7].
- UP: only the maker or, on my reading, its authorised provider [S10][S11][I].
- The pool must pre-qualify bidders on licence or registration. The firm itself needs no lift licence while it only procures and measures [I] (the Acts license erection, maintenance and testing [S3][S7]). If it ever takes the Inventor's "prime contractor" route (concept 17), it would need one [I].

**Parts and tools lock-in.**
- Italy's competition authority found Otis, KONE and Schindler abused dominance by refusing original spare parts to independent maintainers [S22].
- Singapore accepted commitments from lift parts suppliers to supply third-party maintainers [S23].
- India: no lift-sector CCI case found after 2 searches. The car spare-parts order (2014) is the nearest precedent [S24].
- Indian signs: makers declaring controllers obsolete and pushing replacement [S25]; a maker declining to continue a comprehensive AMC on an old lift, with parts unavailable [S26]; maker IoT not compatible with all controllers [S66]; anecdotes of service tools not sold to independents [S67].
- Third-party maintainers hold about 30% of lifts nationally (survey) [S62], 38% in a Bengaluru cut [S70].

**Data protection.** QR reports and guard logs capture residents' phone numbers and movements. The DPDP Rules were notified in November 2025, with fiduciary duties (notice, consent, security, breach notice) starting about May 2027 [S31]. Build notice and consent in from day one; it costs little [I].

**Measurement.** A QR-plus-guard ledger depends on guard discipline [A]. Penalties tied to it will be disputed unless the contract names the ledger as the agreed record [K].

### 3. Calculations

| Item | Inputs | Result | Tag |
|---|---|---|---|
| Pool AMC spend | 200 lifts × Rs 80,000 | Rs 1.6 crore a year | [I] (Inventor's pool; AMC mid-range of [S63][S64]) |
| Firm revenue at 5% saving | 30% of Rs 8 lakh + Rs 200 × 12 × 200 | Rs 7.2 lakh | [I] |
| Firm revenue at 10% saving | 30% of Rs 16 lakh + Rs 4.8 lakh | Rs 9.6 lakh (matches Inventor) | [I] |
| Ongoing ledger work | 20 societies × 2 h a month × 12 × Rs 750 | Rs 3.6 lakh a year against Rs 4.8 lakh admin fee | [I] (2 h [A]) |
| Same at 3 h a month | 20 × 3 × 12 × Rs 750 | Rs 5.4 lakh, above the admin fee | [I] |
| Penalty size, Nalanda-style | 2% of Rs 80,000 per lift per month | Rs 1,600 per lift-month | [I] (rate [S65]) |
| Penalty if read as 2% of the monthly fee | 2% × Rs 6,667 | Rs 133 per lift-month, too small to matter | [I] |

Reading: the admin fee barely covers the founder's own ledger time at 2 hours per society a month [I]. Success depends on the first-year saving and on automating the ledger [I].

### 4. Feasibility class and confidence

**Plausible.** Results-duty lift contracts are in commercial use abroad [S73]; the Inventor also reports UK pooled lift frameworks (not re-checked by me). In India each piece is legal: procurement advice needs no licence and service credits are ordinary contract terms [I]. Two binding limits: UP's maker-or-authorised rule [S10][S11] and a probable general-body vote in Maharashtra [S45][I]. Confidence medium on legality and delivery, low on bidder depth (no Indian parts-access data).

### 5. Production routes compared

| Route | Setup cost | Unit cost driver | Minimum scale | Lead time | Quality risk | Tag |
|---|---|---|---|---|---|---|
| Founder alone plus lawyer | Rs 50,000-1,00,000 contract and tender pack | Founder hours per society | 1 federation round | 8-12 weeks | No lift engineer to check scope claims | [A] |
| Founder plus retired lift engineer (part-time) | Same plus Rs 1,000-1,500 per site hour | Engineer site hours | 10 societies | 8-12 weeks | Low if the engineer is not tied to a bidder | [A] |
| Partner with an existing elevator consultant | Revenue share | Consultant fee | 1 pilot | 4-8 weeks | Consultant may have contractor ties | [A] (consultants exist [S72]) |
| Federation runs it, firm supplies tools only | Low | Software and templates | 1 federation | 12+ weeks | Weak control of standards | [A] |

Cheapest route that still meets quality: founder plus a part-time retired engineer, with a written no-conflict declaration [I].

### 6. Delivery cost sketch (first round, 20 societies, 200 lifts)

| Line | Amount | Tag |
|---|---|---|
| Model AMC, tender pack and mandate letter (lawyer) | Rs 50,000-1,00,000 one-time | [A] (no fee quotes found; test with 2 quotes) |
| Engineer site checks, 1 h per lift × 200 | Rs 2,00,000-3,00,000 at Rs 1,000-1,500 per hour | [A] |
| Founder time, X-rays, tender and meetings, 400 h | Rs 3,00,000 | [I] (hours from the Inventor [A]) |
| QR stickers, WhatsApp bot, ledger sheet | Rs 30,000 | [A] (Inventor figure, not re-checked) |
| DPDP notice and consent text | Rs 10,000 | [A] |
| Total, before any fee is earned | about Rs 5.9-7.4 lakh including founder time; Rs 2.9-4.4 lakh cash | [I] |

Correction to the Inventor: the Rs 1.5 lakh "capital at risk" leaves out engineer site time [I]. Cash needed is about Rs 2.9-4.4 lakh [I], 58-88% of capital [I].

### 7. Safety, compliance, certification

- Bidder pre-qualification: state licence or registration [S3][S7][S12]; in UP, maker authorisation [S10][S11]; contractor's own liability insurance [A].
- Safety floor: the scoring must not let price override safety. Specify minimum monthly visits, rescue training for the contractor's staff, and logbook duties [K]. The 2026 ruling turned partly on missing maintenance records [S36], so the contract should require records the society can inspect [I].
- Conflict of interest: a fee that is 30% of savings rewards the cheapest bidder [I]. If a cheap contractor later causes an accident, the firm that ran the tender may be named [I] (joint liability reasoning [S36][S37]; no case found against a procurement adviser). Mitigation: cap the success fee, or pay a flat tender fee plus a quality bonus [A].
- DPDP notice and consent for resident data [S31].
- No product certification applies [I].

### 8. Intellectual property

Nothing patentable of value. The model contract is copyright, and the brand can be registered [K]. Prior art: the French UNIS Avantage results contract [S73] and UK lift frameworks (Inventor, not re-checked by me). The Inventor's maker-side patents (Inventio US8028807, Hitachi US7194415) do not cover a buyer pool [I]; not re-searched.

### 9. Critical technical risks

1. Too few qualified bidders per brand lot, because of parts and tool lock-in [S22][S25][S67]. This is the deciding risk.
2. In UP the bidder pool is limited by law to makers and their authorised providers [S10][S11][I]. Do not start in UP.
3. Penalties disputed under section 74 [S18][S20]; draft as service credits [K].
4. General-body cycle delays the award to the next AGM [S45][I].
5. Ledger evidence weak or gamed [A].

### 10. Cheapest test to retire the biggest risk (bidder depth)

- Method: in Pune and Bengaluru, ask 8 licensed or registered independent contractors and 3 makers, in writing, whether they would bid for a 50-lift lot of named brands on the draft service-credit terms, and whether they can source parts and controller tools for those brands. In parallel, get a lawyer's one-page opinion on the service-credit clause.
- Cost: founder 30 hours, Rs 22,500 [I]; lawyer opinion Rs 25,000 [A]; total about Rs 47,500 [I], under the Rs 50,000 gate [I]. Cash outlay is the Rs 25,000 lawyer fee [I].
- Duration: 4 weeks [A].
- Pass: at least 3 qualified bidders per brand lot say yes in writing, including at least 2 that confirm parts access, and the lawyer confirms the credit structure is defensible [A].
- Fail: fewer than 3 per lot, or makers refuse service credits and independents cannot get parts for the main brands [A].

### 11. What a qualified expert must review

- Contract lawyer: service-credit and penalty clauses under section 74; limitation-of-liability interplay; mandate letter; arbitration clause.
- Co-operative society lawyer in Maharashtra (and the Karnataka equivalent): whether AMC renewals fall under bye-law 157 and which limits apply [S45][S46].
- UP lawyer: meaning of "authorised service provider" in the 2024 Act and Rules [S11].
- Competition lawyer: buyer-group risk, and a complaint route if makers refuse parts [S24].
- CA: GST on fees and on service credits [S21].

## Lead 2: Inspect-and-insure (independent inspection that sizes and unlocks liability cover)

### 1. Disciplines and deciding questions

| Discipline | Governing principle | Deciding question |
|---|---|---|
| Lift engineering | Inspection to IS 17900 Part 7 and Part 11 [S49][S50] | Who on the team is competent to inspect, and against which checklist? |
| Lift regulation | Statutory inspection and testing are state or licensed activities | What may a private firm do without a licence? (Q2) |
| Insurance regulation | Insurance Act section 40; IRDAI intermediary rules | How can the firm be paid without an insurance licence? (Q6) |
| Insurance product | Public liability wording for lifts | Do insurers write higher limits, and at what price? (Q7) |
| Professional liability | Negligence for a missed defect | Can the firm insure and contract away its inspector risk? |
| Accreditation | ISO/IEC 17020 inspection bodies | Is accreditation reachable on Rs 5 lakh? [A] (capital is the user's constraint) |

### 2. Findings by discipline

**Regulation (who may inspect).**
- No private statutory role exists yet. Maharashtra's third-party scheme is announced, not notified [S6].
- In Maharashtra, "testing" is a licensed activity [S3]. So the firm must stay advisory: visual and functional checks, document checks, and witnessing the contractor's tests [I].
- The firm must not label its report a statutory certificate [I].

**Insurance regulation.**
- Section 40 of the Insurance Act bars paying commission or any reward for soliciting or procuring insurance business to anyone except an agent or intermediary. Penalty up to Rs 1 lakh [S13].
- One source says a new section 40(2A) took effect on 5 February 2026, letting IRDAI set commission rules [S14]. Single source; verify.
- So a broker paying the firm for referrals is unlawful [I].
- Licence routes and their capital: an Insurance Marketing Firm needs Rs 10 lakh net worth [S16]; a corporate agent Rs 50 lakh [S57]. Both exceed the Rs 5 lakh capital [I].
- Broker route: brokers may sell risk-management services (risk assessment, advisory, mitigation) for commercial risks, for a fee that is not a percentage of premium, under a written mandate [S15]. They may engage external experts if they inform the client and stay responsible [S15]. One summary also says brokers may not outsource risk-management services unless they do not do that work at all [S15] (contradictory summary). So a broker might legitimately pay the firm as an outside expert, if a housing society counts as a "commercial risk" [I]. Unconfirmed; needs an IRDAI-specialist lawyer.
- Surveyor route: licensed surveyors carry out risk inspections for insurers [S17]. A surveyor licence is needed to assess general-insurance losses above Rs 20,000 [S17] (attribution uncertain). Qualifications not confirmed. A licensed surveyor-engineer could be paid directly by insurers for pre-acceptance inspections [I].

**Insurance product.**
- One tariff reproduction gives lift third-party liability on the public liability wording at Rs 3 per mille of the annual limit, with a 10% lift loading [S43].
- The any-one-accident limit must be at least a quarter of the annual limit (ratio not over 1:4), and there is a compulsory excess of 0.25% of the per-accident limit, minimum Rs 1,000, maximum Rs 1,00,000 [S43].
- India's general insurance was de-tariffed in 2007 [K], so the figure may be stale. Current quotes are needed.
- No current insurer rate, per-passenger limit or insurer appetite was found after 2 searches [S43].

**Breakdown module.** Machinery-breakdown policies exclude wear and gradual deterioration [S59]. Comprehensive AMCs cost about 60-70% more than non-comprehensive ones (home-lift guide) [S58]. In UP the module is unlawful, because the Act demands a comprehensive AMC [S10]. Elsewhere it shifts parts risk back to a volunteer committee. Only sudden failures move to the insurer [I].

**Professional liability.** No Indian case found where a lift inspector or auditor was held liable, after 1 search [S39]. The common-carrier standard [S36] and criminal negligence practice [S39] make it likely an inspector who rated a failed lift "green" would be joined [I]. Professional indemnity for engineers runs from about Rs 15,000 to Rs 2,00,000+ a year [S44] (aggregator; attribution among results uncertain).

**Accreditation.** TÜV SÜD already holds NABCB lift-inspection accreditation [S48]. ISO/IEC 17020 accreditation needs a documented management system, impartiality controls and witnessed assessments [K]. Cost and duration not found after 1 search. Not reachable as a first step on Rs 5 lakh [I] (time and documentation burden; cost unknown).

**People.** Lift technicians in Pune earn Rs 2.2-6 lakh a year (aggregator, Jan 2025) [S47]. An inspector-grade engineer (degree plus OEM experience) likely costs Rs 6-9 lakh a year [A] (above the technician band; test with 3 job posts).

### 3. Calculations

| Item | Inputs | Result | Tag |
|---|---|---|---|
| Exposure benchmark | Rs 3,01,48,195 × (1 + 9% × 23 years), simple | about Rs 9.26 crore | [I] (award [S36]; simple interest [A]) |
| Premium, Rs 10 lakh annual limit | 3 per mille + 10% + 18% GST | Rs 3,894 | [I] (rate [S43]) |
| Premium, Rs 1 crore | same | Rs 38,940 | [I] |
| Premium, Rs 5 crore | same | Rs 1,94,700 | [I] |
| Premium, Rs 9.3 crore | same | Rs 3,62,142 | [I] |
| Compulsory excess at Rs 1 crore per accident | 0.25% | Rs 25,000 | [I] (rule [S43]) |
| Inspector salary per lift | Rs 75,000 a month ÷ (3 lifts a day × 22 days) | Rs 1,136 | [I] (salary and pace [A]) |
| Full delivery cost per lift | salary Rs 1,136 + travel Rs 300 + contractor technician attendance Rs 1,000 + report 0.5 h × Rs 750 + PI share Rs 125 | Rs 2,936 | [I] (each input [A]) |
| Gross margin at Rs 4,000 fee | (4,000 − 2,936) ÷ 4,000 | about 27% | [I] |
| Same with the Inventor's pace and salary | Rs 568 salary + same extras | about 41% | [I] |

Correction to the Inventor: the 60-85% gross margin leaves out the contractor's technician, travel, reporting and indemnity [I]. On these assumptions the margin is about 27-41% [I]. Real cover sized to the Rs 9.3 crore benchmark would cost a society about Rs 3.6 lakh a year, if insurers write it at the old tariff [I]. Committees are unlikely to pay that [A].

### 4. Feasibility class and confidence

- Paid advisory inspection: **proven** in commercial use (TÜV SÜD in India [S48]; HSB and UK insurers abroad, per the Inventor, not re-checked).
- Insurance tie-in that pays the firm: **speculative**. Legal routes are narrow (broker external expert, or a surveyor licence) [S13][S15][S17], and insurer appetite is unknown [S43].
- Statutory inspector role: **infeasible now**. Not notified [S6]; accreditation is beyond the capital [I].
- Confidence: medium on the legal limits (several consistent sources); low on economics (no fee or insurer data).

### 5. Production routes compared

| Route | Setup cost | Unit cost driver | Minimum scale | Lead time | Quality risk | Tag |
|---|---|---|---|---|---|---|
| Founder inspects (only if a qualified lift engineer) | Rs 30,000-60,000 tools + PI | Founder hours | 1 lift | 2-4 weeks | Depends on competence | [A] |
| Hire one inspector-grade engineer | Salary Rs 50,000-75,000 a month | Lifts per day | about 60 lifts a month to cover salary at Rs 4,000 | 1-2 months to hire | Medium | [A] |
| Subcontract to an accredited body (TÜV SÜD) and coordinate | None | Their fee (not found) | Per job | Weeks | Low; thin margin | [A] (accreditation [S48]) |
| Become a licensed surveyor and sell to insurers | Licence plus training (cost not found) | Insurer fee per survey | Insurer panel | Months | Low | [A] (route [S17]) |
| Work as an external expert to a broker | Contract with broker | Broker's fee share (not % of premium) | One broker | Weeks | Legal uncertainty | [A] (route [S15]) |

Cheapest route that still meets quality: a part-time, experienced lift engineer on a per-lift fee, with the firm selling only advisory reports to committees, and no insurance money until a lawyer confirms the route [I].

### 6. Delivery cost sketch (per lift, first 50 lifts)

| Line | Amount | Tag |
|---|---|---|
| Inspector time, about 2 h per lift | Rs 1,136-1,500 | [I] (from the calculation; per-hour engineer fee [A]) |
| Contractor technician attendance (car top, pit, machine room access) | Rs 1,000 | [A] (not quoted; contractors may charge) |
| Travel | Rs 300 | [A] |
| Report and red-list follow-up, 0.5 h founder | Rs 375 | [I] |
| Professional indemnity, spread over 400 lifts a year | Rs 125 (Rs 50,000 a year) | [A] (premium band [S44]) |
| Tools (one-time): insulation tester, earth tester, multimeter, rope gauge, torch, PPE | Rs 30,000-60,000 | [A] |
| Legal terms (liability cap, scope, no-certification statement) | Rs 25,000-40,000 one-time | [A] |
| Total variable cost per lift | about Rs 2,900-3,300 | [I] |

### 7. Safety, compliance, certification

- The inspector works only with the contractor's licensed technician present and never operates the controller or the brake release [I] (licensed testing [S3]; rescue guidance [S41][S42]).
- PPE and car-top and pit safety drill; machine-room isolation by the contractor [K].
- Report wording: "advisory risk inspection, not a statutory inspection or certificate" [I].
- No insurance solicitation by the firm; any broker relationship needs a written legal opinion [S13][S15].
- DPDP notice for residents' and staff names in reports [S31].

### 8. Intellectual property

The checklist and scoring method are copyright and trade secret [K]. Nothing patentable found worth filing. Sensor-underwriting patents named by the Inventor are not lift-specific; not re-searched.

### 9. Critical technical risks

1. Inspector liability after an accident on a lift rated green [S36][S39][I].
2. No lawful insurance revenue on Rs 5 lakh capital [S13][S16][S57].
3. Insurers may not care: at the old tariff a Rs 1 crore cover costs about Rs 33,000 a year before GST [I], too small for underwriting effort [A].
4. Contractor obstruction of car-top and pit access [A]; the owner's statutory duty helps [S3].
5. Competence: an inspection that misses defects is worse than none [K].

### 10. Cheapest test to retire the biggest risk (lawful revenue and liability)

- Step 1 method: (a) a written opinion from an insurance-regulatory lawyer on three routes: broker external expert, surveyor licence, and fee from the society only; (b) quotes from 3 brokers for a sample Pune society at limits of Rs 1 crore and Rs 5 crore [A] (test limits), asking whether a third-party inspection report changes terms.
- Step 1 cost: lawyer Rs 25,000 [A]; founder 20 hours, Rs 15,000 [I]; total about Rs 40,000 [I], under the Rs 50,000 gate [I].
- Step 2 (only if step 1 passes): a pilot inspection of 5 lifts by an experienced engineer under a liability-capped contract, 5 × Rs 2,936 = Rs 14,680 [I] plus 20 founder hours, Rs 15,000 [I].
- Duration: 4 weeks for step 1, 2 more for step 2 [A].
- Pass: the lawyer confirms at least one lawful paid route; at least 1 insurer quotes a limit of Rs 1 crore or more [A] and says the report counts; in step 2, the pilot finds at least one material red item the contractor's log missed [A].
- Fail: no lawful route except the society fee, and no insurer interest. Then drop the insurance tie-in and test advisory inspection on its own [A].

### 11. What a qualified expert must review

- Insurance-regulatory lawyer: section 40 [S13][S14]; Broker Regulations risk-management and outsourcing rules [S15]; surveyor licensing [S17]; IMF and corporate agent routes [S16][S57].
- Chartered engineer with lift experience: the checklist against IS 17900 Parts 7 and 11 [S49][S50]; tools; what counts as "testing" in Maharashtra [S3].
- Liability lawyer: limitation of liability, consumer-law exposure, report wording.
- Insurer underwriter: whether limits above Rs 1 crore are available for society lifts and at what rate [S43].

## Lead 3: Society-side lift recorder (current and voltage sensing on the lift's feeder)

### 1. Disciplines and deciding questions

| Discipline | Governing principle | Deciding question |
|---|---|---|
| Electrical engineering | Motor current tracks car movement; supply voltage shows outages | Does one current trace separate run, idle and outage across drive types? |
| Electrical safety and law | CEA Safety Regulations 2023; licensed contractors | Who may fit it, and is a voltage tap an alteration of the installation? (Q9) |
| Building services | IS 14665: separate lift supply circuits | Is each lift's feeder reachable in the society's own panel? |
| Telecom regulation | MTCTE for cellular devices | Does the logger need TEC certification? (Q10) |
| Data science | Detection versus false alerts | Can alerts stay below 1 false alert per lift-week? |
| Intellectual property | Patents on current-profile state detection | Freedom to operate in India? (Q11) |
| Data protection | DPDP Act | Limited, unless resident QR data is added |

### 2. Findings by discipline

**Building services.** An amendment to IS 14665 Part 2 says lift supply must be separate from other building services, on separate circuits from the main switch rooms, run in armoured cable; power and lighting get separate cables from the meter room to the machine room [S27]. So each lift's power feeder normally starts at a breaker in the society's main switch room [I]. The car light and fan may sit on the separate lighting circuit, so idle current on the power feeder can be very low [I]. Run detection works by threshold, but outage detection needs a voltage sense [I].

**Electrical safety and licensing.**
- The CEA Safety Regulations 2023 were notified on 8 June 2023 [S28].
- A summary quotes the licensing provision: work on a consumer's installation must be done "by an electrical contractor licenced in this behalf" (attributed to regulation 31; attribution uncertain) [S28].
- States issue contractor licences and supervisor and workman permits [S29].
- A split-core CT clamps around an insulated cable without breaking the circuit [K]. A voltage tap does connect to live conductors, so it needs a fused connection made by a licensed contractor, ideally with the circuit isolated [K][S28].
- Isolating a lift feeder stops the lift, so the work must be booked with the lift contractor and the car emptied first [K].
- Cheaper and safer design: sense bus voltage once per panel through a dedicated fused MCB, not on each lift feeder [I].

**Signal physics.** A 5.5 kW lift motor at 415 V draws about 10.6 A when running, and a 7.5 kW motor about 14.4 A [I] (calculation below; motor ratings [K]). That is well above any plausible idle draw, so run detection is easy [I]. Harder claims:
- "Inspection-speed runs show maintenance visits": speculative [A]; no field data found.
- "Brake drag from current": the patent measures motor current [S68]. On the supply side of a VVVF drive the DC bus smooths the signal [K], so this is speculative [I].
- The Inventio patent compares current-time profiles with stored reference patterns [S32]. Patents show the method, not field accuracy [S34].
- An academic system notes that a device must sit in the car to measure the car's own movement [S35]. Supply-side sensing cannot see doors or entrapments directly [I].
- Hong Kong's regulator asked for a non-intrusive current acquisition device [S69], which supports the concept but gives no accuracy data.

**Telecom.** TEC's list of products under MTCTE includes sensing and tracking devices with cellular connectivity and smart meters with cellular connectivity [S30]. A self-built 4G logger may need its own MTCTE certificate [I]. Using a TEC-certified 4G router with a Wi-Fi logger may avoid that; verify, since Wi-Fi radios have their own approval rules [K].

**Lock-in and warranty.** Nothing is fitted to the lift, so a lift warranty or AMC clause on third-party devices should not bite [I]. One exception: where the AMC scope starts at the main switch, the contractor may still object to work in the panel [A].

**Patents.**
- US11603286B2 (assignee Inventio AG, part of Schindler [K]; granted March 2023) claims determining an elevator's operating state from the supply-line current-time profile with a galvanically separated sensor [S32].
- A US patent has no effect in India [K].
- No Indian counterpart found after 1 search. One Inventio EP application, EP3898486, claims a December 2018 Indian priority (IN201841047653), but its subject ("Elevator") is not shown [S33].
- An Indian freedom-to-operate search by a patent agent is needed before sale [I].

**Prior product.** KALA was launched in India in 2024 as non-invasive monitoring sold by subscription [S55]. Its sensing method was not found after 1 search [S55].

### 3. Calculations

| Item | Inputs | Result | Tag |
|---|---|---|---|
| Running current, 5.5 kW motor | 5,500 ÷ (√3 × 415 × 0.85 pf × 0.85 efficiency) | 10.6 A | [I] (pf and efficiency [K]) |
| Running current, 7.5 kW and 11 kW | same | 14.4 A and 21.2 A, so a 50 A or 100 A CT fits | [I] |
| False "out of service" alerts, fixed 30-minute no-run rule, 12 busy windows a day | P(no trip) = e^(−λ × 0.5); × 12 × 7 | 18.7 per lift-week at 3 trips/h; 4.2 at 6; 0.57 at 10; about 0 at 20 | [I] (Poisson traffic [A]) |
| Data volume | 1 Hz × 4 channels × 4 bytes | 1.38 MB a day, about 41 MB a month | [I] |
| Off-the-shelf meters for a 4-lift panel | 4 × Rs 4,851-4,999 | Rs 19,404-19,996, not Rs 4,000-6,000 | [I] (meter prices [S60][S61]) |
| Custom 4-channel kit | parts below | Rs 5,694-10,984 | [I] |

Correction to the Inventor: the Rs 4,000-6,000 kit was based on one 3-phase energy meter, which monitors one feeder [I]. Four lifts need four meters (about Rs 20,000) or a custom 4-channel logger (about Rs 5,700-11,000) [I].

The pass criterion of fewer than 1 false alert per lift-week fails for any lift averaging under about 10 trips an hour in busy windows, if a fixed 30-minute rule is used [I]. Use instead: twin-lift comparison (one car idle while its neighbour runs), learned per-hour baselines, and voltage loss as a hard signal [I].

### 4. Feasibility class and confidence

- Run counting and outage logging: **plausible to proven**. The principle is patented and in commercial monitoring [S32][S55]; the physics is simple [I].
- Inferring maintenance visits, brake drag or faults from supply current: **speculative** [I].
- Entrapment detection: **infeasible** from supply current alone [I].
- Confidence: high on run and outage detection, low on everything else.

### 5. Production routes compared

| Route | Setup cost | Unit cost (4-lift panel) | MOQ | Lead time | Quality risk | Tag |
|---|---|---|---|---|---|---|
| Off-the-shelf CT energy meters with data export | None | about Rs 20,000 | 1 | Days | Logging interval and export may not suit; per-feeder only | [I] (prices [S60][S61]) |
| Custom ESP32 logger, split-core CTs, certified 4G router | Rs 20,000-40,000 firmware and enclosure work | Rs 5,700-11,000 | 1 | 4-8 weeks | Founder build quality; enclosure and fusing | [A] (CT prices [S53]) |
| Contract manufacture of a custom board | Rs 1-3 lakh design, tooling and certification | Lower at volume | 100+ boards | 3-6 months | MTCTE certification needed if a cellular radio is on board | [A] (MTCTE list [S30]) |
| Buy or resell KALA, DATOMS or similar | Partnership | Their price (not found) | Unknown | Weeks | Loses the "society-owned" difference | [A] (KALA [S55]) |

Cheapest route that meets the quality needed for a pilot: off-the-shelf meters or a hand-built logger on 10 lifts, installed by a licensed electrician [I]. Do not design a board before the pilot passes [I].

### 6. Bill of materials (custom 4-lift kit)

| Line | Amount | Tag |
|---|---|---|
| ESP32 module | Rs 400-700 | [A] (not searched) |
| 4 split-core CTs, 30-100 A | Rs 1,244-2,384 (4 × Rs 311-596) | [I] (unit prices [S53]) |
| ADC and burden front end | Rs 300-500 | [A] |
| Voltage sensing, fused | Rs 450-900 | [A] |
| 4G modem or certified router | Rs 1,500-3,000 | [A] (not found after 1 search) |
| DIN enclosure, power supply, fuses, terminals | Rs 800-1,500 | [A] |
| Licensed electrician installation | Rs 1,000-2,000 per panel | [A] |
| Total one-time | Rs 5,694-10,984 | [I] |
| SIM data | Rs 100-200 a month | [A] |

### 7. Safety, compliance, certification

- Installation only by a licensed electrical contractor, recorded in the society's electrical register [S28][S29].
- Voltage taps fused at the tap point; CT secondaries never left open-circuit (use voltage-output CTs) [K].
- Panel IP rating and heat: the enclosure must not block ventilation or covers [K].
- Coordinate any isolation with the lift contractor, car empty and parked [K].
- MTCTE: confirm whether the final device needs certification [S30].
- DPDP: if resident QR reports are added, notice and consent from day one [S31].
- Alerts must say "possible outage, check", never "safe" [I], to avoid a false sense of safety.

### 8. Intellectual property

- Freedom-to-operate flag: Inventio's US11603286 family covers current-profile state detection [S32]; its Indian status is unknown [S33].
- Protectable: classification thresholds and twin-lift logic as trade secrets; brand; possibly a design registration for the enclosure [K].
- A patent on supply-side run counting is unlikely to be novel [I] (prior art [S32][S34][S69]).

### 9. Critical technical risks

1. False alerts on low-traffic lifts [I] (calculation above).
2. Mixed drive types (old AC2, VVVF, hydraulic) need separate baselines [K]. Hydraulic lifts draw power only going up [K].
3. Patent exposure in India unknown [S33].
4. Installation in a live panel [S28][K].
5. Value without contract terms: a recorder alone may only show that the committee knew [A] (Investigator's "knowing creates duty").

### 10. Cheapest test to retire the biggest risk (signal accuracy)

- Step 1 (1 week): one panel, 2 lifts, two off-the-shelf meters (2 × Rs 4,851 [S60]) plus electrician Rs 1,500 [A], a guard's paper log of outages and visits. Cash about Rs 11,200 [I]; founder 10 hours, Rs 7,500 [I]; total about Rs 18,700 [I].
- Step 2 (6 weeks, only if step 1 shows clean run signatures): 10 lifts across 3 societies, at least 2 drive types, on 3 hand-built 4-channel kits. Hardware up to Rs 32,952 [I] (3 × Rs 10,984); electrician Rs 6,000 [A]; data Rs 3,000 [A]. Cash about Rs 42,000 [I], under the Rs 50,000 gate [I]. Founder 80 hours (Rs 60,000) [I] comes on top, so the full cost with founder time is about Rs 1.02 lakh [I].
- Pass: at least 90% of outages over 30 minutes detected (against the guard log and the contractor's logbook), at most 1 false alert per lift-week after a 2-week learning period, and no safety incident during installation [A].
- Fail: false alerts over 2 per lift-week, or outage detection under 80% [A].

### 11. What a qualified expert or lab must review

- Licensed electrical contractor or chartered electrical engineer: tap method, fusing and isolation procedure, the CEA regulation reading [S28].
- TEC or MTCTE consultant: certification need and cost [S30].
- Indian patent agent: freedom-to-operate search on the Inventio family and Indian filings [S32][S33].
- Lift engineer: drive-type baselines, and whether supply-side signatures can show inspection mode at all.

## Wildcard: the entrapment bounty (per-entrapment payment to the trapped household)

### 1. Disciplines and deciding questions

| Discipline | Governing principle | Deciding question |
|---|---|---|
| Contract law | Section 74; privity | Is a fixed per-event sum enforceable, and can a non-party household benefit? (Q4) |
| Insurance law | Insurance business needs registration | Is it insurance? |
| Safety and human factors | Rescue only by trained lift staff | Does paying by duration push unsafe fast rescues? (Q13) |
| Society governance and tax | Member account credits; GST on LDs | Can the society credit a household's bill? (Q5) |
| Fraud control | Verification | Can staged entrapments be screened out? |

### 2. Findings by discipline

**Contract law.** A trapped household is not a party to the AMC [K]. The clean structure: the contractor credits the society (a party), and the society credits the member by its own resolution [I]. A fixed sum per entrapment is a liquidated-damages clause, cut to reasonable compensation if contested [S18][S19]. Where loss is hard to prove, as with distress and lost time, courts are more willing to accept a genuine pre-estimate [S18][S19][I]. Contractors' standard terms exclude consequential losses [S51] and treat power failure as force majeure [S52]. Power-cut entrapments will be the first dispute [I].

**Insurance law.** Paid by the contractor under its own AMC, this is a price or damages term, not insurance [I]. If the firm or the society collected money in advance to pay out on entrapments, that would look like insurance business needing IRDAI registration [K]; the Inventor reached the same view.

**Safety.** This is the biggest problem.
- Rescue guidance in India and abroad says only trained lift staff should release passengers; untrained people prying doors is a known hazard [S40][S41].
- The car must never travel uncontrolled using the brake-release lever [S42].
- The leading Supreme Court case reportedly turned on a manual brake release during a rescue [S38].
- A payout that rises at 10 and 30 minutes rewards speed, so it can push guards into amateur rescues [I].
- A per-event payment can also tempt residents to cause entrapments (holding doors, overloading) [A].
- Design fix: pay a flat sum per entrapment, measure response as the time to arrival of the contractor's trained technician (not time to release), and forbid any credit when non-lift staff attempt a release [I].

**Tax and governance.** Compensatory liquidated damages are generally outside GST [S21]. Crediting a member's maintenance bill needs a general-body or committee resolution under the bye-laws [A]. The credit is the society's money once received [K].

### 3. Calculations

| Entrapments per lift a year | Payout Rs 2,000 each [A] | Payout Rs 5,000 each [A] | Tag |
|---|---|---|---|
| 1 | Rs 2,000 (2.5% of a Rs 80,000 AMC) | Rs 5,000 (6.2%) | [I] |
| 4 | Rs 8,000 (10%) | Rs 20,000 (25%) | [I] |
| 8 | Rs 16,000 (20%) | Rs 40,000 (50%) | [I] |

The per-lift entrapment rate is unknown [A] (no per-lift rate found by the Inventor or the Investigator). A contractor facing 10-50% of fee at risk will price it in [I]. The society then pays roughly the same total but gains a complete record [I].

### 4. Feasibility class and confidence

**Plausible as a contract clause inside Lead 1. Not viable alone.** It needs Lead 1's contract and ledger, and it has no revenue of its own [I]. Confidence medium on legality and low on contractor acceptance. The safety risk is high unless the payout is redesigned as above [S38][S41][I].

### 5. Production routes compared

| Route | Setup | Running cost driver | Risk | Tag |
|---|---|---|---|---|
| Clause in Lead 1's model AMC | Lawyer drafting within Lead 1's budget | Verification time per event | Disputes | [I] |
| Contractor-offered guarantee (marketing by an independent) | Contractor's own | Contractor's | Contractor may game verification | [A] |
| Firm-funded payout | Capital reserve | Claims | Insurance law breach | [K] |

### 6. Delivery cost sketch

| Line | Amount | Tag |
|---|---|---|
| Clause drafting and verification protocol | Rs 15,000-25,000, inside Lead 1's legal budget | [A] |
| Verification per event (CCTV clip, guard log, QR timestamp, founder review 0.5 h) | Rs 375 | [I] (0.5 h [A]) |
| Dispute handling | Unknown; budget 2 h per disputed event, Rs 1,500 | [A] |

### 7. Safety, compliance, certification

- Payout tied to occurrence, not to release speed [I].
- No credit where non-lift staff attempted a release [I] (guidance [S40][S41][S42]).
- Exclude events caused by misuse, verified on CCTV [A].
- No firm-held fund [K].
- DPDP notice for residents' data [S31].

### 8. Intellectual property

None protectable beyond contract wording (copyright) [K].

### 9. Critical technical risks

1. Unsafe rescue incentive [S38][S41][I].
2. Staged events [A].
3. Contractor refusal or price loading [I].
4. Power-cut entrapments argued as force majeure [S52].

### 10. Cheapest test

- Method: lawyer review of the clause, a lift engineer's safety review, and written reactions from 3 contractors in Lead 1's bidder test.
- Cost: Rs 20,000 lawyer [A]; Rs 5,000 engineer [A]; founder 12 hours, Rs 9,000 [I]; total about Rs 34,000 [I].
- Duration: 3 weeks, alongside Lead 1 [A].
- Pass: at least 1 of 3 contractors accepts a flat per-event credit with safety exclusions, and the lawyer sees no privity or insurance problem [A].
- Fail: no contractor accepts, or the safety review finds no workable design [A].

### 11. What a qualified expert must review

- Contract lawyer: privity, section 74, force-majeure carve-outs [S18][S52].
- Insurance lawyer: confirm it is not insurance business [K].
- Lift safety engineer: rescue protocol and the payout trigger [S41][S42].

## Comparison across concepts

| Factor | Lead 1 Pool | Lead 2 Inspect-and-insure | Lead 3 Recorder | Wildcard |
|---|---|---|---|---|
| Feasibility class | Plausible | Inspection proven; insurance tie-in speculative; statutory role infeasible now | Run and outage plausible to proven; diagnostics speculative | Plausible only as a clause |
| Licence the firm needs | None while it only procures [I] | None for advisory work; insurance revenue needs a licence or a narrow broker route [S13][S15][S16] | Licensed electrician for installation [S28] | None [I] |
| Binding legal limit | UP maker-or-authorised AMC [S10][S11]; general-body vote [S45] | Section 40 [S13]; testing is licensed in Maharashtra [S3] | MTCTE for cellular [S30]; Indian FTO unknown [S33] | Section 74 [S18]; rescue safety [S41] |
| Cost of first test, founder time included | about Rs 47,500 [I] | about Rs 40,000 for step 1 [I] | about Rs 18,700 for step 1; step 2 Rs 42,000 cash plus Rs 60,000 founder time [I] | about Rs 34,000 [I] |
| Liability exposure | Medium (tender adviser) [I] | High (inspector) [I] | Low-medium (alert failure) [I] | High if the payout rewards speed [I] |
| Lock-in exposure | High [S22][S25] | Low [I] | None on the lift [I] | Inherits Lead 1 [I] |
| Main correction to the Inventor | Cash need about Rs 2.9-4.4 lakh, not Rs 1.5 lakh; general-body approval likely [I] | Margin about 27-41%, not 60-85% [I] | 4-lift kit Rs 5,700-20,000, not Rs 4,000-6,000; the false-alert rule fails at low traffic [I] | Duration-based payout is unsafe [I] |

Order of technical and legal risk, lowest first: Lead 3 (step 1 test), Lead 1, wildcard as a Lead 1 clause, Lead 2 [I]. Lead 1 has the largest upside but its deciding risk (bidder depth under parts lock-in) has no Indian data [I]. Run the Lead 1 bidder test and Lead 3 step 1 in the same month; together they cost about Rs 66,200 [I] (Rs 47,500 + Rs 18,700), 13% of capital [I]. Each test on its own is under Rs 50,000 [I].

What I did not check that could change this: Maharashtra's rules under section 37; the UP Rules' definition of "authorised service provider"; current insurer rates; the MTCTE cost; the Indian patent register; any contractor's, insurer's or committee's view.

## Sources

All rows retrieved 2026-10-31. I opened no page; every row is "search summary". Rows marked "not re-checked by me" come from the Inventor's or Investigator's files.

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Maharashtra brings Lift and Escalator Safety Regime into force from 1 November | SCC Online | https://www.scconline.com/blog/?p=399876 | 2026-10 | 2026-10-31 | Commencement 1 Nov 2026 | search summary |
| 2 | Government of Maharashtra: commencement of the Lifts, Escalators and Moving Walks Act, 2017 | TeamLease RegTech | https://teamleaseregtech.com/updates/article/60738/government-of-maharashtra-commencement-of-the-lifts-escalators-and-mov/ | 2026-10 | 2026-10-31 | Notified 22 Oct 2026; replaces 1939 Act; yearly inspection, logbooks (secondary) | search summary |
| 3 | Maharashtra Lifts, Escalators and Moving Walks Act, 2017 (Act XV of 2018) | PRS India | https://prsindia.org/files/bills_acts/acts_states/maharashtra/2018/2018MH15.pdf | 2018 | 2026-10-31 | Approved contractor licence for erection, maintenance or testing; s.18 maintenance contract; s.23 insurance (attribution between PRS PDF and Indian Kanoon section pages uncertain) | search summary |
| 4 | Great move toward safety | Elevator World | https://elevatorworld.com/?p=49622 | not shown (c. 2018) | 2026-10-31 | Third-party insurance wording | search summary |
| 5 | Maharashtra Lifts, Escalators and Moving Walks (Amendment) Bill, 2026 | TeamLease RegTech | https://teamleaseregtech.com/updates/article/53435/maharashtra-lifts-escalators-and-moving-walks-amendment-bill-2026 | 2026-03 | 2026-10-31 | Amends ss.29, 35, 37; contents not found | search summary |
| 6 | Maha to strengthen lift inspection system, 519 posts to be created | Lokmat Times | https://www.lokmattimes.com/national/maha-to-strengthen-lift-inspection-system-519-posts-to-be-created-cm-fadnavis | 2026-03-04 | 2026-10-31 | Planned third-party inspection; not notified | search summary |
| 7 | Karnataka Lifts, Escalators and Passenger Conveyors Act, 2012 (Act 9 of 2013) | India Code | https://www.indiacode.nic.in/bitstream/123456789/7182/1/9_of_2013_%28e%29.pdf | 2013 | 2026-10-31 | s.6 registration for maintenance; s.4 owner licence | search summary |
| 8 | Karnataka amendment bill 65 of 2025 | PRS India | https://prsindia.org/files/bills_acts/bills_states/karnataka/2025/Bill65of2025KA.pdf | 2025 | 2026-10-31 | "Authorised officer" change; enactment unconfirmed | search summary |
| 9 | Call for AMC notice inviting quotation (lifts) | NITK Surathkal | https://www.l4.nitk.ac.in/document/attachments/2369/Call_for_AMC_NIQ_%281%29.pdf | not shown; retrieved 2026 | 2026-10-31 | Tender requires Karnataka registration, qualified engineers, logbook | search summary |
| 10 | Uttar Pradesh Lifts and Escalators Act, 2024 | TeamLease RegTech | https://www.teamleaseregtech.com/updates/article/32469/uttar-pradesh-lifts-and-escalators-act-2024 | 2024 | 2026-10-31 | Comprehensive AMC from OEM or authorised provider | search summary |
| 11 | The Uttar Pradesh Lifts and Escalators Act, 2024 (English) | India Code | https://www.indiacode.nic.in/bitstream/123456789/19956/1/act_lift_eng.pdf | 2024 | 2026-10-31 | AMC definition fragment "his authorized service provider" (OCR garbled) | search summary |
| 12 | Lift and Escalator Act, 2024: Noida dominates registration drive across Uttar Pradesh | The Realty Today | https://therealtytoday.com/news/trending/lift-and-escalator-act-2024-noida-dominates-registration-drive-across-uttar-pradesh | not shown (after Oct 2024) | 2026-10-31 | 87 makers and 98 AMC agencies registered; agency registration with Director of Electrical Safety (attribution among results uncertain) | search summary |
| 13 | Insurance Act 1938, section 40 | Courtbook | https://courtbook.in/insurance-act-1938/section-40 | substituted 2015 | 2026-10-31 | Ban on paying non-licensed persons; penalty up to Rs 1 lakh | search summary |
| 14 | Insurance Act section 41: prohibition of rebates, penalty | Oquilia | https://www.oquilia.com/news/insurance-act-section-41-prohibition-of-rebates-penalty | 2026 | 2026-10-31 | Claimed s.40(2A) from 5 Feb 2026 (single source) | search summary |
| 15 | IRDAI (Insurance Brokers) Regulations 2018 | Department of Financial Services | https://financialservices.gov.in/beta/sites/default/files/2024-11/IRDAI%20(Insurance%20Brokers)%20Regulations%202018.pdf | 2018 | 2026-10-31 | Risk-management services, fee rules, external experts, outsourcing (summary contradictory) | search summary |
| 16 | Insurance Marketing Firm registration | Kanakkupillai | https://www.kanakkupillai.com/insurance-marketing-firm-registration | not shown; retrieved 2026 | 2026-10-31 | IMF net worth Rs 10 lakh (also Business Standard 2015-12) | search summary |
| 17 | Duties and responsibilities of surveyor and loss assessor | Go Digit | https://www.godigit.com/content/dam/godigit/general/documents/duties-and-responsibilities-of-surveyor-and-loss-assessor.pdf | not shown; retrieved 2026 | 2026-10-31 | Surveyors conduct risk inspections; s.64UM threshold Rs 20,000 (attribution uncertain) | search summary |
| 18 | Section 74 proof paradox: liquidated damages in Indian contracts | SCC Online | https://www.scconline.com/blog/post/2026/07/27/section-74-proof-paradox-liquidated-damages-indian-contracts/ | 2026-07-27 | 2026-10-31 | Reasonable compensation; Fateh Chand, Saw Pipes, Kailash Nath | search summary |
| 19 | Liquidated damage clauses: did Kailash Nath dilute the Saw Pipes position? | Bar & Bench | https://www.barandbench.com/columns/liquidated-damage-clauses-did-kailash-nath-dilute-the-saw-pipes-position | not shown; retrieved 2026 | 2026-10-31 | Split readings on proof of loss | search summary |
| 20 | Bombay High Court: liquidated damages cannot be automatically enforced | RawLaw | https://rawlaw.in/?p=7127 | not shown; retrieved 2026 | 2026-10-31 | Award cut from Rs 6,01,000 to Rs 3,00,000 | search summary |
| 21 | Liquidated damages and GST: misconceptions, notices, legal position | TaxGuru | https://taxguru.in/goods-and-service-tax/liquidated-damages-gst-misconceptions-notices-legal-position.html | not shown; circular dated 2022-08-03 | 2026-10-31 | Circular 178/10/2022; Aavanti Solar 2024 | search summary |
| 22 | Press release: lift maintenance and spare parts (Otis, KONE, Schindler) | Autorità Garante della Concorrenza e del Mercato (Italy) | https://en.agcm.it/en/media/press-releases/2000/5/alias-1547 | 2000-05 | 2026-10-31 | Abuse of dominance: refusal to supply parts to independents | search summary |
| 23 | Lift part suppliers provide commitments to CCCS to facilitate lift maintenance in HDB estates | ASEAN Competition | https://asean-competition.org/read-cases-lift-part-suppliers-provide-commitments-to-cccs-to-facilitate-lift-maintenance-in-hdb-estates | not shown; retrieved 2026 | 2026-10-31 | Singapore commitments | search summary |
| 24 | CCI order on car manufacturers for anti-competitive practices | IndiaCorpLaw | https://indiacorplaw.in/2014/09/03/cci-order-on-car-manufacturers-for-anti/ | 2014-09-03 | 2026-10-31 | Indian spare-parts precedent | search summary |
| 25 | Manufacturers declaring elevators obsolete: how ethical is it? | Free Press Journal | https://www.freepressjournal.in/amp/business/manufacturers-declaring-elevators-obsolete-how-ethical-it-is | not shown; retrieved 2026 | 2026-10-31 | Controller obsolescence pressure | search summary |
| 26 | Lift modernisation proposal - Johnson Lifts | srishti-owners Google Group | https://groups.google.com/g/srishti-owners/c/aY3QuvdTo9c | 2022 | 2026-10-31 | Maker declined comprehensive AMC; parts unavailable | search summary |
| 27 | IS 14665 Part 2 Sections 1-2 (with amendment) | BIS via Public.Resource.Org | https://law.resource.org/pub/in/bis/S05/is.14665.2.1-2.2000.pdf | 2000 | 2026-10-31 | Separate lift supply circuits; separate power and lighting cables | search summary |
| 28 | CEA (Measures relating to Safety and Electric Supply) Regulations, 2023 | Central Electricity Authority | https://cea.nic.in/regulations-category/measures-relating-to-safety-and-electric-supply/?lang=en | 2023-06-08 | 2026-10-31 | Notification; licensed contractor provision (wording and regulation number attribution uncertain) | search summary |
| 29 | CEA advisory: One Nation, One Licence for electrical contractors | TeamLease RegTech | https://www.teamleaseregtech.com/updates/article/28173/cea-issued-an-advisory-to-ensure-one-nation-one-license-for-electrical/ | 2023 | 2026-10-31 | State contractor and supervisor licensing | search summary |
| 30 | List of products under TEC certification | Professional Utilities | https://www.professionalutilities.com/blogs/list-of-products-under-tec-certification.php | not shown; retrieved 2026 | 2026-10-31 | Cellular IoT and tracking devices under MTCTE (phase not stated) | search summary |
| 31 | Govt notifies DPDP Rules 2025; rollout stretched over 18 months | YourStory | https://yourstory.com/2025/11/digital-personal-data-protection-dpdp-rules-2025-rollout-over-18-months | 2025-11 | 2026-10-31 | Fiduciary duties from about May 2027 | search summary |
| 32 | US11603286B2 Method and device for determining an operating state of an elevator system | Google Patents | https://patents.google.com/patent/US11603286 | 2023-03-14 | 2026-10-31 | Assignee Inventio AG; current-profile method | search summary |
| 33 | EP3898486 Elevator (Inventio) | European Patent Office | https://data.epo.org/publication-server/rest/v1.2/patents/EP3898486NWA1/document.html | priority 2018-12-17 | 2026-10-31 | Indian priority IN201841047653; subject not shown | search summary |
| 34 | US11524876B2 Monitoring an elevator door arrangement | Google Patents | https://patents.google.com/patent/US11524876 | not shown; retrieved 2026 | 2026-10-31 | Current-profile door monitoring; no field accuracy | search summary |
| 35 | EleTrack (EWSN 2018) | EWSN | https://www.ewsn.org/file-repository/ewsn-2018/013_024_mohammad.pdf | 2018 | 2026-10-31 | Car parameters need an in-car device | search summary |
| 36 | M/s Otis Elevator Co (India) Ltd v Rashmi Handa & Others, 2026 INSC 756 | Verdictum | https://www.verdictum.in/supreme-court/ms-otis-elevator-co-india-ltd-v-rashmi-handa-others-2026-insc-756-1618809 | 2026-07-29 | 2026-10-31 | Common carrier; 70/25/5 upheld; clause 6.1; missing records; award | search summary |
| 37 | Elevator manufacturers, operators and building owners jointly liable for user safety | Bar & Bench | https://www.barandbench.com/news/litigation/elevator-manufacturers-operators-and-building-owners-jointly-liable-for-user-safety-supreme-court | 2026-07 | 2026-10-31 | Joint and several liability | search summary |
| 38 | Senior RAW officer crushed to death during lift rescue operation: SC holds elevators common carriers | RawLaw | https://rawlaw.in/senior-raw-officer-crushed-to-death-during-lift-rescue-operation-supreme-court-holds-elevators-are-common-carriers-and-upholds-manufacturers-primary-liability-for-deficient-maintenance/ | 2026-07 | 2026-10-31 | Death during rescue; manual brake release as immediate cause (attribution among reports uncertain) | search summary |
| 39 | Noida lift crash: 2nd manager of construction company held for negligence | Business Standard | https://www.business-standard.com/india-news/noida-lift-crash-2nd-manager-of-construction-company-held-for-negligence-123091701048_1.html | 2023-09-17 | 2026-10-31 | Criminal negligence practice; no inspector-liability case found | search summary |
| 40 | Safe lifts (Rights column) | The Tribune | https://www.tribuneindia.com/2009/20090419/spectrum/rights.htm | 2009-04-19 | 2026-10-31 | Untrained people prying doors; trained rescue | search summary |
| 41 | Safe release of passengers (revised June 2022) | Lift and Escalator Industry Association (UK) | https://www.leia.co.uk/wp-content/uploads/2022/07/27-Safe-Release-of-Passengers-Revised-June-2022.pdf | 2022-06 | 2026-10-31 | Only trained, competent persons release passengers | search summary |
| 42 | Lift rescue guidance | National Fire Chiefs Council (UK) | https://nfcc.org.uk/?p=13317 | not shown; retrieved 2026 | 2026-10-31 | Never let a car travel uncontrolled on the brake-release lever | search summary |
| 43 | Terms and conditions for Lift Insurance Policy (Liability Cover) | indiacustomercare.com (tariff reproduction) | https://www.indiacustomercare.com/terms-conditions-lift-insurance-policy-liability-cover | undated | 2026-10-31 | Rs 3 per mille; 10% lift loading; 1:4 ratio; excess | search summary |
| 44 | Professional indemnity insurance for engineers | Bimakavach | https://www.bimakavach.com/blog/professional-indemnity-insurance-for-engineers-everything-you-need-to-know/ | not shown; retrieved 2026 | 2026-10-31 | PI premium band Rs 15,000-2,00,000+ (attribution among results uncertain) | search summary |
| 45 | Model bye-laws of cooperative housing society: management affairs | MySocietyClub | https://mysocietyclub.com/bye-laws/maharashtra-cooperative-housing-society-bye-laws/management-affairs | not shown; retrieved 2026 | 2026-10-31 | Bye-law 157 tender and general-body procedure; Rs 1-5 lakh limits (unverified) | search summary |
| 46 | Maharashtra puts draft model bye-laws for housing societies up for public comments | Moneylife | https://www.moneylife.in/article/housing-society-problems-and-solutions-resolving-access-disputes-and-nomination-issues/article/maharashtra-puts-draft-model-byelaws-for-housing-societies-up-for-public-comments-what-is-set-to-change/81379.html | 2026-08-17 | 2026-10-31 | Draft 2026 bye-laws pending | search summary |
| 47 | Lift technician salary, Pune | AmbitionBox | https://ambitionbox.com/profile/lift-technician-salary/pune-location | 2025-01 | 2026-10-31 | Rs 2.2-6 lakh a year | search summary |
| 48 | TÜV SÜD achieves NABCB accreditation for IS 17900 lift safety standard | Industrial Automation India | https://www.industrialautomationindia.in/news/tuv-sud-achieves-nabcb-accreditation-for-is-17900-lift-safety-standard | 2025-12 | 2026-10-31 | Accredited lift inspection incumbent | search summary |
| 49 | IS 17900 Part 7/Section 7: 2024 (inspection and maintenance) | Bureau of Indian Standards | https://services.bis.gov.in/tmp/15090_17102024175006_6.pdf | 2024-10-17 | 2026-10-31 | Inspection and maintenance standard exists | search summary |
| 50 | Safety norms for existing lifts | Elevator World | https://elevatorworld.com/article/safety-norms-for-existing-lifts | not shown; retrieved 2026 | 2026-10-31 | IS 17900 Part 11 risk assessment of existing lifts | search summary |
| 51 | AMC 2024-2025 (Schindler AMC terms) | Vasavi College of Engineering | https://vce.ac.in/facilities/downloads/mcell/amc-2024-2025.pdf | 2024 | 2026-10-31 | Exclusion of loss of use and consequential loss | search summary |
| 52 | Terms and conditions | GPK Elevators | https://sites.google.com/view/gpkelevators/terms-and-conditions | not shown; retrieved 2026 | 2026-10-31 | Power failure as force majeure; no consequential liability | search summary |
| 53 | Non-invasive SCT-013 30A split-core current transformer | Robocraze | https://www.robocraze.com/non-invasive-sct-013-30a-ac-sensor-split-core-current-transformer | not shown; retrieved 2026 | 2026-10-31 | Rs 311 (30 A); also IndiaMART 100 A Rs 596, Robodo 100 A Rs 550 in same search | search summary |
| 54 | Maharashtra: apply for lift or escalator maintenance licence | WikiProcedure | https://wikiprocedure.com/index.php/Maharashtra_-_Apply_for_Lift_or_Escalator_Maintenance_License | not shown; retrieved 2026 | 2026-10-31 | Qualification and electrical licence (secondary) | search summary |
| 55 | PAPL, Ardelisys launch IoT-based elevator monitoring system at SLM World in India | Elevator World | https://elevatorworld.com/news/daily-news/papl-ardelisys-launch-iot-based-elevator-monitoring-system-at-slm-world-in-india | 2024-03 | 2026-10-31 | KALA launch; method not found | search summary |
| 56 | Checklist for registration and inspection of lifts and escalators | Chief Electrical Inspector, Haryana | https://ceiharyana.com/Procedure_For_Registration_Lift_Exclator.aspx | not shown; retrieved 2026 | 2026-10-31 | AMC and insurance for registration (Investigator S21; not re-checked by me) | search summary |
| 57 | Requirements for registering as a corporate agent | IRDAI policyholder portal | https://policyholder.gov.in/web/guest/requirements-for-license-as-a-corporate-agent | not shown; retrieved 2026 | 2026-10-31 | Rs 50 lakh net worth (Inventor S55; not re-checked by me) | search summary |
| 58 | Lift AMC evaluation guide India | Studio Matrx | https://www.studiomatrx.org/guides/lift-amc-evaluation-guide-india | 2026 | 2026-10-31 | Comprehensive 60-70% above non-comprehensive, home lifts (Inventor S23; not re-checked by me) | search summary |
| 59 | Machinery Breakdown Insurance Policy Wording (Commercial) | Zurich Kotak | https://cms.zurichkotak.com/uploads/32_Machinery_Breakdown_Insurance_Policy_Wording_Commercial_78baabcd5f.pdf | not shown; retrieved 2026 | 2026-10-31 | Wear and gradual deterioration excluded (Inventor S24; not re-checked by me) | search summary |
| 60 | 200A three-phase power meter with inbuilt CT | IndiaMART | https://m.indiamart.com/proddetail/three-phase-meter-power-meter-with-inbuilt-ct-2855874857348.html | not shown; retrieved 2026 | 2026-10-31 | Rs 4,851 per meter (Inventor S70; not re-checked by me) | search summary |
| 61 | XPR3SS 100A 3-phase energy meter price history | pricehistory.app | https://pricehistory.app/p/xpr3ss-100a-3-phase-bi-directional-energy-CotD7Ace | 2026-03-20 | 2026-10-31 | Rs 4,999 (Inventor S71; not re-checked by me) | search summary |
| 62 | Got a lift in your apartment? Survey says 46% residents were trapped at least once last year | Business Today (LocalCircles) | https://www.businesstoday.in/amp/india/story/got-a-lift-in-your-apartment-survey-says-46-residents-were-trapped-at-least-once-last-year-546526-2026-07-31 | 2026-07-31 | 2026-10-31 | About 30% third-party maintained (Investigator S1; not re-checked by me) | search summary |
| 63 | Society maintenance charges in Navi Mumbai 2026 | navimumbai.com | https://navimumbai.com/?p=5471 | 2026 | 2026-10-31 | Per-lift AMC (Investigator S33; not re-checked by me) | search summary |
| 64 | Pune property maintenance charges guide 2026 | Pune Reality Hub | https://punerealityhub.pages.dev/blog/pune-property-maintenance-charges-guide-2026 | 2026 | 2026-10-31 | Per-lift AMC (Investigator S34; not re-checked by me) | search summary |
| 65 | Notice inviting tender, lift AMC | Nalanda University | https://nalandauniv.edu.in/wp-content/uploads/2026/03/NIT.pdf | 2026-03 | 2026-10-31 | 2% per month per lift penalty (Investigator S37; not re-checked by me) | search summary |
| 66 | Otis ONE | Otis India | https://www.otis.com/en/in/products-services/otis-signature-service/otis-one | not shown; retrieved 2026 | 2026-10-31 | Controller compatibility limits (Investigator S38; not re-checked by me) | search summary |
| 67 | Otis Gen3 service (r/Elevators thread, mirror) | Reddit mirror | https://lr.us.psf.lt/r/Elevators/comments/1kbbtr6/otis_gen3_service | 2025 | 2026-10-31 | Anecdote: tool not sold to independents (Investigator S53; not re-checked by me) | search summary |
| 68 | US7350883B2 Detecting elevator brake and other dragging by monitoring motor current | Google Patents | https://patents.google.com/patent/US7350883 | 2008 | 2026-10-31 | Brake drag from motor current (Inventor S64; not re-checked by me) | search summary |
| 69 | Non-intrusive current data acquisition device for lift monitoring (wish list) | EMSD Innovation, Hong Kong | https://inno.emsd.gov.hk/en/it-wish-list/index_id_172.html | not shown; retrieved 2026 | 2026-10-31 | Regulator seeks non-intrusive current sensing (Inventor S75; not re-checked by me) | search summary |
| 70 | Four in 10 Bengalureans dread stepping into a lift: survey | Deccan Herald | https://deccanherald.com/india/karnataka/bengaluru/four-in-10-bengalureans-dread-stepping-into-a-lift-survey-4098155 | 2026-08 | 2026-10-31 | 38% third-party in Bengaluru cut (Inventor S40; not re-checked by me) | search summary |
| 71 | Explainer: how to ensure maintenance and safety of your lifts | Citizen Matters | https://citizenmatters.in/explainer-how-to-ensure-maintenance-and-safety-of-your-lifts/ | not shown; retrieved 2026 | 2026-10-31 | Older regime: Chief Electrical Inspector and Lift Inspector sole authority (context only) | search summary |
| 72 | How housing societies can control elevator expenses for their buildings | Free Press Journal | https://www.freepressjournal.in/amp/business/how-housing-societies-can-control-elevator-expenses-for-their-buildings | not shown; retrieved 2026 | 2026-10-31 | Independent elevator consultants (Inventor S43; not re-checked by me) | search summary |
| 73 | Contrat UNIS Avantage ascenseurs (press release) | UNIS Marseille Provence Corse | https://www.unis-immo.fr/app/uploads/2026/04/2026.03.09-CP-UNIS-MPC-Contrat-UNIS-Avantage-ascenseurs.pdf | 2026-03-09 | 2026-10-31 | Results-duty lift contract abroad (Inventor S20; not re-checked by me) | search summary |
