# Audit 5: Natural aroma authenticity lab (C4)

Date 2026-11-01. Auditor: Independent Critic. Script: `runs/2026-11-01-audit/10-audit-5-econ.py`. All hunter claims treated as unverified. Search was cut once by a rate limit; later searches resumed. Fetches of cimap.res.in and worldtradescanner.com failed (host not allowed), so those sources are via search summary only.

## 1. Steelman

Agarwood trade has no agreed grade standard, grading is by smell, and mislabelling is common [S4][S5]. India has just opened regulated exports with a larger quota [S1][S6]. A neutral GC-MS fingerprint per lot could give a Gulf buyer a reason to trust an unknown Assam seller.

## 2. Claims checked

| Claim (C4) | My finding | Status | Tag |
|---|---|---|---|
| Quota is 1,51,080 kg chips and 7,050 kg oil a year to March 2027 | Matches DGFT Notification 52/2024-25 of 20 Jan 2025, period 1 Apr 2024 to 31 Mar 2027, via several secondary pages; one page header still shows 25,000 kg (likely a transcription error). Primary PDF not opened | Verified by multiple secondary sources, not primary | [S1][S6] |
| Quota applies to artificially propagated material only | Yes, per the same sources | Verified | [S1] |
| Quota split not found | Assam got 1,19,400 kg chips and 5,560 kg oil; Tripura is also named | Hunter's gap is closed; Assam holds most of it | [S1][S6] |
| First export 112 kg worth Rs 2.35 crore | Reported May 2026: 100 kg to Saudi Arabia, 12 kg to UAE, with CITES permit and DGFT licence | Verified (news) | [S2] |
| Fee is 1.43% of one kg at first-export price | Rs 3,000 against Rs 2.1 lakh per kg is 1.43% by arithmetic | Arithmetic right. But that price is the one consignment, chips, not oil; one sale is not a price series | [I] |
| No independent Indian grading lab found after 3 searches | I also did not find one, but I found labs that already test oils, so the "gap" is the grading product, not GC-MS capacity (section 3) | Partly supported, weak | [S7][S8] |
| Grading is traditionally by sensory panel | Confirmed; reviews say no worldwide standard exists | Verified | [S4][S5] |
| Aromadendrene and valencene separate grades | Not checked; literature I saw names 10-epi-gamma-eudesmol, beta-agarofuran and alpha-agarofuran as high-grade markers, and calls the method unsettled | Contradicted or unsettled | [S4][S9] |
| Founder cannot buy a GC-MS from Rs 5,00,000 | Plausible; price of an instrument not verified | Unchecked | [H] |
| Fixed cost Rs 10.5 lakh, cost Rs 1,200 a sample | No source; invented basis | Hypothesis | [H] |
| Gulf buyers accept a lab report | Not found; only a market report says buyers "now ask for samples or lab results" | Missing | [S5] |
| 9,100 extraction units in Assam | Not rechecked | Unchecked | [H] |

## 3. Objections

### Fatal-class (no credible fix found yet)

1. **No accepted standard to grade against.** No ISO or BIS standard for agarwood oil grading was found in 2 searches (queries: "ISO 11016 agarwood oud standard grading", "agarwood grading standard GC-MS"). Reviews say there is no overall grading system [S4]; a 2024-era study says there is no established method for classifying grades [S9]. A lab report that issues a grade rests on the lab's own scale. Why this is severe: a buyer pays for a grade only when other buyers recognise it [I]. Fix would need a recognised scale, for example an agreed scheme with a trade body or the Gulf side. No such scheme found.
2. **Volume is too small to carry a lab.** Only one export of 112 kg has been reported [S2]. At 2 samples a lot, 5 to 20 kg lots, and that export size, the script gives 11 to 45 samples and Rs 33,600 to Rs 1.34 lakh revenue a year [I]. Break-even at the hunter's own cost is 583 samples [I]. Reaching it needs roughly 1,000 kg exported a year in 5 kg lots (400 samples) or more [I]. Quota is a ceiling, not a volume: the quota existed since 2021 yet few properly permitted exports are seen [S10]. Whether lots will multiply is unknown.

### Major

3. **Existing GC-MS capacity is cheap, so fees may not hold.** Public institute rate sheets show GC-MS/MS at about Rs 2,500 to Rs 4,500 a sample at one institute and Rs 500 to Rs 1,000 at another, GST extra, both via search summary [S7]. A NABL-accredited private lab (Auriga) lists essential-oil GC-MS profiling [S8]; price not found. CSIR-CIMAP publishes an essential oil test charge list; figures not retrieved [S11]. So the raw measurement sells at or near the hunter's Rs 3,000; the margin must come from the dossier and grade, not the measurement [I].
4. **Buyers' value of a grade is not shown.** No evidence of price premium for graded or lab-certified agarwood lots was found in 3 searches (queries: "agarwood oil grade price lab report accepted", "Gulf buyers lab certificate agarwood", "agarwood certified premium"). Gulf buyers judge by smell and trust relationships [I]; sellers' own GC-MS reports are unproven as a trust signal. Absence is not proof of no demand.
5. **Private lab and CITES.** India's CITES process needs a non-detriment finding and permit for export [S10]. Whether a private lab can hold or ship agarwood samples, and whether sample exports need permits, was not found after 1 search (query: "CITES agarwood private lab sample"). Possession of controlled material by a lab is a legal unknown.
6. **Adulteration is real but the test is not the hard part.** Adulteration is documented [S5][S12]; GC-MS is generally needed to confirm purity [S12]. That supports need for testing, but dispute settlement practice (who is the referee when buyer and seller disagree) was not found.
7. **Government and cluster competition.** FFDC Kannauj is described as an accredited hub for essential oils and attar [S13]; fee schedule not found. Government clusters could add grading [hunter claim, unchecked]. Not verified either way.

### Minor

8. Attar side: 90% of Kannauj output goes to tobacco flavouring, per the hunter [H]. Premium buyers who need fingerprints are few [I].
9. Sandalwood: ISO 3518 exists in a 2022 third edition (1979 edition withdrawn), which sets santalol-based limits [S14]. So sandalwood oil has a standard and routine QC, which weakens the case for a new grader there [I].
10. Currency and tola confusion in price sources; oil prices vary from USD 126 to USD 633 per tola to USD 25,000 to 40,000 per kg across sources [S15]. A 100x spread means lot values are not established.

## 4. What holds up

- The need is real: no common standard, smell-based grading, known adulteration [S4][S5][S12].
- Quota is larger and a first compliant export has happened [S1][S2].
- The fee is small beside the value of one chip lot [I].

## 5. Disagreements with the hunter (file `02-hunt-C-r2.md`, C4)

### Where the hunter's reasoning went wrong

| Hunter claim | Contradicted or unsupported by | Reasoning error |
|---|---|---|
| "No independent Indian grading lab found after 3 searches" read as an opening | I found no grading lab either, but also found a missing standard [S4][S9]. A gap may mean no one can sell the product, not that no one tried | Absence of competitors taken as originality |
| Aromadendrene and valencene separate grades | Literature I found names other markers and says no accepted method exists [S4][S9] | Citing a single paper as settled science |
| "Desired [S]" built from growers' price discovery, adulteration reports, quota raise, one export [I] | These show a need, not that anyone pays Rs 3,000 for it; no buyer spend found | Confusing a need with purchase; ladder L1 at most |
| Quota is a market | Quota is a ceiling; the first export was 112 kg [S2] and few permitted exports occur [S10] | Confusing market size with the base actually moving |
| "Fee 1.43% of one kg" as proof of affordability | One consignment price [S2], chips, not lot sizes or oil; the buyer who pays is unknown | Single data point used as a price; wrong denominator |
| Break-even 583 samples with no volume estimate | Realistic first-year volumes are 11 to 400 samples [I] | Break-even computed without checking if volume exists |
| Fixed Rs 10.5 lakh and cost Rs 1,200 per sample | No source; rented lab rates of Rs 500 to Rs 4,500 [S7] bracket it | Unsourced cost treated as input |
| "Government clusters might compete" as the only rival | Existing accredited labs already sell the measurement [S7][S8][S13] | Missed the near substitute: lab rate cards |
| Test: ask 3 Gulf importers or exporters | Cheap, but does not test whether a grade scale will be accepted | Test aims at willingness to pay, not acceptance of the scale |
| Sandalwood and attar bundled in | Sandalwood has ISO 3518 [S14]; attar demand skew unchecked | Bundling three products with different standards |
| Quota split "not found" | It exists in the notification (Assam 1,19,400 kg and 5,560 kg oil) [S6] | Gap reported before enough search; a killer left open that is partly closed |

## 6. Simpler alternatives

- A planters' association (All Assam Agarwood Planters and Traders Association) could bulk-book an existing accredited lab and publish its own GC-MS reference per lot [S2][S8]. This captures most of the value with no instrument.
- A paper or database of fingerprints licensed to an existing lab, not a new lab [I].

## 7. Verdict: INVESTIGATE, low confidence, leaning weak

Not REJECT: nothing found proves buyers will refuse a report; the evidence gaps (Gulf acceptance, premium, CITES for lab samples) are missing information, not contradiction. Not ADVANCE: demand is L0 to L1, volume is tiny, and no grading scale is recognised.

Cheapest decisive tests (no paid test, no outreach is done by me; these are for the user):
1. Read the primary DGFT PDF and the Assam policy for any grading or certification rule.
2. Obtain rate cards (GC-MS essential oil) from FFDC, CSIR-CIMAP and one NABL private lab.
3. User asks 3 exporters for last year's lot sizes, count and what proof Gulf buyers asked for.

What would change it:
- To REJECT: exporters say Gulf buyers only accept their own nose or a Gulf lab; or annual permitted lots stay under about 100.
- To ADVANCE: a buyer or trade body commits to a named scale and pays per sample; lots exceed about 400 samples a year [I]; a rented lab gives a rate near Rs 1,500 [A].

Confidence: medium on volume and standard objections, low on price and legal points.

## 8. Not checked

Primary DGFT PDF; CIMAP and FFDC fee figures; NABL accreditation cost and time; GC-MS instrument price (searches failed: rate limit); Japanese and Gulf grading practices beyond a market report; Tripura and IAS institutes; Spices Board; failed predecessors; IP.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | DGFT Notification 52/2024-25 summaries (Taxscan, Taxmann, Global Trade Alert) | various | https://www.taxscan.in/?p=481190 | 2025-01-20 | 2026-11-01 | Quota, period, conditions | search summary |
| 2 | Assam ships first legal agarwood chips (ThePrint, Sentinel) | ThePrint | https://theprint.in/economy/assam-exports-first-consignment-of-agarwood-chips-to-saudi-arabia-uae/2930992/ | 2026-05 | 2026-11-01 | 112 kg export, Rs 2.35 crore | search summary |
| 4 | A Review Study of Agarwood Oil and Its Quality Analysis | Jurnal Teknologi (UTM) | https://journals.utm.my/jurnalteknologi/article/view/2419 | 2014 | 2026-11-01 | No standard, sensory grading | search summary |
| 5 | Global agarwood chips market | Bonafide Research | https://www.bonafideresearch.com/product/2610581601/global-agarwood-chips-market | 2026 | 2026-11-01 | No global standard, mislabelling | search summary |
| 6 | State wise quotas for artificial agarwood export | WorldTradeScanner | https://worldtradescanner.com/52-Ntfn-DGFT-20.01.2025.htm | 2025-01-20 | 2026-11-01 | Assam split | search summary |
| 7 | IIIM QCQA sheet and IBSD GC-MS charges | IIIM, IBSD | https://iiim.res.in/wp-content/uploads/2017/11/QCQA.pdf | 2017 (stale) | 2026-11-01 | GC-MS price range | search summary |
| 8 | Auriga Research GC-MS page | Auriga Research | https://aurigaresearch-ankit.pages.dev/about-us/technologies/gc-ms/ | undated | 2026-11-01 | NABL private GC-MS | search summary |
| 9 | Determination of substantial chemical compounds of agarwood oil for quality grading | UiTM | https://ir.uitm.edu.my/id/eprint/42384 | 2020 | 2026-11-01 | Marker compounds, no standard | search summary |
| 10 | NDF study and CITES agarwood coverage | BSI, Down to Earth | https://www.downtoearth.org.in/forests/cites-notified-increase-in-annual-export-quota-for-agarwood-in-india | 2024 | 2026-11-01 | NDF, permits, few exports | search summary |
| 11 | CSIR-CIMAP testing charges | CSIR-CIMAP | https://www.Cimap.Res.In/cimhindi/data/CSIR-CIMAPTesting charge for AYUSH products and Essentiol Oils.pdf | undated | 2026-11-01 | Existence of rate list | search summary |
| 12 | Agarwood adulteration | Aromatic Plant Research Center | https://www.aromaticplant.org/post/agarwood-adulteration | undated | 2026-11-01 | GC-MS to confirm purity | search summary |
| 13 | FFDC Kannauj listing | Delhi University directory | https://cmsmsme.stagingsamarthx.du.ac.in/organisations/fragrance-flavour-development-centre-ffdc-kannauj | undated | 2026-11-01 | FFDC accredited hub | search summary |
| 14 | ISO 3518:2022 sandalwood oil | ISO | https://www.iso.org/standard/8888.html | 2022-02 | 2026-11-01 | Sandalwood standard exists | search summary |
| 15 | Agarwood oil price sources (UTM article, market pages) | various | https://journals.utm.my/jurnalteknologi/article/download/2419/2154/7362 | 2014 (stale) | 2026-11-01 | Price spread | search summary |
