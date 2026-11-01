# Approach A: Market intelligence

Run date 2026-11-01. Hunter: Opportunity Hunter. Brief: `00-brief.md`. Calculations: `01-approach-A-calc.py`, output in `01-approach-A-calc-output.txt`.

## Access status (read first)

No source page could be opened. WebFetch failed on the two hosts tried (www.pib.gov.in and www.theweek.in) with a host-resolution error, so those hosts need to be allowed in the session network settings. I did not try every other host, because the brief says fetching fails everywhere. Every `[S#]` tag below therefore rests on a search summary and is `unverified at source`. Every claim that decides an outcome is marked "(unverified at source)" next to its tag. Because of this, nothing here can be ADVANCE. The best outcome is INVESTIGATE.

Result in one line: zero ADVANCE. Three kept ideas, all INVESTIGATE at low confidence (one evidence-backed thesis, two exploratory bets). Six candidates killed. No winner is forced.

## 1. Industries chosen and why

Three unrelated industries outside the excluded list, plus one regulation-driven area that was killed early.

1. **Power distribution equipment and electrical steel (industrial, B2B).**
   - Grain-oriented steel (CRGO) is short: a shortfall of 30 percent was reported in October 2024, and domestic output meets only 10 to 12 percent of demand [S2] (unverified at source).
   - A grid build-out of Rs 9.15 lakh crore to 2032 is cited as the demand driver [S2] (unverified at source), and an anti-dumping probe on CRGO began on 22 June 2026 [S2] (unverified at source). A trade outlet alleges scrap CRGO is still used in distribution transformers [S5] (unverified at source).
2. **Temple and festival economy (ritual objects, large castings).**
   - Live-elephant use in Kerala festivals is under court and welfare pressure, and large temple spending is documented (a 2,100 kg bell reported at Rs 21 lakh) [S20] (unverified at source).
   - Temple-building spending (Ayodhya and similar) creates one-off premium commissions paid by donors, not by a budget line [I: bell reports in S20 and S21 are donations].
3. **Ship recycling and marine salvage.**
   - The Hong Kong Convention entered into force on 26 June 2025 and India began implementing it at Alang on 30 June 2025 [S1] (unverified at source).
   - Alang's second-hand market of 500 or more shops is documented [S18] but the yard is shrinking [S18].
4. **Diesel generator emissions rules (regulation).** CAQM ordered a ban on diesel generator sets in NCR unless fitted with a retrofit device or dual-fuel kit [S17] (unverified at source). Killed in section 5.

Also scanned and dropped at the size step: rare-earth magnets (scheme of Rs 7,280 crore [S4]) and amorphous-core transformers (Proterial JV in India, reported February 2026 [S29]). Both are capital-heavy and led by large firms.

## 2. Raw candidates

| # | Problem or product | Payer | Signal | Tag |
|---|---|---|---|---|
| 1 | Field check for scrap or non-prime CRGO in distribution transformers | Distribution utilities (DISCOMs) or their inspectors | Alleged scrap use cuts cost by 40 to 50 percent [S5]; failures of 12 to 15 percent a year [S8] | [S5][S8] |
| 2 | Life-size mechanical festival elephants | Temples, mostly donor-funded by PETA India | At least 26 units since 2023 [S11]; price Rs 5.25 lakh [S11] | [S11] |
| 3 | Emission retrofit devices for diesel generator sets | Commercial and industrial generator owners in NCR | Rule in force [S17]; listings from Rs 3.5 lakh to Rs 9.15 lakh per 500 kVA [S16] | [S16][S17] |
| 4 | Designer goods from ship-breaking salvage | Interior buyers, collectors | Trade exists [S18][S19] | [S18][S19] |
| 5 | Rare-earth magnet plants | Industrial investors | Scheme Rs 7,280 crore, 25 firms at pre-bid [S4] | [S4] |
| 6 | Amorphous-core or CRGO-core transformer supply | Utilities | Big-firm JV announced [S29] | [S29] |
| 7 | Harmonically tuned large temple bell, cast by an existing foundry | Temple trusts, donors | Bells of Rs 21 lakh to Rs 25 lakh are commissioned [S20] | [S20] |
| 8 | Magnetic-domain display object made from grain-oriented steel | Collectors, architects, corporate lobbies | None found for demand; ferrofluid art exists [S27] | [S27] |
| 9 | Hazardous-materials inventory help for ship-recycling yards | Yards | 115 of 128 plots hold the compliance statement [S1] (unverified at source) | [S1] |

### Size first (rule 21)

Computed in `01-approach-A-calc.py`.

- Mechanical elephants: 26 to 40 units cumulative at Rs 5 to 6 lakh is Rs 130 lakh to Rs 240 lakh over about three years [I: 26 to 40 units from S11 and S12 times Rs 5 to 6 lakh from S11]. One funder buys most units [S12]. Pool too small for a repeat business.
- Generator retrofit: price range found but installed base not found after 2 searches (queries: "number of diesel generator sets installed India Delhi NCR", "CPCB approved RECD list price per kVA"). Pool not computable.
- Rare earths: capex route, not reachable with Rs 0 [S4].
- Distribution-transformer instrument: about 240 sites and 36 units in 24 months, revenue Rs 216 lakh [A] [I] (counts and the 15 percent share are assumed, see section 3).
- Tuned bell: 10 bells a year at Rs 10 lakh is Rs 100 lakh revenue [A] [I] (units per year assumed). Number of large bell commissions per year not found.
- Domain object: 4 pieces a year at Rs 7.5 lakh is Rs 30 lakh revenue [A].

## 3. Evidence-backed theses

### Thesis 1: Portable scrap-CRGO check for distribution transformers (a B2B instrument)

**Outcome: INVESTIGATE, low confidence.** Not original in method; kept because the pain is documented [S5] and the instrument price would fit a Rs 5 to 10 lakh B2B instrument [A].

**Original.** Five nearest methods and products:
1. Stresstech Rollscan Barkhausen-noise analysers, sold in India through Stresstech Bharat; handheld use is possible, price on request [S7] (unverified at source).
2. Chinese patent CN106199282A: identify distribution transformers built with secondary silicon steel by measuring no-load loss, then again after over-excitation [S6] (unverified at source).
3. Chinese patent CN118760958B: Barkhausen-noise features plus machine learning to assess silicon-steel sheet condition; it states secondary sheets raise quality risk [S10] (unverified at source).
4. Vendor "core loss tester" (VEER make) for motor stator cores, portable [S30] and Epstein frame or single-sheet testers for sheets (standard methods) [S30].
5. Pre-dispatch inspection by RITES for REC schemes [S9] (unverified at source).

Novelty queries run (9): "portable non-destructive core loss tester assembled transformer core"; Chinese "变压器铁芯 硅钢片 铁损 现场 无损 检测仪 便携式"; German "Prüfgerät Elektroblech Kernverlust Transformatorkern zerstörungsfrei"; Hindi on poor-quality scrap CRGO utility inquiries; patent query on secondary steel and Barkhausen; Barkhausen handheld price; "CRGO issues still haunt transformer industry"; "distribution transformer failure rate India"; "DISCOM pre-dispatch inspection no-load loss". Not found: a commercial product sold to utilities for this purpose after these queries. The Chinese patent shows the method is not new and needs only a standard test set, which weakens the case for a new instrument.

**Desired.** Payer: DISCOM procurement or quality department, or an inspection agency such as RITES [S9] (unverified at source). Beneficiary: the utility, which bears the cost of failure. About 12 to 15 percent of distribution transformers fail each year, which is 6 to 8 lakh units a year out of about 70 lakh [S8] (unverified at source). A second report cites about 1.82 crore distribution transformers [S9] (unverified at source). The two stock figures disagree by 2.6 times [I: 182 lakh divided by 70 lakh]. I trust neither; the BIS-hosted paper is older and the CEA article is newer but secondary. Budget line: quality assurance or pre-dispatch inspection. No evidence found that any utility spends on scrap-steel detection. Supplier warranty may carry the loss: that clause was not checked.

**Feasible.** A yoke or flux probe plus a loss meter is established technology [K]. The open engineering question is whether grade can be told reliably on an assembled core without dismantling. Experiment: measure known prime and non-prime core samples. Parts list and catalogue prices not found.

**Profitable.** Script: `01-approach-A-calc.py`. Inputs: price Rs 6 lakh [A: brief range for B2B instruments, not sourced], margin 40 percent [A], 70 utilities [A], 3 sites each [A], 30 labs or inspectors [A], 15 percent captured in 24 months [A], development cost Rs 15 lakh [A], fixed cost Rs 40,000 a month [A], 80 founder hours per unit [A], founder hour value Rs 750 [A: default in `tools/econ.py`].
- Base: 36 units, revenue Rs 216 lakh, margin Rs 86.4 lakh, net after paying own time Rs 40.2 lakh over 24 months [I: script output][A].
- Sensitivity, one unsourced input halved at a time: price halved gives Rs -3.0 lakh [I]; margin halved gives Rs -3.0 lakh [I]; utilities, sites or capture share halved gives positive but below full-time pay (Rs 9.3 lakh to Rs 12.0 lakh a year against Rs 14.4 lakh) [I: script output][A].
- The verdict flips. **Unknown. Driven by the price a utility will pay and the margin.**
- Contrary data: a 500 kVA unit with scrap steel sells for about Rs 5 lakh against Rs 8 to 9 lakh normally [S5] (unverified at source). That shows cost saving for makers, not a utility willing to pay for detection.

**Reachable.** Named buyer list not found; the utility register (AIDA members or CEA list) was not opened. Count of 70 is [A]. First 10: the utilities and inspectors that already run pre-dispatch and acceptance tests [S9]. First 100: not reachable on this count, because the whole buyer base is about 100 sites [A]. Tender-driven sales; cycle length not found, [H] 12 months or more.

**Defensible.** Weak. The method is patented in China [S6] and a Barkhausen maker could add a transformer mode [S7]. What could accumulate: a reference library of measured prime and non-prime cores. A copier could not buy that in a year [H].

**Large enough, within means.** At the base case 36 units need 2,880 founder hours over 24 months, which is 120 hours a month [I: script], within the 160 hours available [A]. Capital before first revenue: Rs 15 lakh development [A] against Rs 0. Funding route: deposits from at least 5 buyers (Rs 15 lakh divided by a 50 percent deposit on Rs 6 lakh) [I: script], or a government R&D grant [H: no scheme checked]. No utility deposit evidence found. If no utility funds it, the loss is Rs 24.6 lakh [I: script].

**Doubt most likely to kill it.** The standard no-load loss test already shows scrap steel, so no new instrument is needed (the patent method uses that same test [S6]). **First test:** ask two inspection engineers whether scrap-core units pass acceptance loss tests today. Not done; the brief forbids contact. **Even-if-true:** if utilities do want it, the whole market is about 240 sites [A], enough for one founder but with no scale beyond it, and a copier can follow. It survives Reachable and Large enough, marginally; Defensible stays weak. Hence INVESTIGATE, not ADVANCE.

## 4. Exploratory bets

Both are bets. Neither has demand evidence at L2 or above.

### Bet A: Harmonically tuned large temple bell (borrowed from carillon founding)

**Field borrowed.** European bellfounders have tuned the lowest five partials since the 17th century and now design with finite element analysis [S25][S26]. The idea applies this to large Indian brass or ashtadhatu temple bells, cast by an existing foundry such as those in Jalesar, with a chosen pitch.

**What it would be if it worked.** Buyer: a temple trust or donor. Price Rs 8 to 10 lakh for a roughly 700 kg bell [A]. Buyer spend evidence is real: the Ayodhya bell was reported at Rs 21 lakh for 2,100 kg [S20] and Rs 25 lakh for 2,400 kg [S20], with a Swarajya figure of Rs 10 to 12 lakh [S20]; those reports differ and I could not resolve it. A 3-tonne bell was made in Kashi for Mathura [S21]. These imply a foundry cost of about Rs 1,000 to 1,190 per kg [I: script, from S20].

**Novelty result.** Queries (9): "tuned temple bell India harmonic partials"; Dutch "klokkengieterij gestemde klok Eijsbouts export India"; Hindi "मंदिर घंटा सुर में ट्यून ओम ध्वनि जलेसर"; Japanese "梵鐘 音響設計 調律 有限要素解析 高岡"; "Om frequency 136.1 Hz tuned bell"; Kickstarter and startup tuned bell search; Kumbakonam and Swamimalai bell price search; Kashi 3-ton bell search; Ayodhya bell search. Near neighbours: US8492632 "Tuned bell harmonic musical instrument" [S23]; patent application on bells and design methods [S24]; University of Melbourne FEA stiffening patent [S24]; Eijsbouts FEA work with Eindhoven University [S25]; Sunreed 136.1 Hz aluminium Om chime at USD 79.98 to USD 134.97 [S22]; Schlagwerk 136.1 Hz gong and forks [S22]; Pune temple acoustic study of bell partials [S26]. Not found after these queries: a large brass temple bell sold in India as tuned to a stated pitch. **Verdict on Original: fails the standard.** The method exists worldwide, so the difference is only that it is new to Indian temple bells. I keep it as a commercial bet only because buyer spend at this price is documented.

**Profitable (script).** Foundry cost Rs 7.0 to 8.3 lakh for 700 kg [I: script]; price Rs 10 lakh [A]; margin Rs 1.7 to 3.0 lakh a bell [I: script]; 80 design hours a bell [A]; 10 bells a year [A]. Net after own time Rs 1.1 to 2.4 lakh a bell [I: script]. Sensitivity: premium over foundry cost halved leaves Rs 0.2 lakh a bell at the high cost; units halved gives Rs 5.3 lakh a year, below full-time. **Unknown. Driven by the price premium buyers pay for tuning and the number of bells a year.**

**Reachable.** Buyers are temple trusts and donors. No named list found. Whether a donor values pitch is [H].

**Defensible.** Weak: patents and FEA methods are public [S23][S24]. A reference library of tuned castings and a tuning method could accumulate [H].

**Large enough, within means.** Cash: foundry advance of 50 percent [A] is Rs 3.5 to 4.2 lakh against a 40 percent buyer deposit of Rs 4.0 lakh [I: script], so the deposit about covers it. Capital Rs 0 is plausible only with deposits. Hours: 800 a year at 10 bells [I: 10 bells times 80 hours]. Best realistic case: gross margin Rs 17 to 30 lakh a year [I: script], the low end near the Rs 14.4 lakh full-time equivalent [A].

**Single experiment.** Ask two foundries and two temple trusts whether pitch matters and what they would pay for it. Not done (brief forbids contact).
**Even-if-true:** passes Reachable and Large enough at small scale; fails Defensible and Original. **Outcome: INVESTIGATE, low confidence, with the Original failure stated.**

### Bet B: Magnetic-domain display table (borrowed from materials science)

**Field borrowed.** Magnetic domains in grain-oriented steel can be shown with Bitter colloid or viewing film [S28]. The idea is a Rs 5 to 10 lakh table or wall piece showing live domain patterns in a real transformer-steel surface.

**What it would be if it worked.** Buyer: collectors, architects, corporate lobbies. Price Rs 7.5 lakh [A]; 4 pieces a year; margin Rs 4.1 lakh a piece, Rs 12.0 lakh a year after own time (150 hours a piece at Rs 750) [A][I: script]. Gross margin Rs 16.5 lakh against the Rs 14.4 lakh full-time equivalent [I: script].

**Novelty result.** Queries (6): "magnetic domain visualization art table ferrofluid furniture"; "magnetic viewing film decorative table Bitter pattern art"; Japanese "磁性流体 アート テーブル 磁区 可視化 電磁鋼板"; German "Magnetfeld sichtbar machen Kunstobjekt Tisch Ferrofluid"; patent hit on ferrofluid sculpting apparatus US6290894 [S27]; Kodama "Protrude, Flow" [S27]. Near neighbours: Kodama ferrofluid sculptures [S27], CZ Ferro "Nano Tree" and the "Ferrite" series [S27], supermagnete levitation sculptures [S27], the MTR "Ferroflow" object [S27]. Not found after these queries: any object that shows domains of electrical steel as art or furniture. This is under 8 distinct novelty angles (no incumbents' catalogue or closed-venture search beyond the above), so "none found" is weak.

**Even-if-true.** Fails Large enough in the sense that it does not scale beyond founder labour: every piece takes 150 hours [A]. Defensible is weak, since any gallery artist could copy once seen. Bitter patterns can take minutes to settle and standard polishing gives poor results on steels [S28], which is an engineering risk.
**Single experiment:** a bench test of one steel sample under viewing film to see if domains are visible at table scale. Not run.
**Outcome: INVESTIGATE as a bet, weakest of the three.**

## 5. Cut candidates and reasons

| Candidate | Reason cut |
|---|---|
| Mechanical festival elephants (#2) | Fails Original: Prasanth Prakashan of Chalakudy builds them at Rs 5.25 lakh including GST [S11], PETA India buys and donates [S11][S12], and a PETA release shows one used at a wedding in Bengaluru [S13]. Pool is Rs 130 lakh to Rs 240 lakh cumulative [I: see section 2] and one funder buys most units [S12]. Rentals by temples are reported [S12]. The Supreme Court stayed the Kerala High Court's elephant guidelines [S14], which weakens the regulatory push. A Spanish-language news item on the robotic elephant also appeared in search (not added to Sources). |
| Generator retrofit devices (#3) | Not original and crowded: Kirloskar sells a retrofit device [S16]; certified vendors only (CPCB list, ARAI certification) [S16] (unverified at source); price sources conflict, Rs 0.7 lakh to Rs 12.5 lakh for 500 kVA [S16]; installed base not found. Diesel generators are about 4 percent of NCR PM2.5 [S17], so rule tightening is not assured. |
| Ship-salvage designer goods (#4) | Fails Original: Trinity Marine, 1stDibs, Pieces of Ship and collector Peter Knego already sell salvage [S19][S18]. Market shrinking: FY 2024-25 was the lowest recycling count in over a decade [S18]. Turkish-language search found no design use but a tax issue on reused items [S18]. |
| Rare-earth magnet plants (#5) | Scheme Rs 7,280 crore for 6,000 tonnes a year [S4]. Capex-heavy and Rs 0 cannot enter. |
| Amorphous or CRGO-core transformers (#6) | Large firms (Proterial JV, Voltamp) [S29]; amorphous costs about 40 percent more (undated Scribd source, weak) [S30]. |
| Hazardous-materials help for ship yards (#9) | Consulting-like and 115 of 128 plots already hold statements [S1] (unverified at source). |

Not checked: whether a first CRGO slitting or cut-to-length service could start without a line. Cost of lines not found, so not sized.

## 6. Sources

All retrieved 2026-11-01. `Via` is search summary for every row: no page could be opened (see Access status).

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | India commences implementation of the Hong Kong Convention from Alang | India Shipping News | https://indiashippingnews.com/trending-news/india-commences-implementation-of-the-hong-kong-convention-from-alang-dg-shipping/ | 2025 | 2026-11-01 | Entry into force, yard compliance | search summary |
| 2 | CRGO Steel Shortage Poses Threat to India's Power Sector Expansion Plans, Warns GTRI | Outlook Business | https://www.outlookbusiness.com/industry/crgo-steel-shortage-poses-threat-to-indias-power-sector-expansion-plans-warns-gtri | 2024-10 | 2026-11-01 | CRGO shortfall, grid spend | search summary |
| 3 | Supply Chain Shortages and Inflation Delay Power Transmission Projects | Mercom India | https://mercomindia.com/supply-chain-shortages-and-inflation-delay-power-transmission-projects | not seen | 2026-11-01 | Lead times | search summary |
| 4 | Cabinet Approves Rs 7,280 Crore Scheme for Rare Earth Magnet Manufacturing | Autocar Pro | https://www.autocarpro.in/news/cabinet-approves-rs-7280-crore-scheme-for-rare-earth-magnet-manufacturing-129930 | 2025-11-26 | 2026-11-01 | Magnet scheme | search summary |
| 5 | CRGO issues still haunt transformer industry | T&D India | https://www.tndindia.com/crgo-issues-still-haunt-transformer-industry/amp/ | not seen | 2026-11-01 | Scrap CRGO allegation, cost saving | search summary |
| 6 | CN106199282A, identification method for distribution transformers using secondary silicon steel | Google Patents | https://patents.google.com/patent/CN106199282A/zh | not seen | 2026-11-01 | Prior art | search summary |
| 7 | Barkhausen noise equipment, Rollscan range | Stresstech | https://www.stresstech.com/products/barkhausen-noise-equipment/ | not seen | 2026-11-01 | Incumbent instruments | search summary |
| 8 | Distribution transformer failure paper | BIS training site | https://www.services.bis.gov.in/php/BIS_2.0/trainings/assets/uploads/54548_26102021125430_1.pdf | 2021 | 2026-11-01 | Failure rate, stock of 70 lakh | search summary |
| 9 | CEA finalizes standard transformer specifications | SolarQuarter | https://solarquarter.com/2026/05/18/cea-finalizes-standard-transformer-specifications-to-improve-power-distribution-efficiency-across-india/ | 2026-05-18 | 2026-11-01 | Stock of 1.82 crore, RITES inspection | search summary |
| 10 | CN118760958B, HHT-based silicon steel fault diagnosis | Patsnap Eureka | https://eureka.patsnap.com/patent/CN118760958B | not seen | 2026-11-01 | Prior art | search summary |
| 11 | Mechanical elephants replace jumbos in Kerala temple festivals | Onmanorama | https://www.onmanorama.com/news/kerala/2026/02/11/mechanical-elephants-replace-jumbos-in-kerala-temple-festivals.html | 2026-02-11 | 2026-11-01 | Price, builder, 26 units | search summary |
| 12 | Robotic Elephants Enter Indian Temples as Devotees Push Back | eWeek | https://www.eweek.com/news/robotic-elephants-indian-temples-apac/ | 2026 | 2026-11-01 | 40 units, PETA funding, rental | search summary |
| 13 | Swami Baba Ramdev Enchanted by First Mechanical Elephant at a Wedding | PETA India | https://www.petaindia.com/?p=93442 | 2026 | 2026-11-01 | Wedding use | search summary |
| 14 | Kerala High Court captive elephant guidelines and Supreme Court stay | Deccan Herald | https://www.deccanherald.com/amp/story/india%2Fkerala%2Fkerala-has-a-double-standard-on-elephants-say-activists-amid-festival-deaths-3409449 | 2025 | 2026-11-01 | Court status | search summary |
| 15 | Elephants in Kerala culture | Wikipedia | https://en.wikipedia.org/wiki/Elephants_in_Kerala_culture | 2025 | 2026-11-01 | Captive count about 400 (weak) | search summary |
| 16 | RECD price listings (Automoto, IndiaMART, Jotform, Kirloskar) | Various vendors | https://www.aajjo.com/product/750-kva-retrofit-emission-control-device-in-north-west-delhi-automoto-genset-sales-and-services-llp | not seen | 2026-11-01 | Price range, incumbents | search summary |
| 17 | To curb pollution in NCR, diesel generators banned from Oct 1 | The Tribune | https://www.tribuneindia.com/news/haryana/to-curb-pollution-in-ncr-diesel-generators-banned-from-oct-1-521401 | 2023 | 2026-11-01 | CAQM rule, 4 percent PM2.5 share | search summary |
| 18 | Alang market, decline, and yard utilisation | The Better India, Marine Insight, Al Jazeera | https://www.aljazeera.com/news/2025/12/15/no-work-indias-alang-the-worlds-largest-graveyard-of-ships-is-dying | 2025-12-15 | 2026-11-01 | Shrinking yard, 500 shops | search summary |
| 19 | Ship salvage collections | Trinity Marine | https://www.trinitymarine.co.uk/collections?page=4 | not seen | 2026-11-01 | Incumbent salvage sellers | search summary |
| 20 | Hindu, Muslim artisans cast bell for Ram Temple | The Tribune (also IANS, Swarajya) | https://www.tribuneindia.com/news/nation/hindu-muslim-artisans-cast-bell-for-ram-temple-124482 | not seen | 2026-11-01 | Bell cost Rs 21 lakh to 25 lakh | search summary |
| 21 | Country's first three-ton bell made in Kashi | Amar Ujala | https://www.amarujala.com/uttar-pradesh/varanasi/country-first-three-ton-bell-made-in-kashi-will-echo-in-mathura-2024-05-23 | 2024-05-23 | 2026-11-01 | Large bell commissions | search summary |
| 22 | 136.1 Hz Om Tuned Healing Chime | Sunreed | https://sunreed.com/136-1-hz-om-tuned-healing-chime | not seen | 2026-11-01 | Near neighbour, price | search summary |
| 23 | US8492632 Tuned bell harmonic musical instrument | USPTO | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8492632 | not seen | 2026-11-01 | Prior art | search summary |
| 24 | Bells and methods of their design and production (20120304846) | Justia Patents | https://patents.justia.com/patent/20120304846 | 2012 | 2026-11-01 | Prior art, FEA design | search summary |
| 25 | Bellfounding | Wikipedia | https://en.wikipedia.org/wiki/Bellfounding | not seen | 2026-11-01 | Eijsbouts FEA | search summary |
| 26 | Pune temple acoustics study | Annals, Univ. Politehnica Timisoara | https://annals.fih.upt.ro/pdf-full/2019/ANNALS-2019-2-10.pdf | 2019 | 2026-11-01 | Partials of temple bells | search summary |
| 27 | Ferrofluid sculpting apparatus US6290894 and ferrofluid art | Google Patents, Digital Art Archive | https://patents.google.com/patent/US6290894 | not seen | 2026-11-01 | Near neighbours | search summary |
| 28 | Magnetic Materials Background 8, Domain Observation | University of Birmingham | https://www.birmingham.ac.uk/Documents/college-eps/metallurgy/research/Magnetic-Materials-Background/Magnetic-Materials-Background-8-Domain-Observation.pdf | not seen | 2026-11-01 | Bitter method | search summary |
| 29 | Proterial to Establish a Production Site for Metglas in India | PV Magazine India | https://www.pv-magazine-india.com/?p=13836 | 2026-02 | 2026-11-01 | Incumbent JV | search summary |
| 30 | Core loss testing, Epstein and single-sheet methods; amorphous cost note | eTesters; Scribd | https://etesters.com/product/34C76FC7-A7AA-49D6-8550-F4B441D0EDE5/core-loss-tester | not seen | 2026-11-01 | Standard test methods | search summary |
