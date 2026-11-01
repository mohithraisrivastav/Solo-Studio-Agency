# Audit 1: Cask passport (hunter claim C1)

Date: 2026-11-01. Auditor: Independent Critic. Scope: desk research only. Many hosts were blocked in this session (WebFetch failed for businesstoday.in, patents.google.com, trendhunter.com, bindt.org), so every source below was seen as a search summary, not opened. Economics script: `runs/2026-11-01-audit/10-audit-1-cask-econ.py`.

## 1. Steelman

Indian cask-ownership buyers pay large sums for a cask they never see, in a climate where loss is several times the Scottish rate [H]. A per-cask logger would let each owner see their own loss and temperature history, and a distillery could use that as proof against doubt [H]. Fees of Rs 2,500 a year are small beside the cask price [H].

## 2. Claims checked

| Claim (file C1) | My finding | Status | Tag |
|---|---|---|---|
| "No Indian product found after 3 searches" | Absence in 3 English queries is not evidence of originality. A near-identical concept is already marketed: SmartCask by Checkpoint (CCL Label), a per-cask data chip called a "digital passport", announced 2026, aimed at distilleries and bonded warehouses [S1]. | Contradicted in spirit | [S1] |
| Concept is new ("new category") | Patents exist for bung sensors, barrel-face sensors, weight-loss monitoring and per-cask evaporation tracking [S2][S3]. A trademark exists for a sensor bung "SmartBarrel" (Trenlot) [S2]. Inspectahire sells a non-invasive ultrasonic whisky gauge, a 2026 award winner [S4]. | Contradicted | [S2][S3][S4] |
| SmartCask, Sensiolink, CaskEye as named by the user | SmartCask is a chip for identity and custody, not a level or weight sensor [S1]. Sensiolink: Not found after 2 searches (queries: "Sensiolink cask barrel sensor", "Sensiolink LoRaWAN sensors company"). CaskEye: Not found after 1 search (query: "CaskEye cask monitoring"). | SmartCask checked; others missing | [S1] |
| Buyers pay Rs 2 lakh to over Rs 14 lakh [S14 of hunter] | Not re-verified. Diageo India's programme entry is reported near Rs 30 lakh with a stock of over 20,000 barrels to choose from [S5][S6]. Diageo calls it a cask purchase programme, made to order, with no stock held for investment [S7]. | Range not confirmed; higher end seen | [S5][S6][S7] |
| Owners lose 8 to 12% a year | Not re-checked. The Scotland figure of up to 2% a year was seen [S8]. | Unverified | [K] |
| Fewer than a dozen programmes | I saw two named leaders, Diageo and John Distilleries (Paul John) [S5]. Amrut and Indri: Not found after 2 searches (queries: "...Paul John Amrut Indri private cask...", "Cask Couture ... Amrut"). | Count unverified | [S5] |
| Excise rules unknown | Still unknown. See section 5. | Missing | |
| Tag Rs 4,000, fee Rs 2,500 | Tag cost range from my script Rs 2,750 to Rs 6,950 [A]; hunter figure is inside it but at the low end. Fee never tested. | Hypothesis | [A] |

## 3. Originality

| Product | Measures | Attaches | Price | Customers / base | India | Status |
|---|---|---|---|---|---|---|
| SmartCask by Checkpoint (CCL) | Identity, origin, ownership, movement; chip life 30 to 50 years | RFID data chip on cask | Not found | Aimed at Scotch distilleries and warehouses, in development per some coverage [S1] | Not found after 1 search | Active, announced 2026 [S1] |
| SmartBarrel (Trenlot) | Bung with sensors, cloud upload | Bung | Not found | Not found | Not found | Trademark only seen; status unknown [S2] |
| Inspectahire Ultrasonic Whisky Gauge | Liquid level and volume from outside | Handheld, moves along cask | Not found | Scottish industry; won a 2026 award [S4] | Not found | Active [S4] |
| Kigtek cask monitoring | Weight and ABV at disgorge to give volume per cask | Weighing at emptying | Not found | A global spirits producer [S9] | Not found | Active [S9] |
| Barrel Proof | Barrel-face sensor: volume, proof, environment | Barrel head | Not found | Marketing page only, details to investors [S2] | Not found | Unclear |
| US11954554, DT Whisky Solutions, bung-pack patent | Weight loss, per-cask evaporation, bung level and temperature | Various | n/a | Patents, not sales [S2][S3] | n/a | n/a |
| Dewar's/Bacardi robot dog | Ethanol vapour in warehouse | Mobile | n/a | Trial [S8] | No | Trial |
| SmartWinery cork | Ullage, temperature, cracks | Cork | Research | Wine casks, academic [S10] | No | Prototype |
| Sensiolink, CaskEye | Not found | | | | | Not found |

Finding: the passport, as the hunter described it (a per-cask record that an owner can show), overlaps SmartCask on the record and identity side, and overlaps the patent and gauge literature on the measurement side [I]. What is left that is different is a combined level, temperature and humidity logger made for Indian heat and sold to Indian distilleries [I]. That is a local adaptation, not a new category. For a buyer it is worth something only if the buyer wants the data (section 4) [I]. Checked and not found: cask-ledger platforms (Cask Trade offers cask management [S11]); I did not read their feature lists. Bonded warehouse tracking and angel's-share meters beyond the above: Not searched in depth.

## 4. Buyer value

- What distilleries give today: Diageo gives a personalised blending programme for invited clients [S5][S7]. Certificates, visits and apps for other programmes: Not found after 2 searches (queries: "Cask Couture ... certificate bottling excise", "...Indri Amrut..."). 
- Complaint or demand evidence for per-cask proof in India: Not found after 3 searches. Demand for proof exists abroad: the CCL launch followed a BBC investigation of fraud in cask investment schemes involving false ownership and fictitious casks [S1]. That is demand for identity and ownership proof, which a chip answers; it is not demand for level readings [I].
- Price paid by owners: one report puts the Diageo entry at about Rs 30 lakh [S6]. Hunter's range is lower and unverified.
- Who pays the fee: the hunter sells to distilleries but justifies the fee by owner cask value [I]. That mixes who benefits with who pays. Whether the owner would pay is untested [H]. Cheapest test: ask 3 programme managers, no purchase needed.
- What a distillery gains: a differentiator [H]. What it risks: a reading showing loss above its stated rate makes it liable to dispute, so some may not want the data [H]. Neither side tested.

Evidence level: L0 to weak L1 (the BBC-driven fraud concern supports a transparency need, not this product).

## 5. Rules

Primary text of the Maharashtra Foreign Liquor (Storage in Bond) Rules, 1964 and the Karnataka Excise (Distillery and Warehouse) Rules, 1967 was not opened; I saw only the search summary, which returned definitions, not device or seal provisions [S12]. Goa and others: Not found after 1 search. Not found after 2 searches (queries: "excise rules bonded warehouse maturation cask seal officer device sale of cask to individual India", "India private cask ... excise") whether fitting a device to a bonded cask needs excise permission, whether an individual may hold title to a cask in bond, or how ownership works legally. Seen: individual possession of liquor is capped by state law, and above the cap needs a licence [S13]. Diageo describes its offer as a cask purchase programme [S7], and one source says cask ownership is not a regulated financial product [S5]. Conclusion: the hunter's assumption that private cask ownership works as in Scotland is unverified in the sources I saw; what owners legally hold (title, a contract right, bottled stock) is unknown [H]. Excise counsel needed.

## 6. Economics (script output, all inputs [A])

- Tag BOM plus assembly, volume of about 1,000 units: Rs 2,750 to Rs 6,950 [A]. No component catalogue price could be fetched in this session, so these are my estimates, not catalogue figures. Plus gateway Rs 15,000 to 30,000 per warehouse [A], install labour Rs 150 to 400 per tag [A].
- Battery: about 9.6 years at 25 uA average [A], so the claim is plausible but moisture and alcohol vapour exposure untested.
- Level resolution: a 2% annual loss lowers the level about 25 mm; a 10% loss about 92 mm [A, from barrel geometry in script, [K] dimensions]. A sensor through a bunghole must hold error under a few mm in ethanol vapour and foam-free liquid; this is the technical risk, since Inspectahire's work is the proof that a research-grade method exists but at gauge level [S4].
- Selling price at 40% margin: Rs 4,600 to Rs 11,600 per tag [A]. The hunter's Rs 4,000 is only reached at the cheapest BOM. Running cost about Rs 780 per cask per year [A] (battery swap, support, cloud, recalibration, field visits).
- Customer pool: two named leaders [S5]. Scenarios: 5 programmes with 300 tagged casks at 30% uptake gives 450 casks and Rs 11.2 lakh a year; 12 programmes gives 3,840 casks and Rs 96 lakh; the hunter's two customers of 1,000 casks gives Rs 50 lakh [A]. Break-even for one founder at Rs 70,000 a month is about 489 casks [A].
- Capital: Rs 5,00,000 buys about 68 to 172 tags before gateways, legal and trials [A]. Tag capex for 450 casks is about Rs 33 lakh [A], so any deal needs the distillery to prepay or buy tags. The hunter's own "payback 1.6 years" uses Rs 4,000 and Rs 2,500 and omits running cost, gateway and churn [I].

## 7. Distribution

First 10 customers: there are not 10 programmes visible; I saw two [S5], so the first 10 is not reachable by counting [I]. First 100: there is no pool of 100 [I]. Alternative pool: other maturation-stage buyers (all distilleries for inventory loss control) and Indian-bottler warehouses, untested [H]. Decision maker: unknown; likely a master blender, brand head or excise/compliance head at a large group like Diageo, where tag purchase involves corporate procurement and Indian excise [H]. Not found: any source naming who buys.

## 8. Where the hunter's reasoning went wrong

1. "No Indian product found after 3 searches", used as the basis for "high difference": absence of evidence taken as evidence of absence, with only English queries and no search of RFID cask passports, bung sensors or the fraud news. A per-cask "digital passport" exists [S1]. Error: weak search treated as originality test.
2. "New category for a known buyer": the hunter cited a barrel-face sensor patent [S20 hunter] and robot dog and spectroscopy trials but still rated novelty high. Error: prior art listed and then ignored.
3. Claim "premium buyers already spend Rs 2 lakh and up, so fees are small" [H]: affordability confused with willingness to pay; spending on whisky is not spending on proof. Error: interest taken for purchase.
4. Fee justified by owner value but sold to distilleries: payer and beneficiary confused. Error: wrong buyer logic.
5. "Fewer than a dozen programmes visible" then "two customers of 1,000 casks": scale assumed from one hypothetical; I could verify two leaders only [S5]. Error: market size confused with share and with individual deal size.
6. Claim "tag Rs 4,000" [A]: hunter's cost is at the bottom of my range and omits gateway, install, battery, calibration, support. Error: gross margin counted as profit, hidden costs missing.
7. "Owner will want proof": asserted from the hunter's own view; no evidence of complaint. The hunter flagged it as [H]; but the ranking "High difference, Medium effort" treats it as settled. Error: hypothesis promoted by ranking.
8. Excise noted as unknown yet ranked INVESTIGATE as a cheap test; fitting devices to bonded casks could be a gate that kills the idea at zero cost to check. Error: test order backwards (legal check should come before sensor trial).
9. Distillery incentive ignored: the data could expose losses above a distillery's advertised rate [H]. Error: one-sided incentive analysis.

## 9. Outcome

**INVESTIGATE, narrowed, low priority.** Not REJECT because: no evidence yet that Indian distilleries do not want per-cask data (absence of buyers is not proof) and a tailored Indian-heat logger is not shown to exist. Not ADVANCE because: originality is largely gone [S1][S2][S4], the visible pool is about two [S5], excise permissibility is unknown, and the unit economics are thin and the tag is not proven in a bung.

What would change it:
- To REJECT: excise rules forbid fitting any device or opening seals on bonded casks, or three programme managers say they would not share per-cask data, or SmartCask (or a rival) is shown on sale in India.
- To ADVANCE: a written excise opinion that tags are allowed; at least 8 verified programmes; two managers (L2) confirming loss is complained about and naming who pays; a bench test of a sensor at the needed few-mm accuracy in a 200 L cask.

Simpler alternative: a gauged level and weight report issued by the distillery staff using a handheld gauge (Inspectahire-type) twice a year [S4]. Gives most of the proof at no tag cost [I].

Unchecked: Sensiolink and CaskEye identity; Goa, Uttar Pradesh and other states; component catalogue prices; Amrut, Indri, Rampur programmes; Cask Trade feature list.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| S1 | SmartCask (by Checkpoint), a new era of cask transparency | CCL Label / Packaging Europe | https://ccllabel.com/news/smartcask-by-checkpoint-a-new-era-of-cask-transparency/ | 2026-02/04 (sources differ) | 2026-11-01 | Competitor facts | search summary |
| S2 | Barrel Proof sensors; SmartBarrel trademark; bung patent 20150198474 | various | https://patents.justia.com/patent/20150198474 | not found | 2026-11-01 | Prior art | search summary |
| S3 | US11954554 Monitoring weight loss from casks | Google Patents | https://patents.google.com/patent/US11954554 | not found | 2026-11-01 | Prior art | search summary |
| S4 | Inspectahire wins Innovation of the Year 2026 | BINDT | https://www.bindt.org/News/may-2026/inspectahire-wins-innovation-of-the-year-at-scottish-knowledge-exchange-awards-2026/ | 2026-05 | 2026-11-01 | Ultrasonic gauge | search summary |
| S5 | Cask Couture: private cask ownership in India | Business Today | https://www.businesstoday.in/magazine/deep-dive/story/cask-couture-how-private-cask-ownership-is-redefining-luxury-in-indias-whiskey-landscape-497651-2025-10-10 | 2025-10-10 | 2026-11-01 | Programmes | search summary |
| S6 | Diageo India Rare Spirits coverage | The Spirits Business | https://www.thespiritsbusiness.com/?p=871095 | not found | 2026-11-01 | Entry price | search summary |
| S7 | Diageo India Rare Spirits | Drinks Business / Diageo India | https://www.diageoindia.com/en/news-and-media/press-releases/2025/diageo-india-launches-india-rare-spirits-a-first-of-kind-personalised-cask-program-in-the-country | 2024-12 / 2025 | 2026-11-01 | Programme model | search summary |
| S8 | Robot dog monitors angel's share | The Manufacturer | https://www.themanufacturer.com/articles/automation-in-scottish-whisky-robot-dog-monitors-the-angels-share-at-john-dewar-sons/ | 2025 | 2026-11-01 | Loss rate, trial | search summary |
| S9 | Smarter cask monitoring, global spirits producer | Kigtek | https://www.kigtek.com/references/smarter-cask-monitoring-unlocks-multi-million-pound-savings-for-global-spirits-producer/ | not found | 2026-11-01 | Weighing | search summary |
| S10 | SmartWinery | Sensors (MDPI) | https://www.mdpi.com/1424-8220/18/3/803 | 2018 | 2026-11-01 | Wine prototype | search summary |
| S11 | Cask management | Cask Trade | https://casktrade.com/cask-management | not found | 2026-11-01 | Ledger platform exists | search summary |
| S12 | Karnataka Distillery and Warehouse Rules 1967; Maharashtra Storage in Bond Rules 1964 | Legitquest / Bombay HC | https://www.legitquest.com/act/karnataka-excise-distillery-and-warehouse-rules-1967/B12F | 1967 | 2026-11-01 | Rules (definitions only) | search summary |
| S13 | Public Notice 78/2023 | Jawahar Customs | https://www.jawaharcustoms.gov.in/pdf/PN-2023/PN-78-2023.pdf | 2023 | 2026-11-01 | Possession limits | search summary |
