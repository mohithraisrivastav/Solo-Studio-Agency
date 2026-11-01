# 01 Hunt D: new capability into products

Date: 2026-11-01. Role: Opportunity Hunter. Lens D: a material, process, device, or component that recently became cheap, available, or proven, making a better physical product possible.

Method note: 35 web searches. WebFetch was not used. Every source below was seen only as a search summary, so no page was read in full. Where a search summary gave a figure but did not show which of several results carried it, the Sources table says "attribution uncertain".

Isolation: only `00-brief.md` and `09-director-assessment.md` were read from this run. Excluded industries (gold jewellery, textile dyeing, lift maintenance, pharmaceutical manufacturing, hospital oxygen, construction waste, steel export compliance, metal foundries, estate settlement) were not used.

## 1. Industries chosen and why

### Deciding questions (written before searching)

| Industry | Deciding questions |
|---|---|
| I1 Commercial cooking heat | Has the LPG cost or supply position of eateries changed? What stops a switch to electric? Who already sells electric commercial cooking, and is there a part of the problem a new device solves? Who keeps the fuel saving? |
| I2 Onion storage | How large are losses in farm storage sheds (kanda chawls)? Who owns the stored onion and keeps the price gain? Does forced or controlled ventilation cut losses? What products exist and what do they cost? |
| I3 Speciality crop processing | Is makhana popping or cardamom drying still manual or poor? Do machines exist, at what price, and are they used? How much value does better processing add per kg? |
| I4 Fresh-produce export packaging | Do exporters import modified-atmosphere liners or SO2 pads? Do Indian makers exist? |
| I5 Roof coatings | Has a new coating (radiative cooling) reached the market? What do buyers pay for cool roofs now? |

### Industries and why now

**I1. Commercial cooking heat (energy at small scale: restaurants, caterers, small food units).** 13 searches.
- A West Asia supply shock cut commercial LPG in March 2026, and the Delhi 19 kg commercial cylinder rose from ₹2,078.50 to ₹3,071.50 in May 2026 [S1].
- LFP battery cells were about US$54.59 per kWh in China [S2], and battery-buffered induction cooktops that avoid wiring upgrades have been sold in the US since 2024 [S3].

**I2. Onion post-harvest storage (agriculture).** 10 searches.
- In the 2026 season the Lasalgaon average rose from ₹1,021 per quintal on 17 May [S4] to about ₹3,700 in mid-August, while farmers reported about 30% storage losses [S5].
- Small solar panels and DC fans now run forced ventilation in research stores (a 130 W panel driving ten 6 W fans) [S6]; a solar IoT onion-store prototype is costed at ₹60,000-70,000 [S7].

**I3. Speciality crop processing: makhana (fox nut) and cardamom (food processing).** 8 searches.
- The Makhana Board launched in September 2025 with a scheme outlay of ₹476.03 crore for 2025-26 to 2030-31 [S8], and ministers name mechanisation as a need [S9].
- Cardamom auctions averaged ₹3,146 per kg on 7 October 2026 [S10], so drying quality is worth more per batch than in past years [I] (high price per kg raises the value of any quality gain).

**I4. Fresh-produce export packaging.** 2 searches; stopped once incumbents were clear.
- Indian pomegranate exports are shifting to sea freight, with value up over 20% in 2025-26 [S11].
- India exported 224,401.27 tonnes of fresh grapes worth US$367.99 million in 2025-26 [S12].

**I5. Roof coatings (building materials).** 2 searches; stopped once incumbents were clear.
- JNCASR reported a radiative cooling paint with 96.3% solar reflectance [S13] that cut surface temperature about 10°C in tests [S14].
- Large paint makers already market heat-reflective coatings (Indicus Heatseal [S15], Nerolac Perma NoHeat [S16]).

## 2. Raw candidates

| # | Problem | Payer | Signal | Tag |
|---|---|---|---|---|
| R1 | Eateries need to cut LPG use; plain commercial induction cooktops resold | Restaurant owner | Induction bought at ₹23,000 that was priced ₹9,000 during the shortage | [S25] |
| R2 | Eateries that switch to induction exceed their electricity connection; a battery-buffered induction station keeps them under the load step | Restaurant owner | Pune commercial tariff steps from ₹8.51 to ₹12.40 per unit above 20 kW | [S40] |
| R3 | Institutional and canteen kitchens move bulk cooking off LPG | Caterer or client firm | HungerBox committed ₹3.5 crore to move kitchens to electric | [S32] |
| R4 | Powder-coating and other small LPG-fired process heat units shut in the shortage | MSME owner | Powder-coating units in Maharashtra reportedly stopped when supply was cut | [S48] |
| R5 | Onion rots and shrinks in farm storage sheds; a humidity-controlled forced-ventilation retrofit kit | Farmer or trader who stores | About 30% storage losses reported in 2026 | [S5] |
| R6 | Onion storage monitored by sensors only | Farmer or warehouse | Godaam founder said its sensors could not identify spoilage or quantity | [S54] |
| R7 | Onion sprouting controlled by irradiation | Buffer-stock agencies | Irradiation stopped sprouting in trials | [S51] |
| R8 | Makhana popping is manual, slow, and injurious; a village-scale machine that gives top-grade pops | Makhana processor or FPO | Bihar subsidises popping machines at 50-60% | [S79] |
| R9 | Cardamom drying with firewood or electric heaters loses colour; a heat-pump dryer | Estate or drying-centre owner | Heat-pump and solar dryers dried in 6-12 hours with better quality in a comparison | [S89] |
| R10 | Exporters need fruit-specific modified-atmosphere liners for sea freight; laser micro-perforated locally | Fruit exporter | Uflex sets micro-perforations by fruit respiration rate | [S93] |
| R11 | Grape exporters use SO2 pads whose dose is hard to control | Grape exporter | SO2 inside a box varies with humidity; residue limit 10 mg/kg | [S95] |
| R12 | Metal-roofed sheds overheat; a radiative cooling roof paint | Factory or warehouse owner | Cool roof coatings sell at ₹10-45 per sq ft | [S96, S97] |

## 3. Opportunity theses

### T1. Battery-buffered induction stations for eateries that cannot or should not raise their electricity load

**Problem.** Small and mid-size eateries depend on commercial LPG, which was rationed in March 2026 [S21] and still costs far more than in January 2026 (Delhi ₹2,747.50 in September [S19], against ₹1,866 in Nagpur on 1 January [S20]; different cities, so the comparison is a proxy) [I]. Moving burners to induction needs a strong electricity connection [S26]. Adding several 3.5-10 kW induction units pushes many eateries past the connection size at which tariffs and fixed charges step up, or needs a load upgrade they cannot get quickly [A] (basis is the Pune tariff step in [S40] and the Indore report in [S26]; test by asking 20 eateries and one discom office).

**Who pays, who uses, who can block.**
- Payer: the owner-operator of the eatery, who keeps both the fuel saving and the avoided tariff step [I] (owner pays both the LPG bill and the electricity bill).
- Not the payer: caterers on cost-plus or client-paid utility contracts. HungerBox funding the shift [S32] suggests platforms or clients bear transition costs in canteens [I]; contract terms not checked.
- Users: cooks. They can block on cooking style; one report says induction cooking takes longer [S26], and NRAI described the shift as a stopgap [S23].
- Blockers: the landlord or mall (electrical works), the discom (how it counts load behind a battery), fire safety approval for a battery in a hot kitchen [A] (not checked).

**Current alternatives and what buyers spend.**
- LPG: Delhi ₹3,071.50 in May, ₹3,113.50 in June [S17], ₹2,930 in July [S18], ₹2,747.50 in September 2026; Mumbai ₹2,701 [S19].
- Commercial induction units: a 3.5 kW unit at ₹19,850 and an induction kadai at ₹36,000 [S28]; induction fryers at ₹1,29,990 and ₹1,41,436 [S29] (seller asking prices, dates not shown).
- Turnkey bulk induction kitchens (Lorman Kitchen Equipment) [S30]; the vendor claims about 60% lower energy cost than LPG [S31] (vendor claim).
- Diesel burners and charcoal as stopgaps, which raised costs [S50].

**Frequency and cost of the problem (reference eatery, Pune, all [A] inputs to test).**
- LPG energy cost: ₹2,701 per 19 kg (Mumbai, used as a proxy for Pune) [S19] is ₹142.2 per kg [I]; at 12.8 kWh per kg [K] that is ₹11.1 per kWh of fuel [I].
- Useful heat: commercial burner efficiency 35-50% [A] (typical open-flame range; test with a water-boil test) gives ₹22.2-31.7 per useful kWh [I]. Induction at about 85% [K] on the Pune 0-20 kW tariff of ₹8.51 plus ₹1.60 wheeling per kWh [S40] gives ₹11.9 per useful kWh [I]; above 20 kW, ₹12.40 plus ₹1.52 per kVAh [S40] gives ₹16.4 [I, assuming power factor near 1, A].
- Reference eatery uses one commercial cylinder a day [A] (test by survey): 243 kWh of fuel a day, about 97 kWh useful at 40% efficiency, about 114 kWh of electricity a day, about 3,430 kWh a month [I] (19 × 12.8; × 0.40; ÷ 0.85; × 30).
- Monthly LPG cost ₹81,030 [I] (30 × ₹2,701).
- Electric, staying at or under 20 kW: ₹35,220 a month [I] (3,430 × ₹10.11 + ₹540 fixed charge from S40), a saving of about ₹45,800 [I].
- Electric, above 20 kW at a 30 kVA load [A]: ₹64,250 a month [I] (3,430 × ₹13.92 + 30 × ₹550 from S40), a saving of about ₹16,800 [I].
- Staying under the step is worth about ₹29,000 a month, about ₹3.5 lakh a year, for this eatery [I]. This is the value a battery buffer can capture; the LPG saving itself belongs to induction, which anyone can sell.
- Taxes: LPG prices are retail as published; the tariff figures exclude electricity duty and other levies; GST treatment for the buyer was not checked [A].
- Benchmark fit: the tariff is from a non-official guide for Pune (MSEDCL, FY 2026-27) [S40]; other discoms differ. The LPG price is Mumbai's, not Pune's. Both must be confirmed before any pitch.

**Why now.**
- Supply shock: commercial supply was cut, restored to 70% in April [S21] and freed from limits around 1 July 2026 [S22]. Restaurants are not on the priority list for LPG allocation [S24], so the next shock hits them first [I].
- Cheap storage: LFP cells about US$54.59 per kWh (₹5,209 per kWh) in China, with Indian landed cost 13-23% higher [S2]. EV replacement packs cost ₹8,000-15,000 per kWh including GST [S41]; retail stationary systems ₹20,000-35,000 per kWh [S42].
- Proven capability: Impulse Labs (US$5,500, about 3 kWh battery) and Channing Street Copper (US$6,000, 4 kWh LFP) use batteries so stoves run on ordinary sockets [S3]. These are US home products; they prove the concept, not Indian commercial demand or price.
- Policy push: the government urged makers to scale induction output [S27]; BEE showcased commercial electric cooking from seven makers and announced a vendor directory [S33]. Grid strain is a stated worry: one report projects 13-27 GW of extra infrastructure if induction demand rises 30-40% [S39].

**Why unsolved.** (f) newly possible, plus (d) trust and distribution. Induction sellers sell cooktops; battery makers sell backup systems; nobody found sells a kitchen unit whose purpose is to keep the grid draw under a tariff step [I] (from S28-S38 and search below). Partial (a): NRAI says the industry is about 95% gas-dependent and the shift was a stopgap [S23]. Battery-buffered commercial induction in India: not found after 2 searches (queries: "battery backed induction cooking commercial kitchen India startup...", "battery integrated induction stove Impulse Labs Channing Street Copper ... India").

**Competitors, including failed attempts.**
- Commercial induction sellers: Transglobe, Stella, HIKE listings [S28, S29]; Lorman turnkey bulk induction [S30]; BEE's seven showcased makers [S33] (names not shown).
- Alternatives to LPG: Reurja plasma cooking [S37]; Greenvize hydrogen cooktop [S35] at about ₹1,50,000 [S36].
- Closest to the idea: Etroly India lists a solar induction cooktop with battery backup as a B2B product [S34]; SWELECT sells off-grid solar cooking and notes that induction needs large, costly battery storage [S38].
- Battery and inverter majors (Exide, Amara Raja, Luminous, Tata Power) were not searched by name; they could enter quickly.
- Failed attempts: none found; not searched separately. Channing Street Copper was supply-limited to one region [S3].

**Barrier for a small entrant, and the way in.**
- Barriers: BIS registration is model-wise for lithium packs under IS 16046 Part 2 [S43], with rated-capacity verification added in 2026 [S44]; kitchen heat and grease raise fire risk [K]; the discom may count induction load behind the battery as connected load [A] (the decisive unknown).
- Way in: buy BIS-registered packs and a certified hybrid inverter rather than building cells or packs; sell the control logic (cap grid draw, schedule recharge, keep cooking through an LPG cut) and an Indian-format cooking surface; start in one discom where the tariff step is verified; use induction sellers as the channel.
- Within ₹5,00,000: one 3.5 kW unit ₹19,850 and one induction kadai ₹36,000 [S28], a 10 kWh pack ₹80,000-1,50,000 [I] (10 × S41 range), a hybrid inverter ₹60,000-1,00,000 [A], controls and enclosure ₹30,000 [A]: about ₹2.3-3.4 lakh [I]. That leaves about ₹1.6-2.7 lakh for one paid pilot [I]. A sellable system for the reference eatery is about ₹2.5-4.25 lakh [I] (15 kWh at S41 rates plus ₹1-1.5 lakh inverter and ₹0.3-0.5 lakh integration, both A), giving about 0.7-1.2 years payback against ₹3.5 lakh a year [I]. At retail battery prices [S42] the system is ₹3-5.25 lakh for the battery alone [I], and payback roughly doubles [I].
- Battery sizing is unknown: average draw is about 9.5 kW over 12 hours [I] (114 kWh ÷ 12), but rush peaks and the existing AC and refrigeration load decide the size [A] (test with one week of load logging).

**Reachable buyer pool (bottom-up).**
- Mumbai has 141,456 restaurants [S45]; Hyderabad 74,807 [S46]; organised outlets were 43.8% of the sector by value in FY24 [S47].
- Share that are owner-run, cook on commercial LPG, have a 3-phase connection and sit near a tariff step: 10-20% [A] (test with 50 eateries in one ward) gives 21,600-43,300 eateries in the two cities [I].
- Three-year reach 1-2% gives about 220-870 systems [I]; at ₹3-4.5 lakh each [A], about ₹6.5-39 crore cumulative revenue [I].
- Benchmark fit: Mumbai is served by utilities other than MSEDCL [A] (not checked), so the Pune tariff step may not apply there. Counts for Pune, Nashik, and Nagpur were not found.

**Demand evidence level.** L1 for problem spend (LPG bills, inflated induction purchases [S25], HungerBox's ₹3.5 crore [S32]); all from news reports, not primary buyer data. L0 for the battery-buffered solution type in India.

**What would make this large.** Repeated LPG shocks; discoms confirming that a battery-isolated load is not connected load; extension to street-food carts, sweet shops, dairies, and chapati units, which the shortage also hit [S48]; a national e-cooking push [S33].

**What would kill it.** A discom ruling that load behind the battery counts as connected load; eateries mostly using domestic cylinders, which makes LPG look cheap to them [A] (test in survey); battery packs installed at retail prices [S42]; a battery or inverter major launching the same bundle; LPG prices returning to January 2026 levels.

**Confidence.** Medium-low. The spend and the tariff step are sourced (the step from a non-official guide), but the solution is unproven in India, and the decisive regulatory point was not checked.

**Not checked.** MERC tariff order itself; BESCOM, TSSPDCL, Mumbai utility tariffs; fire rules for kitchen batteries; whether induction sellers already bundle batteries.

### T2. Humidity-controlled forced-ventilation retrofit kit for farm onion storage sheds

**Problem.** Rabi onions stored for four to six months lose weight, rot, and sprout. Indian studies report 30-60% of bulbs damaged in storage [S51], with shrinkage 30-40%, rot 10-12%, and sprouting 8-10% in one chawl-type study [S52]. An ICAR source reports losses up to 46% in four months even in bottom- and side-ventilated structures [S61]. In 2026 farmers reported about 30% storage losses after rain [S5], and rot was found at a Central Warehousing Corporation godown in Lasalgaon [S71]. Maharashtra's price commission chairman put onion lost in storage and transport at 80-90 lakh tonnes [S66].

**Who pays, who uses, who can block.**
- Payer: the farmer or trader who owns the stored onion. They keep the saving, because every tonne not lost is sold at the later, higher price [I] (no allowance or pass-through applies to own stock).
- Users: the farm family or hired labour who load and watch the shed.
- Blockers: the subsidy rules, which require the prescribed chawl design [S65]; KVK and onion research station advice; government price action (buffer releases and procurement at ₹1,235 per quintal [S67], later ₹1,730 [S68]) that caps the price gain.

**Current alternatives and what buyers spend.**
- Naturally ventilated chawls built at a cost norm of ₹6,000 per tonne, with subsidy of 25% or at most ₹1,500 per tonne under RKVY [S65]; Maharashtra schemes created 42,282 low-cost structures with 9.65 lakh tonnes capacity [S55].
- An ICAR low-cost steel-pipe structure of about 30 tonnes costs about ₹50,000, or ₹167 per quintal stored, against ₹140 per quintal to rent in Nashik district, and reports 8-10% losses [S53].
- Tata Steel Nest-In's Agronest "smart warehouse" with airflow design and temperature, humidity and gas sensors, launched 2020 [S62]; price not found.
- Godaam's warehouse sensors, claimed to cut wastage 20-25%; its founder said the sensors could not identify spoilage or quantity [S54].
- Solar cold storage is being promoted in Nashik [S5 search set; not used for figures].

**Frequency and cost of the problem (reference 25-tonne chawl).**
- Storage happens once a year per farm, for four to six months [A] (rabi harvest to October sale, consistent with S4 and S63).
- Value of one percentage point of loss avoided: 0.25 tonne. At the August 2026 average of ₹3,700 per quintal [S5] that is ₹9,250 [I]; at ₹1,000 per quintal, the middle of the August 2025 range of ₹800-1,200 [S57], it is ₹2,500 [I].
- If a kit cuts losses by 5-10 points [A] (test with a paired-bay trial), it is worth ₹46,250-92,500 in a 2026-type year and ₹12,500-25,000 in a 2025-type year [I].
- Kit price ₹25,000-40,000 [A] (four to six DC fans, 200-400 W of solar, small battery, controller with temperature and humidity sensors; consistent with the 130 W, ten-fan research store in S6 and the ₹60,000-70,000 full prototype in S7). That is 17-27% of a ₹1.5 lakh chawl [I] (25 × ₹6,000 from S65).

**Why now.** Cheap DC fans, small solar panels and humidity sensors let a controller run fans only when outside air is dry or cool enough, and stop them when it would add moisture [K for the psychrometric principle; S6 for a working solar-fan store]. The 2026 season showed both sides of the bet: a large price rise from ₹1,021 per quintal in May [S4] to a ₹4,525 maximum on 19 October [S63], and heavy rot [S5]. The government's Onion Grand Challenge sought storage designs in 2022 [S69], and a parliamentary panel called central onion storage poor [S70].

**Why unsolved.** (b) technically uncertain and (e) fragmented buyers. Forced ventilation cut rot in trials (about 25% against 35-38% without ventilation [S58]; weight loss 25.23% against about 35% [S60]; weight loss under 4% against about 9% [S6]), but in one Indian trial it raised moisture loss and left slightly less usable onion [S59]. Uncontrolled fans can make things worse; control is the point. Partial (a): in low-price years storage itself loses money (August 2025 prices of ₹800-1,200 against a cost of at least ₹2,500 per quintal [S57]; spring 2026 average ₹1,250 against a cost of about ₹1,800 [S64]). A commercial retrofit fan-and-controller kit for existing chawls: not found after 3 searches (queries: "onion storage startup Nashik solar powered ventilation sensors...", "onion storage India company solar fan ventilation kit...", Marathi "कांदा चाळ पंखा ... सोलर फॅन").

**Competitors, including failed attempts.** Tata Steel Agronest (new-build warehouse) [S62]; Godaam (monitoring only; founder admitted weak results) [S54]; ICAR designs [S53]; academic solar prototypes [S6, S7]; irradiation for sprouting [S51]. Not searched by name: Ecozen, NHRDF, the onion research directorate at Rajgurunagar, agri-input majors.

**Barrier for a small entrant, and the way in.**
- Barriers: proving the effect takes a full season; farmers are price-sensitive; a kit outside the prescribed design may not be subsidised [S65].
- Way in: a retrofit for the existing installed base rather than a new structure; solar-powered so no farm wiring; sold through FPOs and input dealers in Nashik, Ahmednagar, and Pune; evidence from side-by-side bays in farmers' own sheds; later, seek inclusion in the scheme design.
- Within ₹5,00,000: three prototype kits about ₹90,000, data loggers about ₹30,000, travel and trial costs about ₹50,000, about ₹1.7 lakh in total [A for each item]; founder time for one season about 300 hours, worth ₹2.25 lakh at ₹750 an hour [I].

**Reachable buyer pool (bottom-up).**
- 42,282 subsidised structures holding 9.65 lakh tonnes [S55], about 22.8 tonnes each [I]. Maharashtra storage was 1.5 million tonnes in 2015-16, with about 0.5 million tonnes added by 2021-22 [S56], about 80,000 structures at 25 tonnes [I].
- 50-60% of Maharashtra's rabi crop is stored [S56], so the sheds are used, not idle [I]. This passes the real-need check.
- Three-year reach 1-2% gives 800-1,600 kits [I]; at ₹30,000 [A], about ₹2.4-4.8 crore cumulative revenue [I].

**Demand evidence level.** L1 for problem spend: farmers build and rent storage at a known price [S53, S55], and losses are widely reported [S5, S66]. L0 for paying for a retrofit kit.

**What would make this large.** Inclusion in state chawl subsidy designs; FPO bulk orders; extension to garlic and potato kept outside cold stores; data from many sheds that sharpens the control rule.

**What would kill it.** A paired-bay season showing under 3 points of loss reduction, or higher weight loss; two low-price years in a row; government price caps; farmers unwilling to pay a quarter of the chawl's cost.

**Confidence.** Low-medium. The loss and the payer are clear; whether the kit works in Indian monsoon conditions is not.

**Not checked.** Current subsidy rules (the Marathi page is undated [S65]); Agronest price and uptake; whether any input company already sells chawl fans.

### T3. Village-scale makhana popping machine that produces top-grade pops

**Problem.** Makhana is still roasted and popped largely by hand, which is labour-heavy and cumbersome [S84] and harms workers' health [S75]. A blog claims manual popping yields 65-70% against 90-95% by machine, at ₹12-15 per kg against ₹8-12 [S72]. Pop size sets price: top-grade "lava" pops earn a 7-11% premium over mixed pops [S78].

**Who pays, who uses, who can block.**
- Payer: the processor or trader who buys raw seed and sells popped makhana; they keep any yield or grade gain [I]. Farmers who sell raw seed do not.
- Users: skilled popping teams, who may resist a machine that replaces them [A].
- Blockers: subsidy officers (machine sales lean on the 50-60% subsidy [S79]); traders who grade by bag weight and pop size [S78].

**Current alternatives and what buyers spend.**
- Hand popping by hired teams (wage rates not found after 2 searches).
- Machines: IndiaMART listings from ₹75,000 (semi-automatic) to ₹7,50,000 (popping machine) [S73]; a blog lists ₹1.53 lakh, ₹12.5 lakh and ₹27 lakh tiers [S72].
- ICAR's Darbhanga centre launched a popping machine in December 2013 and demonstrated it to 200 farmers and traders [S74], reporting over 90% popping efficiency [S75]; ICAR-CIPHET has a mechanised chain [S76].
- Bihar subsidy up to ₹1.5 lakh on a popping machine [S79].

**Frequency and cost of the problem.** Daily during the processing season [A]. Raw seed is ₹28,000-40,000 per quintal, about double 2023-24 [S80]; good popped makhana sells at ₹700-1,700 per kg retail [S81] (retail, not processor price, so a weak benchmark). The value of a better machine rests on two unmeasured numbers: the real yield and grade gain over skilled hand popping, and the processor's price gap between grades [I].

**Why now.** Board and scheme [S8], mechanisation as a stated priority [S9], seed prices doubled [S80], and new large processors (Proventus Agro opened a 2,500 tonne-a-year unit at Purnia in 2026 [S82]). Production figures disagree widely (about 11,500 tonnes projected [S85] against about 60,000 tonnes [S86]).

**Why unsolved.** Unclear, which is the main weakness. Early machines could not make lava and needed manual help [S77]; ICAR now says machine quality is better than hand popping [S75]. If that is true, the problem may already be solving itself through subsidised machines [I], which points to (a) or to slow diffusion, not to an opening. Machine adoption counts: not found after 3 searches.

**Competitors, including failed attempts.** ICAR and CIPHET designs [S74, S76]; many fabricators on IndiaMART [S73]; large processors with their own lines [S82]. No failed ventures found; not searched separately.

**Barrier for a small entrant, and the way in.** Existing fabricators and subsidy-linked sales. The only way in found: a smaller machine proven to match hand-popped size distribution, sold with subsidy paperwork and operator training in Darbhanga, Madhubani, Purnia and Katihar, which supply about 80% of processed makhana [S83]. A first prototype at ₹1.5-3 lakh [A] (based on S72-S73 prices) fits ₹5 lakh.

**Reachable buyer pool (bottom-up).** Processor counts not found after 2 searches. Assume 500-2,000 popping units in the four districts [A] (test with district industries centre or Makhana Board lists); 5-10% reach in three years gives 25-200 machines [I]; at ₹1.5-3 lakh [A], ₹0.4-6 crore [I].

**Demand evidence level.** L1, weak: subsidy and listings show machines are sold; no evidence of how many processors buy, or why others do not.

**What would make this large.** Proof that a new machine beats both hand popping and current machines on grade; Makhana Board procurement or FPO programmes.

**What would kill it.** A field check showing that current subsidised machines already match hand-popped grades; processors preferring large lines; buyers paying for pop size the machine cannot reach.

**Confidence.** Low. Kept as the third thesis because it is a product opportunity in an industry unrelated to T1 and T2 with real spend, but it is the closest to a cut.

## 4. Cut candidates and reasons

| # | Candidate | Reason for cut |
|---|---|---|
| R1 | Reselling commercial induction cooktops | Commodity reselling; many sellers and turnkey firms already exist [S28, S30, S33]; price spikes were temporary [S25]. |
| R3 | Electric bulk cooking for canteens | Turnkey incumbents (Lorman) [S30]; canteen caterers may not keep fuel savings under client-paid utility terms [A] (not checked). |
| R4 | Electrifying powder-coating and small process heat | Electric ovens are old technology, not a new capability; the industry body called the disruption a logistics problem, not a shortage [S49]. |
| R6 | Sensor-only onion storage monitoring | Monitoring without control does not cut loss; Godaam's founder said the sensors failed to identify spoilage [S54]. |
| R7 | Onion irradiation | Large regulated facility, beyond a ₹5 lakh entrant [A]; sprouting is the smallest loss share (8-10% in one study [S52]). |
| R9 | Cardamom heat-pump dryer | Drying costs ₹2.10 per kg with LPG [S87] or about ₹8 per kg by one grower's account [S88], tiny against a ₹3,146 per kg price [S10]; colour premium from better drying not found after 2 searches; electric dryers and local designs that keep green colour already exist [S91]. |
| R10 | Locally laser-perforated export liners | Uflex already sets micro-perforations by respiration rate and has ICAR accreditation for pomegranate [S92, S93]; StePac's Xtend is sold in India through a distributor [S94]. |
| R11 | SO2 pads for grape export | No Indian maker or price found after 1 search; dosing is hard to control [S95]; likely registration burden [A] (not checked). |
| R12 | Radiative cooling roof paint | Crowded coatings market with large makers [S15, S16] and claims of 80-90% reflectance at ₹20-40 per sq ft [S96]; the 96.3% lab result [S13] is not a commercial product; durability not checked. |

## 5. Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Commercial LPG Prices Skyrocket by ₹993, Delhi Rate Crosses ₹3,000 Mark | Open Magazine | https://openthemagazine.com/business/commercial-lpg-prices-skyrocket-by-993-delhi-rate-crosses-3000-mark | 2026-05 | 2026-11-01 | Delhi price ₹2,078.50 to ₹3,071.50 | search summary |
| 2 | Lithium battery (tag page) | JMK Research | https://jmkresearch.com/tag/lithium-battery/ | not shown (recent) | 2026-11-01 | LFP cell US$54.59/kWh, India landed 13-23% higher | search summary |
| 3 | Induction ovens with big batteries solve lots of problems | Electrek | https://electrek.co/2024/02/29/induction-ovens-with-big-batteries-solve-lots-of-problems/ | 2024-02-29 | 2026-11-01 | Impulse Labs and Channing Street Copper prices, batteries | search summary |
| 4 | Wholesale onion prices go up by 25 percent at Lasalgaon, Pimpalgaon mandis | Business Today | https://www.businesstoday.in/india/story/wholesale-onion-prices-go-up-by-25-percent-at-lasalgaon-pimpalgaon-mandis-549144-2026-08-14 | 2026-08-14 | 2026-11-01 | Lasalgaon average ₹1,021 (May) to ₹1,740 (June) | search summary |
| 5 | Nashik: Onion Rotting In Storage Sheds As Rainfall Hits Quality; Lasalgaon Prices Touch ₹4,051/Quintal | Free Press Journal | https://www.freepressjournal.in/pune/nashik-onion-rotting-in-storage-sheds-as-rainfall-hits-quality-lasalgaon-prices-touch-4051quintal | 2026-08 | 2026-11-01 | August prices, about 30% storage losses | search summary |
| 6 | Capillary cooling technology with forced-air cross ventilation: an eco-friendly onion storage technology | Energia na Agricultura (UNESP) | https://seer.tupa.unesp.br/BIOENG/article/view/1308 | 2026 (per summary) | 2026-11-01 | Solar fan store design, weight loss under 4% vs 9% | search summary |
| 7 | An IoT based controlled environment storage (onion) | arXiv 2601.10745 | https://arxiv.org/pdf/2601.10745 | 2026-01 | 2026-11-01 | Solar IoT prototype ₹60k-70k, target losses | search summary |
| 8 | PM Launches National Makhana Board In Bihar | Drishti IAS | https://www.drishtiias.com/state-pcs-current-affairs/pm-launches-national-makhana-board-in-bihar/print_manually | 2025-09-16 | 2026-11-01 | Board launch, ₹476.03 crore scheme (attribution uncertain within result set) | search summary |
| 9 | Makhana Mahotsav 2025: Beyond the Ceremonies | Agriculture Post | https://agriculturepost.com/agribusiness/makhana-mahotsav-2025-beyond-the-ceremonies-the-real-stakes-of-fox-nut-prosperity/ | 2025 | 2026-11-01 | Mechanisation stated as a need | search summary |
| 10 | Indian cardamom holds firm as auction volumes stay high | Commodity Board | https://commodity-board.com/indian-cardamom-holds-firm-as-auction-volumes-stay-high | 2026-10 | 2026-11-01 | Auction average ₹3,146/kg on 7 Oct 2026 | search summary |
| 11 | Switch to sea shipments lifts Indian pomegranate exports by 20% | FreshPlaza | https://www.freshplaza.com/article/9799397/switch-to-sea-shipments-lifts-indian-pomegranate-exports-by-20/ | 2026 | 2026-11-01 | Sea-freight shift | search summary |
| 12 | Nashik: Grapes, Onions, Pomegranates And Wine Drive Export Growth In 2026 | Free Press Journal | https://www.freepressjournal.in/pune/nashik-grapes-onions-pomegranates-and-wine-drive-export-growth-in-2026 | 2026 | 2026-11-01 | Grape exports 2025-26 | search summary |
| 13 | JNCASR eco-friendly radiative cooling paint cuts energy use | Mysuru Infra Hub | https://mysuruinfrahub.com/jncasr-eco-friendly-radiative-cooling-paint-cuts-energy-use-and-beats-the-heat/ | not shown | 2026-11-01 | 96.3% reflectance | search summary |
| 14 | Affordable radiative cooling paint developed by scientists | The Daily Pioneer | https://www.dailypioneer.com/2023/india/affordable-radiative-cooling--paint-developed-by-scientists.html | 2023 | 2026-11-01 | About 10°C surface reduction | search summary |
| 15 | Indicus Paints launches heat reflective coating Heatseal | Indian Chemical News | https://www.indianchemicalnews.com/chemical/indicus-paints-launches-heat-reflective-coating-heatseal-17100 | 2023-04 | 2026-11-01 | Incumbent coating | search summary |
| 16 | Kansai Nerolac puts Perma NoHeat to the test | Pulse (pulse.bot) | https://www.pulse.bot/marketing/news/kansai-nerolac-puts-perma-noheat-to-the-test-in-public-spaces-via-new-activation-85c07ba5-f489-4aad-b643-f2491e3894de | not shown | 2026-11-01 | Incumbent coating | search summary |
| 17 | Commercial LPG cylinder price hiked from June 1 | fuelprice.co.in | https://fuelprice.co.in/news/commercial-lpg-cylinder-price-hike-june-2026-delhi-3113-food-business-impact | 2026-06 | 2026-11-01 | Delhi ₹3,113.50 | search summary |
| 18 | Major relief! Price of 19 kg LPG cylinder cut by ₹183.50 | Business Today | https://www.businesstoday.in/amp/india/story/major-relief-price-of-19-kg-lpg-cylinder-cut-by-rs-183-50-check-new-rates-540145-2026-07-01 | 2026-07-01 | 2026-11-01 | Delhi ₹2,930 | search summary |
| 19 | LPG price September 2026: commercial hike, domestic steady | Indian Pay Calculator | https://www.indianpaycalculator.in/govt-news/lpg-price-september-2026-commercial-hike-domestic-steady | 2026-09 | 2026-11-01 | Delhi ₹2,747.50, Mumbai ₹2,701 (weak source) | search summary |
| 20 | Commercial LPG cylinder price hiked by Rs 111 to cost Rs 1866 in Nagpur | Nagpur Today | https://www.nagpurtoday.in/commercial-lpg-cylinder-price-hiked-by-rs-111-to-cost-rs-1866-in-nagpur/ | 2026-01-01 | 2026-11-01 | January 2026 price (Nagpur) | search summary |
| 21 | Hormuz crisis initially halted commercial LPG supply, now restored to 70% of pre-war levels | WION | https://wionews.com/india-news/hormuz-crisis-initially-halted-commercial-lpg-supply-now-restored-to-70-of-pre-war-levels-govt-1774614547513 | 2026-03/04 | 2026-11-01 | Supply cut and staged restoration | search summary |
| 22 | Restaurant Times (commercial LPG limits lifted) | Restaurant Times | https://www.restauranttimes.com/?p=9483 | 2026-07-01 | 2026-11-01 | Limits lifted | search summary |
| 23 | Restaurants turn frugal as LPG shortage bites; NRAI seeks govt support | Storyboard18 | https://storyboard18.com/how-it-works/india-restaurants-adapt-to-lpg-shortage-amid-west-asia-conflict-92051.html | 2026-03 | 2026-11-01 | NRAI: 95% gas-dependent, shift a stopgap (attribution uncertain within result set) | search summary |
| 24 | LPG Concerns Spark Electric Cooking Rush | Open Magazine | https://openthemagazine.com/business/lpg-concerns-spark-electric-cooking-rush-as-homes-and-restaurants-scramble-for-alternatives | 2026-03 | 2026-11-01 | Restaurants not a priority LPG sector | search summary |
| 25 | LPG shortage: Bought a Rs 9,000 commercial induction cooktop for Rs 23,000 | WION | https://www.wionews.com/india-news/lpg-shortage-bought-a-rs-9-000-commercial-induction-cooktop-for-rs-23-000-says-mumbai-restaurateur-1773292765974/amp | 2026-03 | 2026-11-01 | Induction price spike anecdote | search summary |
| 26 | Indore News: Food Hubs Struggle As Shortage Starts To Bite | Free Press Journal | https://www.freepressjournal.in/amp/indore/indore-news-food-hubs-struggle-as-shortage-starts-to-bite | 2026-03 | 2026-11-01 | Induction needs strong connections, slower cooking | search summary |
| 27 | Govt urges manufacturers to scale induction cooktop output | Angel One | https://www.angelone.in/news/economy/govt-urges-manufacturers-to-scale-induction-cooktop-output-amid-lpg-disruptions | 2026-03 | 2026-11-01 | Government push | search summary |
| 28 | Induction Kadai (listings) | IndiaMART | https://m.indiamart.com/impcat/induction-kadai.html | not shown | 2026-11-01 | Transglobe kadai ₹36,000; Stella 3.5 kW ₹19,850 (attribution between IndiaMART pages uncertain) | search summary |
| 29 | Induction Deep Fryer (listings) | IndiaMART | https://m.indiamart.com/impcat/induction-deep-fryer.html | not shown | 2026-11-01 | HIKE fryers ₹1,29,990 and ₹1,41,436 | search summary |
| 30 | West Asia tensions push hospitality sector to explore LPG-free kitchens | UNI | https://www.uniindia.com/west-asia-tensions-push-hospitality-sector-to-explore-lpg-free-kitchens/business-economy/news/3769815.html | 2026 | 2026-11-01 | Lorman turnkey bulk induction | search summary |
| 31 | West Asia tensions spur push for induction cooking systems | Lokmat Times | https://www.lokmattimes.com/business/west-asia-tensions-spur-push-for-induction-cooking-systems-to-cut-lpg-dependence | 2026 | 2026-11-01 | Vendor claim of about 60% saving | search summary |
| 32 | HungerBox invests 3.5 crore to enable electric cooking shift | CSR Universe | https://thecsruniverse.com/articles/hungerbox-invests-3-5-crore-to-enable-electric-cooking-shift-amid-lpg-supply-disruptions | 2026 | 2026-11-01 | Canteen platform funding the shift | search summary |
| 33 | Commercial electric cooking technologies (BEE showcase) | Energetica India | https://www.energetica-india.net/keyword/commercial-electric-cooking-technologies | 2026 | 2026-11-01 | Seven makers, vendor directory | search summary |
| 34 | Etroly India (startup profile) | Kerala Startup Mission | https://startups.startupmission.in/startups/pQOjq | not shown (retrieved 2026) | 2026-11-01 | Solar induction with battery backup | search summary |
| 35 | Indian startup launches plug-and-play hydrogen cooking unit | pv magazine | https://www.pv-magazine.com/2026/04/07/indian-startup-launches-plug-and-play-hydrogen-cooking-unit | 2026-04-07 | 2026-11-01 | Greenvize | search summary |
| 36 | A Rs 1,50,000 stove that runs on water | Business Today | https://www.businesstoday.in/india/story/a-rs150000-stove-that-runs-on-water-indias-new-bet-on-hydrogen-cooking-525477-2026-04-14 | 2026-04-14 | 2026-11-01 | Hydrogen stove price | search summary |
| 37 | Reurja launches 1300°C plasma technology in India | ThePrint (ANI release) | https://theprint.in/ani-press-releases/amid-growing-demand-for-high-performance-electric-cooking-reurja-launches-1300c-plasma-technology-in-india/2909305/ | 2026 | 2026-11-01 | Competitor | search summary |
| 38 | SWELECT brings solar cooking to induction stoves | Whalesbook | https://www.whalesbook.com/news/English/renewables/SWELECT-Brings-Solar-Cooking-to-Induction-Stoves-Amid-LPG-Price-Hikes/69df9c02498f7e9bcb0144fd | 2026 | 2026-11-01 | Off-grid solar cooking, battery cost | search summary |
| 39 | India's induction cooker demand surge tests power grid | Whalesbook | https://www.whalesbook.com/news/English/industrial-goodsservices/Indias-Induction-Cooker-Demand-Surge-Tests-Power-Grid-Amid-LPG-Crisis/69d8ddd2e0ea10058db692e6 | 2026 | 2026-11-01 | 13-27 GW projection | search summary |
| 40 | Commercial electricity rate per unit in Pune | NoBroker | https://www.nobroker.in/packers-and-movers/guides/commercial-electricity-rate-per-unit-in-pune/ | 2026-04 (FY 2026-27 rates) | 2026-11-01 | LT-II(A) and LT-II(B) tariffs (non-official) | search summary |
| 41 | EV battery price in India (2026) | MeraEV | https://www.meraev.com/blog/ev-battery-price-in-india-2026-replacement-costs-per-kwh-rates-and-why-youll-probably-never-pay-them | 2026 | 2026-11-01 | Pack ₹8,000-15,000/kWh incl. GST (weak) | search summary |
| 42 | Solar battery price India | QuickEstimate | https://quickestimate.co/blog/solar-battery-price-india | 2026 | 2026-11-01 | Retail LFP ₹20,000-35,000/kWh (weak) | search summary |
| 43 | BIS certification for lithium ion batteries: IS 16046 | IndiaFilings | https://www.indiafilings.com/bis-certification/lithium-ion-batteries | not shown (retrieved 2026) | 2026-11-01 | Model-wise pack registration (consultant source) | search summary |
| 44 | India: compliance framework for rated capacity verification of Li-ion cells and batteries | SIQ | https://www.siq.si/en/news/india-compliance-framework-for-rated-capacity-verification-of-li-ion-cells-and-batteries/ | 2026-04-09 | 2026-11-01 | 2026 capacity verification rule | search summary |
| 45 | NRAI released India Food Services Report 2024 | Hospitality & Catering News (hospemag) | https://www.hospemag.me/cms/national-restaurant-association-of-india-nrai-released-india-food-services-report-2024 | 2024 | 2026-11-01 | Mumbai 141,456 restaurants | search summary |
| 46 | NRAI releases India Food Services Report 2024 | MediaBrief | https://mediabrief.com/nrai-releases-india-food-services-report-2024/ | 2024 | 2026-11-01 | Hyderabad 74,807 restaurants | search summary |
| 47 | Food services sector set to reach Rs 7.76 lakh crore | India Retailing | https://www.indiaretailing.com/2024/07/10/food-services-sector-set-to-reach-rs-7-76-lakh-crore | 2024-07-10 | 2026-11-01 | Organised share 43.8% FY24 | search summary |
| 48 | Medium and small units bear brunt of gas crisis | Lokmat Times | https://www.lokmattimes.com/aurangabad/medium-and-small-units-bear-brunt-of-gas-crisis | 2026-03 | 2026-11-01 | Powder-coating and food units hit (attribution uncertain within result set) | search summary |
| 49 | LPG supply disruption likely due to logistics issues, not shortage | Free Press Journal | https://www.freepressjournal.in/india/lpg-supply-disruption-likely-due-to-logistics-issues-not-shortage-indian-industries-association | 2026-03 | 2026-11-01 | Industry body view | search summary |
| 50 | Commercial LPG price hike, supply crunch push restaurants to brink | Pulse (ET EnergyWorld) | https://www.pulse.bot/energy/news/commercial-lpg-price-hike-supply-crunch-push-restaurants-to-brink-f88fe0e3-0ccd-439b-925c-22b6bb365498 | 2026 | 2026-11-01 | Diesel and induction stopgaps raised costs | search summary |
| 51 | Onion storage study (phytojournal 2020, vol 9 issue 6) | Journal of Pharmacognosy and Phytochemistry | https://phytojournal.com/archives/2020/vol9issue6/PartT/9-6-339-608.pdf | 2020 | 2026-11-01 | 30-60% storage damage; irradiation stops sprouting (attribution uncertain within result set) | search summary |
| 52 | Onion storage study (Indian Journal of Horticulture) | Indian Academy of Horticultural Sciences | https://journal.iahs.org.in/index.php/ijh/article/download/1953/589 | not shown (retrieved 2026) | 2026-11-01 | Shrinkage 30-40%, rot 10-12%, sprouting 8-10% (attribution uncertain) | search summary |
| 53 | An innovative onion storage structure | ICAR Indian Horticulture | https://epubs.icar.org.in/index.php/IndHort/article/view/126543 | not shown (retrieved 2026) | 2026-11-01 | ₹50,000 structure, ₹167 vs ₹140/q, 8-10% losses, about 30 t | search summary |
| 54 | Onion price rise: woman entrepreneur's IoT sensors (Godaam) | The Better India | https://www.thebetterindia.com/240698/onion-price-rise-costly-warehouse-storage-research-iot-sensors-woman-entrepreneur-nashik-ros174/ | not shown (retrieved 2026) | 2026-11-01 | Godaam claim and founder's admission | search summary |
| 55 | Low cost onion storage | Krishi Jagran | https://krishijagran.com/news/low-cost-onion-storage/ | not shown (retrieved 2026) | 2026-11-01 | 42,282 structures, 9.65 lakh t | search summary |
| 56 | Peeling layers: Maharashtra's onion supply chain | WRI India | https://wri-india.org/perspectives/peeling-layers-maharashtras-onion-supply-chain | not shown (retrieved 2026) | 2026-11-01 | 50-60% stored; 1.5 MT storage 2015-16, 0.5 MT added (attribution between WRI India and an IDEAS/RePEc paper uncertain) | search summary |
| 57 | As prices fall onion growers want Maharashtra CM to chair urgent meet | The Week (PTI) | https://www.theweek.in/wire-updates/national/2025/08/03/bom2-mh-onion-growers-cm.html | 2025-08-03 | 2026-11-01 | ₹800-1,200/q vs cost ₹2,500 | search summary |
| 58 | Forced ventilation onion storage trial | Food Science and Preservation (Korea) | https://koreascience.or.kr/article/JAKO200111920919046.page | 2001 | 2026-11-01 | Rot about 25% vs 35-38% | search summary |
| 59 | Vigyan Ashram onion storage blower trial | Vigyan Ashram (Google Docs) | https://docs.google.com/document/d/1zsQ4sItuTJs_iNV6AXHfDVlCDtoDRQRT/export?format=pdf | not shown (retrieved 2026) | 2026-11-01 | Fans cut rot but raised moisture loss | search summary |
| 60 | Forced vs natural ventilation onion storage (90-day study) | Scinapse | https://www.scinapse.io/papers/4298008407 | not shown (retrieved 2026) | 2026-11-01 | Weight loss 25.23% vs 34.47-35.10% (attribution uncertain) | search summary |
| 61 | Onion cold storage: potential to stabilize price fluctuation | ICAR | https://icar.org.in/en/node/4701 | not shown (retrieved 2026) | 2026-11-01 | Losses up to 46% in four months in ventilated structures (attribution uncertain) | search summary |
| 62 | Tata Steel launches Agronest by Nest-In, India's first smart warehouse for onion storage | Tata Steel | https://www.tatasteel.com/newsroom/press-releases/india/2020/tata-steel-launches-agronest-by-nest-in-india-s-first-smart-warehouse-for-onion-storage/ | 2020-07 | 2026-11-01 | Incumbent product | search summary |
| 63 | Nashik: Onion prices rise ₹700 per quintal in a week as fresh arrivals are delayed | Free Press Journal | https://www.freepressjournal.in/pune/nashik-onion-prices-rise-700-per-quintal-in-a-week-as-fresh-arrivals-are-delayed | 2026-10 | 2026-11-01 | Max ₹3,601 to ₹4,525 (10-19 Oct) (attribution uncertain within result set) | search summary |
| 64 | Indian onion prices fall below production cost | FreshPlaza | https://www.freshplaza.com/asia/article/9821553/indian-onion-prices-fall-below-production-cost/ | 2026 (not shown exactly) | 2026-11-01 | Cost about ₹1,800/q, average ₹1,250 | search summary |
| 65 | Kanda chawl scheme (Marathi) | Vikaspedia | https://mr.vikaspedia.in/agriculture/policies-and-schemes/936947924915930940-92c93e91c93e930 | undated (retrieved 2026) | 2026-11-01 | ₹6,000/t norm, 25% or max ₹1,500/t, design rule | search summary |
| 66 | 80 to 90 lakh tonnes of onion get spoiled during storage and transportation: Pasha Patel | Deccan Herald | https://www.deccanherald.com/amp/story/india%2Fmaharashtra%2F80-to-90-lakh-tonnes-of-onion-get-spoiled-during-storage-and-transportation-pasha-patel-3674351 | not shown (retrieved 2026) | 2026-11-01 | National loss estimate | search summary |
| 67 | Nashik: Centre begins onion procurement at ₹1,235 per quintal | Free Press Journal | https://www.freepressjournal.in/pune/nashik-centre-begins-onion-procurement-at-1235-per-quintal-farmers-call-it-temporary-relief | not shown (retrieved 2026) | 2026-11-01 | Procurement price (from title) | search summary |
| 68 | Nashik: Centre raises onion procurement price to ₹1,730 per quintal | Free Press Journal | https://www.freepressjournal.in/pune/nashik-centre-raises-onion-procurement-price-to-1730-per-quintal-relief-for-farmers-across-india | not shown (retrieved 2026) | 2026-11-01 | Procurement price (from title) | search summary |
| 69 | Centre announces grand challenge for onion storage technologies | AgroSpectrum India | https://agrospectrumindia.com/2022/07/18/centre-announces-grand-challenge-for-development-of-technologies-for-primary-processing-storage-and-valorisation-of-onions.html | 2022-07-18 | 2026-11-01 | Onion Grand Challenge | search summary |
| 70 | Centre draws flak from parliamentary panel over state of onion silos | Down To Earth | https://www.downtoearth.org.in/amp/story/agriculture/centre-draws-flak-from-parliamentary-panel-over-state-of-onion-silos-86595 | not shown (retrieved 2026) | 2026-11-01 | Poor central storage | search summary |
| 71 | Nashik: Rotten onions, worms and maggots found at Lasalgaon CWC godown | Free Press Journal | https://www.freepressjournal.in/pune/nashik-rotten-onions-worms-and-maggots-found-at-lasalgaon-cwc-godown-questions-raised-over-storage | not shown (retrieved 2026) | 2026-11-01 | Warehouse rot | search summary |
| 72 | Makhana popping machine vs manual: cost, yield, ROI | AgriJob | https://www.agrijob.in/makhana-popping-machine-vs-manual-cost-yield-roi/ | not shown (retrieved 2026) | 2026-11-01 | Machine tiers and yield claims (blog) | search summary |
| 73 | Makhana Processing Machine (listings) | IndiaMART | https://m.indiamart.com/impcat/makhana-processing-machine.html | not shown (retrieved 2026) | 2026-11-01 | ₹75,000 to ₹7,50,000 listings | search summary |
| 74 | Makhana Popping Machine Launched | ICAR | https://icar.org.in/index.php/en/node/9014 | 2013-12 (event) | 2026-11-01 | ICAR machine, 200-farmer demonstration | search summary |
| 75 | Mechanizing Makhana Popping | ICAR | https://icar.org.in/en/node/4761 | not shown (retrieved 2026) | 2026-11-01 | Over 90% efficiency, quality, health | search summary |
| 76 | Press note (makhana mechanisation) | ICAR-CIPHET | https://ciphet.solarman.in/wp-content/uploads/2022/09/Press-note_English.pdf | 2022-09 | 2026-11-01 | Mechanised chain (attribution uncertain) | search summary |
| 77 | Interview with Dr S. N. Jha | Krishi Jagran | https://krishijagran.com/interviews/an-exclusive-interview-with-dr-s-n-jha-the-man-behind-india-s-makhana-revolution/ | not shown (retrieved 2026) | 2026-11-01 | Early machines could not make lava | search summary |
| 78 | The makhana value chain in Bihar: evidences | SlideShare | https://es.slideshare.net/mkrishnasingh/the-makhana-value-chain-in-bihar-evidences | not shown (retrieved 2026) | 2026-11-01 | Lava premium 7-11%; grading by pop size (attribution uncertain) | search summary |
| 79 | Subsidy of up to 1.5 lakh on a makhana popping machine | Tractor News | https://tractornews.in/news/excellent-news-for-makhana-farmers-you-can-get-a-subsidy-of-up-to-1-5-lakh-on-a-makhana-popping-machine-apply-here | not shown (retrieved 2026) | 2026-11-01 | 50-60% subsidy | search summary |
| 80 | Makhana business profit per acre | AgriJob | https://www.agrijob.in/makhana-business-profit-per-acre-cost-income-breakdown/ | 2026-07 | 2026-11-01 | Raw seed ₹28,000-40,000/q | search summary |
| 81 | Makhana price in India | Mera Kisan | https://merakisan.com/?p=7191 | 2026-07 | 2026-11-01 | Popped ₹700-1,700/kg retail | search summary |
| 82 | Proventus Agro press release | NSE filing | https://nsearchives.nseindia.com/corporate/PROVENTUSAGRO_12052026202559_Press_Release_.pdf | 2026-05-12 | 2026-11-01 | 2,500 t/yr Purnia unit | search summary |
| 83 | A study on constraints of makhana cultivation | Journal of Pharmacognosy and Phytochemistry | https://www.phytojournal.com/archives/2020.v9.i1.10580/a-study-on-constraints-of-makhana-cultivation-and-suitable-measures-for-its-better-development | 2020 | 2026-11-01 | About 80% of processed makhana from four districts | search summary |
| 84 | Model DPR Makhana | Bihar Horticulture Department | https://horticulture.bihar.gov.in/HORTMIS/BAIPP/Downloads/ModelDPRMakhana.pdf | not shown (retrieved 2026) | 2026-11-01 | Processing labour-intensive | search summary |
| 85 | Policy update (makhana) | IMPRI | https://www.impriindia.com/?p=61662 | not shown (retrieved 2026) | 2026-11-01 | Projected output about 11,500 MT | search summary |
| 86 | Makhana (current affairs PDF) | Drishti IAS | https://www.drishtiias.com/pdf/1788559292.pdf | not shown (retrieved 2026) | 2026-11-01 | Output about 60,000 MT 2025-26 | search summary |
| 87 | LPG fired cardamom dryer study (Idukki) | Indian Journal of Agricultural Engineering (i-scholar) | https://i-scholar.in/index.php/Ijae/article/view/48335 | not shown (retrieved 2026) | 2026-11-01 | ₹2.10/kg drying cost | search summary |
| 88 | Spice growers in India to get new technology for crop drying | Sputnik (mirror site) | https://sibitex.duckdns.org/20190225/india-innovators-farmer-crop-spices-1072720359.html | 2019-02-25 | 2026-11-01 | ₹800 per quintal drying anecdote (weak mirror) | search summary |
| 89 | Comparative analysis of cardamom drying technologies | IRJET (Issuu) | https://issuu.com/irjet/docs/comparative_analysis_of_cardamom_drying_technologi | not shown (retrieved 2026) | 2026-11-01 | Heat-pump and solar 6-12 h, better quality | search summary |
| 90 | Spice market weekly, 15.08.2026 | Spices Board India | https://indianspices.com/indianspices/sites/default/files/15.08.2026%20Spicemarket_.pdf | 2026-08-15 | 2026-11-01 | Cardamom grade prices (context only) | search summary |
| 91 | Cardamom drying chamber (Abraham low pressure) | National Innovation Foundation | https://nif.org.in/innovation/cardamom_drying_chamber/116 | not shown (retrieved 2026) | 2026-11-01 | Existing design keeps green colour | search summary |
| 92 | Flexfresh liner bag earns ICAR-NRCP accreditation for pomegranates | Packaging Strategies | https://packagingstrategies.com/articles/100745-flexfresh-liner-bag-earns-icar-nrcp-accreditation-for-pomegranates | not shown (retrieved 2026) | 2026-11-01 | Uflex incumbent | search summary |
| 93 | Indian papayas packed in Uflex's Flexfresh ideal for sea | Packaging Europe | https://packagingeurope.com/indian-papayas-packed-in-uflexs-flexfresh-ideal-for-sea | not shown (retrieved 2026) | 2026-11-01 | Respiration-based micro-perforation | search summary |
| 94 | StePac pomegranate solution | Packaging Europe | https://packagingeurope.com/stepac-pomegranate-solution | not shown (retrieved 2026) | 2026-11-01 | StePac Xtend; Indian distributor (attribution uncertain) | search summary |
| 95 | Marine Newslink January 2023 | Tata AIG | https://www.tataaig.com/s3/Marine_Newslink_Tata_AIG_January_2023_59d08073e8.pdf | 2023-01 | 2026-11-01 | SO2 dosing difficulty, 10 mg/kg limit | search summary |
| 96 | Cool roof coating for warehouse metal sheet | coolroofpaint.com | https://www.coolroofpaint.com/?p=4035 | not shown (retrieved 2026) | 2026-11-01 | Acrylic and ceramic coating prices and reflectance | search summary |
| 97 | Cool roof paint price India | Lumincoat | https://lumincoat.com/pages/cool-roof-paint-price-india | not shown (retrieved 2026) | 2026-11-01 | ₹10-45 per sq ft | search summary |
