# Hunt C: underserved and premium (2026-11-01)

Lens C. Four industries only: craft spirits and supply chain, aromatic natural products, para-sport and assistive equipment, archive and heritage preservation. No fifth added. Founder defaults from the brief: capital Rs 5,00,000 [A] (brief default), time Rs 750 an hour [A] (brief default). Economics script: `runs/2026-11-01-controlled/01-hunt-C-econ.py` (run output reproduced in the text where used).

Method limits. WebFetch failed on every page tried (hosts not resolvable here), so every source is `via search summary`. Prices and counts below are read from search-result text, not from opened pages. Rupee conversions use Rs 85 per USD, 2026-11-01 [A] (assumed rate, not checked).

## Verdict

Nothing exceptional yet. One thesis is kept as a weak INVESTIGATE (agarwood export-lot assay in Assam). Four evidence-backed theses are REJECT. Three exploratory bets were given a real attempt; all three fail the even-if-true test on "Large enough, within means". No winner is manufactured.

## 1. Industries chosen and why

1. Aromatic natural products (agarwood, sandalwood, attar).
   - Assam made its first legal agarwood chip export on 13 May 2026, 112 kg worth Rs 2.35 crore [S6, S7], about Rs 2,09,821 per kg [I] (2.35 crore / 112 kg, script).
   - No grading standard in force was found for Assam exporters [S56]; Indonesia grades by SNI 7631-2011, which rests on a grader's senses [S53].
2. Premium and craft spirits.
   - Indian casks lose 10 to 12% a year to evaporation [S41], and one maker adds 12% a year interest on stock [S42]. The cask-ownership market in India is new [S43].
   - Kentucky holds a record 16.1 million barrels [S44], so imported used casks are not scarce on that side.
3. Para-sport equipment.
   - A sports wheelchair costs Rs 4 to 5 lakh imported against about Rs 40,000 for an ordinary chair [S23]. Athletes crowdfund chairs [S23]. Banks and CSR donors already fund kits [S28].
4. Archive and heritage.
   - About 80% of Indian manuscripts are privately held [S39]. Private business records are held by families who lack preservation standards [S40].
   - The National Archives tendered for acid-free boxes with a pH floor of 7.0 [S36].

## 2. Raw candidates

| # | Problem | Payer | Signal | Tag |
|---|---|---|---|---|
| 1 | No objective grade or lot certificate for Assam agarwood chips and oil | Exporters, growers | First export May 2026, no standard in force [S6, S56]; adulteration with solvents and cooking oil needs GC-MS to detect [S10] | [S] |
| 2 | Sports wheelchairs priced out of reach | Athletes, CSR, banks | Rs 4 to 5 lakh imported [S23]; Rs 65,000 domestic [S24] | [S] |
| 3 | Growers cannot see heartwood in standing sandalwood | Growers | Only ERT training at ICFRE [S18]; no validated NIR in standing trees found [S19] | [S] |
| 4 | Cask contents cannot be checked without opening | Cask owners, warehouses | Strathclyde prototype [S1]; Inspectahire product [S2] | [S] |
| 5 | Imported archival boxes cost Rs 7,285 to 11,645 each | Archives, museums | [S34]; domestic listing Rs 100 to Rs 1,000 with no stated test [S35] | [S] |
| 6 | Analogue video tape backlog | Broadcasters | Doordarshan about 70,000 hours [S37] | [S] |
| 7 | Sandalwood oil shortage in Kannauj | Attar makers | Oil about Rs 1 lakh per kg [S22] | [S] |
| 8 | Private manuscripts lack conservation | Owners | 80% private [S39] | [S] |
| 9 | Sports blades cost Rs 2.5 to 10 lakh | Athletes | Vendor figures [S32] | [S] |
| 10 | Standing high-value trees cannot be insured against theft or valued for credit | Growers, lenders | UIIC wording excludes theft and 20% first loss [S21] | [S] |
| 11 | Warehouse placement in hot climates is uncontrolled | Distilleries | Mapping is routine in pharma [S45] | [S] |

## 3. Evidence-backed theses

### T1. Agarwood export-lot assay and grade certificate (Assam). Outcome: INVESTIGATE (weak)

**Original.** Five nearest methods:
1. Human graders by smell, colour, weight (traditional practice) [S53].
2. Lab GC-MS at government labs, Rs 4,000 plus GST per sample at IIHR, top five peaks only [S15].
3. FRIM Malaysia resin-content grading by Z-score, a research method, no service found [S12, S54].
4. Cheap e-nose on an Arduino for Gyrinops, research only [S52].
5. Bench NIR on powdered chips predicting resin, research only [S52].

Also near: DNA barcoding for species ID [S14]; image-based chip grading at 62.8% accuracy [S52]; a vendor blog series on blockchain traceability, unvalidated [S14].

Novelty queries run (10): "agarwood oud chips grading authentication GC-MS lab price"; "agarwood chips handheld NIR OR e-nose grading"; "agarwood traceability DNA tagging provenance CITES blockchain"; "agarwood quality grading laboratory certificate service Indonesia Malaysia Thailand startup kit"; "patent agarwood grading device OR method spectral resin"; "Assam first agarwood export Gulf certification grading standard"; "Assam Agarwood Promotion Policy registered growers exporters"; "CSIR NEIST agarwood oil testing service BIS"; "agarwood chips price per kg grade A kinam"; "Hojai agarwood distillation units adulteration". Not found: a commercial third-party certificate service, a handheld validated on chips, or a BIS standard. Not searched: trademark registers, crowdfunding sites, Chinese or Arabic sources. Verdict: the method is not new; a certificate service tied to Assam export lots appears unoffered, but only because legal export is five months old [S6]. That is weak originality.

**Desired.**
- Payer: the licensed exporter. Beneficiary: the grower who sells (price discovery) and the Gulf buyer (lot quality). Budget line: export-preparation cost, a fee set against the lot value. A grower selling a 2 kg lot at Rs 5,000 per kg [S11] would not pay Rs 10,000 [I].
- Why the payer would act: only if a buyer or the permit process demands it. Not found. Buyers in the Gulf may grade by their own experts [H].
- Behaviour shown: none yet. Adulteration is "common and accepted" in forum posts, anecdotal [S10].

**Feasible.** Outsource GC-MS at Rs 4,000 plus GST per sample [S15]; build a reference library from graded samples; a 2026 study ran headspace GC-MS on 304 samples as a basis for standardisation [S53]. Risk: no accepted standard exists, so a certificate is tied to my own method [S53]. Experiment: blind-grade 30 samples against two experienced traders.

**Profitable.** Script section T1. Fee Rs 25,000 per lot [A] (about 0.1% of the first lot's Rs 2.35 crore value, S7), two samples at Rs 4,000 each [S15], 3 hours at Rs 750: margin Rs 14,750 per lot [I]. At 100 customers with 4 lots each: 400 lots, margin about Rs 59 lakh a year before tax and rent [I]. At 10 customers: about Rs 5.9 lakh [I]. Halve the fee: about Rs 9 lakh. Verdict: Unknown. Driven by customer count and the fee a lot will bear. Contrary data: the whole first shipment was one consignment [S7].

**Reachable.** Named count: not found after 3 searches (queries: "registered exporters agarwood Assam", "agarwood DGFT restricted licence holders", "Assam Agarwood Promotion Policy registered growers"). Only trees are counted: about 1.433 million in non-forest land, 91% in four districts [S9]. Exports need a CITES permit and a DGFT licence [S56]. First 10 would come from the Hojai trader community and the state forest department (names: not found). First 100 customers probably do not exist today [H].

**Defensible.** A graded-sample library and a method that exporters and buyers come to cite. That takes 2 to 3 years of sample volume [H]. A government lab could copy it with a mandate.

**Large enough, within means.** Capital to start: sampling kit and travel, under Rs 1 lakh [A]. Hours at 100 customers: 1,200 of 1,440 available [I, script]. Best realistic case at 10 customers pays about Rs 5.9 lakh [I], below the founder's value.

**Doubt most likely to kill it:** nobody pays for a third-party grade because Gulf buyers re-grade on arrival [H]. **First test:** read the CITES and DGFT paperwork for any lab-certificate requirement, then call 5 exporters and 2 Gulf importers. **Even-if-true:** if they pay Rs 25,000 and 100 customers exist, Reachable and Large enough hold. **Outcome: INVESTIGATE, low confidence.** The count of customers is the real risk and may fail Reachable.

### T2. Domestic sports wheelchairs for Indian para-athletes. Outcome: REJECT

- **Original: no.** Nearest: NeoMotion (IIT Madras spin-out, Chennai) sells NeoFly at Rs 39,900 [S26] and is reported to supply sports chairs at Rs 65,000 [S24]; RGK/Quickie All Court at USD 2,695 to 3,929 [S27]; Top End Pro, Ottobock (no price found); imported chairs at Rs 2 to 2.5 lakh [S24]. Queries: "India sports wheelchair cost imported lakh", "Chennai firm sports wheelchair Rs 65,000", "wheelchair basketball chair price", "SAI tender para sports wheelchair", "NeoMotion sports wheelchair price" (no sports price found).
- **Desired.** Payer is split between the athlete, CSR funders (SBI Rs 93 lakh [S28], HCL Rs 37 lakh for 14 athletes [S28]) and PCI. Purchases are one-off gifts, not a budget line [I].
- **Profitable.** Script T2: price Rs 85,000 [A], parts Rs 32,000 [A] (no catalogue prices found), 12 hours: margin Rs 44,000 per chair [I]. At Rs 65,000 the margin is Rs 24,000 [I]. Capital at 100 chairs a year: Rs 7.3 lakh [I], above Rs 5 lakh.
- **Reachable.** No registry of wheelchair athletes found. India sent 73 athletes to the 2025 World Para Athletics Championships [S55]; a guess of 1,500 serious users gives about 375 chairs a year [A, script].
- **Defensible: no.** **Reason:** fails Original and Reachable; payer is episodic charity.

### T3. Non-destructive heartwood probe for sandalwood growers. Outcome: REJECT

- **Original: weak.** Nearest: ICFRE electrical resistivity tomography training for growers [S18]; sonic tomography units, about USD 3,000 to 18,000 per old US Forest Service estimate [S50]; NIR-AI platform for post-harvest oil [S19]; a 2007 paper saying standing-tree oil assessment is "largely untested and unreliable" [S19]. Queries: "sandalwood heartwood non-destructive standing tree NIR", "sandalwood growers cannot know heartwood before felling", "sonic tomography price", "Karnataka sandalwood growers number", "sandalwood grading".
- **Desired.** Value per tree is Rs 60,000 to Rs 1,50,000 (10 to 15 kg at Rs 6,000 to 10,000 per kg) [S20, I]. But Karnataka growers sell to three government agencies at prices set from 18 grades [S17], so the grower's pre-felling knowledge does not move the price.
- **Reachable.** At least 1,000 growers across three states [S16]; no official count [S16]. One-time scan market Rs 20 crore at 400 trees, Rs 500 [A, script], then it is gone.
- **Reason:** the buyer pool is small and the market is one-time; a public institute already trains growers. Fails Reachable and Large enough.

### T4. Ultrasonic cask-level gauge. Outcome: REJECT

- **Original: no.** Inspectahire sells a non-invasive pulse-echo gauge and won Innovation of the Year in 2026 [S2]; Strathclyde published centimetre accuracy [S1]; CCL SmartCask RFID tags [S4]; Proof 8 blockchain deeds [S5]. Queries: "cask contents gauging non-invasive", "Inspectahire cask gauge price", "cask RFID blockchain tracking", "cask investment fraud verification".
- **Desired.** Fraud is real (reported over GBP 150 million [S3]) but the gauge proves volume, not title or existence [S3]. Reachable buyers are UK bonded warehouses, a long sales route for a one-person Indian firm [H].
- **Reason:** not original; funded incumbent.

### T5. Tested archival boxes made in India. Outcome: REJECT

- **Original: no.** Domestic suppliers list boxes at Rs 100 (MOQ 50) and Rs 1,000 [S35]; imports Archival Methods Rs 8,245, Lineco Rs 7,285 to 8,600, including GST and duty [S34].
- **Desired.** Buyer such as the National Archives tenders on GeM with a pH floor of 7.0 only [S36]. A tested premium (buffered, passed photographic activity test) is not what the tender buys [S36]. Lowest price wins on GeM [H].
- **Profitable.** Script T4 at 200 boxes per customer: margin Rs 150 to 550 per box [A].
- **Reason:** commodity tender buying; the quality premium has no payer. Fails Desired and Defensible.

## 4. Exploratory bets (marked as bets, not theses)

### Bet B1. Standing-tree acoustic assay for agarwood as a basis for credit and insurance
- **Borrowed:** sonic tomography from arboriculture [S13, S50] plus asset-backed lending logic. **If it worked:** a resin map per tree lets a lender value a plantation and a grower avoid felling unresin-bearing trees. Plantation insurance excludes theft and applies a 20% first loss [S21]; no price floor for agarwood exists [S8].
- **Novelty (8 queries):** "agarwood tree resin detection acoustic OR sonic tomography", "bank loan insurance against sandalwood OR agarwood plantation", "sandalwood plantation insurance theft India", "NABARD plantation collateral", "sonic tomography price", "agarwood patent grading", "sandalwood heartwood non-destructive", "Karnataka sandalwood grading". Near neighbours: PiCUS-based studies on A. malaccensis and A. microcarpa [S13]; ICFRE ERT for sandalwood [S18]. No lender or insurer product found. The method exists; the lending use appears unoffered.
- **Even-if-true.** Script B1: 1,440 founder hours allow about 3,456 scans at 25 minutes [I]; at Rs 400 that is about Rs 13.8 lakh [I]. Scanning 10% of the 1.433 million trees [S9] would need about 41 years of one person's hours [I, script]. Fails Large enough, and lenders are few. **Outcome: DISCARD as a business.** It adds a data asset to T1 (same Assam growers and exporters). **Experiment if ever run:** scan 30 trees, then fell and weigh resinous wood.

### Bet B2. Rackhouse microclimate mapping for Indian malt distilleries
- **Borrowed:** pharma and wine cold-chain mapping [S45]. **If it worked:** distilleries place casks by measured hot and cold positions. A distillery with 5,000 casks at Rs 60,000 spirit value each [A] changing loss by 2 points is worth Rs 60 lakh a year [A, script].
- **Novelty (5 queries):** "whisky warehouse temperature mapping rack position", "AI rackhouse microclimate optimization" (a blog proposal [S45]), "Indian whisky 10 to 12% angel's share", "why one year in Indian cask worth three", "distillery sensors cask placement". No dedicated whisky service found. Near neighbours: MadgeTech pharma mapping kits [S45].
- **Even-if-true.** Named Indian malt makers in my sources: about six [S41, S43, S47, A]. At 6 buyers, Rs 2 lakh setup and Rs 60,000 a year [A]: Rs 15.6 lakh once, Rs 3.6 lakh a year [I, script]. Fails Large enough. **Outcome: DISCARD.** Hot-top-tier ageing is also wanted by makers [S41], so "less loss" is not clear savings [I].

### Bet B3. Seasoned native-wood staves and inserts for Indian single malt
- **Dropped assumption:** the finishing wood is oak. **If it worked:** Indian makers already finish in mahua, sal and cherry casks, made in-house [S47]. A supplier sells seasoned native staves with toast data.
- **Novelty (4 queries):** "Madhuca mahua cask finish staves supplier", "alternative oak native wood spirits staves supplier", "India cooperage re-char", "India ex-bourbon cask supply cost". Oak-alternative suppliers exist (Innerstave, The Barrel Mill, Oak Solutions Group) [S49]; no native-wood supplier found.
- **Even-if-true.** 15 buyers at Rs 8 lakh [A] caps revenue at Rs 1.2 crore [I]; seasoning inventory of 24 months ties up Rs 96 lakh [A, script] against Rs 5 lakh capital. Fails Large enough within means. **Outcome: DISCARD.**

## 5. Cut candidates

| Candidate | Reason |
|---|---|
| Kannauj attar inputs | Sandalwood-based share fell to about 10% [S22]; payers are shrinking, regulation heavy |
| Analogue tape digitisation | Large vendors and tender-driven buyers; Doordarshan about 70,000 hours [S37], film digitisation priced by NFAI at Rs 2,216 a minute [S38]; no gap found |
| Family and corporate archivist service | Past Perfect already operates [S40]; a service with no asset |
| Para-sport equipment loan library | Exists in Canada at USD 100 a year [S30] and Australia [S30]; new to India only, so not original; payer is CSR |
| Sports running blades | Ottobock with ALIMCO plans Made-in-India parts from 2026 [S33] |
| Private manuscript conservation | Payer is state mission; owners cannot pay [S39] |
| Contract tropical maturation | Compendium Spirits operates in Singapore [S48]; Indian bonded-import duty and licence rules unchecked, capital far above Rs 5 lakh [H] |
| Cask fraud verification | Crowded: SmartCask, Proof 8 [S4, S5] |

## 6. Unchecked items

- Indian excise and import rules for bonded spirits and the UK-India trade agreement effect on Scotch duty (not checked).
- Number of licensed agarwood exporters and registered growers (not found).
- Quota figure for agarwood exports comes only from a commercial blog and is unverified [S57].
- Catalogue prices for wheelchair parts and archival board (not found; costs in the script are assumptions).
- No trademark, crowdfunding, Chinese, Arabic or Japanese source searches were run for any idea.
- No buyer was contacted; all demand evidence is L1 at most.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Innovative non-invasive ultrasound method for whisky cask liquid level measurement | Strathclyde / Measurement | https://strathprints.strath.ac.uk/88237 | 2024 | 2026-11-01 | Cask gauge prototype | search summary |
| 2 | Inspectahire wins Innovation of the Year | BINDT | https://www.bindt.org/News/may-2026/inspectahire-wins-innovation-of-the-year-at-scottish-knowledge-exchange-awards-2026/ | 2026-05 | 2026-11-01 | Incumbent gauge | search summary |
| 3 | The risks and safeguards in whisky cask investment | Food Manufacture | https://www.foodmanufacture.co.uk/Article/2025/03/21/the-risks-and-safeguards-in-whisky-cask-investment | 2025-03-21 | 2026-11-01 | Cask fraud size | search summary |
| 4 | SmartCask by Checkpoint | CCL Label | https://ccllabel.com/news/smartcask-by-checkpoint-a-new-era-of-cask-transparency/ | n/d | 2026-11-01 | RFID cask tags | search summary |
| 5 | Proofworks launches (Proof 8, Metacask) | BevNET | https://www.bevnet.com/pr/2024/06/17/proofworks-launches-to-unlock-a-new-era-of-digital-transformation-in-the-spirits-industry | 2024-06-17 | 2026-11-01 | Blockchain cask deeds | search summary |
| 6 | Assam exports first consignment of agarwood chips to Saudi Arabia and UAE | ThePrint | https://theprint.in/economy/assam-exports-first-consignment-of-agarwood-chips-to-saudi-arabia-uae/2930992/ | 2026-05 | 2026-11-01 | First export, 112 kg | search summary |
| 7 | Saudi, UAE receive export consignment valued at Rs 2.35 crore | Daily Pioneer | https://www.dailypioneer.com/news/saudi-uae-receive-export-consignment-valued-at-rs-2-35-crore-from-assam | 2026-05 | 2026-11-01 | Consignment value | search summary |
| 8 | Lok Sabha answer on agarwood (AU2259) | Lok Sabha | https://eparlib.nic.in/bitstream/123456789/1931589/1/AU2259.pdf | 2023-03 | 2026-11-01 | No MSP, policy dates | search summary |
| 9 | The Assam Agarwood Promotion Policy 2020 | Mahabahu | https://mahabahu.com/the-assam-agarwood-promotion-policy-2020/ | n/d | 2026-11-01 | Tree count 1.433 million (attribution inferred from search summary) | search summary |
| 10 | Agarwood Adulteration | Aromatic Plant Project | https://aromaticplant.org/BlogDetails/Agarwood-Adulteration | n/d | 2026-11-01 | Adulterants, GC-MS need | search summary |
| 11 | Agarwood chips, oil seized | Assam Tribune | https://assamtribune.com/agarwood-chips-oil-seized | n/d | 2026-11-01 | Mumbai chip price range | search summary |
| 12 | Classification of agarwood (gaharu) by resin content | J Trop Forest Science (FRIM) | https://jtfs.frim.gov.my/jtfs/article/download/107/56/129 | 2013 | 2026-11-01 | Resin-content grading | search summary |
| 13 | Evaluation of incense-resinous wood in agarwood using sonic tomography | ANRES | https://li01.tci-thaijo.org/index.php/anres/article/view/240166 | n/d | 2026-11-01 | Tomography in agarwood | search summary |
| 14 | DNA barcoding of agarwood | PMC | https://pmc.ncbi.nlm.nih.gov/articles/PMC4851384 | 2016 | 2026-11-01 | DNA authentication | search summary |
| 15 | IIHR SAIF GC-MS facility tariff | ICAR-IIHR | https://saif.iihr.res.in/facilities/301 | n/d | 2026-11-01 | GC-MS Rs 4,000 plus GST | search summary |
| 16 | Against the grain | Down To Earth | https://www.downtoearth.org.in/forests/against-the-grain | 2025-03-16 | 2026-11-01 | Grower counts, prices | search summary |
| 17 | Reassessing Indian Sandalwood Grading | Indian Forester | https://indianforester.co.in/index.php/indianforester/article/view/170380 | 2024 | 2026-11-01 | Three buyers, 18 grades | search summary |
| 18 | ICFRE training report on ERT for sandalwood | ICFRE | https://hindi.icfre.org/institute_update_file/inst_update2235.pdf | 2025-03 | 2026-11-01 | ERT in the field | search summary |
| 19 | Non-destructive sampling of Indian sandalwood for oil | Jones et al. (AGRIS) | https://agris.fao.org/search/zh/records/65e007af4c5aef494fe7a826 | 2007 | 2026-11-01 | Standing-tree assessment untested | search summary |
| 20 | How to start a sandalwood plantation in Karnataka | IIFL | https://www.iifl.com/blogs/gold-loan/how-to-start-a-sandalwood-plantation-in-karnataka-business | n/d | 2026-11-01 | Trees per acre, heartwood kg, price | search summary |
| 21 | Plantation Insurance policy wording | United India Insurance | https://uiic.co.in/web/sites/default/files/Policy-Document/Rural%20%26%20Social%20-%20Plantation%20Insurance_1.pdf | n/d | 2026-11-01 | Theft exclusion, 20% first loss | search summary |
| 22 | Sandalwood is giving Kannauj's perfume industry a headache | ThePrint | https://theprint.in/india/fragrant-but-expensive-sandalwood-is-giving-kannaujs-perfume-industry-a-headache/626611 | n/d | 2026-11-01 | Oil cost, closures | search summary |
| 23 | No funding for para athletes | Deccan Chronicle | https://deccanchronicle.com/sports/badminton/040318/no-funding-for-para-athletes.html | 2018-03-04 | 2026-11-01 | Chair price range (stale, over 18 months) | search summary |
| 24 | Ankur's chair of joy | Telegraph (TTEF) | https://obeta.ttef.in/sports/ankurs-chair-of-joy-to-aim-for-his-dreams/cid/1779467 | n/d | 2026-11-01 | Rs 65,000 domestic vs imported | search summary |
| 26 | IIT Madras develops India's first indigenous motorized wheelchair | IIT Madras | https://www.iitm.ac.in/happenings/press-releases-and-coverages/iit-madras-develops-indias-first-indigenous-motorized | 2021-08 | 2026-11-01 | NeoFly price (stale) | search summary |
| 27 | RGK/Quickie All Court | SportAid | https://sportaid.com/quickie-all-court-wheelchair.html | n/d | 2026-11-01 | Import chair USD prices | search summary |
| 28 | CSR: SBI donates Rs 93 lakhs to para-sports; HCL Foundation | CSR Journal; NewKerala | https://thecsrjournal.in/csr-sbi-donates-rs-93-lakhs-to-support-para-sports/ | n/d | 2026-11-01 | CSR spending on para kit | search summary |
| 30 | BC Wheelchair Sports; Wheelchair Sports NSW equipment library | bcwheelchairsports.com; GIO | https://bcwheelchairsports.com/get-involved/become-an-athlete/ | n/d | 2026-11-01 | Loan libraries abroad | search summary |
| 32 | Sports Prosthetics in India: Running Blades | Robobionics | https://robobionics.in/?p=18510 | n/d | 2026-11-01 | Blade prices (vendor) | search summary |
| 33 | India's prosthetics revolution | The Week | https://www.theweek.in/news/health/2025/11/18/india-s-prosthetics-revolution-how-new-tech-is-changing-life-after-limb-loss.html | 2025-11-18 | 2026-11-01 | Ottobock-ALIMCO | search summary |
| 34 | Archival Methods flat storage box | Tanotis | https://www.tanotis.com/products/archival-methods-04-520-flat-storage-box-20-x-16-5-x-5-short-top | n/d | 2026-11-01 | Imported box price incl. duty | search summary |
| 35 | Acid-free archival box | TradeIndia | https://www.tradeindia.com/products/acid-free-archival-box-for-textiles-photographic-materials-natural-history-collection-8393853.html | n/d | 2026-11-01 | Domestic box Rs 100 | search summary |
| 36 | NIT for archival acid-free boxes | National Archives of India | https://nationalarchives.nic.in/sites/default/files/2025-01/NITBOX.pdf | 2025-01 | 2026-11-01 | pH 7.0 tender spec | search summary |
| 37 | DD digitises 1400 hours of content | Indian Television | https://indiantelevision.com/technology/dd-digitises-1400-hours-of-content/ | n/d (stale) | 2026-11-01 | 70,000 hours backlog | search summary |
| 38 | NFAI digitised and restored services | NFAI | https://nfai.nfdcindia.com/pdf/Digitized%20and%20Restored_services_v7PDF.pdf | n/d | 2026-11-01 | Film digitisation rate | search summary |
| 39 | Reviving India's National Mission for Manuscripts | GKToday | https://www.gktoday.in/reviving-indias-national-mission-for-manuscripts/ | 2024-25 | 2026-11-01 | 80% private manuscripts | search summary |
| 40 | Godrej, Cipla, Tata private archives | ThePrint | https://theprint.in/feature/godrej-cipla-tata-private-archives-are-filling-the-gaps-in-the-story-of-modern-india/1360871 | n/d | 2026-11-01 | Past Perfect, private archives | search summary |
| 41 | Why does Indian whisky mature so fast | Whiskey Wash | https://thewhiskeywash.com/whiskey-articles/why-does-indian-whisky-mature-so-fast-the-science-of-tropical-aging/ | n/d | 2026-11-01 | Angel's share 10 to 12% | search summary |
| 42 | Expensive to make single malts in India (DeVANS) | Business Today | https://www.businesstoday.in/amp/lifestyle/top-story/story/its-expensive-to-make-single-malts-in-india-as-compared-to-scotland-devans-modern-breweries-md-382328-2023-05-22 | 2023-05-22 | 2026-11-01 | 12% loss, 12% interest (stale) | search summary |
| 43 | Cask Couture: private cask ownership in India | Business Today | https://www.businesstoday.in/amp/magazine/deep-dive/story/cask-couture-how-private-cask-ownership-is-redefining-luxury-in-indias-whiskey-landscape-497651-2025-10-10 | 2025-10-10 | 2026-11-01 | Paul John cask from Rs 2 lakh | search summary |
| 44 | Kentucky bourbon distillers in high spirits | BusinessDay (Reuters) | https://www.businessday.co.za/world/international-companies/2026-04-07-kentucky-bourbon-distillers-in-high-spirits-despite-inflation-and-falling-demand/ | 2026-04-07 | 2026-11-01 | 16.1 million barrels | search summary |
| 45 | Warehouse mapping brochure; AI rackhouse microclimate | MadgeTech; blog | https://www.madgetech.com/warehouse-mapping-br.pdf | n/d | 2026-11-01 | Mapping practice | search summary |
| 47 | Crazy Cock Madhuca: world's first mahura cask finished | Whiskey Wash | https://thewhiskeywash.com/whiskey-news/crazy-cock-madhuca-worlds-first-mahura-cask-finished-whisky/ | 2025-12 | 2026-11-01 | In-house native wood casks | search summary |
| 48 | Chartered by Compendium Spirits | Robb Report Singapore | https://robbreport.com.sg/chartered-by-compendium-spirits-is-a-unique-barrel-ageing-programme-allows-you-to-craft-your-spirits-from-scratch/ | n/d | 2026-11-01 | Tropical ageing for others | search summary |
| 49 | Staves, cubes, chips suppliers | Distillery Trail | https://distillerytrail.com/suppliers/categories/staves-cubes-chips | n/d | 2026-11-01 | Oak-alternative suppliers | search summary |
| 50 | Tree decay detection equipment | US Forest Service | https://www.fs.usda.gov/eng/techdev/IM/tree_decay/tree_decay_detect_equip.shtml | n/d (stale) | 2026-11-01 | Tomograph price estimate | search summary |
| 52 | E-nose and image grading of agarwood | Unram; UTM | https://scholar.unram.ac.id/papers/W3047420962 | 2020 | 2026-11-01 | Low-cost grading research | search summary |
| 53 | Agarwood grading in Indonesia (SNI 7631-2011); 304-sample study | Biodiversitas | https://www.smujo.id/biodiv/article/download/18315/7921/1129591 | n/d | 2026-11-01 | Grading by senses, no standard | search summary |
| 54 | FRIM workshop on agarwood grading | FRIM | https://shop.frim.gov.my/proceedings-of-the-workshop-on-agarwood-grading-method-development-through-an-integrated-scientific-approach | n/d | 2026-11-01 | Malaysian grading research | search summary |
| 55 | PCI president predicts 20 medals; 73 athletes | LatestLY | https://www.latestly.com/agency-news/sports-news-pci-president-devendra-jhajharia-predicts-historic-20-medal-haul-for-india-at-new-delhi-2025-world-para-athletics-championships-7114021.html | 2025-09 | 2026-11-01 | Para-athlete squad size | search summary |
| 56 | Assam exports first consignment of agarwood chips | Drishti IAS | https://www.drishtiias.com/state-pcs-current-affairs/assam-exports-first-consignment-of-agarwood-chips-to-saudi-arabia-and-uae/print_manually | 2026-05-18 | 2026-11-01 | CITES and DGFT clearances | search summary |
| 57 | Agarwood export license | Shiprocket (blog) | https://www.shiprocket.in/blog/agarwood-export-license/amp | n/d | 2026-11-01 | Quota claim, unverified | search summary |
