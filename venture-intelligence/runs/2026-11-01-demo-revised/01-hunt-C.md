# Hunt C: underserved and premium (Opportunity Hunter)

Date: 2026-11-01. Lens C. Brief: `runs/2026-11-01-demo-revised/00-brief.md`. Searches used: about 41. WebFetch could not reach any outside host (DNS refused), so every source below was read as a search summary only. No primary document was opened.

**Result: zero theses kept.** Two candidates came close (agarwood export desk, para-sport equipment). Both fail at least one of the buyer's three questions. Five more were killed by a cheaper or subsidised rival. This is a valid result and I did not pad it.

Deciding questions were written before searching: `runs/2026-11-01-demo-revised/01-hunt-C-questions.txt`. Payback script and output: `buyer_payback_C.py` and `buyer_payback_C.out.txt` in the same folder.

## 1. Industries chosen and why

Four unrelated industries, none on the excluded list.

| Industry | Why it might hide an opportunity now |
|---|---|
| Para-sport equipment | Athletes pay Rs 4 to 5 lakh for imported sport chairs [S1]. India hosted the World Para Athletics Championships in October 2025 [S5]. |
| Craft whisky and spirits supply chain | Indian single malt is growing and Indian cask programmes sell at Rs 2 lakh and up [S9]. Angel's share is reported at 8 to 12% a year [S10]. |
| Agarwood (Assam, Tripura) | DGFT raised chips and oil export quotas on 20 January 2025 [S11]. The first legal Assam consignment shipped in May 2026 [S12]. |
| Heritage and archive preservation | Union Budget 2025-26 raised the manuscripts mission allocation sharply [S17]. Less than ten per cent of cultural objects sit in museums [S16]. |

Also scanned with one or two searches each: coffee drying, tea plucking, bowling machines, Braille embossers, planetarium domes, dental labs, veterinary diagnostics, craft chocolate, padel, art storage, gin packaging, Kannauj attar, Miraj instruments.

## 2. Raw candidates

| # | Problem | Payer | Signal | Tag |
|---|---|---|---|---|
| 1 | Sport wheelchairs imported at Rs 4 to 5 lakh | Athlete, federation, CSR | Crowdfunding for Rs 3 lakh chair; Rs 6 lakh need after sponsor budget used up | [S1] |
| 2 | Compliant export of cultivated agarwood | Gulf buyers, growers | Quota raised; 112 kg shipped for Rs 2.35 crore | [S11][S12] |
| 3 | Cask supply and maturation for Indian malt | Distilleries | Spanish-made Solares cask already adopted | [S9][S18] |
| 4 | Mechanical drying for specialty coffee | Estates | Coffee Board subsidy 40% to Rs 25 lakh per curing unit | [S19] |
| 5 | Tea plucking labour shortage | Small growers | Machine subsidy 25% general, 100% SC/ST (2019 report) | [S20] |
| 6 | Bowling machines for academies | Academies | Listings Rs 56,000 to Rs 2,09,500 | [S21] |
| 7 | Braille embossers imported | Blind schools, state presses | Imported units Rs 3.7 lakh to over Rs 12 lakh | [S22] |
| 8 | Archival boxes and tissue imported | Archives, museums | Indian maker lists a box at Rs 100 | [S23] |
| 9 | Dental lab zirconia outsourcing | Dental labs | Only patient prices found | [S24] |
| 10 | Veterinary in-house diagnostics cost | Vet clinics | No Indian per-test cost found | [S25] |
| 11 | Planetarium domes imported | State governments | Rs 21.5 crore Mangaluru system; no Indian maker found | [S26] |

## 3. Opportunity theses

**None kept.** Below are the two closest misses, run through the full test so the cut is checkable.

### Near-miss A: Compliant agarwood export desk (cut)

- **Problem:** Small Assam growers sell trees cheaply to a few traders who control distillation around Hojai [S13]. Growers lack price discovery and struggle with CITES paperwork, so they sell to informal buyers [S13].
- **Who pays, uses, blocks:** Payer is the Gulf importer or the grower. Forest department and DGFT block (Certificate of Origin, CITES permit, restricted licence) [S12][S14].
- **Why now:** Chips quota rose from 25,000 kg to 1,51,080 kg a year for April 2024 to March 2027; oil from 1,500 kg to 7,050 kg [S11]. First legal Assam shipment on 13 May 2026 [S12].
- **Why unsolved:** (c) regulated, plus (e) fragmented growers. 
- **Existing solutions:**

| Product | Maker | Price | Date | Does | Misses |
|---|---|---|---|---|---|
| Cluster processing centres, Golaghat and Tripura (sorting, grading, distillation, testing) | Central government via NERAMAC | Rs 80 crore for both [S15] | 2026 | Connects about 5,000 growers to markets [S15] | Not yet shown as operating |
| PPP licensee tender to run Golaghat plant | NERAMAC | Not stated | draft | Operator model [S33] | Award status unknown |
| Assam Agarwood Promotion Policy 2020 | Assam government | n/a | 2020 | Policy for growers [S12] | Quota split not found |
| Informal trader and distiller network in Hojai | Private | Rs 500 to Rs 12,000 per tola of oil, wide range [S13] | n/d | Buys trees | Pays growers poorly [S13] |

Prior-art searches (8): "agarwood growers middlemen Hojai", "DGFT notification agarwood", "Assam policy first consignment", "oil price per tola", "quota allocation Assam", "cultivated chips price Vietnam Indonesia Malaysia", "Agarwood Centre Golaghat", "Kannauj attar". Not found after 8: any private compliant exporter with published prices, a failed entrant, or university trial of grower-level economics.

- **Load-bearing assumption:** A small private firm can get a share of the state quota and a CITES permit. Source needed: DGFT notification 52/2024-25 annexure and Assam Forest Department circular. **UNVERIFIED KILLER.** Search summaries say only that quota is state-wise [S11]; none says how it is split. Who could answer: Assam Forest Department or the planters' association, one phone call.
- **Cheapest rival:** Selling through the informal trader at no compliance cost, and soon the government cluster centres (subsidised). Price not found.
- **Buyer payback:** `buyer_payback_C.py`. The implied export price is Rs 2.10 lakh per kg [I: Rs 2.35 crore / 112 kg] [S12]. At that price the whole quota would be worth Rs 3,170 crore a year [I], which is not credible, so the first shipment is a top-grade price and not an average. On Rs 5,00,000 capital, with an assumed 20% margin [A], gross margin is about Rs 1.25 lakh per cycle [I]. Four cycles give Rs 5 lakh a year [I], below founder time of Rs 9 lakh at Rs 750 per hour for 1,200 hours [A].
- **Three questions:** Why buy: partly supported (growers want better prices [S13]). Why this over existing options: not supported (state cluster centres are subsidised [S15]). Why a small firm earns money: not supported (margin unknown, quota access unverified, one season of rules ending 31 March 2027 [S11]).
- **Demand evidence level:** L1, weak.
- **Verdict:** Cut. Would revive if a registered grower group confirms it cannot get quota or CITES help through the cluster centres, and a buyer quotes a price for a named grade.
- **Confidence:** low.

### Near-miss B: Indian-made sport wheelchairs and blades (cut)

- **Problem:** Para-athletes need chairs priced at Rs 4 to 5 lakh [S1]; the federation says special wheelchairs are not made in India [S1]. Mona Agarwal needed about Rs 6 lakh after her Rs 15 lakh sponsor budget ran out [S1].
- **Payer:** Not the user. Athletes crowdfund (Rs 3 lakh petition) [S1]. Government aid scheme ADIP is capped; a secondary source reports Rs 15,000 for a wheelchair from 26 September 2024, unconfirmed [S6]. Sports funds buy bows and kits for archers at about Rs 3.5 lakh per athlete [S7].
- **Existing solutions:**

| Product | Maker | Price | Date | Does | Misses |
|---|---|---|---|---|---|
| YD One daily active chair, 9 kg | IIT Madras and Thryv Mobility | Rs 74,700 [S4] | Jul 2025 | Light rigid chair at one-third of import | Not a sport chair; no sport plans found [S4] |
| Sport-specific repair and support | Ottobock with Paralympic Committee of India | Free on-site repairs [S5] | Mar 2025 onward | About 300 repairs at the Oct 2025 championships [S5] | Supply terms unclear |
| Imported sport chairs | foreign makers | Rs 4 to 5 lakh [S1] | 2024 | Competition chairs | Price, import wait |
| Low-cost racing chair (abroad) | Motivation, with the Agitos Foundation | under USD 1,000 [S8] | 2012 | Cheap racing chair | Old, not Indian |

Prior-art searches (7): sport wheelchair cost India, Indian-made sports wheelchair startup, ADIP guidelines, Ottobock-PCI, Khelo India Para Games, YD One, TOPS equipment. Not found: an Indian sport-chair maker with a price list; wheelchair-user counts.

- **Load-bearing assumption:** A funded payer buys at scale. Primary source not reached (ADIP official guideline PDF, TOPS rules). **UNVERIFIED KILLER.** Answer from the Ministry of Social Justice or Sports Authority of India.
- **Cheapest rival:** Donated chairs (16 sports chairs and 20 by sponsors reported) [S2], and the do-nothing option of a second-hand or crowdfunded import.
- **Buyer payback:** Pool is about 1,300 athletes in all sports [S3]. If 30% use chairs and replace every 4 years [A], that is about 98 chairs a year [I]. At an assumed Rs 1.5 lakh local price [A] the whole market is about Rs 1.46 crore a year [I]. A 30% share at 30% margin gives about Rs 13 lakh gross profit [I], 1.46x founder time [I]. The buyer saves about Rs 3 lakh once [I] but has no income stream to repay it.
- **Three questions:** Why buy: supported (price gap) [S1]. Why this over the existing options and cheapest rival: partly (IIT Madras spinout can extend to sport; Ottobock holds the federation) [S4][S5]. Why a small firm earns money: not supported (tiny pool, payer without budget, grant-funded rivals).
- **Demand evidence level:** L1.
- **Verdict:** Cut on payer and pool size. Confidence: medium.

## 4. Cut candidates and reasons

| Candidate | Why cut |
|---|---|
| Cask supply for Indian malt | Reason (a) and incumbent. Solares cask, built for warm climates, is already adopted by Indian distilleries and its maker says 10,000 casks are possible [S18]. Casks are stacking up unused near Delhi [S34]. Fast tropical maturation is a selling point, not a defect [S10]. No Indian cask shortage found. |
| Specialty coffee dryers | Subsidised rival: 40% grant up to Rs 25 lakh per curing unit, dryer eligible [S19]. Pain not evidenced; estates dry on raised beds in polyhouses [S27]. |
| Tea plucking machines | Subsidised rival: 25% general, 100% SC/ST in a 2019 report (stale), 50% in Himachal with a cap [S20]. Machines and an IIT Guwahati prototype exist [S20]. |
| Bowling machines | Indian makers sell at Rs 56,000 to Rs 2,09,500 [S21]. No import gap. |
| Braille embossers | Payer is state schools and presses with thin budgets [S22]. Several low-cost efforts exist (Tactall, Drishti, OpenBraille) [S35]. Margin too small. |
| Archival boxes and tissue | Commodity. An Indian maker lists a box at Rs 100 with a 50-piece minimum [S23]. National Archives buys by tender through GeM [S36]. No margin for a newcomer. |
| Dental lab zirconia | Mature, crowded, only patient prices found (Rs 8,000 to Rs 25,000 a tooth) [S24]. |
| Vet diagnostics | No Indian per-test cost found; clinic prices only [S25]. Unresolved, not pursued. |
| Planetarium domes | Government buyer, project sizes of Rs 21.5 crore and up [S26]. Capital far over Rs 5,00,000 and tender-led. |
| Craft chocolate equipment | Segment about Rs 10 crore in sales [S28]. Too small. |
| Padel courts | Crowded, trend-led; cost Rs 18 to 33.5 lakh a court [S29]. Common startup theme. |
| Fine art storage | Served: Saffronart, Crown, Astaguru run climate-controlled vaults [S30]. |
| Kannauj attar | Declining market, 90% goes to tobacco flavouring [S31]. Weak demand. |
| Miraj instruments | Evidence is seller-side only; no buyer complaint data [S32]. |

## 5. Sources

All pages were read as search summaries. WebFetch failed on `outlookindia.com`, `pdicai.org`, and `theprint.in` (hosts not reachable from this session; they would need allowing in network settings).

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Funds to buy new wheelchair hindering champion para shooter Mona's preparation | Daily Pioneer | https://dailypioneer.com/2024/sports/funds-to-buy-new-wheelchair-hindering-champion-para-shooter-mona-s-paralympic-preparation.html | 2024 | 2026-11-01 | Chair cost, funding gap | search summary |
| 2 | Para athletes get sports kits, wheelchairs (Project Wings) | Lokmat Times / ANI | https://www.lokmattimes.com/other-sports/para-athletes-get-sports-kits-wheelchairs-to-enter-national-international-level-championships/amp | 2023-03-30 | 2026-11-01 | Donated chairs | search summary |
| 3 | Khelo India Para Games 2025 | Newsonair | https://newsonair.gov.in/khelo-india-para-games-2025-to-conclude-with-grand-closing-ceremony-in-new-delhi-today | 2025-03-27 | 2026-11-01 | Participant count | search summary |
| 4 | IIT Madras launches YD One | IIT Madras | https://www.iitm.ac.in/happenings/press-releases-and-coverages/iit-madras-develops-launches-indias-lightest-active | 2025-07-16 | 2026-11-01 | YD One price | search summary |
| 5 | Ottobock supports India's largest para-sporting event | Ottobock | https://corporate.ottobock.com/en/media/newsroom/ottobock-supports-indias-largest-para-sporting | 2025 | 2026-11-01 | Support terms | search summary |
| 6 | ADIP scheme: free wheelchairs and hearing aids | righttoinformation.wiki | https://righttoinformation.wiki/adip-scheme-disability-aids-appliances-india | 2024 | 2026-11-01 | ADIP cap (unconfirmed) | search summary |
| 7 | Sports Authority of India MOC approves second bow sets, TOPS archers | SAI | https://sportsauthorityofindia.nic.in/sai_new/public/assets/uploads/press_release/1660649899_72nd MOC approves financial assistance for second bow sets for Asian Games and World Cup bound TOPS Archers.pdf | 2022-08-16 | 2026-11-01 | Rs 3.5 lakh per archer equipment | search summary |
| 8 | IPC supports design of low-cost racing chair | Paralympic.org | https://www.paralympic.org/news/ipc-supports-design-low-cost-racing-chair | 2012 | 2026-11-01 | Foreign low-cost chair (stale) | search summary |
| 9 | Cask Couture: private cask ownership in India | Business Today | https://www.businesstoday.in/magazine/deep-dive/story/cask-couture-how-private-cask-ownership-is-redefining-luxury-in-indias-whiskey-landscape-497651-2025-10-10 | 2025-10-10 | 2026-11-01 | Cask prices | search summary |
| 10 | Why does Indian whisky mature so fast | The Whiskey Wash | https://thewhiskeywash.com/whiskey-articles/why-does-indian-whisky-mature-so-fast-the-science-of-tropical-aging/ | 2025 | 2026-11-01 | Angel's share | search summary |
| 11 | DGFT amends export policy for agarwood chips, powder, oil (Notification 52/2024-25) | Taxscan | https://www.taxscan.in/?p=481190 | 2025-01-20 | 2026-11-01 | Quotas, dates | search summary |
| 12 | Assam exports first consignment of agarwood chips to Saudi Arabia, UAE | Daily Pioneer | https://www.dailypioneer.com/news/saudi-uae-receive-export-consignment-valued-at-rs-2-35-crore-from-assam | 2026-05 | 2026-11-01 | First export, value, permits | search summary |
| 13 | Agarwood: Assam's next big rural economy | Sentinel Assam | https://www.sentinelassam.com/more-news/editorial/agarwood-assams-next-big-rural-economy | n/d (2025) | 2026-11-01 | Grower position, tola prices | search summary |
| 14 | Government increases export limits for agarwood and agar oil | Legality Simplified | https://legalitysimplified.com/?p=61047 | 2025 | 2026-11-01 | Permit requirements | search summary |
| 15 | Scindia launches Rs 80 crore agarwood value chain scheme in Tripura | GKToday | https://www.gktoday.in/scindia-launches-%E2%82%B980-crore-agarwood-value-chain-scheme-in-tripura/ | 2026-01 | 2026-11-01 | Cluster centres | search summary |
| 16 | Preserving heritage: India needs 10,000 trained conservators | Daily Excelsior | https://www.dailyexcelsior.com/?p=2214624 | n/d (2024) | 2026-11-01 | Museum coverage | search summary |
| 17 | National Mission for Manuscripts and Gyan Bharatam | Drishti IAS | https://www.drishtiias.com/daily-updates/daily-news-analysis/gyan-bharatam-mission-and-nmm/print_manually | 2025-02-04 | 2026-11-01 | NMM allocation | search summary |
| 18 | SOLARES: Dhavall Gandhi's game-changer for Indian whisky maturation | Master of Malt | https://www.masterofmalt.com/blog/post/solares-dhavall-gandhis-game-changer-for-indian-whisky-maturation | 2025 | 2026-11-01 | Incumbent cask | search summary |
| 19 | Notification and modalities for support to curing units 2026 | Coffee Board | https://coffeeboard.gov.in/Schemes/Notification and Modalities for support to  Curing Units 2026.pdf | 2026 | 2026-11-01 | Dryer subsidy | search summary |
| 20 | Assam tea growers start no sickles campaign; Himachal 50% subsidy on plucking machines | Eastern Mirror; Newsdrum | https://www.newsdrum.in/business/himachal-govt-to-provide-50-pc-subsidy-on-tea-plucking-machines-equipment | 2019 | 2026-11-01 | Plucker subsidies (stale) | search summary |
| 21 | Cricket bowling machine listings | IndiaMART | https://m.indiamart.com/impcat/cricket-bowling-machine.html | n/d (2026) | 2026-11-01 | Indian machine prices | search summary |
| 22 | Braille printing machine listings; Indian Braille innovation article | IndiaMART; See Positive | https://m.indiamart.com/impcat/braille-printing-machine.html | 2026 | 2026-11-01 | Embosser prices | search summary |
| 23 | Acid free archival box listing | TradeIndia | https://www.tradeindia.com/products/acid-free-archival-box-for-textiles-photographic-materials-natural-history-collection-8393853.html | n/d (2026) | 2026-11-01 | Box price | search summary |
| 24 | Zirconia crown price in India | DocIndia | https://www.docindia.org/healthblog/articles/zirconia-crown-price-in-india | 2025 | 2026-11-01 | Patient prices | search summary |
| 25 | Feline blood test cost in India | Vetic | https://vetic.in/blog/pet-health/feline-blood-test-cost-in-india-types-and-pricing-explained/ | 2025 | 2026-11-01 | Clinic prices only | search summary |
| 26 | Pilikula planetarium inaugurated | Udayavani | https://www.udayavani.com/english-news/pilikula-swami-vivekananda-planetarium-inaugurated | 2022 | 2026-11-01 | Dome project cost | search summary |
| 27 | Onyx Coffee India Kerehaklu Estate | Sigma Coffee | https://sigmacoffee.co.uk/products/onyx-coffee-india-kerehaklu-estate | 2025 | 2026-11-01 | Drying methods | search summary |
| 28 | Bean-to-bar chocolate makers circle India | Confectionery News | https://www.confectionerynews.com/Commodities/India-single-origin-chocolate-Brands-to-build-up-cocoa-sector | 2020 | 2026-11-01 | Segment size (stale) | search summary |
| 29 | Padel court business in India: cost, investment | Franchise India | https://www.franchiseindia.com/insights/en/article/padel-court-business-in-india-cost-investment-space-profit.59902 | 2025 | 2026-11-01 | Court cost | search summary |
| 30 | The rise of fine art in India: logistics | Crown Fine Art | https://www.crownfineart.com/articles/the-rise-of-fine-art-in-india-the-role-of-logistics-in-a-fast-growing-market | 2025 | 2026-11-01 | Vault supply | search summary |
| 31 | Can ittar town survive with French help? | Business Standard | https://www.business-standard.com/article/beyond-business/can-ittar-town-survive-with-french-help-115060600797_1.html | 2015-06-06 | 2026-11-01 | Attar decline (stale) | search summary |
| 32 | Once buzzing with music, sitar gallis of Miraj go silent | The Federal | https://thefederal.com/features/once-buzzing-with-music-sitar-gallis-of-miraj-go-silent-under-covid-shadow | 2020 | 2026-11-01 | Instrument trade | search summary |
| 33 | Draft RFP: agarwood processing, Golaghat (PPP licensee) | NERAMAC | https://www.neramac.com/files/draft-rfp-agarwood-processing-assam-golaghat.pdf | n/d (2025) | 2026-11-01 | Operator tender | search summary |
| 34 | India's love of homegrown single malts shakes up Pernod, Diageo | Reuters via The Star | https://www.thestar.com.my/business/business-news/2023/12/19/indias-love-of-homegrown-single-malts-shakes-up-pernod-diageo | 2023-12-19 | 2026-11-01 | Casks stacking up at Indri | search summary |
| 35 | IIT Guwahati student innovates low-cost braille printer | The Better India | https://thebetterindia.com/296335/iit-guwahati-student-innovates-low-cost-braille-printer | n/d (2020) | 2026-11-01 | Low-cost Braille efforts | search summary |
| 36 | Notice inviting e-tender: acid free carton boxes | National Archives of India | https://nationalarchives.nic.in/sites/default/files/2025-01/NITBOX.pdf | 2024-12-21 | 2026-11-01 | Tender buying | search summary |
