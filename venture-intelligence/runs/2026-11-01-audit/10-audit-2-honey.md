# Audit 2: Honey pre-screen at the collection point (hunter claim I5)

Date: 2026-11-01. Critic: independent. Script: `runs/2026-11-01-audit/10-audit-2-honey-econ.py`.
Limits of this audit: WebFetch could not resolve eicindia.gov.in, techindiacsir.anusandhan.net, apac.cxotv.news (network not allowed), so every source below is `via search summary`. No page was opened. I could not read the EIC honey circular, the FSSAI RAFT approved list, or any lab price list.

## 1. Steelman

India exported about 100,773 tonnes of honey worth USD 206.47 million in 2024-25, about 78% to the US [S1]. Exports need NMR testing, done at a small number of places [S2]. Small beekeepers and FPOs have no way to know before a lot travels whether a bought-in lot will pass. A cheap reader at the collection point could cut failed lots and testing cost, and nobody appears to sell it.

## 2. Claims checked

| # | Claim (I5) | My finding | Status | Tag |
|---|---|---|---|---|
| 1 | NMR mandatory for exports since 1 Aug 2020 | Several news sources say 1 Aug 2020; one low-reliability source says February 2020. Issuer is Commerce/EIC, not FSSAI. Domestic sale does not require NMR [S2][S3]. Circular itself not read. | Partly verified | [S2][S3] |
| 2 | NMR fee INR 15,000 to 25,000 | Not found in any lab list. Seen: INR 5,000 to 15,000 and "a few hundred" from the same seller blog, neither with a tariff [S4]; a general university 1H NMR rate of INR 1,200 to 1,300 per sample [S5], not a honey test. | Unverified, range wide | [S4][S5] |
| 3 | Export value USD 206m | Matches APEDA/DGCIS figure [S1]. | Verified | [S1] |
| 4 | CSIR-CEERI patent, 8% detection limit | A CSIR handheld detector patent application exists (IN202411019851) and a technology profile [S6]. I could not see the 8% figure or what adulterants it covers. Patent stage, no price found. | Existence verified, limit unverified | [S6] |
| 5 | Dabur mobile lab 2017 | Dabur launched a mobile honey lab, a lab on wheels, not a device sold to others [S7]. | Verified | [S7] |
| 6 | "No startup selling a screener to beekeepers" (1 search) | I ran 3 differently worded searches and found no Indian seller. Found others: Honey.AI pollen microscope for beekeepers, traders and customs (Microfy, EU) [S8]; academic low-cost multispectral and smartphone work [S9][S10]. Absence in my searches is not proof of absence. | Not contradicted; incomplete | [S8][S9][S10] |
| 7 | 5% failure rate | No source. Hunter did not label it. I found no Indian export-lot failure rate. | Missing | [A] |
| 8 | Screening at INR 300 avoids about INR 775 per lot | 5% x 15,000 = 750, minus 300 = 450. The 775 does not reconcile [I]. | Arithmetic error | [I] |
| 9 | A rejected export lot is "the real prize" | No value found. Exporters report paying farmers INR 85/kg after testing vs INR 65-75 domestic, a politician/industry claim [S11]. | Missing | [S11] |

## 3. Existing methods (what a cheap reader competes with and where it breaks)

| Method | Detects | Limit / weakness | Who sells in India |
|---|---|---|---|
| Lab NMR (EIC Mumbai lab, others) | Profile deviation vs honey database; flags syrups. | Reported to detect additives but not the amount [S12]. UK FSA: not accepted as a yes/no regulatory test in UK/EU, widely used [S11]. FSSAI said no Indian honey database exists, so NMR utility is limited [S3]. | EIC, NDDB CALF (honey lab, NABL) [S13], private labs |
| C3/C4 isotope tests (FSSAI-prescribed) | Cane/corn syrup | CSE's spiking test: all spiked samples but one passed C3/C4. The failure was 25% honey + 75% syrup [S12]. | Labs |
| SMR (Specific Marker for Rice syrup) | Rice syrup | Made mandatory by FSSAI [S3]; TMR not mandatory. | Labs |
| Portable NIR (research) | Syrup, origin | Pure vs adulterated 92% accuracy; quantification only above about 10% (unifloral) to 20% (multifloral) adulterant, 244 samples [S14]. | Not sold as a honey product that I found |
| Portable FTIR (research) | Sucrose, HMF, adulteration | 147 samples, no sample prep [S14]. | Research |
| Smartphone/multispectral (research) | Cane syrup | 6-wavelength device, accuracy 0.91 to 0.98 for cane syrup [S9]. Small lab sets; model accuracy 100% claims on own test sets [S10]. | Research |
| Home tests (water/flame/paper) | Crude dilution | Water test does not detect rice/corn syrup [S15]. | Free |
| FSSAI RAFT | See below | No honey kit found on any approved list I could see. | Not applicable |

Not found after 3 searches on Indian kit pricing: Indiamart, Amazon.in or Dabur kit with INR price (queries: "honey purity test kit price indiamart", "honey adulteration tester", "honey purity tester refractometer"). No detection limits, false-positive rates or per-test costs for commercial kits are available to me. Raman: no limit-of-detection source found.

**RAFT, exactly.** RAFT is Rapid Analytical Food Testing: FSSAI's scheme to approve kits, equipment and methods so food safety officers and mobile labs can do on-the-spot field tests, for screening and surveillance, not legal proof [S16]. A manufacturer applies on the RAFT portal with third-party validation; final approval carries a three-year certificate, provisional one year [S16]. At one snapshot 53 approved, 12 provisional, 44 rejected of 109 [S16]. RAFT is not a honey programme and not an export programme. A RAFT approval would make a kit usable by regulators; it does not make its result accepted by EIC. The approved list (status PDF dated 13 April 2026) exists but I could not read it [S16].

**FSSAI 2024-25 honey guidance.** Not found after 3 searches (queries: "FSSAI honey 2024 2025 guidance testing parameters", "FSSAI honey advisory SMR TMR NMR", "FSSAI RAFT approved honey kit"). All results dated 2018 to 2021.

**Technical bottom line.** Syrups are sold as "all pass" products designed to defeat C3/C4 and Indian protocols [S12]. A cheap reader trained on authentic honey has to catch blends of those syrups at low percentages. Best published portable results quantify only above 10-20% adulterant [S14]. A blend at 10% syrup can plausibly pass such a reader [I: published limit above 10%]. Whether it can meaningfully screen modern syrups is unproven, and the published evidence points against reliability at low blends [I]. Unknown: whether any study tested "beat-the-test" syrups specifically. Confidence: medium.

## 4. Buyer value

- Who pays for a failed lot: the exporter (who holds the lot and the NMR bill), then the aggregator or FPO if the exporter passes the loss back. No source on who bears it. [H]
- How often lots fail: no EIC/APEDA rejection statistics found after 3 searches (queries: "honey export rejection NMR failed consignments India", "EIC NMR failed lots", "APEDA honey rejected"). 2009-10 EIC data: 29.2% of 362 samples exceeded antibiotic or heavy-metal limits, old and not about syrup [S17]. Missing.
- Export price context: an NBB executive reported prices falling from about USD 2,900 to 1,500 per tonne because of adulteration [S11]. Minimum export price was cut from USD 2,000 to 1,400 per tonne to 31 Dec 2025 [S18]. Thin margins mean exporters care about per-lot cost.
- What buyers pay now: NMR fee unknown (see claim 2). EIC lab described as the only testing point and as hard for small beekeepers to access [S11][S12]. This is access friction, which is real demand evidence at L1 only if you read it as buyers wanting something nearby, but it supports a cheap fast screen, not necessarily a screen with this accuracy [I].
- Who would pay: exporters running bought-in lots are the only party with a cost and a rejection to avoid [I]. Beekeepers lose only if their lot is refused, and have no money for devices [H].
- Demand level: L0 to weak L1. No buyer has spoken.

## 5. Rules

- Export: NMR is required for export consignments, via EIC [S2]. A pre-screen has no legal status. Only the notified lab result counts [I: EIC requires its own lab test; circular not read].
- Domestic: FSSAI makes SMR mandatory; NMR and TMR are not [S3].
- RAFT approval would give the reader standing for FSSAI field officers only, as a screening tool [S16].
- US CBP uses NMR for all honey imports [S11]; EU uses its own suspicion tests (46% of 320 imported samples suspicious in 2021-22; India not in the figures I found) [S19].
- APEDA/NMPB requirements: not found beyond the above. Missing.

## 6. Economics (script: `10-audit-2-honey-econ.py`)

All device and library figures are assumptions; I found no component or vendor catalogue prices.

- Value of screening per lot = failure rate x sensitivity x NMR fee [I]. At fee INR 15,000 `[A]`, 5% failure `[A]`, a screen that flags half of failing lots saves INR 375 a lot, only INR 75 more than a INR 300 screen cost; at 10% sensitivity it loses `[I]` (script).
- At fee INR 500, saving never exceeds INR 75 a lot at 15% failure and full sensitivity, so test-cost saving fails [I].
- A negative screen does not skip NMR (the law still demands it), so saving arises only on lots the screen stops from being sent [I].
- Reachable pool: 97 beekeeper/honey FPOs formed by March 2025 [S20]; 14,859 beekeepers, 269 societies, 150 firms, 206 companies on the NBB portal (Oct 2025) [S20]. Exporter and aggregator counts not found; I assumed 150 and 100 [A]. Total about 347 [A]. At 10% share and INR 60,000 device, revenue is about INR 21 lakh once [I]. Consumables and subscription unknown.
- BOM assumed about INR 22,000 for a NIR-class unit [A], basis: none sourced, test by getting 2 module quotes.
- Calibration library: 500 to 2,000 authentic, reference-labelled honeys at INR 3,000 to 15,000 each is INR 15 lakh to INR 300 lakh [A], against a default founder capital of INR 5 lakh. Published portable studies used 59 to 244 samples [S14], which is small and shows why they do not generalise to new floral sources and syrups [I].
- Verdict on economics: library cost alone exceeds founder capital unless a research partner supplies samples. Medium confidence, because the inputs are assumptions.

## 7. Distribution

- First 10: FPOs formed under NAFED, NDDB and TRIFED (60/26/14 of 97) [S20] are reachable through those agencies; exporters through APEDA/NBB workshops [S21]. Channel plausible for 10 [I].
- First 100: pool is about 350 organisations [A], so 100 customers is about 30% of all of them. Not credible [I]. Alternative is lab-as-a-service rather than devices [H].

## 8. Where the hunter's reasoning went wrong

1. "NMR mandatory since 1 Aug 2020 [S16]" presented with one date; sources conflict (Aug vs Feb 2020) and the mandate is export-only. Error: single-source certainty; export vs domestic confusion.
2. Treated the INR 15,000 to 25,000 fee as the buyer's value without verifying it `[S4]`; the other candidate was "a few hundred". Error: anchoring on an unverified number. Then the economics were conditional on an unknown (the hunter admitted this).
3. The "5% failure rate" `[A]` has no source and no label. Error: invented parameter inside a calculation.
4. Arithmetic: 750 - 300 is 450, not 775. Error: calculation mistake.
5. Assumed the reader catches syrup at "8% limit" from a patent. A patent limit is a claim, not validation, and says nothing about syrups built to pass tests. CSE showed designed syrups pass C3/C4 [S12]. Error: treating a claim as performance; ignoring an adversary who adapts.
6. Assumed a pre-screen has value without asking whether it replaces NMR. It does not; the law still requires NMR. Error: ignoring the process the test sits in.
7. "No startup found after 1 search" used as support for originality. Error: absence of evidence from a single search. I found related efforts in 3 searches.
8. Confused total export value (USD 206m `[S1]`) with the value of the pre-screening need. Error: market size vs addressable spend.
9. Overlooked the calibration-data problem entirely. Error: skipping the hardest dependency.
10. "Buyers: aggregators, FPOs, exporters" with no count, and "beekeeper collection point" without noting beekeepers cannot pay. Error: user and payer conflated.
11. Rated desirability Medium with no buyer evidence (L0). Error: unsupported rating.

## 9. What holds up

- Export size and US share [S1].
- NMR access friction for small beekeepers (EIC lab described as the only point, hard to access) [S11][S12].
- Technology interest is real: CSIR patent, EU and academic prototypes [S6][S8][S9][S14].

## 10. Objections

- Fatal (on current evidence): a low-cost reader unlikely to detect designed syrups at blends below 10-20% [S12][S14]; a pre-screen has no legal weight and does not remove the NMR bill [S2][I]. Both could be reversed only by evidence I did not find.
- Major: library cost versus capital [A]; buyer pool about 350 [A]; NMR fee unknown; failure rate unknown.
- Minor: date and issuer of the NMR mandate to confirm.

## 11. Simpler alternatives

Sell nothing hardware: a pooling and traceability service where lots are NMR-tested once per pooled batch (aggregation spreads testing cost across small producers [S11]). Or a sampling plan service: test every n-th lot. [H]

## 12. Verdict: REJECT in the form proposed (low-cost reader); revisit only on named evidence

Reasons: designed syrups defeat cheap tests and published portable methods quantify only above about 10-20% [S12][S14]; a pre-screen only saves the NMR fee on lots it correctly stops; the arithmetic is unsupported and was mis-stated; calibration data likely exceeds founder capital [A]. This is reject on credible figures and on contradicted technical premise, not on missing evidence, but confidence is medium because I read no full papers, circulars or price lists.

What would change it to INVESTIGATE: (1) a written NMR tariff from EIC or NDDB CALF above about INR 10,000 per lot `[A]`; (2) a validation study or CSIR data showing detection of "all-pass" rice/beet syrup blends at 5% or below on blind samples; (3) one exporter confirming it would reject lots on a screen result and not re-test; (4) free access to a reference library (CSIR/NDDB).
What would move to ADVANCE: all four plus L2 evidence from three exporters.

## Not checked

EIC honey circular text, RAFT approved list contents, NDDB tariff, APEDA rejection data, exporter count, Indiamart/Amazon listings, component prices, patents beyond one CSIR entry.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | APEDA honey dashboard / India Briefing honey exports 2026 | APEDA; India Briefing | https://apeda.gov.in/sites/default/files/2025-10/MIC_Monthly_dashboard_Honey_22092025.pdf | 2025 | 2026-11-01 | Export volume, value, US share | search summary |
| 2 | Govt wants NMR testing mandatory for honey exported from India | Business Insider India / News Nation | https://www.businessinsider.in/business/news/govt-wants-nmr-testing-mandatory-for-honey-exported-from-india/articleshow/72212477.cms | 2019 | 2026-11-01 | Export NMR requirement, EIC lab | search summary |
| 3 | FSSAI reviews issue raised by CSE; Honey I shrunk the tests | foodsafetyhelpline; FoodNavigator | https://www.foodnavigator.com/Article/2020/06/29/Honey-I-shrunk-the-tests-India-retains-just-one-of-three-major-quality-parameters-prompting-adulteration-fears/ | 2020-06-29 | 2026-11-01 | SMR mandatory, TMR not, NMR limited utility | search summary |
| 4 | Fake honey / fake honey test | Organic Mandya (seller blog) | https://www.organicmandya.com/know-your-food/sweeteners/fake-honey-test/ | n/d | 2026-11-01 | NMR cost claims (weak) | search summary |
| 5 | NMR test price | Indrashil University | https://indrashiluniversity.edu.in/brochures/pdf/NMR_TEST_PRICE.pdf | 2023 | 2026-11-01 | General 1H NMR rate | search summary |
| 6 | Handheld non-destructive honey adulteration detection system IN202411019851 | CSIR Technology Portal | https://techindiacsir.anusandhan.net/online/handheld-non-destructive-honey-adulteration-detection-system-and-method-IN202411019851-patent.htm | 2024 | 2026-11-01 | CSIR prior art | search summary |
| 7 | Dabur launches Mobile Honey Testing Lab | exchange4media | https://www.exchange4media.com/marketing-news/dabur-india-launches-country's-first-mobile-honey-testing-lab-68041.html | 2017 | 2026-11-01 | Dabur lab | search summary |
| 8 | Honey.AI practice abstract | EU CAP Network | https://eu-cap-network.ec.europa.eu/projects/practice-abstracts/honeyai_en | n/d | 2026-11-01 | Pollen microscope for beekeepers | search summary |
| 9 | Low-cost multispectral device for honey adulteration | KMITL/TCI | https://li01.tci-thaijo.org/index.php/cast/article/view/265920 | 2025 | 2026-11-01 | Multispectral accuracy | search summary |
| 10 | Smartphone camera honey study | Smart Agricultural Technology | https://doaj.org/article/2195a47e75ee43fcb5642b06345665c5 | 2024-08 | 2026-11-01 | Smartphone ML | search summary |
| 11 | Strategies to Boost India's Honey Exports; NMR coverage | ICRIER; UK FSA; others | https://icrier.org/publications/strategies-to-boost-indias-honey-exports/ | n/d | 2026-11-01 | Access friction, price fall, FSA view | search summary |
| 12 | It's not honey: how the magic syrup beat Indian testing protocols | Down To Earth / CSE | https://www.downtoearth.org.in/health/it-s-not-honey-how-the-magic-syrup-beat-indian-testing-protocols-74496 | 2020-12 | 2026-11-01 | All-pass syrups, C3/C4 spiking | search summary |
| 13 | NDDB honey testing laboratory | NDDB | https://www.nddb.coop/node/1896 | 2020-07 | 2026-11-01 | CALF lab, no tariff | search summary |
| 14 | Portable NIR to trace honey origin and detect syrup adulteration | PMC | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11476024/ | 2024 | 2026-11-01 | Portable NIR/FTIR limits | search summary |
| 15 | Honey purity guides | Organic Mandya; others | https://www.organicmandya.com/know-your-food/adulteration-in-india/fake-honey/ | n/d | 2026-11-01 | Home tests limits (weak) | search summary |
| 16 | RAFT kit/equipment/method; approved status lists | FSSAI | https://fssai.gov.in/cms/raft.php | 2026-04 list | 2026-11-01 | What RAFT is | search summary |
| 17 | The Honey Trap | Down To Earth | https://www.downtoearth.org.in/news/health/the-honey-trap-74476 | 2020 | 2026-11-01 | Old EIC sample data | search summary |
| 18 | Govt cuts minimum export price on natural honey | Outlook Business | https://www.outlookbusiness.com/economy-and-policy/govt-cuts-minimum-export-price-on-natural-honey-to-usd-1400-per-tonne-till-dec-31-this-year | 2025 | 2026-11-01 | MEP | search summary |
| 19 | EU coordinated action honey 2021-2022 | European Commission | https://food.ec.europa.eu/food-safety/eu-agri-food-fraud-network/eu-coordinated-actions/honey-2021-2022_en | 2023-03 | 2026-11-01 | 46% suspicious | search summary |
| 20 | FPO and NBB registration counts | PIB; SFAC; NBB | https://sfacindia.com/UploadFile/Statistics/RS Qus No. S1498 dt. 28.01.2025.pdf | 2025 | 2026-11-01 | Honey FPO and beekeeper counts | search summary |
| 21 | NBB workshop on export potential of honey | Krishi Jagran | https://krishijagran.com/agriculture-world/national-bee-board-hosts-workshop-on-strengthening-of-export-potential-of-honey | n/d | 2026-11-01 | Channel | search summary |
