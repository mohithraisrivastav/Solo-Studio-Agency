# Audit 4: Broiler live-haul shrink and heat kit (hunter claim I1)

Date: 2026-11-01. Calculation script: `runs/2026-11-01-audit/10-audit-4-broiler-calc.py` (run output reproduced in section 3).
Limits of this audit: WebFetch could not open pmc.ncbi.nlm.nih.gov, avinews.com or other hosts (not on the session's allowed domains), and a rate limit interrupted searching once. Every source below is `via search summary`. No paid test, no contact with anyone.

## 1. Steelman

Indian broilers travel in open vehicles in heat, and the stopped vehicle at loading and at the market is the hot moment [S5]. Weight and birds are lost on every trip [S1]. A cheap kit that wets and ventilates the load could pay for itself if one party both bears the loss and runs the truck. Cooling at the stopped moment has working precedents abroad [S5][S3].

## 2. Claims checked

| # | Claim (hunter, file 02-hunt-A-r2.md, I1) | My finding | Status | Tag |
|---|---|---|---|---|
| 1 | No Indian retrofit seller exists (3 searches) | I found none in 4 searches (queries: "Tata Ace broiler cage vehicle India", "broiler transport vehicle misting sprinkler", "poultry transport trailer misting fans Regulation 1/2005", "India broiler transport vehicle"). Absence in English web search is weak: Indian body builders sell via IndiaMART and dealers, not indexed pages. | Unproven both ways | [H] |
| 2 | Chennai shrink 2.36% winter, 3.01% summer; mortality 0.43/0.53% | Matches the abstract, 24 trips [S1]. The same abstract says the winter-summer difference was not significant. | Verified, but the hunter omitted the "no significant difference" | [S1] |
| 3 | Mean shrink 4.47% in another Indian study | Not re-found. A slide deck gives 4-5% transport shrink, unattributed [S13]. Pre-slaughter Indian study finds 8.17% after 8 hours [S8]. Figures span 2.4% to 8% depending on trip length. | Unverified, range is wide | [S13] |
| 4 | 2,236 birds a truck, 2 kg birds | The count is from the Chennai study per the hunter [S1]. Weight 2 kg is an assumption. Small Indian vehicles (Tata Ace class) carry far fewer birds [A]. | Partly assumed | [A] |
| 5 | Loss per trip Rs 9,499 to Rs 17,499 | Arithmetic reproduces: 2,236 birds x 2 kg x 2.36% x Rs 90 = Rs 9,499; same with 3.01% x Rs 130 = Rs 17,499 [I]. It pairs the low shrink with the low price and the high with the high, and excludes mortality. | Arithmetic right, range stacked | [I] |
| 6 | 5% recovery saves Rs 71,239 to Rs 2,18,737 a year at 150 to 250 trips | Reproduced [I]. 5% of loss is 0.12 to 0.15 percentage points of body weight [I], tiny against the 0.65 point winter-summer gap [S1], so 5% is technically modest. The weak parts are the trips and who gets the saving. | Arithmetic right | [I] |
| 7 | Payback 2.7 to 8.4 months on Rs 50,000 | Reproduced [I]. Every input is an assumption, and benefit is credited to the kit all year. | Unsupported | [A] |
| 8 | Wetting by hand is free and practised, more in summer | Consistent with [S1]. This is the incumbent solution and the hunter's own evidence that buyers treat the problem as handled. | Verified | [S1] |
| 9 | A patent says retrofits are expensive | I found two US patents for a mobile cooling trailer for stopped poultry trucks [S5]. Cost statements not seen. | Not verified | [S5] |
| 10 | Fasting shrink 0.18 to 0.60% an hour | Matches Indian summary figures [S8]. Gut emptying is about 80 to 85% of loss in the first 6 hours [S6]. | Verified | [S6][S8] |

## 3. Economics (Python, saved script)

Reproduction of the hunter's numbers, then my cases. All inputs are assumptions unless sourced.

- Hunter reproduced: low case Rs 9,499 a trip, 5% is Rs 475, Rs 71,239 a year, payback 8.4 months. High case Rs 17,499, Rs 875, Rs 2,18,737, payback 2.7 months [I].
- Bill of materials, my estimate, not from catalogues: tank 500 L Rs 4,000; 12 V pump Rs 3,000; nozzles and hose Rs 2,500; four DC fans Rs 6,000; wiring and battery Rs 6,000; installation Rs 3,000; total Rs 24,500 [A]. Test: get three quotes. Search evidence: IndiaMART lists 12 V DC diaphragm pumps at Rs 125 to 175 at 2 to 3 L/min, a 5 L/min 100 bar misting pump at Rs 34,000, and a DIY misting set at Rs 5,800 [S12]. So a real misting pump costs about 10x a toy pump, and my Rs 3,000 pump line is a low guess [I].
- Selling price at 40% gross margin: Rs 41,000 before GST, Rs 48,380 with 18% GST [A]. The hunter's Rs 50,000 price and Rs 30,000 cost are similar order [A].
- Capital for 50 kits: Rs 12,25,000 for materials [A], plus installation, a demo truck, working capital and after-sales; likely Rs 20 lakh in total [A].
- Hot-season case: 60 to 150 hot trips a year instead of 150 to 250 all-year, recovery 0.1 to 0.65 points of body weight, price Rs 90 to 130 a kg. Payback ranges from 0.9 to 20 months, centre about 5 to 7 months at 0.3 points and 100 trips [I]. So the payback claim survives arithmetically if the kit works and the truck owner gets the saving. The result is very sensitive to recovery: at 0.1 points and 60 hot trips payback is 14 to 20 months [I].
- Mortality: 0.53% of 2,236 birds is about 12 birds, about Rs 2,600 a trip [I]. Worth including; the hunter left it out.
- Truck counts in a reachable region: Not found after 2 searches (queries: "broiler transport vehicles number Tamil Nadu", "live bird trader trucks Namakkal"). Missing.

Is 5% recovery credible? Physically yes, it is small. The only direct trial I found: misting plus ventilation after a 45-minute summer trip improved stress markers and meat quality, but did not report weight recovery [S3]. A US study kept trailer interiors within 2 degrees C of ambient up to 36 C using evaporative assist during loading, which shows temperature control, not weight saved [S5]. Held at 34 C for 12 hours, shrink was 5.7% against 3.2% at 25 C [S6], so heat can matter a lot on long holds; Indian short urban trips are different [A]. Wetting also may add water weight to feathers or crates, which could be penalised at the market [H].

## 4. Originality and what exists

- Worldwide: trailer ventilation, misting and fans at lairage exist for pigs and poultry [S15][S5]. The Dutch guidance asks for trucks with automatic fans and working water [S5]. Research in Brazil says summer is the critical season [S2]. Brazil dry-season mortality was twice as high on the 15 km trips [S2]. Trade vehicles by Rotem or Tuffy: Not found after 2 searches (queries: "Rotem poultry transport trailer", "Tuffy poultry truck"). Price data for any of these: not found.
- India: poultry trucks listed on dealer sites from Rs 4.47 lakh [S11]; no live-bird body or kit price found. FAO says without equipped vehicles mortality of 5 to 10% is possible [S8], a number I do not trust for modern trips.
- Why adoption could be low: the losses measured (2 to 3%) are priced into the trade and the hand-wetting is free [S1][I]. Whether buyers undervalue it is not tested [H].

## 5. Buyer value: who bears the loss

- Contract farming: the grower is paid a fixed charge per bird on live weight at the farm [S10]. Transport shrink after the farm weighing falls on the integrator or trader [I]. Integrators in India are large and run their own fleets [S14][A].
- Open market: Not found after 3 searches (queries: "farm lifting weight deduction broiler India", "borne by trader", "Namakkal dead bird deduction"). I could not establish whether traders deduct shrink from the farmer at the farm, or sell on at market with an allowance. Missing, and it decides who benefits.
- The FAO annex shows one trader absorbing transport cost per kg [S8], so the trader can be the loss bearer, but this is old and a single example.
- What traders do now: wet by hand, more in summer [S1], and travel at night [A, not verified].
- Season: shrink and mortality differ little by season in the one Chennai study [S1], while Brazil finds a summer dry-season mortality effect [S2]. Heat-driven share: not separated in any source. Fasting and gut emptying explain most early loss [S6]. A Dutch trial found transport added about 0.30% an hour beyond fasting [S7].

## 6. Distribution

Not found after 2 searches (queries: "who sells poultry vehicle accessories India traders", "poultry equipment dealers Namakkal"). Hypothesis: sales go through truck body builders, poultry equipment dealers and integrator transport managers [H]. First 10 customers would be reached by the founder directly in one cluster; first 100 need a dealer or an integrator contract, because a trader's truck is often one of a few [H]. Decider: the owner of the truck, not the driver, who runs the loading [H]. Test: ask 5 body builders and 5 traders.

## 7. Objections

Fatal: none proven.

Major:
1. Who bears and captures the saving is unknown (section 5). If the farmer is paid at the market weight, the trader gains nothing; if the farm weighs it, the trader or integrator gets it [I].
2. The benefit is seasonal and small per trip: Rs 475 to Rs 875 at the hunter's own 5% [I]. The kit competes with free hand-wetting [S1].
3. Heat-avoidable share is not measured; the one Indian seasonal study found no significant difference [S1].
4. Water at farms and markets, power, and corrosion are unexamined [S5].

Minor: the hunter's loss pairing, omitted mortality, fixed trip count.

## 8. Where the hunter's reasoning went wrong

1. "No Indian retrofit seller found after 3 searches" treated as a gap. Error: absence of evidence read as an opening, from English searches in a market that trades through local dealers. The hunter did flag the doubt, but still scored it "New capability".
2. Cites 2.36 to 3.01% shrinkage as proof of a large loss but omits that the same abstract finds no significant seasonal difference [S1]. Error: selective quoting; it undercuts "heat-driven".
3. Calls the buyer "trader or integrator" with "[H]" but computes payback as if the buyer gets all the saving. Error: assuming the payer is the beneficiary.
4. Stacks the range: low shrink with low price and low trips, high with high. Error: range compounding, which makes 2.7 to 8.4 months look like a tight interval. It is not a confidence interval.
5. Uses 150 to 250 trips a year for a seasonal benefit. Error: annualising a summer-only effect.
Item six: treats five percent recovery as conservative without any trial. Error: an assumed number given the look of caution. It is small in physical terms but unevidenced.
7. Mixes fasting loss with heat-avoidable loss. The hunter flags it, yet the economics ignore it. Error: noted risk not carried into the number.
8. Says hand-wetting "is free" but then claims the kit adds control and airflow, with no evidence the buyer values that. Error: feature versus value.
9. Rs 50,000 kit, Rs 30,000 unit cost are `[H]` with no catalogue check. Error: cost invented, and pump prices I found vary 10x [S12].
10. Mortality omitted from the saving. Error: incomplete benefit (adds about Rs 2,600 a trip [I]).

## 9. What holds up

The loss is real and measured at 2.4 to 3.0% [S1]. The stopped vehicle is a known hot moment and cooling at loading has precedents [S5]. The arithmetic of the hunter's figures reproduces. A 5% recovery is a small physical ask.

## 10. Simpler alternatives

Hand wetting and shaded waiting [S1]; a loading routine alone (free); an integrator changing time of day of lifting [A].

## 11. Verdict: INVESTIGATE (low confidence, leaning stop if answer 1 is no)

Reasons: no evidence kills it, and no evidence shows buyers want it. Demand level L0 to L1 at most.
What would change it:
- To REJECT: 5 trader/integrator calls show shrink is borne by the farmer or priced in at the market, or hand-wetting is judged sufficient.
- To ADVANCE (all three needed): a trader or integrator confirms they bear the shrink and pay for it, plus a weigh test (farm vs market, 10 loads, with and without misting) showing at least 0.3 points of body weight saved on hot trips [H], plus a quote showing unit cost under Rs 30,000 [H].

Unchecked: truck counts, actual Indian body builders, ISO or Indian rules (the Prevention of Cruelty to Animals transport rules for poultry), night transport share, the full text of [S1] and of the 2025 Scientific Reports paper (see [S8]).

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Estimation of live weight shrinkage and mortality during broiler transport in summer and winter, Chennai | TANUVAS via KrishiKosh | https://krishikosh.egranth.ac.in/items/4ef51cec-b772-4074-a37b-a567ca891303/full | 2018 | 2026-11-01 | shrink, mortality, wetting, no seasonal difference | search summary |
| 2 | Effect of transportation distances, seasons and crate microclimate on broiler production losses | PLoS ONE (dos Santos) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7176147/ | 2020 | 2026-11-01 | summer mortality, Brazil | search summary |
| 3 | Misting with forced ventilation after 45-minute transport | Asian-Australasian J Animal Sci | https://koreascience.kr/article/JAKO201502151148758.page?lang=en | 2015 | 2026-11-01 | misting trial | search summary |
| 4 | Sprinkler technology for broiler production, mini review | Frontiers Vet Sci | https://www.frontiersin.org/articles/10.3389/fvets.2020.544814/full | 2020 | 2026-11-01 | misting needs pressure | search summary |
| 5 | Mobile cooling apparatus / evaporative cooling patents and Arkansas study | USPTO; Eyes on Animals | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6546743 | not stated | 2026-11-01 | stopped-truck cooling, water limits | search summary |
| 6 | Feed withdrawal and shrink guides | ThePoultrySite, Meatingplace | https://www.thepoultrysite.com/articles/preprocessing-handling-in-broilers | not stated | 2026-11-01 | fasting share, heat 34 C 5.7% | search summary |
| 7 | Feed withdrawal of broilers before transport | Utrecht University | https://research-portal.uu.nl/en/publications/feed-withdrawal-of-broilers-before-transport-changes-plasma-hormo/ | not stated | 2026-11-01 | 0.42%/h vs 0.30%/h | search summary |
| 8 | Livestock industrialization, India poultry (annex II); pre-slaughter transport India | FAO; Scientific Reports | https://openknowledge.fao.org/server/api/core/bitstreams/97b6225d-2cf1-4bfa-a7b8-94cabcf0f0e1/content/x6115e0c.htm | not stated; 2025 | 2026-11-01 | trader cost, 5-10% mortality, 8.17% | search summary |
| 10 | Kalamkar, broiler contract farming | AgEcon Search | https://ageconsearch.umn.edu/bitstream/136383/2/17-SS-Kalamkar.pdf | not stated | 2026-11-01 | grower paid on live weight | search summary |
| 11 | Poultry trucks listing | Trucksfloor | https://trucksfloor.com/en/poultry | not stated | 2026-11-01 | vehicle prices | search summary |
| 12 | DC water pump category; misting pump listings | IndiaMART; Space Cool Systems | https://m.indiamart.com/impcat/dc-water-pump.html | not stated | 2026-11-01 | pump prices | search summary |
| 13 | Broiler marketing slide deck | SlideShare | https://de.slideshare.net/gurramsrinivas39/marketing-of-meat | not stated | 2026-11-01 | 4-5% shrink (weak) | search summary |
| 14 | Is contract broiler farming exploitative to small farmers? | ICAR IJAnS | https://epubs.icar.org.in/index.php/IJAnS/article/view/2237 | not stated | 2026-11-01 | integrator contracts | search summary |
| 15 | Cooling systems for pigs; pig trailer sprinklers | Farms.com | https://m.farms.com/news/cooling-systems-for-pigs-a-hot-topic-133303.aspx | not stated | 2026-11-01 | adjacent practice | search summary |
