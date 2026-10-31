# Invention 2: Re-dyeing in job-work dye houses

Specialist: Inventor. Date: 2026-10-31.
Constraints from the brief: founder capital ₹5,00,000; founder time ₹750 per hour; primary market India [A] (basis: Director's brief; not re-checked).

Method and limits.
- Inputs: 03-market-3-redyeing.md (Market Investigator) and Thesis 2 of 01-hunt-A.md (Hunter). I treated both as hypotheses.
- I ran 34 web searches. I did not use WebFetch. Every source is marked `search summary`.
- Sources S45-S57 are pages the Market Investigator found. I did not re-search them. Their Via column says so.
- Search summaries sometimes did not tie a statement to one URL. Those rows say "mapping uncertain".
- I contacted no one. Nothing here is above demand level L1. Each concept itself is at L0.
- Base case unit used throughout: a Tirupur job-work knit dyer doing 2 t a day for 300 days, so 6,00,000 kg a year [A] (basis: the Market Investigator's mid unit; test with CETP flow records).
- Base case failure cost: 6% of kg re-processed at about ₹60 per kg extra [A] (basis: the Market Investigator's estimate in 03-market-3 section 7, built from S45 cost ratios and an assumed 60/40 split of additions and strips; test with lot logs). That is ₹21.6 lakh a year of direct cost [I] (chain: 6,00,000 kg × 6% × ₹60).
- GST on any fee is assumed at 18% [A] (basis: the usual rate for business services; confirm with a tax adviser).

## 1. Problem framing

**The job.** The dye-house owner must deliver each lot at the approved shade, on the promised day, at the quoted rate per kg. A failed lot costs a second pass through water, steam, dye, chemicals, effluent treatment and machine time. A strip and re-dye adds 170-200% of the first dyeing cost and an addition 24-36% [S45]. It also costs days. Tirupur consignment rejections are mainly for delay [S52].

**Who pays today.** It is negotiated. A Delhi fabric owner claimed about ₹25.4 lakh from a dyer whose own unpaid charges were about ₹1.64 lakh [S46]. So the dyer often carries the routine re-dye cost and is exposed to a tail claim many times its fee [I] (chain: S46 claim against charges; S45 cost ratios). The exporter carries the delay [S52].

**What the buyer already spends.**
- On the failure itself: about ₹21.6 lakh a year for the base unit [I] (chain above).
- On instruments: spectrophotometers listed at ₹1,75,000 and up [S47]; lab dyeing machines ₹80,000-2.45 lakh [S48]; dye dissolving systems ₹2-5 lakh [S49]; dye-house software ₹4 lakh for a one-year licence [S56].
- On people: a dyeing master with 10 or more years of shade-matching experience [S55]; follow-up staff at ₹25,000-30,000 a month [S54].
- On free or bundled help: dye-maker right-first-time programmes, such as Archroma's 16-week ONE WAY+ with 2-3 experts [S50].

**Where failures come from, and who controls each cause.** This decides which party should pay and which mechanism can fix it.

| Cause | Chemistry or mechanism | Who controls it | Evidence |
|---|---|---|---|
| Dye strength and dose | Drums vary from type strength; reactive dye powders take up moisture, so a gram holds less dye; small weighings for pale shades carry large relative errors [K] | Dye supplier, dye store, dyeing master | "Dye strength variation" named a root cause in a right-first-time case study [S5]; small job workers may lack labs to test incoming dyes [S10] |
| Substrate | Yarn lots of different cotton maturity, or uneven scouring and bleaching (absorbency, residual peroxide or alkali), take up dye differently [K] | Fabric owner, knitter, spinner; pretreatment by the dyer | "Dyeability of yarn" named a root cause [S5]; raw-material irregularity named a source of dyeing error in a patent [S26] |
| Process | Liquor ratio, salt and alkali timing, temperature and pH change exhaustion and fixation; lab and bulk differ [K] | Dyer | Cotton Incorporated advises basing lab formulas on greige weight and holding fabric moisture constant [S6] |
| Water | Hardness, metals and pH shift reactive dye behaviour [K] | Dyer, CETP (recovered water and brine) | Water pH named a root cause [S5]; Tirupur CETPs return recovered water and brine to members [S1, S2] |
| Assessment | Visual judgement under different lights, ageing physical standards, metamerism [K] | Exporter's merchandiser, dyer | Professional colourists may make up to 25% wrong visual pass/fail decisions (secondary claim) [S27] |

No source gave the share of failures by cause for Indian job-work units. Not found after 3 searches (queries: "causes of shade variation reprocessing knit dyeing percentage lab dip dye lot weighing water study", "pareto analysis root causes re-dyeing knit dyeing factory shade percent of reprocessed batches", "effect of dye weighing error on colour difference pale shades study"). One vendor says manual weighing causes about 40% of mismatches, and another says yarn quality caused 51% of one mill's defects; both are untraced marketing claims and I do not rely on them [I] (chain: search summaries named no study).

**Buyer decision criteria** [A] (basis: the Market Investigator's barriers in 03-market-3 section 8; test in interviews):
- No capital outlay, because cash is tight.
- Proof in the owner's own unit before paying.
- Does not expose recipes or customer lists.
- Does not humiliate the dyeing master.
- Does not slow the lot.
- Keeps or wins the exporter's orders.

**The measure of "better".**
- Re-processed kg as a share of kg dyed (additions plus strips).
- Failure cost per kg dyed that the dyer actually bears.
- Days of delay per failed lot.
- Disputes and debit notes per month.
- Capital the dyer must spend.

## 2. Inherited assumptions

Every current solution (dye-maker programmes, instruments, dosing machines, software, consultants) shares these. Each is a lever.

1. **The dye house weighs its own dye** from bulk drums in its own store.
2. **Dye is bought by the kg of dye**, not by the kg of fabric dyed right.
3. **Label strength is trusted.** Incoming drums are rarely tested against a reference [S10].
4. **Fabric is taken as it comes.** The dyer cannot reject or test the fabric owner's yarn mix before dyeing.
5. **Shade is judged once, at the end, often by eye**, by the stronger party.
6. **Who pays is settled afterwards by negotiation**, case by case [S46].
7. **Correction happens in the same unit and the same machine.**
8. **Help is sold as advice or equipment**, not as a product with a price per good lot.
9. **Each unit solves it alone.** Nothing is shared across the 40-50 units on one CETP [S53].
10. **The dyer carries the tail risk uninsured.** Standard liability wordings exclude faulty workmanship and property in the insured's care [S19, S20].

## 3. Raw concepts

| # | Concept | Method | One-line mechanism |
|---|---|---|---|
| 1 | ShadeKit: strength-assayed, pre-weighed lot kits from a shared cluster kitchen, fee per kg dyed, waived on failed lots | Mechanism transfer (paint tinting; car-paint cost-per-unit billing) + consolidation | Moves weighing and strength correction out of the dye house and prices on good output |
| 2 | Drum potency labels: each drum assayed and labelled with a strength factor the recipe uses | First principles (feed-forward of a measured disturbance) | Corrects dose for real strength before dyeing instead of correcting shade after |
| 3 | Liquid, strength-standardised pale-shade concentrates dispensed by volume | Constraint change (form of the dye) | Removes small-powder weighing error for pale shades |
| 4 | Pre-flight check at the machine: lot weight, liquor volume, water hardness and pH, fabric pH and residual peroxide | Mechanism transfer (aviation checklist; process-control feed-forward) | Catches gross input errors before dye goes in |
| 5 | ShadeCert: neutral lot certificate against a spectral standard, with retained samples and a loser-pays cause test | Inversion (cost follows cause) + mechanism transfer (commodity-trade survey certificates; retained samples) | Turns each dispute into a measured question with a contract answer |
| 6 | Yarn-lot dyeability passport before knitting | Elimination (remove fabric-caused failures upstream) | Standard test dyeing of each yarn lot so mixed lots never reach the dyer |
| 7 | Dyer scorecard sold to exporters | Mechanism transfer (credit bureau) | Verified right-first-time record steers orders to good dyers |
| 8 | Light-booth lamp and calibration subscription for each dyer-exporter pair | Elimination (of perception mismatch) | Both sides judge under the same light |
| 9 | ShadeCover: inspected, insured cover for high-stakes lots | Business model shift + mechanism transfer (boiler insurance with inspection; insured performance guarantees) | Prices and carries the tail claim; inspection lowers the loss rate |
| 10 | CETP re-dye mutual fund collected on the CETP bill | Business model shift (mutual) | Members pool routine re-dye cost |
| 11 | Risk-priced job rates: quote each shade by its predicted failure risk | Business model shift (insurance rating) | Prices risk in instead of absorbing it |
| 12 | Dyer-of-record: asset-light firm sells shade-guaranteed dyeing to exporters, subcontracts to certified units | Inversion (become the accountable party) | Captures the spread for carrying shade risk |
| 13 | Correction house: specialist line in rented capacity that corrects other units' failed lots | Consolidation (mechanism transfer from repair and rework shops) | Frees the owner's machine and concentrates correction skill |
| 14 | Off-shade lot exchange: re-allocate failed lots to orders or darker shades that accept them | Inversion (sell, do not re-dye) | Avoids the second pass entirely |
| 15 | DyeWatch: low-cost in-bath monitor that flags drift before alkali is added | Research application (multivariate fibre-optic spectroscopy) | Moves the correction to the cheapest point in the cycle |
| 16 | Shade-safe recovered brine, paid by the CETP | Constraint change (water and salt) | Makes CETP brine reuse safe for shade |

## 4. Clusters

| Cluster | Core principle | Business model | Members | Status |
|---|---|---|---|---|
| A. Control dose and dye strength before dyeing | Feed-forward on the dye side | Consumable, fee per kg dyed | 1, 2, 3 | 2 and 3 merged into 1 as features |
| B. Error-proof the machine and the bath | Detect deviations during the cycle | Hardware lease or per-lot fee | 4, 15 | 15 taken as the wildcard; 4 is a cheap add-on, but dosing vendors can copy it [I] (chain: they already sell controllers [S7, S37]) |
| C. Measure, attribute, allocate | Neutral evidence moves cost to the cause | Per-lot testing fee; data | 5, 6, 7, 8 | 6 and 8 merged into 5; 7 is 5's scale path |
| D. Transfer or pool the risk | Someone other than the dyer carries the tail | Premium or guarantee fee | 9, 10, 11, 12 | 10 risks being unlicensed insurance [I] (chain: insurer-sold warranties are IRDAI products [S38]); 12 needs working capital far above ₹5 lakh [A] (basis: exporters pay job charges on credit; test with exporters); 11 is weak alone |
| E. Handle the failed lot differently | Avoid the second pass in the owner's machine | Per-kg service; marketplace | 13, 14 | 13 needs a pollution consent or a host unit, and fabric movement adds delay [A] (basis: Tirupur units operate under consent and CETP linkage; test with a CETP); 14 lacks liquidity because fabric is customer-specific [K] |
| F. Collective water and brine | Fix a shared input | CETP-paid | 16 | Dropped: softened recovered brine gave colour difference below 1.0 dE [S3], and older work found no difference in tone [S4]; I found no sign of dyer reluctance in 2 searches |

Lead picks: 1 from A, 5 from C, 9 from D. Wildcard: 15 from B.

## 5. Three lead concepts

### Lead 1: ShadeKit, strength-assayed lot kits paid per right-first-time kg

**Method.** Mechanism transfer from two fields.
- Paint point-of-sale tinting: standard colourants plus a formula plus exact dispensing let any shop hit a shade [K].
- Car paint shops: BASF is typically paid by cars painted, not paint used [S12], and under "cost per unit" invoicing only for bodies that leave the line with a flawless finish [S13]. PPG sells pay-per-build [S14].
- Consolidation: dye purchase, incoming testing, dye store and weighing become one service.

**Core mechanism.** Remove two named root causes, dye strength variation and dose error [S5], before the lot starts. Weighing and strength correction move out of each dye house into one kitchen that assays every drum.

**How it works.**
1. A partner dye trader holds stock on his normal terms. ShadeKit runs a kitchen near one CETP, whose 40-50 member units sit close together [S53].
2. Every incoming drum gets a strength assay: a test dyeing against a retained reference, in the manner of IS 7845 [S11], read on a spectrophotometer. The result is a strength factor, for example 0.96, printed on the drum label.
3. When a lot is loaded for scouring and bleaching, the dyer's lab sends the approved recipe (% on weight of fabric for each dye) and the lot weight by phone or app. Pretreatment takes hours, so there is time [K].
4. The kitchen computes weight = recipe % × lot weight ÷ strength factor. It weighs each dye, seals it in a moisture-barrier sachet with a QR label (lot, drum, factor, weight), and delivers by two-wheeler within about 2 hours [A] (basis: one CETP catchment is a few km; test with a timed run).
5. Small sealed addition packs from the same assayed drums stay at the unit on consignment for corrections.
6. Billing: dye at price parity with the trader, plus a kit fee of ₹0.50 per kg of fabric [A] (basis: below the value range below; test by asking). The fee is waived on any lot that needs an addition or strip. Use of addition packs flags those lots.
7. A 20 g retained sample of every drum is kept. It is the evidence base for Lead 2.

**Chemistry notes.**
- Water-soluble PVA sachets for reactive dyes exist [S9], but PVA adds organic load to ZLD effluent [K]. Use laminate sachets emptied into the dissolving tank.
- Reactive dye solutions start to hydrolyse once alkali is present, so kits stay as dry powder until use [K].
- For Surat's polyester mills the same model works with disperse dyes; dispersion quality and dyebath pH then matter as much as dose [K].

**What the buyer experiences.** No dye store and no weighing. Send a recipe, receive a sealed kit. A monthly statement shows kg dyed, lots failed and fees waived.

**Measurable advantage over the best current alternative.**
- Against in-plant dosing: dye dissolving systems alone list at ₹2-5 lakh [S49]. Dispensing vendors claim weighing accuracy of 0.01-0.1 g [S37], but a machine weighs to the label strength; ShadeKit also corrects for the drum [I] (chain: S37 claims cover weighing only). ShadeKit needs no capital from the dyer [I].
- Against dye-maker programmes: those run about 16 weeks with 2-3 experts [S50]. ShadeKit starts on the first lot, is multi-brand, and is priced on output [I].
- Value to the base unit: a 1-2 point cut in re-processing is worth ₹3.6-7.2 lakh a year [I] (chain: 6,00,000 kg × 1-2% × ₹60). Removing the dye-store job saves about ₹1.8 lakh a year [A] (basis: one store hand at ₹15,000 a month; test with owners). Fee: about ₹2.9 lakh a year [I] (chain: 6,00,000 kg × ₹0.50 × 95.5% of lots not waived). The size of the cut is unproven [A].

**Who pays, price logic, frequency.**
- Payer: the dyer, out of the dye budget he already spends. At 2.5% average depth and ₹300 per kg of dye, that budget is about ₹45 lakh a year for the base unit [I] (chain: 6,00,000 × 0.025 × ₹300; depth is [A]; price sits inside IndiaMART listings of ₹180-450 per kg [S35]).
- Frequency: every lot, daily.
- What the dyer can see before buying: a free 2-week trial on one shade family with the fee waiver visible on the statement [A].

**Production and delivery outline.**
- Kitchen of about 300 sq ft, two precision balances, a sealer, sachets, an entry spectrophotometer listed at ₹1,75,000 [S47], and a lab dyeing machine from ₹80,000 [S48].
- Start-up equipment: about ₹3.1-3.5 lakh [I] (chain: balances ₹40,000-80,000 [A] + sealer and sachets ₹15,000 [A] + S47 + S48). This leaves little reserve, so the first months can rent test dyeings from a partner lab instead [A].
- At 10 units: about 67 kits a day [I] (chain: 20 t a day ÷ 300 kg lots [A]); fee revenue about ₹28.7 lakh a year [I]; running costs about ₹16.2 lakh a year [A] (basis: 4 staff at ₹20,000 a month, rent ₹25,000 a month, 2 delivery bikes, lab consumables); contribution about ₹12.5 lakh a year before the founder [I].
- Owning the dye stock is out of reach: 10 units use about ₹1.5 lakh of dye a day, so 30 days of credit would tie up about ₹45 lakh [I] (chain: 20,000 kg × 2.5% × ₹300 × 30). Hence the trader partner.
- A grant route may exist: MSE-CDP common facility centres can include raw-material depots and testing facilities [S39]. Whether a dye bank qualifies was not checked.

**What must be true.**
1. Dose and drum strength cause at least a third of failures at target units [A] (basis: below that, the cut is under 1 point and the fee exceeds the gain; test with a shadow audit).
2. A trader will consign stock to the kitchen in return for locked-in volume.
3. Dyeing masters accept kits. Their standing rests on recipe skill [S55]. Whether they take supplier commissions was not found after 1 search ("dyeing master commission from dye suppliers India dyeing units dye chemical traders influence purchase").
4. Kits arrive before the bath is ready, every time.
5. The waiver can be policed: dyers might claim failures to avoid fees.

**Biggest risk.** Most failures turn out to come from fabric, process or judgement, not dose. Then the fee looks like a tax and the master quietly routes lots back to his own weighing.

**Why incumbents would not copy quickly.**
- Dye makers sell by weight through traders. A per-kg-of-fabric fee, waived on failures and blind to brand, cuts their volume and exposes drum strength [I] (chain: assumption 2 above; no per-kg contracts found, see prior art).
- Dispensing vendors would cannibalise machine sales [I].
- The fastest copier is a large local dye trader, who already has stock and relationships [I]. Defences: the assay record per drum, the waiver, and a CETP tie-up. These are thin.

**Prior-art check (8 searches).**
- Products, "pre-weighed dye kits per batch supplied to dyehouses central dye dispensing service small dyers": in-plant colour kitchens only, such as Thies MPS Colourmatic weighing into pans [S7] and THEN's colour kitchen linking several dyehouses of one group [S8].
- Products, "colour kitchen OR dye kitchen outsourced service multiple dyeing units shared dispensing centre cluster India Bangladesh": none found; dispensing is sold as equipment to each mill [S37].
- Patents, "water-soluble film unit dose packaged reactive dye pouch textile dyeing patent": Ciba-Geigy's PVA envelopes for fibre-reactive dyes [S9].
- Patents (Google Patents), "patent method supplying pre-measured dye recipe packages to remote dyeing plant per batch strength corrected weighing station": recipe-driven dye solution preparation [S42]; a hair-dye method that corrects component weights for batch variation [S41]. No textile match.
- Business model, "chemical management services textile dyehouse paid per kilogram fabric dyed" and "dye manufacturer performance-based contract dyehouse priced per kg fabric": no per-kg or shared-savings dye contracts found.
- Papers, "effect of dye weighing error on colour difference pale shades study": no study found; vendor claims only [S37].
- Crowdfunding, "Kickstarter OR Indiegogo textile dyeing shade matching dyebath sensor OR dye dispensing": no dye-kit campaign; only consumer colour sensors [S30].
- Closest existing thing: the in-plant central colour kitchen [S7, S8]. Real difference: shared across independent units, assay of every drum, and priced per kg of fabric with a failure waiver. No close match found in 8 searches. This is not a claim of novelty.

**Cheapest test (about 4 weeks, about ₹1.25 lakh [I]).**
- Shadow audit at 3 units: re-weigh 50 dye issues per unit against the recipe; assay 10 drums per unit.
- Cost: balance ₹20,000 [A]; 30 outsourced strength tests at about ₹1,000 each [A] (basis: guess; get quotes from Tirupur labs); travel ₹30,000 [A]; founder 60 hours × ₹750 = ₹45,000 [I].
- Success: at least 20% of issues are more than 3% off recipe weight, or at least 3 of 30 drums are more than 5% off reference strength; and 2 of 3 owners agree to a paid 30-day trial [A] (basis: judgement thresholds; a few per cent strength error is roughly where shade differences start to show [K]).
- Kill: weighing within 2% and drums within 3% [A].

### Lead 2: ShadeCert, a neutral lot certificate with a loser-pays cause test

**Method.** Inversion: the cost of a failed lot moves from whoever is weaker to whoever caused it. Mechanism transfer from commodity trade, where independent surveyors' certificates decide payment [K]; from food and drug makers' retained samples [K]; and from arbitration's loser-pays rule [K].

**Core mechanism.** An agreed instrumental tolerance plus retained samples turns each disputed lot into a measured question with a contractual cost answer.

**How it works.**
1. A dyer and an exporter sign a one-page shade clause. It fixes the approved standard as spectral data held by ShadeCert, the illuminants, the tolerance, and who pays for each cause. Brands already set such numbers: Kohl's applies 0.8 CMC ΔE for solid lab dips [S22]. Best practice has a third party supply the standard [S23].
2. For every lot the dyer keeps a 20 g swatch of the prepared fabric before dyeing and a sample of each dye drum used (ShadeKit drums come with one).
3. At dispatch a conditioned swatch is read at a ShadeCert hub, or by a technician on a bike. A certificate goes out the same day: pass or fail, with ΔE, its lightness and hue parts, and a metamerism check.
4. If the exporter rejects a lot that passed, or the dyer disputes a fail, ShadeCert runs the cause test within 48 hours. It dyes the retained fabric swatch beside a reference fabric in a standard recipe (fabric dyeability), assays the drum, and reads the dyer's process log.
5. The clause allocates the cost. Fabric cause: the fabric owner pays for re-processing. Dye or process cause: the dyer. Within tolerance: the exporter accepts the lot. The party at fault pays the test fee.
6. Over time each dyer builds a verified right-first-time record that it can show to win orders (concept 7).

**What the buyer experiences.** The dyer gets a document to answer a debit note. The exporter replaces arguments and some QA visits with a certificate.

**Measurable advantage over the best current alternative.**
- Against visual approval: up to 25% of professional visual pass/fail decisions may be wrong (secondary claim) [S27]. If 15-25% of a unit's re-processed kg are false rejections or fabric-caused [A] (basis: S27 plus S5; test in the pilot), moving them off the dyer is worth ₹3.2-5.4 lakh a year to the base unit [I] (chain: 6,00,000 kg × 6% × 15-25% × ₹60).
- Against the dyer's own spectrophotometer (₹1,75,000 and up [S47]): the other side does not have to accept the dyer's own reading [I].
- Against brand colour platforms such as X-Rite Pantone's Textile Color Hub [S28] and UL's colour services [S21]: those serve brand lab-dip approval. They do not certify bulk lots between job workers and exporters, and they do not allocate cost [I] (chain: product descriptions in S21, S28).

**Who pays, price logic, frequency.**
- Certificate: ₹100 per lot, split equally between dyer and exporter, plus GST [A] (basis: under 1% of a lot's job charge; test by asking). The base unit dispatches about 2,000 lots a year [I] (chain: 6,00,000 kg ÷ 300 kg lots [A]), so up to ₹2 lakh a year per unit across both parties [I].
- Cause test: ₹1,500 per disputed lot, paid by the party at fault [A]. At 3% of lots disputed [A], that is about ₹90,000 a year per unit [I].
- Frequency: every dispatched lot; tests only on disputes.

**Production and delivery outline.**
- A hub in a rented room near a CETP office: spectrophotometer ₹1.75-4.69 lakh [S47], D65 light booth ₹40,000-80,000 [A], lab dyeing machine from ₹80,000 [S48]. Two technicians. Spreadsheet and messaging at first.
- Start-up equipment: about ₹3-3.4 lakh with the entry spectrophotometer [I] (chain: S47 + booth + S48).

**What must be true.**
1. Exporters will sign an instrumental tolerance clause. Visual approval is still treated as essential in the industry [S44].
2. A meaningful share of rejections is false or fabric-caused.
3. Dyers will let a third party hold lot data.
4. ShadeCert is seen as neutral. It must sell no dyes and no instruments. **Running Lead 1 and Lead 2 in one firm breaks this**, because ShadeKit's own drums could be the cause [I].

**Biggest risk.** The exporter is the stronger party. The clause removes its freedom to push costs back. If exporters refuse, only dyers pay, and only for rare disputes, which is too little volume.

**Why incumbents would not copy quickly.**
- Dye makers cannot be neutral when their dye may be the cause. DyStar owns Texanlab, which opened in Tirupur in 2017 [S25] [I].
- Instrument vendors sell the tools to anyone; field certification at job-work level is a service business they do not run [I].
- The real threat is a compliance lab such as Eurofins Tirupur [S24]. It could add the service, but its work is brand testing at brand prices [A] (basis: its listed services are fastness and laundering tests [S24]; test by asking for a quote).

**Prior-art check (8 searches).**
- Services, "independent lab dip approval colour assessment service for retailers suppliers India instrumental pass fail shade": UL colour evaluations for brands [S21].
- Services, "digital colour approval third-party lab dip assessment service brands suppliers spectral data tolerance": Kohl's spectral review with colorists [S22]; third-party standards providers [S23].
- Local labs, "Tirupur textile testing laboratory shade colour measurement spectrophotometer service per sample job work dyeing dispute": Eurofins [S24] and Texanlab [S25]; no per-lot dispute service found.
- Software, "cloud shade approval software exporter dyer bulk shade pass fail spectrophotometer India startup": X-Rite Pantone Textile Color Hub [S28]; a paper using CMC ΔE 1.2 as a commercial pass limit [S29]; no Indian bulk-lot service found.
- Patents (Google Patents), "patent system determining cause of colour deviation dyed textile lot fabric substrate versus dyeing process attribution": measuring the dye receptivity of raw material [S26]; nothing assigns blame between parties.
- Papers, "visual versus instrumental shade assessment disagreement percentage pass fail": S27.
- Disconfirming, "why suppliers mills resist instrumental colour approval digital standards barriers": visual assessment remains essential in practice [S44].
- Crowdfunding (same query as Lead 1): low-cost colour sensors such as Nix [S30]; no certification service.
- Closest existing thing: brand-side digital colour approval [S21, S22, S28]. Real difference: bulk lots, at the job-work dyer, retained-sample cause test, and a signed cost-allocation clause. No close match found in 8 searches. This is not a claim of novelty.

**Cheapest test (6 weeks, about ₹1.7 lakh [I]).**
- Two dyer-exporter pairs and about 150 lots. Rent spectrophotometer time from a partner lab; buy a light booth.
- Cost: booth ₹50,000 [A]; lab time ₹30,000 [A]; travel ₹30,000 [A]; founder 80 hours × ₹750 = ₹60,000 [I].
- Success: at least 15% of rejected or re-processed lots are within tolerance or fabric-caused; at least 1 exporter signs the clause; at least 1 dyer pays ₹100 per lot [A] (basis: judgement thresholds).
- Kill: 5 of 5 exporters refuse to sign [A].

### Lead 3: ShadeCover, inspected and insured cover for high-stakes lots

**Method.** Business model shift and mechanism transfer.
- Hartford Steam Boiler, 1866: insurance was the incentive to inspect, and inspection was the guarantee of the insurance [S15]. Heavy inspection raised costs but historically cut losses [S16].
- Munich Re's aiSure: the vendor gives a performance guarantee and a separate policy moves the vendor's liability to the insurer. It covers, for example, an AI visual quality inspection firm's warranty to its customers [S17].
- Construction inherent-defect insurance, which prices failure probability for insurers [S43].

**Core mechanism.** Carry the tail of a failed lot, the fabric owner's claim beyond the processing charge plus re-processing, with inspection conditions that lower the loss rate. Routine re-dyes stay with the dyer and with Leads 1 and 2.

**Why the tail and not routine re-dyes.**
- Routine re-dyes are frequent and small. Insuring them only adds loading, so self-insurance is cheaper [K].
- The tail can be many times the dyeing charge [S46].
- Standard Indian wordings exclude faulty workmanship [S19] and property in the insured's care, custody or control [S20]. So dyers carry this tail uninsured [I].

**How it works.**
1. The dyer, or the exporter, opts in per lot for high-stakes lots: a new shade, costly fabric, or a tight shipment.
2. Conditions: drums assayed (or ShadeKit drums), retained fabric swatch kept, process log kept, certificate at dispatch.
3. Fee: ₹1.5-3 per kg of the covered lot [A] (basis: the loss arithmetic below; test with an insurer). That is about 1.1-3.3% of a ₹90-140 per kg job charge [I] (chain: the charge range is the Market Investigator's estimate from S57 and older data).
4. Cover pays a fixed re-processing allowance of ₹60 per kg [A] (basis: as above) and the fabric owner's documented loss up to a cap, for example twice the fabric value [A]. It applies if the lot is rejected for shade within 30 days of dispatch and the cause test does not put the fault on the fabric.
5. Legal form: ShadeCover gives the guarantee and buys warranty-liability insurance from an Indian general insurer, as in aiSure [S17]. Indian insurers already sell warranty insurance [S38] and service-contract liability cover [S18]. Whether ShadeCover needs its own IRDAI registration was not resolved after 1 search ("Insurance Act 1938 section 3 ... warranty extended warranty not insurance India"). A lawyer must answer this first.
6. Lot data by shade family, fabric and unit builds the pricing.

**What the buyer experiences.** The dyer can tell an exporter "this lot is covered". The exporter gets a payer who pays against a certificate, without argument.

**Measurable advantage over the best current alternative.**
- Today the alternative is no cover and a negotiation. I found no Indian policy for re-dyeing or shade failure in 1 search ("insurance policy covering re-dyeing cost shade failure textile processing error dyeing insurance cover India").
- Worked lot: 500 kg [A]. Fee ₹750-1,500 [I] (chain: 500 × ₹1.5-3). Cover up to about ₹2.8 lakh of fabric loss [I] (chain: 500 kg × ₹280 per kg greige [S36] × 2) plus ₹30,000 of re-processing [I] (chain: 500 × ₹60).

**Who pays, price logic, frequency.**
- Payer: the dyer, recovered through a better job rate, or the exporter for critical orders. Per lot, opt-in.
- Loss arithmetic: if 0.1-0.3% of covered kg end in a severe claim [A] (basis: no data; test with 10 dyers' claim histories) costing ₹500-600 per kg [A] (basis: greige ₹280 per kg [S36] + job charge + re-processing + some downstream cost), expected loss is ₹0.5-1.8 per kg [I]. An insurer premium with 40% loading would be ₹0.7-2.5 per kg [I].
- So the fee leaves ShadeCover about ₹0.5-0.8 per kg at the low loss rate, and nothing at the high one [I] (chain: fee minus premium).
- If 20% of 20 units' volume is covered [A], margin is about ₹12 lakh a year at ₹0.5 per kg [I] (chain: 20 × 6,00,000 × 20% × ₹0.5).

**Production and delivery outline.** Inspection and claims run on the same hub, retained samples and certificates as Lead 2. The insurer provides the capacity. Little capital is needed beyond legal work [I].

**What must be true.**
1. An insurer will write the cover on thin data. It may want 6-12 months of lot data first [A] (basis: insurers price from loss history; test with 3 insurers).
2. Severe claims are common enough to fear and rare enough to price.
3. The structure is legal without ShadeCover holding an insurance licence.
4. Inspection conditions keep out adverse selection: dyers buying cover only for lots they expect to fail.

**Biggest risk.** No insurer appetite until there is data. Then ShadeCover cannot start before Lead 2 has run for a year.

**Why incumbents would not copy quickly.**
- Dye makers will not carry the process risk of other people's dye houses [I].
- Insurers lack per-lot textile inspection and data. More likely they partner than compete, as HSB-type insurers do with inspection [S15, S17] [I].
- A broker could copy once the data exists. The data is the only lasting moat [I].

**Prior-art check (7 searches).**
- Products, "insurance policy covering re-dyeing cost shade failure textile processing error dyeing insurance cover India": no product found; a service-contract liability wording exists [S18].
- Model, "Hartford Steam Boiler founded 1866 inspection and insurance business model": S15, S16.
- Model, "Munich Re performance guarantee insurance product warranty insurance manufacturers aiSure": S17.
- Gap, "India commercial general liability faulty workmanship exclusion job worker goods in care custody control": S19, S20.
- Supplier guarantees, "dyestuff supplier guarantees right first time shade money back OR re-dye free OR shade guarantee": none found.
- Patents (Google Patents), "patent method pricing warranty or insurance premium for manufacturing batch quality failure using process inspection data": a batch warranty with sequential inspection [S40]; nothing for dyeing.
- Regulation, "Insurance Act 1938 section 3 ... warranty extended warranty not insurance India": insurer warranties are registered products [S38]; the rule for a non-insurer guarantor is unclear.
- Crowdfunding: not applicable to an insurance product; none found in the shared crowdfunding search.
- Closest existing thing: insured performance guarantees such as aiSure [S17], and HSB's inspection-plus-insurance [S15]. Real difference: applied to job-work dyeing lots, triggered by a per-lot certificate, covering the claim that standard wordings exclude. No close match found in 7 searches. This is not a claim of novelty.

**Cheapest test (3 weeks, about ₹55,000-80,000 [I]).**
- A two-page term sheet to 3 general insurers through a broker; a lawyer's opinion on the legal form at ₹25,000-50,000 [A]; founder 40 hours × ₹750 = ₹30,000 [I].
- Ask 10 dyers, during the Lead 2 interviews, for claim histories.
- Success: one insurer gives indicative terms; at least 4 of 10 dyers report a fabric-owner claim above the processing charge in the last 2 years [A] (basis: judgement thresholds).
- Kill: all insurers decline without 12 months of data. Then ShadeCover waits behind Lead 2.

### How the three compare

| | ShadeKit | ShadeCert | ShadeCover |
|---|---|---|---|
| Payer | Dyer | Dyer and exporter | Dyer or exporter, per lot |
| Start-up equipment | About ₹3.1-3.5 lakh [I] | About ₹3-3.4 lakh [I] | Mostly legal costs [I] |
| Main dependency | Trader consignment | Exporter signs the clause | Insurer appetite |
| Concept demand level | L0 [I] | L0 [I] | L0 [I] |
| Cheapest test | About ₹1.25 lakh [I] | About ₹1.7 lakh [I] | About ₹55,000-80,000 [I] |

- ShadeCert and ShadeCover fit in one neutral firm; ShadeKit does not, because it sells dyes [I].
- The three tests together cost about ₹3.5-4.2 lakh [I], most of the founder's capital. The Lead 1 audit and the Lead 2 interviews can share one Tirupur trip [A].

## 6. Wildcard

**DyeWatch: a low-cost in-bath monitor that flags drift before alkali is added.** Method: research application.

**Mechanism.**
- A side stream of the bath runs through a cooling coil and a short-path flow cell. A low-cost spectrometer reads it.
- A multivariate calibration estimates each dye's concentration in a three-dye mixture. Fibre-optic spectroscopy with multivariate calibration has done this in research [S33].
- The exhaustion curve is compared with the lab dip's curve. Before the fixation alkali goes in, the dyer gets an alert and a calculated addition.
- The salt stage is the last cheap point to correct, because dye added before fixation can still level [K].

**Why it might work.**
- HueMetrix "Dye-It-Right" monitors tracked each dye in the bath and were used for right-first-time dyeing in some plants (mapping uncertain) [S31].
- Closed-loop dosing from bath readings is patented [S32]. In-line dye-tank spectral monitors are sold [S34].
- Spectral sensors are now cheap, and units already buy per-lot services [I] (chain: S30 shows consumer-priced colour sensors; leads above).
- If it caught a third of failures and cut their cost by 80%, the base unit would save about ₹5.8 lakh a year [I] (chain: 6,00,000 × 2% × ₹60 × 0.8; both shares are [A]).
- Price: lease ₹8,000-12,000 a month per machine on the 1-2 machines that dye risky shades [A] (basis: under the saving; test by asking).

**Why it is risky.**
- Lint and foam foul sampling loops [K].
- Hydrolysed and active reactive dye look the same spectrally, so the monitor sees exhaustion, not fixation [K].
- Each dye needs calibration.
- HueMetrix-type systems did not spread widely, a disconfirming sign whose cause I did not find [I] (chain: S31 says "select plants"; 2 searches found no current commercial forecaster).
- Prototype ₹1.5-2.5 lakh [A] (basis: pump, flow cell, spectrometer module and enclosure; get quotes). That is half the capital for a device with no proof.

**Prior art seen (2 searches, plus the shared crowdfunding search):** S31, S32, S33, S34, and a patent on optical readings of packaged yarn during dyeing. No close match for a low-cost, leased, mid-cycle forecaster.

## 7. Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Paper on Tirupur CETP water and brine recovery | Indian Journal of Chemical Technology (NISCPR) | https://or.niscpr.res.in/index.php/IJCT/article/download/21354/5799/132747 | not shown | 2026-10-31 | RO brine reclaimed and distributed to member units for reuse | search summary |
| 2 | Zero discharge system (Angeripalayam CETP) | Clean India Journal | https://cleanindiajournal.com/zero_discharge_system/amp | not shown | 2026-10-31 | About 11% of feed as NF brine to dyeing; RO permeate said to improve dyeing (source's claim) | search summary |
| 3 | Reuse of the treated textile wastewater and membrane brine in wet textile processes | Istanbul University-Cerrahpasa (AVESIS) | https://avesis.iuc.edu.tr/yayin/36831828-899b-4745-9a3f-2ee10918cef2/reuse-of-the-treated-textile-wastewater-and-membrane-brine-in-the-wet-textile-processes-distorting-effects-on-the-cotton-fabric | 2015 (per summary) | 2026-10-31 | Softened NF brine gave dE below 1.0 | search summary |
| 4 | Savings and re-use of salts and water present in dye house effluents | Lenntech (abstract) | https://www.lenntech.com/abstracts/1069/savings-and-re-use-of-salts-and-water-present-in-dye-house-effluents.html | not shown (older) | 2026-10-31 | Recycled brine matched conventional dyeing in tone and intensity | search summary |
| 5 | Case study on right-first-time dyeing, root cause analysis | Daffodil International University journal (mapping uncertain) | https://journals.diu.edu.bd/index.php/jaiit/article/download/21/12/426 | not shown | 2026-10-31 | Root causes: yarn dyeability, dye strength variation, water pH | search summary |
| 6 | ISP 1014 Lab to Plant Correlation in Jet Dyeing | Cotton Incorporated | https://www.cottoninc.com/wp-content/uploads/2017/12/ISP-1014-Lab-to-Plant-Correlation-in-Jet-Dyeing.pdf | 2017-12 (upload path) | 2026-10-31 | Greige weight basis; constant fabric moisture | search summary |
| 7 | Thies unveils new dispensing system | Textile World | https://www.textileworld.com/textile-world/dyeing-printing-finishing-2/2008/05/thies-unveils-new-dispensing-system/ | 2008-05 | 2026-10-31 | In-plant automatic weighing into pans | search summary |
| 8 | THEN dyehouse network | Fong's Europe | https://fongs.eu/site/assets/files/1398/then_dyehouse_network_feu_2021.pdf | 2021 | 2026-10-31 | Colour kitchen linking several dyehouses to central order management | search summary |
| 9 | US5145484 Polyvinyl alcohol envelopes as packing material for fibre-reactive dyes (family EP0457715) | Google Patents (Ciba-Geigy) | https://patents.google.com/patent/US5145484 | about 1991-1992 (from patent numbers) | 2026-10-31 | Prior art: unit packaging of reactive dyes | search summary |
| 10 | Standardisation of dyes | Fibre2Fashion | https://www.fibre2fashion.com/industry-article/7674/standardisation-of-dyes | not shown | 2026-10-31 | Small processors may lack incoming QC labs; about 1,000 Indian dye makers | search summary |
| 11 | IS 7845:2022 strength of reactive dyes by dyeing test | Bureau of Indian Standards | https://services.bis.gov.in/tmp/1734843202.pdf | 2022 | 2026-10-31 | Standard dyeing test for strength against an agreed standard | search summary |
| 12 | Automotive painting techniques article | just-auto | https://www.just-auto.com/?p=4445 | not shown | 2026-10-31 | BASF typically paid per car painted, not material used | search summary |
| 13 | Ten years as a system supplier at the Rastatt site | BASF | https://www.basf.com/ru/ru/media/news-releases/2007/06/p-coat-1806.html | 2007-06 | 2026-10-31 | Cost-per-unit invoicing; paid only for flawless bodies | search summary |
| 14 | Suppliers on board for new roles | WardsAuto | https://www.wardsauto.com/news/archive-wards-suppliers-on-board-new-roles-relationships-chop-costs/764145/ | not shown (archive) | 2026-10-31 | PPG pay-per-build | search summary |
| 15 | The history of HSB | Munich Re / HSB | https://www.munichre.com/hsb/en/about-hsb/hsb-group/history.html | not shown | 2026-10-31 | Founded 1866; insurance as incentive and guarantee of inspection | search summary |
| 16 | HSB annual filing | US SEC (EDGAR) | https://sec.gov/Archives/edgar/data/310823/000031082396000009/0000310823-96-000009.txt | 1996 | 2026-10-31 | Inspection raised costs but historically cut losses | search summary |
| 17 | Insure AI (aiSure) | Munich Re | https://www.munichre.com/en/solutions/for-industry-clients/insure-ai.html | not shown | 2026-10-31 | Insured performance guarantee; Relimetrics visual inspection warranty | search summary |
| 18 | Service contract liability insurance policy wording | Future Generali India | https://general.futuregenerali.in/downloads/commercial-insurance/service-contract-liability-insurance-policy/policy-wording/service-contract-liability-insurance-policy-policy-wordings.pdf | not shown | 2026-10-31 | An Indian service-contract liability product exists | search summary |
| 19 | Contractors all risk insurance (retail) prospectus | Future Generali India | https://general.futuregenerali.in/downloads/other-insurance/contractors-all-risk-insurance-retail/prospectus-forms/contractors-all-risk-insurance-retail-prospectus.pdf | not shown | 2026-10-31 | Faulty workmanship exclusion | search summary |
| 20 | Contractors all risk insurance (retail) wording | Tata AIG | https://tataaig.com/s3/contractors_all_risk_insurance_retail_v2_15_01_2025_c30dac4c71.pdf | 2025-01-15 (file name) | 2026-10-31 | Care, custody or control exclusion | search summary |
| 21 | Color services sell sheet | UL Solutions | https://collateral-library-production.s3.amazonaws.com/uploads/asset_file/attachment/58961/RCP22CS617224_-_CRS_110_Color_Services_Sell_Sheet__2_.pdf | not shown | 2026-10-31 | Colour evaluation for brands; spectral and virtual-lightbox review | search summary |
| 22 | Kohl's color review process requirements | Kohl's | https://link.kohls.com/content/dam/klink/pdfs/Kohls-Color-Review-Process-Requirements.pdf | not shown | 2026-10-31 | 0.8 CMC ΔE for solid lab dips | search summary |
| 23 | The lab dip process | Cotton Incorporated (CottonWorks) | https://cottonworks.com/en/topics/sourcing-manufacturing/dyeing/the-lab-dip-process | not shown | 2026-10-31 | Third-party colour standards provider as best practice | search summary |
| 24 | Eurofins Tirupur location | Eurofins | https://www.eurofins.com/textile-leather/about-us/locations/tirupur-india/ | not shown | 2026-10-31 | Tirupur lab for fastness and laundering tests | search summary |
| 25 | Texanlab to set up a lab in Tirupur | Apparel Resources | https://apparelresources.com/business-news/trade/texanlab-to-setup-a-lab-in-tirupur/ | 2017 | 2026-10-31 | DyStar-group lab in Tirupur | search summary |
| 26 | EP0125556 Process and device for controlling the dye receptivity of textiles | Google Patents | https://patents.google.com/patent/EP0125556B1/en | about 1984 (from patent number) | 2026-10-31 | Raw material irregularity as a source of dyeing error | search summary |
| 27 | Instrumental pass/fail analysis (Westland and Pan) | Journal of Textile Science and Engineering (White Rose eprints) | https://eprints.whiterose.ac.uk/id/eprint/155294/1/westland_pan_JTSE_2017.pdf | 2017 | 2026-10-31 | Up to 25% wrong visual decisions (cited from a secondary reference) | search summary |
| 28 | X-Rite Pantone Textile Color Hub | Industry Today | https://industrytoday.com/?p=42058 | not shown | 2026-10-31 | Cloud digital lab-dip approval for brands | search summary |
| 29 | Conference paper on colour matching in a dyehouse | IEOM Society (Kuala Lumpur 2011) | https://www.ieomsociety.org/proceedings/kualalumpur2011/165.pdf | 2011 | 2026-10-31 | CMC ΔE commercial factor of 1.2 as pass limit | search summary |
| 30 | Nix color sensor helps you match your paint to your new shirt | The Gadgeteer | https://the-gadgeteer.com/2013/09/16/nix-color-sensor-helps-you-match-your-paint-to-your-new-shirt/ | 2013-09-16 | 2026-10-31 | Crowdfunded low-cost colour sensor | search summary |
| 31 | Report chapter describing HueMetrix Dye-It-Right monitor | P2 InfoHouse (mapping uncertain) | https://p2infohouse.org/ref/08/07014.pdf | not shown (1990s) | 2026-10-31 | Per-dye bath monitoring used for right-first-time in select plants | search summary |
| 32 | US5846265 Closed-loop textile dyeing process with real-time metered dosing | USPTO | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5846265 | about 1998 (from patent number) | 2026-10-31 | Closed-loop dosing from bath measurement | search summary |
| 33 | Optical fibre spectroscopy for dye concentration monitoring | CORE | https://core.ac.uk/download/147467517.pdf | not shown | 2026-10-31 | Multivariate calibration predicts each dye in a mixture | search summary |
| 34 | LTMS product sheet | Ocean Insight | https://www.OceanInsight.com/globalassets/catalog-blocks-and-images/pdfs/ltms-product-sheet_v7.pdf | not shown | 2026-10-31 | Commercial in-line dye-tank monitor | search summary |
| 35 | Reactive dyes listings | IndiaMART | https://m.indiamart.com/impcat/reactive-dyes.html | not shown | 2026-10-31 | About ₹180-450 per kg; black ₹200-260 per kg; listing asks, GST excluded | search summary |
| 36 | 160-165 gsm, 100% cotton, greige, single jersey | Fibre2Fashion | https://www.fibre2fashion.com/fabrics/cotton-fabric-suppliers-1490820 | not shown | 2026-10-31 | ₹280 per kg, Tirupur origin, undated listing | search summary |
| 37 | Italy's Color Service automatic dosing offers consistent dye quality | Fibre2Fashion | https://fibre2fashion.com/news/textile-news/italy-s-color-service-s-automatic-dosing-offers-consistent-dye-quality-287296-newsdetails.htm | not shown | 2026-10-31 | Vendor accuracy claims 0.01-0.1 g | search summary |
| 38 | Warranty insurance (retail) customer information sheet | Generali Central Insurance | https://www.generalicentralinsurance.com/downloads/other-insurance/warranty-insurance/customer-information-sheet/warranty-insurance-retail-cis.pdf | not shown | 2026-10-31 | Indian insurers sell warranty insurance | search summary |
| 39 | New guidelines MSE-CDP | TANSIDCO (Government of Tamil Nadu) | https://www.tansidco.tn.gov.in/pdf/MSMEGOs/New%20Guidlines%20MSE-CDP%2024.05.2022.pdf | 2022-05-24 | 2026-10-31 | Common facility centres can include testing and raw-material depots | search summary |
| 40 | US5608658 System and method for inspection of products with warranties | USPTO | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5608658 | about 1997 (from patent number) | 2026-10-31 | Batch warranty with sequential inspection | search summary |
| 41 | WO2012142404A1 Formulation of hair dye colors using manufacturers' standardized packaging | Google Patents | https://patents.google.com/patent/WO2012142404A1/en | 2012 | 2026-10-31 | Weight correction for component batch variation (outside textiles) | search summary |
| 42 | EP0421742B1 Apparatus for automatic preparation of a dye solution | Google Patents | https://patents.google.com/patent/EP0421742B1/de | not shown | 2026-10-31 | Recipe-driven dye solution weighing | search summary |
| 43 | Reliability index and failure probability of inherent defect insurance | PubMed Central | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10884417/ | not shown | 2026-10-31 | Insurer modelling of defect probability (construction) | search summary |
| 44 | Color management in textiles | Datacolor | https://www.datacolor.com/business-solutions/blog/color-management-in-textiles-how-to-deliver-accuracy-and-speed/ | not shown | 2026-10-31 | Visual assessment still essential in approval | search summary |
| 45 | Right-First-Time: a necessity not a luxury | Textile Today (Bangladesh) | https://textiletoday.com.bd/right-first-time-a-necessity-not-a-luxury | not shown | 2026-10-31 | Addition 24-36%; strip and re-dye 170-200% | search summary (from 03-market-3 S1; not re-searched) |
| 46 | Delhi High Court suit on defective dyeing | LatestLaws | https://www.latestlaws.com/judgements/delhi-hc/2005/january/2005-latest-caselaw-133-del | 2005-01 | 2026-10-31 | ₹25.4 lakh claim against ₹1.64 lakh charges | search summary (from 03-market-3 S11; not re-searched) |
| 47 | Colour spectrophotometer listings | Spectra Labtech via IndiaMART | https://m.indiamart.com/spectra-labtech/color-spectrophotometer.html | not shown | 2026-10-31 | ₹1,75,000 to ₹4,69,000 | search summary (from 03-market-3 S19; not re-searched) |
| 48 | Lab dyeing machine listings | IndiaMART | https://m.indiamart.com/impcat/lab-dyeing-machine.html | not shown | 2026-10-31 | ₹80,000-2.45 lakh | search summary (from 03-market-3 S24; not re-searched) |
| 49 | Dyestuff dissolving system | TradeIndia | https://www.tradeindia.com/products/dyestuff-dissolving-system-c4736061.html | not shown | 2026-10-31 | ₹2,00,000-5,00,000 | search summary (from 03-market-3 S23; not re-searched) |
| 50 | Archroma tailors sustainable solution for mills and brands | Just Style | https://www.just-style.com/news/archroma-tailors-sustainable-solution-for-mills-brands/ | not shown | 2026-10-31 | ONE WAY+ about 16 weeks, 2-3 experts | search summary (from 03-market-3 S29; not re-searched) |
| 51 | ESCO financing: opportunities and challenges (SIDBI) | SlideShare | https://www.slideshare.net/aspcv/sidbi-presentation | not shown | 2026-10-31 | Outcome contracting disputes in Indian MSMEs (background) | search summary (from 03-market-3 S51; not re-searched) |
| 52 | Export scenario of knitwear units of Ludhiana compared with Tirupur | Punjab Agricultural University (KrishiKosh) | https://krishikosh.egranth.ac.in/items/05c0354b-8a39-4bd0-8385-5eefce5a1f8c | not shown | 2026-10-31 | Tirupur rejections mainly for delay | search summary (from 03-market-3 S56; not re-searched) |
| 53 | CETPs: an untapped opportunity for energy efficiency | CAG | https://www.cag.org.in/blogs/cetps-untapped-opportunity-energy-efficiency | not shown | 2026-10-31 | About 19 CETPs serving 40-50 units each | search summary (from 03-market-3 S42; also in my own results) |
| 54 | Dyeing and finishing follow-up job, Tiruppur | Evanios Jobs | https://www.evaniosjobs.com/job-apply/2437366/dyeing-and-finishing-folow-up-job-in-tiruppur | 2026 (approx.) | 2026-10-31 | ₹25,000-30,000 a month | search summary (from 03-market-3 S52; not re-searched) |
| 55 | Dyeing master, Ramesh Textiles, Indore | foundit | https://www.foundit.in/job/dying-master-ramesh-textiles-indore-46456974 | not shown | 2026-10-31 | 10+ years; consistent shade matching | search summary (from 03-market-3 S54; not re-searched) |
| 56 | Textile software | Pinnacle Systems via IndiaMART | https://m.indiamart.com/pinnacle-systems-perundurai/textile-software.html | not shown | 2026-10-31 | Dyeing software ₹4,00,000 one-year licence | search summary (from 03-market-3 S26; not re-searched) |
| 57 | Higher dyeing charges as raw material costs rise | Indian Apparel | https://www.indian-apparel.com/apparel-and-textile-news/higher-dyeing-charges-raw-material-costs-rise/ | 2026 (approx.) | 2026-10-31 | 2026 job-charge rise behind the ₹90-140 per kg range | search summary (from 03-market-3 S13; not re-searched) |
