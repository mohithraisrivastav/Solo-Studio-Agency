# Business design 3: Lift safety and AMC accountability for Indian housing societies

Run: 2026-10-31 acceptance test. Role: Business Architect. Inputs: `05-invent-3-lifts.md` (Inventor; commercial claims treated as unverified hypotheses) and `03-market-5-lifts.md` (Market Investigator; best available buyer research, still checked where my design depends on it). I read no other file in the run folder.

Constraints: founder capital Rs 5,00,000; founder time Rs 750 per hour; India first [A] (user-set constraints, not market facts).

## Method, deciding questions and limits

**Deciding questions, set before searching.** These are the questions whose answers could change which model wins. Searches were spent on them first.

| # | Deciding question | Searches | Result in one line |
|---|---|---|---|
| D1 | How does a volunteer committee approve each offer's price, and when does the general body have to vote? | 3 | Committee spends up to a limit the general body sets; above it, tenders go to the general body [S1]. Limits seen: Rs 10,000 to Rs 1-3 lakh [S2][S3][S64]. |
| D2 | What do societies already pay that each price can be anchored to? | 9 | Lift AMC Rs 30,000-1,25,000 per lift a year [S9][S10][S13]; state inspection Rs 1,000-2,000 [S54][S55]; app Rs 5-12 per flat a month [S65]. No price found for independent lift audits, Form B agencies or PMC fees for societies. |
| D3 | Does any Indian federation already run a joint tender or group scheme for members? | 4 | No joint AMC or service tender found; BAF did sponsor a group insurance scheme for domestic workers [S35]. |
| D4 | Can an insurer or broker pay an independent inspector (Lead 2's revenue)? | 2 | Unlikely. Corporate agents may not pay referral fees and brokers were fined for using unlicensed entities [S22][S23][S24]. |
| D5 | What does it cost to reach committees (CAC evidence)? | 5 | Meta CPC about Rs 3-40 and B2B CPL Rs 150-400 (agency blogs) [S30][S31]; a society trade show drew 3,212 societies in 2020 [S32]; app ad rates not published [S28][S29]. |
| D6 | Who can copy each model: lift makers, FM firms, society apps? | 5 | ADDA and MyGate already track AMC renewals [S26][S27]; makers can withdraw comprehensive scope [S15]; no residential FM firm offering AMC procurement found. |
| D7 | Is the Maharashtra trigger real now? | 2 | Yes: the 2017 Act is in force from 1 November 2026 [S17][S18]; an amendment awaits notification [S19]. |
| D8 | Lead-specific costs (indemnity cover, sensor parts, AMC terms) | 6 | PI for engineers not priced [S44][S45]; sensor parts Rs 289-549 each [S46][S47]; institutional AMCs use 2-hour response and Rs 1,000 penalty [S39]. |

- 38 web searches in total. WebFetch was not tried because the Director said it is blocked. Every source was seen only through search-result summaries; I opened no page.
- Arithmetic was done with a short Python script, not by hand. The script is not part of the deliverable; every figure it produced is shown with its inputs.
- Sources from the Inventor's or Investigator's files that I did not re-check are marked "not re-checked by me" in the Sources table.
- Not checked: any buyer's view (evidence stays at L1); full text of any Act, rule, bye-law or IRDAI regulation; the bye-law limit tiers for societies above 25 members; GST registration thresholds; the price of an engineering PI policy; the fee of a retired lift engineer; whether lift makers will bid against each other for society lots; lift modernisation prices; NABCB or state accreditation cost for third-party inspectors.

## 1. Buyer and trigger

### 1.1 How a volunteer committee actually approves spending

- The general body fixes how much the managing committee may spend on repairs and maintenance. A one-time expense above that needs prior general body sanction. For such work the committee must invite tenders, place them before a general body meeting, and only then sign [S1].
- The limit reported for Maharashtra model bye-laws is Rs 1,00,000 for societies with up to 25 members; the higher tiers were cut off in the result [S2]. A Rs 3 lakh figure for 2025-26 is unverified [S3]. One Bengaluru association reportedly needs owner approval above Rs 10,000 [S64].
- The statutory auditor is appointed by the general body from a state panel and paid what the AGM fixes [S6]. So committees already buy one independent professional service each year through the AGM [I].
- Karnataka's 2026 apartment law caps committee terms at two years and sets a general body quorum of 50% of owners [S4]; it passed the Assembly on 21 August 2026 [S5]. I found no expenditure ceiling in it after 1 search.
- Decisions stall. A Maharashtra resident raised rooftop solar at a November 2025 AGM; the committee said it would consult an expert, and it was still unresolved after a February 2026 reminder [S8]. A solar seller says society projects take 12-20 weeks, with permissions a main cause of delay [S7] (seller's claim).
- Committee misconduct is real in large contracts: a Mumbai column reports a committee taking bribes on a redevelopment deal [S50]. No lift-AMC kickback case was found after 1 search, so the risk for Lead 1 is plausible but untested [A].

**What this means for design** [I] (from [S1][S2][S6]): an offer priced below the committee's own limit can be signed by the committee. A new AMC for a 10-lift society at Rs 60,000 a lift is Rs 6 lakh a year [I], above every limit found, so the AMC itself goes to the general body. The seller should hand the committee a ready resolution and time the switch to the AGM or a special general meeting.

### 1.2 Who signs, uses and influences, by concept

| Party | Lead 1: AMC renewal and results contract | Lead 2: independent lift check | Lead 3: power-side recorder |
|---|---|---|---|
| Society committee (secretary, chair, treasurer) | Signs the engagement and the success-fee letter; signs the new AMC after general body sanction [S1][I] | Signs; a 10-lift check at Rs 4,000 a lift is Rs 40,000, inside a Rs 1 lakh limit [S2][I] | Signs; kit priced near the lowest limit found, Rs 10,000 [S64][A] |
| General body | Approves the new AMC when it exceeds the limit [S1] | Needed only where limits are low, such as Rs 10,000 [S64][I] | Rarely needed [I] |
| Federation (BAF, district housing federations, NOFAA) | Endorses the standard contract and hosts sessions; does not sign or pay [A]. BAF has sponsored a group insurance scheme before [S35] | Channel only [A] | Channel only [A] |
| Estate manager or FM firm | Supplies AMC papers and breakdown logs; can help or obstruct [A] | Arranges access [A] | Daily user of alerts [A] |
| Builder | Controls lifts before handover; out of scope until handover [A] | Pre-handover check is a later segment [A] | n/a |
| Insurer or broker | No role | Beneficiary, not payer; cannot legally pay us a referral fee in most structures [S22][S23][S24][I] | No role |
| Lift maker or AMC contractor | Bidder; may resist [A] | Must give access with its technician present [A] | Not involved; nothing touches the lift [I] |

### 1.3 Trigger to buy now

| Concept | Trigger | Frequency | What they compare it with |
|---|---|---|---|
| Lead 1 | AMC renewal due within about 120 days; a renewal price rise; the maker dropping comprehensive cover, as Johnson Lifts did for one society [S15]; AGM budget | Once a year per society [A] | Renewing with the incumbent; asking 2-3 vendors themselves |
| Lead 2 | Maharashtra Act in force from 1 November 2026 [S17]; a local death or FIR [S61][S62]; the July 2026 Supreme Court ruling [S60] | Yearly if renewed [A] | The state inspection at Rs 1,000-2,000 [S54][S55], often not done (about 26% done in Pune) [S63]; the contractor's own report |
| Lead 3 | Repeated outages and disputes over who caused them [A] | Monthly subscription [A] | Guard register, CCTV, app complaint log [S65][A] |

Where AMC is the right lever: in UP the Act ties maintenance to makers or authorised providers [S69], residents complain makers raised prices, and the district administration says it cannot fix rates [S16]. A buyer-side tender has little to work with there [I]. Start in Maharashtra or Karnataka.

## 2. Offer

### Lead 1 (chosen): Lift AMC Renewal Desk

I changed the Inventor's design in four ways. Each change answers a problem found in this run.

1. **One society at a time, pooled when lots form.** The Inventor's version needs 15-30 societies to renew together through a federation. I found no Indian federation running a joint tender after 2 searches, and the Inventor found none after 2 (queries listed after the Sources table). Renewal dates are spread across the year [A]. So each society runs its own tender on the shared standard contract. When 5 or more societies with the same brand in one area renew in the same quarter, the desk tenders them as one lot [A].
2. **Paid entry instead of free.** A free check costs about 3 founder hours, Rs 2,250 [I]. A Rs 5,000 fee filters out committees that are not serious and still sits under the lowest limit found [S64][A].
3. **Fee counted over a 2-year AMC term.** On a 1-year basis the base case needs 10.8% savings to cover founder time; on a 2-year basis it needs 5.4% [I] (Python check, section 6). Two-year fixed-price AMCs must be acceptable to bidders [A].
4. **Monthly fee cut from Rs 200 to Rs 100 per lift.** Rs 200 a lift a month equals 56-133% of what a society pays for its whole society app per 30 flats (Rs 150-360) [I] (from Rs 5-12 per flat [S65]). ADDA and MyGate already send AMC renewal reminders [S26][S27], so a scorecard alone cannot carry a premium price.

**What is sold.**

| Tier | What the society gets | Price, ex GST | Tag |
|---|---|---|---|
| Entry: AMC Health Check | Read AMC, invoices and breakdown log; benchmark price per lift against other societies; scope gaps (comprehensive or not, response time, exclusions); statutory status under the state Act; one-page red-flag list | Rs 5,000 per society | [A] |
| Core: Renewal tender and results contract | Standard contract with 30-minute entrapment response (an Indian institutional AMC uses 2 hours [S39]; an NSW public contract uses 30 minutes [S78]), proven visits, penalties of a set share of the fee [S40], one-month exit [S41]; tender with 3 or more bidders; draft general body resolution; signing support | 30% of verified saving against the incumbent's own renewal quote, counted over the contract term (2 years in base); nothing if no saving | [A] |
| Recurring: Lift Scorecard | QR in each car, 2-minute guard round, contractor check-in; monthly one-page scorecard and penalty credit note | Rs 100 per lift per month | [A] |
| Year 2: Contract compliance check | Yearly site visit by a retired lift engineer that checks the contractor did what the contract says (visits, rescue device, licence, insurance). It does not certify the lift as safe | Rs 1,000 per lift per year | [A] |

Design detail that matters: the baseline is the incumbent's renewal quote received before the engagement, so a maker that matches the best bid to keep the contract still produces a saving and a fee [A]. GST at 18% is added to every fee [A] (standard rate assumed; confirm with a CA).

### Lead 2 (runner-up): Lift Duty-of-Care Check, paid by the society

Changed from the Inventor's "inspect-and-insure": the insurance revenue is removed. IRDAI's corporate-agent code bars paying referral or lead fees [S22]; brokers were fined Rs 1 crore each for using unlicensed people or entities to bring business [S23][S24]; and a broker cannot take both commission and a fee for the same risk-management service [S21]. So the society pays. A broker may still be a free referral channel [I].

- Yearly site check per lift by an engineer, with the contractor's technician present: brakes, ropes, door locks, rescue device, alarm, intercom, pit, machine room, earthing, documents [A] (Inventor's list).
- Red, amber, green report; red list sent to the contractor with a deadline; re-check of red items.
- Price: Rs 4,000 per lift a year plus Rs 1,500 per re-checked lift, ex GST [A]. That is 2-4 times the state fee of Rs 1,000-2,000 [S54][S55][I] and 4.0-13.3% of an AMC of Rs 30,000-1,00,000 [I].

### Lead 3 (third): Society-side lift recorder

- Split-core current clamps and a logger in the society's panel; WhatsApp alerts; monthly duty-of-care report [A] (Inventor's design).
- Kit sold at cost, about Rs 5,000 for a 4-lift panel [A]; subscription Rs 250 per lift a month [A]. Current clamps cost Rs 289-549 each and an ESP32 board about Rs 399 [S46][S47][S48], so clamps plus controller for 4 lifts come to about Rs 1,763-2,635 [I]; modem, enclosure, power supply and voltage tap not priced.

## 3. Price architecture and evidence

**What societies already pay** (all ex GST unless stated).

| Item | Price found | Date, place | Tag | Use in design |
|---|---|---|---|---|
| Society passenger lift AMC | Rs 4,000-8,000 per lift per month, i.e. Rs 48,000-96,000 a year | 2026, Navi Mumbai | [S9][I] | Lead 1 base |
| Same | Rs 1.5-2.5 lakh a year for a two-lift, 60-flat building, i.e. Rs 75,000-1,25,000 per lift | 2026, Pune | [S10][I] | Lead 1 high |
| Same | Rs 30,000-60,000 a year for a typical Bangalore-style residential building (attribution uncertain) | 2026 | [S13] | Lead 1 low |
| Residential lift AMC, all types | Rs 10,000-50,000 a year | date not shown | [S11] | Shows the range is wide |
| Home-lift AMC | Non-comprehensive Rs 20,000-38,500; comprehensive 60-70% more | 2026 | [S12] | Not used for societies |
| Old society data | Rs 45,000 per lift a year | 2012, Dwarka; stale | [S14] | Not used |
| Repairs outside AMC | Rs 15,000-50,000 per incident | date not shown | [S11] | Growth path |
| State lift inspection fee | Rs 1,000-2,000 | Assam schedule, date unclear; Bhopal | [S54][S55] | Lead 2 anchor |
| Society app | Rs 5-12 per flat a month | 2026 | [S65] | Scorecard anchor |
| Society software, one vendor | Rs 10 per flat a month | date not shown | [S58][A] | Scorecard anchor (attribution uncertain, see Sources) |
| PMC fee ceiling, one bank redevelopment | Up to 3% of project cost | 2026, SBI (attribution uncertain) | [S56] | Modernisation tender fee |
| Housing society package insurance | Rs 30,000-60,000 a year for about 50 flats | 2026, blog | [S25] | Context for Lead 2 |
| Lift liability insurance | Rs 3 per mille of the annual limit (one insurer, undated) | undated | [S70] | Not re-checked; no other premium found after 1 search |
| Independent lift auditor fee | Not found after 2 searches by me and 3 by the Investigator | n/a | n/a | Lead 2 price is untested |
| Fire Form B agency fee | Not found after 2 searches | n/a | n/a | Precedent exists, price unknown |

**Contradiction.** AMC sources disagree by about 4 times at the low end (Rs 30,000 against Rs 1,25,000 a lift) [S9][S10][S13][I]. All are blogs. I use Rs 60,000 as base, not the Inventor's Rs 80,000, because two of three society sources sit at or below it [I]. Confidence low.

**Lead 1 price logic.** At base (10 lifts, Rs 60,000, 8% saving, 30% share, 2-year term) the success fee is Rs 28,800, about 4.8% of one year's AMC [I]. The society keeps 70% of the saving: Rs 67,200 over two years [I]. The fee is paid out of money the society would otherwise have paid the contractor, so it adds no new budget line [I]. The entry fee of Rs 5,000 sits under the lowest committee limit found [S64].

**Lead 2 price logic.** Rs 4,000 a lift has no observed anchor except the state fee, which is lower [S54][S55]. Societies do pay licensed agencies for mandated fire Form B twice a year [S53], but even that mandated duty is widely skipped: about 2,700 Mumbai buildings received notices [S52], and a headline says only 40,000 Maharashtra housing complexes file fire reports [S51] (headline only). Voluntary payment for a lift check is untested [I].

**Lead 3 price logic.** Rs 250 a lift a month is 69-167% of a society's whole app cost per 30 flats (Rs 150-360) [I] (from [S65]). KALA already sells non-invasive monitoring by subscription in India; its price was not found after 1 search [S49].

## 4. Route to market: first 10 customers, first 100 customers

### Lead 1 (chosen)

**Where.** Pune first, then Bengaluru, or whichever of the two the founder lives in [A]. Reasons: the Maharashtra Act is in force from 1 November 2026 [S17]; Maharashtra bye-laws already push above-limit work to tender [S1]; the Pune district housing federation's chairman says 18,000+ societies are registered with it (attribution uncertain) [S37], and model bye-laws require societies to affiliate with their district federation [S38]; Bengaluru has BAF with 1,400+ member associations [S36] and a reported 38% of lifts with third-party maintainers in one survey cut [S71]. Not UP, because the law ties AMCs to makers [S69][S16].

**First 10 paying societies** (success fee earned, not just a health check).

| Step | Weeks | What | Cost | Tag |
|---|---|---|---|---|
| 1 | 1-4 | Lawyer drafts the standard results contract and engagement letter; build the benchmark sheet; sign up one retired lift engineer per visit | Rs 50,000 lawyer; Rs 30,000 QR, bot and site | [A] |
| 2 | 2-10 | 2 federation or cluster sessions, society WhatsApp groups, and direct visits to about 40 societies with 8 or more lifts; book 25 health checks (first 5 free as references, rest Rs 5,000) | Founder time; travel | [A] |
| 3 | 4-20 | Pick the health-check societies renewing within 120 days; run tenders with 3 or more bidders; present to the general body | Rs 2,000 engineer visit per tender client | [A] |
| 4 | By month 6-9 | 10th signed AMC with a verified saving | n/a | [A] (renewal dates spread across the year) |

Proof committees need before paying: a benchmark built from at least 20 real society contracts; a contract a lawyer has vetted; named bidders with registration; fee only on saving; 2-3 reference societies [A].

**First 100.** Months 9-30 [A]. Channels in order:

| Channel | Fee or margin it takes | Sales cycle | Proof needed | Tag |
|---|---|---|---|---|
| Federation endorsement of the standard contract (BAF, district housing federations) | No fee found; budget 0-5% sponsorship | Months to agree; then each session yields bookings | Track record from the first 10 | [A]; precedent of a federation-sponsored scheme [S35] |
| Estate manager and FM referral | 10% of first-year fees | Weeks | Clear disclosure to the committee to avoid a kickback look | [A] |
| Society trade show (HSMS, Mumbai) | Stall price not found; a Mumbai shell-scheme proxy is Rs 11,000 per sq m, 9 sq m minimum, plus 18% GST, about Rs 1,16,820 | 3 days plus follow-up | Case studies | [S34][I]; the 2020 show drew 3,212 societies, 85% decision makers, with 87 exhibitors [S32] |
| MyGate or NoBrokerHood pincode ads | Rate card not published | Weeks | Case studies | [S28][S29] (27,000+ and 25,000+ societies, self-reported) |
| Meta ads to committee members | CPC about Rs 3-40; B2B CPL Rs 150-400 (agency blogs) | Weeks | Saving calculator | [S30][S31] |

Capacity limit: at base hours a solo founder can win about 3 new tender clients a month, about 38 a year [I] (120 productive hours a month [A] ÷ 37.6 hours per client [I]). 100 societies therefore needs either a junior analyst by about month 18 [A] or hours per client falling toward the high case of 20.7 hours (about 70 a year) [I].

Sales cycle overall: 2-9 months from first contact to the success fee, driven by the renewal date and the general body meeting [A]. Test it by recording the next AGM and renewal date of every health-check society.

### Lead 2 (runner-up)

- Where: Pune and Mumbai, launched with the Maharashtra Act start [S17]. Offer 10 committees a check in November-December 2026 [A].
- First 10: 100 pitches at a 10% conversion [A]; brokers asked to refer clients for free [I] (they cannot pay us [S22][S23]).
- First 100: limited by engineer hours. At 4 lifts a day [A] and 10 lifts a society, one engineer covers about 2.5 days per society [I]; 100 societies a year needs about 250 engineer-days [I].
- If Maharashtra notifies third-party lift inspection (planned, not notified [S67]), apply for accreditation [A]. TÜV SÜD already has lift inspection accreditation in India [S68], so a small firm would compete with it.

### Lead 3

- First 10: 10 lifts in 3 societies as a 6-week accuracy test with guard logs as ground truth [A] (Inventor's test). No revenue route should be scaled before that test passes [I].

## 5. Customer acquisition cost estimate

No CAC benchmark exists for selling to Indian housing committees; none was found after the searches listed after the Sources table. These are built from the few sourced costs above, sales hours at Rs 750 [A], and assumed conversion rates [A]. They are estimates, not benchmarks.

**Lead 1: cost per health-check customer, by channel.**

| Channel | Build | Range per health check | Tag |
|---|---|---|---|
| Federation or cluster session | 8 founder hours plus Rs 1,000 travel, yielding 1-6 bookings | Rs 1,167-7,000; base Rs 2,333 at 3 bookings | [I] (hours and yield [A]) |
| Meta ads | CPL Rs 150-400 [S30][S31]; 2-10% of leads book [A]; 2 follow-up hours | Rs 3,000-21,500 | [I] |
| Trade show | Stall proxy Rs 1,16,820 [I from S34], 30 hours, Rs 10,000 collateral and travel [A]; 10-40 bookings [A] | Rs 3,733-14,932 | [I] |
| Cold visits to society offices | 1 hour per society; 5-10% book [A] | Rs 7,500-15,000 | [I] |

**Blended inputs used in the model:** 3/5/10 sales hours plus Rs 1,000/2,000/4,000 cash per health-check customer [A], i.e. Rs 3,250 / Rs 5,750 / Rs 11,500 [I]. Dividing by the health-check-to-tender conversion of 60% / 40% / 20% [A] gives **CAC per tender client of Rs 5,417 (best), Rs 14,375 (base), Rs 57,500 (worst)** [I].

**Lead 2: CAC per paying society.** 1/2/3 sales hours per society pitched [A], conversion 20% / 10% / 5% [A], plus Rs 1,000 / 3,000 / 8,000 cash [A]: **Rs 4,750 (best), Rs 18,000 (base), Rs 53,000 (worst)** [I].

Confidence: low. Every conversion rate is an assumption. The first 30 conversations will replace them.

## 6. Business model comparison and choice

**Per-society check** (Python; inputs are the section 10 values; founder time at Rs 750 an hour [A]). Year 1 includes the society's share of acquisition cost and of unconverted health checks.

| Measure | Lead 1 low | Lead 1 base | Lead 1 high | Lead 2 low | Lead 2 base | Lead 2 high | Lead 3 base (4-lift site) |
|---|---|---|---|---|---|---|---|
| Year-1 revenue [I] | Rs 2,430 | Rs 48,500 | Rs 1,95,767 | Rs 16,800 | Rs 47,500 | Rs 1,14,000 | Rs 17,000 |
| Founder hours, year 1 [I] | 93.6 | 37.6 | 20.7 | 64 | 44 | 35.5 | 20 |
| Year-1 contribution after founder time [I] | -Rs 91,134 | Rs 8,450 | Rs 1,77,550 | -Rs 44,600 | Rs 8,800 | Rs 84,975 | -Rs 7,880 |
| Year-2 contribution (expected) [I] | -Rs 2,472 | Rs 1,788 | Rs 30,232 | -Rs 2,640 | Rs 16,080 | Rs 74,780 | not run |

All figures in the table above are [I] from section 10 inputs, mostly [A].

Reading [I]: both leads are negative in their low case and modestly positive in base. Lead 2 earns more per society over two years in base (Rs 24,880 against Rs 10,238) because its fee repeats yearly. Lead 1's base case breaks even only if savings reach 5.4% on a 2-year fee basis, or 10.8% on a 1-year basis. Lead 3 is negative in base.

**Model comparison.**

| Model | Capital needed before first fee | Margin | Founder dependence | Scalability | Main risk |
|---|---|---|---|---|---|
| A. Lead 1: success-fee procurement plus scorecard | About Rs 1.45 lakh [I] (lawyer, bot, PI, 6 months fixed costs, 10 engineer visits, all [A]) | Service margin high; thin per society in base [I] | High; needs negotiation skill, not an engineering licence [A] | Medium: benchmark data and lots improve with each society [I] | Savings smaller than 5.4%; makers refuse to bid or withhold parts [S15][S42] |
| B. Lead 2: fixed-fee inspection | About Rs 1.45 lakh if the founder is a lift engineer; about Rs 4.45 lakh with a hired engineer for 6 months [I] | Good per society once renewed [I] | Very high; needs a qualified engineer [A] | Linear in engineer-days [I] | Inspector named after an accident; voluntary demand unproven; state hiring 519 inspectors could shrink the gap [S67] |
| C. Lead 3: hardware plus subscription | Rs 60,000 for a 10-lift pilot [A]; 100 kits at Rs 5,000 would use all Rs 5 lakh [I] | Negative in base year 1 [I] | Medium | High if the signal works [A] | Signal ambiguity; KALA exists [S49]; parts cheap to copy [I] |
| D. Prime AMC contractor (sell guaranteed uptime) | Above Rs 5 lakh for technicians, spares and cover [A] | Unknown | Very high | Medium | Carries failure risk; Otis took a majority stake in WeMaintain, an independent maintainer, in April 2026 [S75] |
| E. Licence the benchmark and standard contract to apps or FM firms | Low [A] | High if it sells [A] | Low | High | Needs the data asset first; apps could build it themselves [S26][S27] |

**Choice: A (Lead 1), redesigned as the Lift AMC Renewal Desk. Runner-up: B (Lead 2).** Confidence low.

Why A over B, even though B earns more per society in base [I]:
1. Bounded downside. A has no safety-certification liability; B can see its inspector named in an FIR, as office-bearers, makers and maintenance firms have been [S61][I]. Engineering PI cover was not priced [S44][S45].
2. No licence needed. A needs a part-time engineer per visit; B needs a qualified lift engineer full time, which costs Rs 3 lakh of the Rs 5 lakh for 6 months if hired [I].
3. Price anchored to spend that already exists. A's fee comes out of the AMC saving [I]; B's fee is 2-4 times a state fee that most lifts skip [S54][S63][I].
4. It builds an asset. Each society adds a real contract to the benchmark, which raises later win rates and opens model E [A].

What would flip the choice to B: the first 10 health checks show median savings below 5% [A], or Maharashtra notifies third-party inspection with a fee schedule [S67]. The test in section 4 settles the first within about 6 months [A].

## 7. Operations and capacity

**Lead 1, a founder's typical week** [A]:
- 3 days in the field: 2 health checks or general body presentations a day.
- 1 day on tenders: bid packs, bidder calls, comparison sheets, contract redlines.
- Half a day on scorecards and credit notes (automated WhatsApp bot plus a spreadsheet).
- Half a day on channel work: one federation session a month, estate-manager calls.

**Outsourced** [A]: lawyer for the contract (one-off) and disputes; retired lift engineer per visit for scope checks and the year-2 compliance check; CA for GST; freelance developer for the bot.

**Capacity** [I]: about 120 productive hours a month [A] gives about 3.2 new tender clients a month at 37.6 hours each, or 5.8 at the high case of 20.7 hours.

**Working capital** [A]: no inventory. Base assumes the whole 2-year success fee is billed in year 1, half when the new AMC is signed and half after 3 months of contractor compliance. Committees may insist on paying year by year; then half the success fee moves into year 2 (same 2-year total, later cash) [I]. Receivables 30-90 days; health-check fee paid upfront. The main cash need is founder time before the first fees (3-9 months).

**Lead 2** [A]: one engineer inspects 4 lifts a day (Inventor's estimate); November-March demand peak if the Act drives it; PI cover and written scope limits before the first visit.

## 8. Defensibility

What stops a copier within 12 months, for the chosen model:

| Copier | What it can do | What limits it | Tag |
|---|---|---|---|
| Lift maker (Otis, KONE, Johnson) | Match the best bid at renewal; refuse to bid; withdraw comprehensive cover, as Johnson did for one society [S15]; withhold parts from independents, as alleged in Singapore [S42]; argue for OEM-only maintenance [S43] | A maker cannot credibly run a tender against itself [I]. Matching the bid still pays the desk's fee because the baseline is the maker's own renewal quote [A]. India's competition regulator fined car makers for restricting spare parts [S77], a route to complain but not a fast one [I] | [S15][S42][S43][I] |
| FM firm | Offer "AMC procurement" free as part of its contract | Its independence is weak where it earns from vendor ties [A]; it lacks multi-society price data unless large [A]. No residential FM firm offering this was found after 1 search | [A] |
| Society apps (ADDA, MyGate, NoBrokerHood) | Already store AMCs and send renewal reminders [S26][S27]; reach 25,000-27,000 societies each (self-reported) [S28][S29]; could publish benchmarks | They sell to the same committees and avoid fights with vendors who advertise on them [A]. Treat them as a distribution partner, not a target | [S26][S27][A] |
| Independent consultants | Already advise some Mumbai societies [S73] | Few, local, and none found offering a success-fee model [A] | [S73][A] |

**Moat sources** [A]: the benchmark from real contracts (grows with each society); the federation-endorsed standard contract; a record of penalties actually collected; committee trust. **Overall 12-month defensibility: low to medium** [I]. The data moat needs about 50-100 contracts before it is hard to copy [A].

For Lead 2 [I]: makers cannot credibly inspect lifts they maintain (France requires its lift control to be independent of owner and maintainer [S76]); TÜV SÜD [S68] and the state's planned 519 new posts [S67] are the real threats. Low.

For Lead 3 [I]: parts cost about Rs 1,763-2,635 per 4-lift panel [I], KALA is in the market [S49], and patents exist (Inventor's file). Low.

## 9. Repeat revenue and growth path

**What brings the society back (Lead 1)** [A]:
- Scorecard every month; year-2 compliance check; re-tender at the end of each 2-year term.
- Repair-quote review for out-of-AMC repairs of Rs 15,000-50,000 per incident [S11], at 20% of the reduction [A].

**Next products, same buyer** [A]:
- Lift modernisation tenders for 15-20-year-old lifts (Mumbai societies already use audits for this [S74]) at about 2% of project value, under the 3% PMC ceiling seen at one bank [S56]. Modernisation prices were not checked.
- AMC tenders for DG sets, pumps and fire systems; fire Form B is mandatory twice a year from licensed agencies [S53].
- Handover audits for new associations (Inventor's concept 9).

**Next segments** [A]: commercial buildings, hospitals and schools, where institutional AMCs already include response times and penalties [S39][S40]; licensing the benchmark to an app or FM firm (model E).

## 10. Inputs for the financial model

Read this first:
- All money is INR, ex GST. Add GST at 18% on fees [A] (standard rate; confirm with a CA).
- Values run from low to high. For revenue items the low value is conservative. For hours, costs, fees paid out and time to first fee, the **high** value is conservative.
- Founder time is valued at Rs 750 an hour [A] (user constraint).
- Almost every input is an assumption. The Financial Investigator should treat the low column as a plausible outcome, not a stress case.

### 10.1 Chosen concept: Lead 1, Lift AMC Renewal Desk

| Item | Low | Base | High | Unit | Currency | Basis tag |
|---|---|---|---|---|---|---|
| Lifts per paying society (targeting societies with 8+ lifts) | 6 | 10 | 15 | lifts | n/a | [A] basis: about 1 lift per 30 flats in a Pune example [S10]; test: count in the first 20 health checks |
| Current AMC per lift per year | 30,000 | 60,000 | 1,00,000 | per lift per year | INR | [S9][S10][S13] (blogs, 2026; low confidence) |
| Saving against the incumbent's renewal quote | 3% | 8% | 15% | of annual AMC | % | [A] basis: US consultant claims 10-15% [S66]; no Indian figure found |
| Years of saving counted in the success fee | 1 | 2 | 2 | years | n/a | [A] needs bidders to accept 2-year fixed prices |
| Share of the 2-year success fee billed in year 1 | 50% | 100% | 100% | of success fee | % | [A] design choice; low case = committees pay year by year |
| Success fee share of verified saving | 25% | 30% | 35% | of saving | % | [A] Inventor's 30%; no Indian benchmark found |
| Health check price per society | 0 | 5,000 | 10,000 | per society | INR | [A] capped at the lowest committee limit found, Rs 10,000 [S64] |
| Health check to tender conversion | 20% | 40% | 60% | of health checks | % | [A] |
| Scorecard price | 50 | 100 | 150 | per lift per month | INR | [A] below an app's Rs 150-360 per 30 flats a month [I from S65] |
| Scorecard uptake among tender clients | 30% | 60% | 80% | of tender clients | % | [A] |
| Scorecard retention into year 2 | 60% | 80% | 90% | of scorecard clients | % | [A] |
| Year-2 compliance check price | 0 | 1,000 | 2,000 | per lift per year | INR | [A] anchored to state fees Rs 1,000-2,000 [S54][S55] |
| Year-2 compliance check uptake | 0% | 50% | 70% | of tender clients | % | [A] |
| Founder hours per health check | 2 | 3 | 4 | hours | n/a | [A] Inventor's 2 hours plus report |
| Founder hours per tender client, year 1 (tender, bids, general body, signing) | 10 | 14 | 20 | hours | n/a | [A] |
| Founder hours per scorecard client | 0.25 | 0.5 | 1 | hours per month | n/a | [A] |
| Founder sales hours per health-check customer won | 3 | 5 | 10 | hours | n/a | [A] section 5 |
| Cash acquisition cost per health-check customer (travel, ads, events) | 1,000 | 2,000 | 4,000 | per health check | INR | [I] section 5 from [S30][S31][S34] and [A] conversions |
| CAC per tender client, all-in (hours at Rs 750 plus cash, ÷ conversion) | 5,417 | 14,375 | 57,500 | per tender client | INR | [I] section 5 |
| Referral or federation share of first-year fees | 0% | 10% | 15% | of first-year fees | % | [A] |
| Retired lift engineer, scope check | 1,000 | 2,000 | 3,000 | per tender client | INR | [A] not checked |
| Engineer cost per year-2 compliance check | 300 | 500 | 800 | per lift | INR | [A] not checked |
| Founder hours per lift for the compliance check (coordination and report) | 0.5 | 0.75 | 1 | hours | n/a | [A] |
| One-time: lawyer for standard contract and terms | 30,000 | 50,000 | 1,00,000 | one-time | INR | [A] Inventor's estimate, not checked |
| One-time: QR stickers, WhatsApp bot, one-page site | 15,000 | 30,000 | 50,000 | one-time | INR | [A] |
| Fixed: software, phone, WhatsApp API, base travel | 3,000 | 5,000 | 8,000 | per month | INR | [A] |
| Professional indemnity cover | 5,000 | 15,000 | 40,000 | per year | INR | [A] basis: Rs 1 crore cover advertised "from" Rs 1,731 [S44]; doctors Rs 3,150-12,000 [S45]; no engineering quote |
| Health checks booked at steady state (solo founder) | 2 | 5 | 8 | per month | n/a | [A] capacity about 3.2 tender clients a month at base hours [I] |
| Months from launch to first success fee | 3 | 5 | 9 | months | n/a | [A] |
| Receivable days | 30 | 45 | 90 | days | n/a | [A] |
| Success fees lost to disputes | 5% | 10% | 20% | of billed success fees | % | [A] |
| GST on fees | 18% | 18% | 18% | of fee | % | [A] standard rate assumed |

### 10.2 Runner-up: Lead 2, Lift Duty-of-Care Check

| Item | Low | Base | High | Unit | Currency | Basis tag |
|---|---|---|---|---|---|---|
| Lifts per paying society | 6 | 10 | 15 | lifts | n/a | [A] as Lead 1 |
| Check fee | 2,500 | 4,000 | 6,000 | per lift per year | INR | [A] above state fees of Rs 1,000-2,000 [S54][S55] |
| Re-check fee | 1,000 | 1,500 | 2,000 | per re-checked lift | INR | [A] Inventor's figure |
| Share of lifts needing a re-check | 30% | 50% | 80% | of lifts | % | [A] |
| Engineer hours per lift (travel, check, report) | 1.5 | 2 | 3 | hours | n/a | [A] Inventor's 2 hours |
| Committee meeting and report hours per society | 3 | 4 | 6 | hours | n/a | [A] |
| Pitch-to-paid conversion | 5% | 10% | 20% | of societies pitched | % | [A] |
| Sales hours per society pitched | 1 | 2 | 3 | hours | n/a | [A] |
| Cash acquisition cost per paying society | 1,000 | 3,000 | 8,000 | per society | INR | [A] |
| CAC per paying society, all-in | 4,750 | 18,000 | 53,000 | per society | INR | [I] section 5 |
| Yearly renewal rate | 40% | 60% | 80% | of clients | % | [A] |
| Insurance commission or broker fee | 0 | 0 | 0 | per society | INR | [I] from IRDAI rules [S21][S22][S23][S24] |
| Hired engineer salary (if the founder is not a lift engineer) | 40,000 | 50,000 | 70,000 | per month | INR | [A] Inventor's figure, not checked |
| Lifts one engineer checks per day | 3 | 4 | 5 | lifts per day | n/a | [A] Inventor's figure |
| Professional indemnity cover | 10,000 | 25,000 | 60,000 | per year | INR | [A] basis as Lead 1; inspection liability is higher [I] |
| One-time: tools, checklist, legal terms | 60,000 | 90,000 | 1,50,000 | one-time | INR | [A] Inventor's Rs 1.5 lakh start-up estimate |
| Travel per site visit (2 visits per society) | 300 | 600 | 1,200 | per visit | INR | [A] |
| Fixed: software, phone, base travel | 3,000 | 5,000 | 8,000 | per month | INR | [A] |
| Paying societies won at steady state | 1 | 3 | 5 | per month | n/a | [A] |
| Months to first paid check | 1 | 2 | 4 | months | n/a | [A] timed to the Act's start [S17] |
| GST on fees | 18% | 18% | 18% | of fee | % | [A] |

## 11. Risks

| # | Risk | Concept | Severity | Evidence | Mitigation and test |
|---|---|---|---|---|---|
| 1 | Savings smaller than the 5.4% break-even | Lead 1 | Fatal if true | No Indian saving data; US claim 10-15% [S66] | First 10 health checks: median gap to benchmark of 8% or more; first 3 real tenders [A] |
| 2 | Makers refuse to bid, or independents cannot get parts | Lead 1 | High | Johnson withdrew comprehensive cover for one society [S15]; Singapore parts case [S42]; UP law [S69] | Start outside UP; lots by brand; confirm 3 bidders before promising a tender [A] |
| 3 | Committees prefer the incumbent (ties, inertia, "knowing creates duty") | Lead 1, 2 | High | Committee bribery reported in redevelopment [S50]; solar decisions stall [S8] | Fee only on saving; resolution draft for the general body; record refusals and reasons [A] |
| 4 | Sales cycle tied to renewal and AGM dates | Lead 1 | Medium | General body sanction above the limit [S1] | Pipeline built on renewal dates; health-check fee covers early hours [A] |
| 5 | Society apps add benchmarks and scorecards | Lead 1 | Medium | ADDA, MyGate already track AMCs [S26][S27] | Partner with one app for distribution; keep contract data proprietary [A] |
| 6 | Inspector named after an accident | Lead 2 | Fatal for a solo firm | FIRs name office-bearers, makers and maintainers [S61][S62] | Scope as condition-at-visit, not certification; PI cover before first visit; get a PI quote first [A] |
| 7 | No insurance revenue | Lead 2 | Settled | IRDAI rules [S21][S22][S23][S24] | Design already removes it [I] |
| 8 | State fills the inspection gap | Lead 2 | Medium | 519 new posts planned in Maharashtra [S67] | Watch the rules under the Act [S17][S19] |
| 9 | Signal ambiguity and false alerts | Lead 3 | High | Inventor's analysis | 10-lift accuracy test before any sale [A] |
| 10 | AMC prices lower than assumed | Lead 1 | High | Sources range Rs 30,000-1,25,000 [S9][S10][S13] | Target societies with 8+ lifts and Rs 50,000+ per lift [A] |

Top three uncertainties for the decision:
1. Achievable saving on a like-for-like renewal (decides Lead 1's economics) [A].
2. Whether committees pay any outside fee for lifts without a mandate (decides both leads) [A].
3. Founder hours per client, which dominate cost at Rs 750 an hour [I].

## 12. Sources

All rows retrieved 2026-10-31. I opened no page; every row is "search summary". Rows marked "not re-checked by me" come from the Inventor's (`05`) or Investigator's (`03`) files and are used as reported there. Searches that found nothing are listed after the table.

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Model bye-laws of cooperative housing society: maintenance accounts | MySocietyClub | https://mysocietyclub.com/bye-laws/maharashtra-cooperative-housing-society-bye-laws/maintenance-accounts | not shown; retrieved 2026-10-31 | 2026-10-31 | Committee repair limit set by general body; tenders above it placed before the general body (re-checked with my own query; also Investigator S57) | search summary |
| 2 | Mumbai housing society queries | Free Press Journal | https://www.freepressjournal.in/mumbai/clone-of-mumbai-housing-society-queries-can-societies-interview-flat-buyers-know-the-rules | not shown; retrieved 2026-10-31 | 2026-10-31 | Rs 1,00,000 limit for societies up to 25 members (attribution among several FPJ copies uncertain) | search summary |
| 3 | New bylaws of housing society Maharashtra | NoBrokerHood | https://www.nobrokerhood.com/blog/new-bylaws-of-housing-society-maharashtra/ | 2025-26 | 2026-10-31 | Claimed Rs 3 lakh limit (unverified) | search summary |
| 4 | Karnataka's new apartment bill explained | The News Minute | https://www.thenewsminute.com/karnataka/karnatakas-new-apartment-bill-explained-what-changes-for-flat-owners | 2026 | 2026-10-31 | Two-year committee term; 50% quorum | search summary |
| 5 | Karnataka Assembly passes apartment ownership bill | The News Minute | https://www.thenewsminute.com/amp/story/karnataka/karnataka-assembly-passes-apartment-ownership-bill-amid-bjp-jds-protest | 2026-08 | 2026-10-31 | Passed 21 August 2026 | search summary |
| 6 | Audit of co-operative housing and credit societies in Maharashtra | Taxguru | https://taxguru.in/finance/audit-of-co-operative-housing-credit-societies-in-maharashtra.html | not shown; retrieved 2026-10-31 | 2026-10-31 | General body appoints auditor from panel and fixes fee at AGM (attribution among results uncertain) | search summary |
| 7 | Eligibility and documentation to install solar for housing societies | SolarSquare | https://www.solarsquare.in/blog/eligibility-and-documentation-to-install-solar-for-housing-societies/ | not shown; retrieved 2026-10-31 | 2026-10-31 | AGM or committee resolution; 12-20 weeks (seller's claim; attribution among SolarSquare pages uncertain) | search summary |
| 8 | Denial of rooftop solar installation by housing society | Kaanoon | https://www.kaanoon.com/498425/denial-of-rooftop-solar-installation-by-housing-society | 2026 | 2026-10-31 | Committee delay after AGM, Nov 2025 to Feb 2026 | search summary |
| 9 | Society maintenance charges in Navi Mumbai 2026 | navimumbai.com | https://navimumbai.com/?p=5471 | 2026 | 2026-10-31 | Rs 4,000-8,000 per lift a month (also Investigator S33) | search summary |
| 10 | Pune property maintenance charges guide 2026 | Pune Reality Hub | https://punerealityhub.pages.dev/blog/pune-property-maintenance-charges-guide-2026 | 2026 | 2026-10-31 | Rs 1.5-2.5 lakh a year for two lifts, 60 flats (also Investigator S34) | search summary |
| 11 | Elevator maintenance checklist | NoBrokerHood | https://www.nobrokerhood.com/blog/elevator-maintenance-checklist/ | not shown; retrieved 2026-10-31 | 2026-10-31 | Rs 10,000-50,000 a year; repairs Rs 15,000-50,000 per incident | search summary |
| 12 | Lift AMC evaluation guide India | Studio Matrx | https://www.studiomatrx.org/guides/lift-amc-evaluation-guide-india | 2026 | 2026-10-31 | Home-lift non-comprehensive Rs 20,000-38,500; comprehensive 60-70% more | search summary |
| 13 | Lift installation cost India residential 2026 | Aecord | https://aecord.com/blog/lift-installation-cost-india-residential-2026 | 2026 | 2026-10-31 | Rs 30,000-60,000 a year for a Bangalore-style building (attribution among results uncertain) | search summary |
| 14 | Info request: OTIS lift AMC | dwarka-residents Google Group | https://groups.google.com/g/dwarka-residents/c/EIce9AlzmhQ | 2012 | 2026-10-31 | Rs 45,000 per lift a year (stale) | search summary |
| 15 | Lift modernisation proposal - Johnson Lifts | srishti-owners Google Group | https://groups.google.com/g/srishti-owners/c/aY3QuvdTo9c | 2022 | 2026-10-31 | Johnson unable to continue comprehensive (platinum) AMC; society moved to labour-only Gold | search summary |
| 16 | Noida administration meets lift manufacturers over maintenance costs under new Act | Homzcare | https://homzcare.in/?p=19365 | not shown (c. Dec 2024) | 2026-10-31 | Administration cannot fix rates; NOFAA monopoly fear; makers raised prices | search summary |
| 17 | Maharashtra brings Lift and Escalator Safety Regime into force from 1 November | SCC Online | https://www.scconline.com/blog/?p=399876 | 2026-10 | 2026-10-31 | Act in force 1 Nov 2026, notified 22 Oct 2026 (re-checked; also Inventor S48) | search summary |
| 18 | Commencement of the Lifts, Escalators and Moving Walks Act, 2017 | TeamLease RegTech | https://teamleaseregtech.com/updates/article/60738/government-of-maharashtra-commencement-of-the-lifts-escalators-and-mov/ | 2026-10 | 2026-10-31 | Commencement notification | search summary |
| 19 | Maharashtra Lifts, Escalators and Moving Walks (Amendment) Bill, 2026 | PRS India | https://prsindia.org/files/bills_acts/bills_states/maharashtra/2026/Bill7of2026MH.pdf | 2026-03 | 2026-10-31 | Passed 5 and 12 March 2026; commencement by notification; contents not seen | search summary |
| 20 | Great move toward safety | Elevator World | https://elevatorworld.com/?p=49622 | not shown (c. 2018) | 2026-10-31 | Owner to ensure third-party insurance (status in enacted text unclear) | search summary |
| 21 | IRDAI (Insurance Brokers) Regulations 2018 | Department of Financial Services | https://financialservices.gov.in/beta/sites/default/files/2024-11/IRDAI%20(Insurance%20Brokers)%20Regulations%202018.pdf | 2018 | 2026-10-31 | Broker cannot take both remuneration and a fee for the same risk-management service; written mandate (as summarised; attribution among results uncertain) | search summary |
| 22 | Key notes: general insurer, corporate agency and remuneration | Mondaq | https://mondaq.co.uk/india/insurance-laws-and-products/822978/key-notes-general-insurer-|-corporate-agency-and-remuneration--commission | not shown; retrieved 2026-10-31 | 2026-10-31 | Corporate agents may not pay referral or lead-generation fees (attribution among results uncertain) | search summary |
| 23 | IRDAI imposes Rs 1 crore penalty on Muthoot Risk Insurance and Broking Services | Moneylife | https://moneylife.in/article/irdai-imposes-rs1-crore-penalty-on-muthoot-risk-insurance-and-broking-services-for-selling-insurance-through-unqualified-bdms/63472.html | not shown; retrieved 2026-10-31 | 2026-10-31 | Unlicensed solicitation penalised | search summary |
| 24 | D2C Insurance Broking penalised Rs 1 crore by IRDAI | Moneylife | https://moneylife.in/article/d2c-insurance-broking-penalised-rs1-crore-by-irdai-also-gets-warning-for-running-renewbuycom/64578.html | not shown; retrieved 2026-10-31 | 2026-10-31 | Broker penalised for using unlicensed entities to bring business | search summary |
| 25 | ICICI Lombard housing society insurance review for RWAs 2026 | constructionestimatorindia.com | https://constructionestimatorindia.com/?p=9856 | 2026 | 2026-10-31 | Rs 30,000-60,000 a year for about 50 flats (blog) | search summary |
| 26 | As an admin, how can I manage asset AMCs on ADDA? | ADDA | https://support.adda.io/portal/en/kb/articles/as-an-admin-how-can-i-manage-asset-amcs-on-adda | not shown; retrieved 2026-10-31 | 2026-10-31 | AMC module and expiry reminders | search summary |
| 27 | How do I set up AMC renewal reminders for my assets? | MyGate | https://adminfaq.mygate.com/articles/130339-how-do-i-set-up-amc-renewal-reminders-for-my-assets-added-in-mygate | not shown; retrieved 2026-10-31 | 2026-10-31 | AMC renewal reminders | search summary |
| 28 | Mygate ad platform | MyGate | https://mygate.in/ad-platform/ | not shown; retrieved 2026-10-31 | 2026-10-31 | Pincode targeting; 27,000+ societies (self-reported); no rate card | search summary |
| 29 | Advertise with NoBrokerHood | NoBrokerHood | https://www.nobrokerhood.com/advertise/ | not shown; retrieved 2026-10-31 | 2026-10-31 | 25,000+ societies (self-reported); no rate card | search summary |
| 30 | Paid social ads benchmarks India and Southeast Asia 2026 | Sotros Infotech | https://sotrosinfotech.com/blog/paid-social-ads-benchmarks-india-southeast-asia-2026/ | 2026 | 2026-10-31 | Meta CPC and B2B CPL ranges (agency blog; attribution among several blogs uncertain) | search summary |
| 31 | Meta ads benchmarks India | Owlclaw | https://owlclaw.com/benchmarks/meta-ads-benchmarks-india | 2025 | 2026-10-31 | Meta CPC ranges (agency blog) | search summary |
| 32 | Housing Society Management Show 2020 ends on a high note | Kashmir Pulse | https://kashmirpulse.com/business-economy/housing-society-management-show-2020-ends-on-a-high-note/38529.html | 2020-02 | 2026-10-31 | 87 exhibitors, 1,350 sq m, 3,212 societies, 85% decision makers | search summary |
| 33 | Housing Society Management Show 2025 | ghar.tv | https://ghar.tv/events/view/housing-society-management-show-2025-bandra-east-mumbai-eid78198 | 2025 | 2026-10-31 | 350+ exhibitors, 15,000+ visitors (listing) | search summary |
| 34 | Venue and rates, Mumbai | Gartex India | https://www.gartexindia.com/?p=3281 | not shown; retrieved 2026-10-31 | 2026-10-31 | Shell scheme Rs 11,000 per sq m, 9 sq m minimum, plus 18% GST (other industry, proxy only) | search summary |
| 35 | Bangalore Apartments' Federation to launch health insurance for domestic workers | Citizen Matters | https://citizenmatters.in/bangalore-apartments-federation-baf-group-health-insurance-domestic-workers-bamboos/ | not shown; retrieved 2026-10-31 | 2026-10-31 | Federation-sponsored group scheme (MADHURA); uptake not found | search summary |
| 36 | BAF urges govt to table, implement Karnataka Apartment Ownership Act | Devdiscourse (IANS) | https://www.devdiscourse.com/article/politics/3717296-baf-urges-govt-to-table-implement-karnataka-apartment-ownership-act | 2025-12 | 2026-10-31 | BAF 1,400+ associations (re-checked; also Investigator S65) | search summary |
| 37 | Maharashtra housing societies oppose draft rule on training fund contributions | Free Press Journal | https://www.freepressjournal.in/amp/mumbai/maharashtra-housing-societies-oppose-draft-rule-on-training-fund-contributions-submit-objections-to-state-government | not shown; retrieved 2026-10-31 | 2026-10-31 | Pune federation chairman: 18,000+ societies registered (attribution among results uncertain) | search summary |
| 38 | Model housing bye-laws | Scribd (copy of model bye-laws) | https://www.scribd.com/document/452539621/Model-housing-byelaws-pdf | not shown; retrieved 2026-10-31 | 2026-10-31 | Society must affiliate with district housing federation | search summary |
| 39 | NIT for AMC of passenger lift | IIM Indore | https://www.iimidr.ac.in/wp-content/uploads/nitamcpassengerliftatiimindore.pdf | not shown; retrieved 2026-10-31 | 2026-10-31 | 2-hour emergency response; Rs 1,000 penalty | search summary |
| 40 | Lift AMC tender | ICAT | https://icat.in/storage/app/public/uploads/tender_1652244726.pdf | not shown (c. 2022) | 2026-10-31 | Tiered penalties of 1-2% of contract price (attribution between two ICAT tenders uncertain) | search summary |
| 41 | Tender for Johnson Lifts AMC 2020-21 | NIFT Chennai | https://www.nift.ac.in/chennai/sites/chennai/files/2020-12/Tender%20for%20Johnsons%20Lifts-%20Annex%20%26%20SMAC%202020-21.pdf | 2020-12 | 2026-10-31 | One-month termination by either party | search summary |
| 42 | Consultation on proposed commitments to supply lift spare parts by C&W Services | Competition and Consumer Commission of Singapore | https://www.ccs.gov.sg/case-register/public-consultations/closed---investigations/consultation-on-proposed-commitments-to-supply-lift-spare-parts-by-c-w-services-operations-pte-ltd/ | not shown; retrieved 2026-10-31 | 2026-10-31 | Parts withheld from third-party maintainers | search summary |
| 43 | Otis India emphasising maintenance of elevators by OEMs | MGS Architecture | https://www.mgsarchitecture.in/building-materials-products/elevators/otis-india-emphasising-maintenance-of-elevators-by-oems.html | not shown; retrieved 2026-10-31 | 2026-10-31 | Maker promotes OEM-only maintenance (title only) | search summary |
| 44 | Reliance General professional indemnity insurance | Policybazaar | https://www.policybazaar.com/insurance-companies/reliance-general-professional-indemnity-insurance/ | not shown; retrieved 2026-10-31 | 2026-10-31 | Rs 1 crore cover "from" Rs 1,731 a year (marketing; attribution among Policybazaar pages uncertain) | search summary |
| 45 | Insurance policy detail | Indian Academy of Neonatology / United India schedule | https://ianindia.org/insurance-policy-detail.html | not shown; retrieved 2026-10-31 | 2026-10-31 | Doctors' Rs 1 crore PI at Rs 3,150 and Rs 12,000 | search summary |
| 46 | SCT-013-000 100A non-invasive AC current sensor | Electronicscomp | https://electronicscomp.com/sct-013-000-100a-non-invasive-ac-current-sensor-split-core-type-clamp-meter-sensor | not shown; retrieved 2026-10-31 | 2026-10-31 | Rs 548.7 incl. tax | search summary |
| 47 | SCT-013-000 100A non-invasive AC current sensor | Electropi | https://www.electropi.in/sct-013-000-100a-non-invasive-ac-current-sensor-split-core-type-clamp-meter-sensor | not shown; retrieved 2026-10-31 | 2026-10-31 | Rs 289 ex GST | search summary |
| 48 | ESP32 development board with CP2102 | Robocraze | https://robocraze.com/products/esp32-development-board-with-cp2102-wifi-bluetooth-dual-core-30-pin | not shown; retrieved 2026-10-31 | 2026-10-31 | Rs 399 | search summary |
| 49 | PAPL, Ardelisys launch IoT-based elevator monitoring system at SLM World in India | Elevator World | https://elevatorworld.com/news/daily-news/papl-ardelisys-launch-iot-based-elevator-monitoring-system-at-slm-world-in-india | 2024-03 | 2026-10-31 | KALA subscription; no price found | search summary |
| 50 | Mumbai Masala: Making a killing | Free Press Journal | https://freepressjournal.in/amp/mumbai/mumbai-masala-making-a-killing | not shown; retrieved 2026-10-31 | 2026-10-31 | Committee bribery alleged in redevelopment | search summary |
| 51 | Only 40,000 Maharashtra housing complexes submit reports on fire system maintenance | Propscience | https://www.propscience.com/stories_detail/2392/only-40-000-maharashtra-housing-complexes-submit-reports-on-fire-system-maintenance | not shown; retrieved 2026-10-31 | 2026-10-31 | Low compliance with mandated fire reports (headline only) | search summary |
| 52 | Mumbai: 2,700 buildings served notices for fire safety violations | Lokmat Times | https://www.lokmattimes.com/mumbai/mumbai-2700-buildings-served-notices-for-fire-safety-violations-a507 | not shown; retrieved 2026-10-31 | 2026-10-31 | Notices to about 2,700 societies | search summary |
| 53 | Fire Safety Week: Mumbai FD says Form B mandatory for all buildings | Free Press Journal | https://www.freepressjournal.in/amp/mumbai/mumbai-fire-safety-week-begins-form-b-mandatory-for-all-structures | not shown; retrieved 2026-10-31 | 2026-10-31 | Form B from licensed agency twice a year (re-seen; also Inventor S32) | search summary |
| 54 | Schedule of fees for lifts and escalators | Chief Electrical Inspector, Assam | https://cei.assam.gov.in/sites/default/files/Schedule%20of%20fees%20for%20Lift%20and%20Escalators_0.pdf | not shown; retrieved 2026-10-31 | 2026-10-31 | Inspection Rs 1,000-2,000 (currency of schedule unclear) | search summary |
| 55 | BMC conducts safety audit of only 400 lifts in Bhopal high-rise buildings | Free Press Journal | https://www.freepressjournal.in/amp/bhopal/bmc-conducts-safety-audit-of-only-400-lifts-in-bhopal-high-rise-buildings | not shown; retrieved 2026-10-31 | 2026-10-31 | Rs 2,000 electrical safety fee (re-seen; also Inventor S14) | search summary |
| 56 | Notice inviting tender (PMC) | State Bank of India | https://sbi.bank.in/documents/39129/51516783/NOTICE+INVITING+TENDER20260728111719862.pdf | 2026-07 (from file name) | 2026-10-31 | PMC fee capped at 3% of project cost (attribution between two SBI documents uncertain) | search summary |
| 57 | Comparison between OEM and third-party elevator parts suppliers in India | SSJ Elevator (blog) | https://ssjelevator.blogspot.com/2025/03/comparison-between-oem-and-third-party.html | 2025-03 | 2026-10-31 | Vendor claim that third-party parts are cheaper; no figures | search summary |
| 58 | Society maintenance charges | SoftwareSuggest | https://www.softwaresuggest.com/blog/society-maintenance-charges/ | not shown; retrieved 2026-10-31 | 2026-10-31 | One vendor's Rs 10 per flat a month (attribution among results uncertain) | search summary |
| 59 | Got a lift in your apartment? Survey says 46% residents were trapped at least once last year | Business Today (LocalCircles) | https://www.businesstoday.in/amp/india/story/got-a-lift-in-your-apartment-survey-says-46-residents-were-trapped-at-least-once-last-year-546526-2026-07-31 | 2026-07-31 | 2026-10-31 | Entrapments; maker vs third-party share (Investigator S1; not re-checked by me) | search summary |
| 60 | M/s Otis Elevator Co (India) Ltd v Rashmi Handa & Others, 2026 INSC 756 | Verdictum | https://www.verdictum.in/supreme-court/ms-otis-elevator-co-india-ltd-v-rashmi-handa-others-2026-insc-756-1618809 | 2026-07-29 | 2026-10-31 | Joint liability ruling (Investigator S9; not re-checked by me) | search summary |
| 61 | Woman's death in lift: Noida police lodges FIR against society's maintenance firm, office-bearers, lift maker | Deccan Herald | https://www.deccanherald.com/india/womans-death-in-lift-noida-police-lodges-fir-against-societys-maintenance-firm-office-bearers-lift-maker-1243725.html | 2023-08 (approx.) | 2026-10-31 | FIR naming office-bearers, maintainer and maker (Investigator S12; not re-checked by me) | search summary |
| 62 | Pune: man dies after lift crash in Talegaon, case filed against society chairman and 11 others | Free Press Journal | https://www.freepressjournal.in/amp/pune/pune-man-dies-after-lift-crash-in-talegaon-case-filed-against-society-chairman-11-others | 2026-03 | 2026-10-31 | Case against society chairman (Investigator S13; not re-checked by me) | search summary |
| 63 | Sinhagad Road lift tragedy puts spotlight on delayed safety audits | Punekar News | https://www.punekarnews.in/?p=235806 | 2026-05 | 2026-10-31 | About 26% of Pune lifts inspected in FY 2025-26 (Investigator S7; not re-checked by me) | search summary |
| 64 | Dispute with apartment association, Bengaluru | Vidhikarya | https://www.vidhikarya.com/FreeLegalAdvice/43211/dispute-with-apartment-association-bengaluru-bangalore | not shown; retrieved 2026-10-31 | 2026-10-31 | Rs 10,000 approval threshold in one association (Investigator S60; not re-checked by me) | search summary |
| 65 | Best society management app India 2026 | Codingclave | https://codingclave.com/blog/best-society-management-app-india-2026 | 2026 | 2026-10-31 | MyGate Rs 5-12 per flat a month (Investigator S62; not re-checked by me) | search summary |
| 66 | VDA supplier page (nonprofit) | OMNIA Partners | https://www.omniapartners.com/suppliers/vda/nonprofit | not shown; retrieved 2026-10-31 | 2026-10-31 | Consultant claim of 10-15% maintenance cost reduction (Inventor S16; not re-checked by me) | search summary |
| 67 | Maha to strengthen lift inspection system, 519 posts to be created | Lokmat Times | https://www.lokmattimes.com/national/maha-to-strengthen-lift-inspection-system-519-posts-to-be-created-cm-fadnavis | 2026-03-04 | 2026-10-31 | 519 posts; planned third-party inspection, not notified (Inventor S25; not re-checked by me) | search summary |
| 68 | Independent third-party lift inspections tailored for India | TÜV SÜD (PresseBox) | https://www.pressebox.com/pressrelease/tuev-sued-ag/independent-third-party-lift-inspections-tailored-for-india/boxid/1277681 | not shown; retrieved 2026-10-31 | 2026-10-31 | Accredited inspection firm in India (Investigator S56; not re-checked by me) | search summary |
| 69 | Uttar Pradesh Lifts and Escalators Act, 2024 | Lawgist | https://lawgist.in/states/uttar-pradesh/uttar-pradesh-lifts-and-escalators-act-2024/22 | 2024 | 2026-10-31 | Comprehensive AMC from maker or authorised provider (Investigator S20; not re-checked by me; consistent with S16) | search summary |
| 70 | Terms and conditions for Lift Insurance Policy (Liability Cover) | indiacustomercare.com | https://www.indiacustomercare.com/terms-conditions-lift-insurance-policy-liability-cover | undated; retrieved 2026-10-31 | 2026-10-31 | Rs 3 per mille of annual limit (Inventor S11; not re-checked by me) | search summary |
| 71 | Four in 10 Bengalureans dread stepping into a lift: survey | Deccan Herald | https://deccanherald.com/india/karnataka/bengaluru/four-in-10-bengalureans-dread-stepping-into-a-lift-survey-4098155 | 2026-08 | 2026-10-31 | 38% third-party maintainers in Bengaluru cut (Inventor S40; not re-checked by me) | search summary |
| 72 | Lift and Escalator Act, 2024: Noida dominates registration drive across UP | The Realty Today | https://therealtytoday.com/news/trending/lift-and-escalator-act-2024-noida-dominates-registration-drive-across-uttar-pradesh | not shown (after Oct 2024) | 2026-10-31 | 87 makers and 98 AMC agencies registered (Inventor S39; figure re-seen in my search, attribution uncertain) | search summary |
| 73 | How housing societies can control elevator expenses for their buildings | Free Press Journal | https://www.freepressjournal.in/amp/business/how-housing-societies-can-control-elevator-expenses-for-their-buildings | not shown; retrieved 2026-10-31 | 2026-10-31 | Independent consultants advise societies (Investigator S69; not re-checked by me) | search summary |
| 74 | Audit: time to elevate | Construction World | https://www.constructionworld.in/gold/policy-updates-and-economic-news/audit--time-to-elevate/85415 | not shown; retrieved 2026-10-31 | 2026-10-31 | Mumbai societies used independent audits for ageing lifts (Investigator S55; not re-checked by me) | search summary |
| 75 | Otis Worldwide to buy majority stake in WeMaintain | Nasdaq | https://www.nasdaq.com/articles/otis-worldwide-buy-majority-stake-wemaintain | 2026-04 | 2026-10-31 | Independent maintainer absorbed by a maker (Investigator S50; not re-checked by me) | search summary |
| 76 | Contrôle technique quinquennal des ascenseurs (FAQ) | French Ministry of Ecology | https://www.ecologie.gouv.fr/sites/default/files/documents/Questions%20r%C3%A9ponses%20addititif%20n%C2%B01%20concernant%20les%20contr%C3%B4les%20techniques%20quinquennaux%20-%20mars%202014.pdf | 2014-03 | 2026-10-31 | Independence of lift control from owner and maintainer (Inventor S52; not re-checked by me) | search summary |
| 77 | CCI imposes Rs 2,544 crore fine on 14 car manufacturers | Bar & Bench | https://www.barandbench.com/news/cci-imposes-rs-2544-crore-fine-14-car-manufacturers | 2014 | 2026-10-31 | Indian precedent on spare-parts restriction (Inventor S41; not re-checked by me) | search summary |
| 78 | TK Elevator Australia lift maintenance contract (redacted) | NSW Department of Planning | https://www.dpie.nsw.gov.au/__data/assets/pdf_file/0007/624796/TK-Elevator-Australia-Pty-Ltd-Lift-Maintenance-Contract_Redactedv4.pdf | not shown; retrieved 2026-10-31 | 2026-10-31 | 30-minute entrapment response (Inventor S15; not re-checked by me) | search summary |

Searches that found nothing usable (reported as gaps, not filled):
- Federation joint tenders or group buying of AMCs: not found after 2 searches ("apartment federation group buying collective negotiation member associations lift AMC discount Bangalore OR Noida OR Pune", "RWA federation joint tender common procurement for member societies India security OR housekeeping OR solar aggregated bulk contract").
- Independent lift auditor fees: not found after 2 searches ("lift safety audit charges per lift independent elevator consultant India society fees Rs", "\"elevator auditor\" OR \"lift auditor\" housing society Mumbai fees audit report cost ageing lifts modernisation").
- Fire Form B agency fees: not found after 2 searches ("fire audit Form B charges housing society Mumbai cost per building licensed agency", "\"Form B\" fire certificate charges Rs society licensed agency cost per wing OR building Mumbai Pune half-yearly fee").
- Success-fee or shared-savings consultants for Indian societies: not found after 1 search ("housing society consultant fee percentage of savings ... \"share of savings\" apartment India").
- Lift-AMC kickbacks: not found after 1 search ("housing society committee kickbacks vendor contracts AMC commission office-bearers allegation lift contract India").
- Quantified OEM vs third-party AMC price gap in India: not found after 1 search ("third party lift AMC cheaper than OEM Otis KONE Schindler society India price difference spare parts availability").
- Lift-specific liability premium per lift: not found after 1 search ("lift insurance policy premium housing society India third party liability passengers premium per lift").
- KALA price: not found after 1 search ("KALA elevator monitoring PAPL Ardelisys price subscription per lift India residential").
- Residential FM firms offering AMC procurement: not found after 1 search.
- HSMS stall prices: not found after 2 searches.
