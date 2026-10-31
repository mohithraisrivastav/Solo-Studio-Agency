# 04 Shortlist (Intelligence Director)

Inputs: `01-hunt-A/B/C.md` (unverified theses) and five independent market investigations `03-market-1..5`. All market files pass `tools/check_evidence.py` with 0 problems (sourced share 56% to 75%). Every source was seen through search summaries only. Each investigator stopped at 35 to 44 searches because of a per-agent search limit.

## A distinction this run exposed

The investigators rated demand for the **specific service each hunter proposed**. Gate G1 asks whether buyers already spend on the **problem**. These differ. For example, gold loss is strong L1 as a problem for in-house manufacturers (`03-market-1-gold-loss.md` section 9) but weak L1 for a paid audit sold to wholesalers. Shortlisting below judges both. The gate definition in `CLAUDE.md` will be tightened after this run.

## Hunter claims against independent findings

| # | Opportunity | Hunter claim | Investigator finding | Disagreement | Problem spend | Proposed-service demand | Decision |
|---|---|---|---|---|---|---|---|
| 1 | Gold loss in karigar workshops | Sell loss audits to gold-issuing wholesalers (`01-hunt-A.md` T1) | Wholesalers cap loss with a fixed allowance, so they gain nothing from lower real loss; the savings go to job-work workshop owners and in-house manufacturers; a listed manufacturer credits about 100 bps of margin to cutting loss from above 1.5% to about 0.5% (`03-market-1`) | Wrong payer in the hunter's thesis | Strong L1 (manufacturers) | Weak L1 | **Go**, reframed to the buyer who keeps the savings |
| 2 | Shared supplier audits for small drug makers | Compulsory task, unserved segment (`01-hunt-C.md` T1); hunter B called it crowded consulting | No small domestic plant shown paying; Indian acceptance of shared reports unknown; foreign guidance accepts them only with the plant's own review; the regulator now licenses high-risk solvent makers and tracks batches; market about ₹0.65 to 11.9 crore a year (`03-market-2`) | Both hunters partly right | Weak | Weak L1 | **Drop.** Small market, regulator covering the riskiest inputs, acceptance unknown |
| 3 | Re-dyeing in job-work dye houses | Instruments sold, outcomes not (`01-hunt-A.md` T2) | Costly and recognised; dye makers already sell right-first-time programmes in India; who pays is negotiated case by case; fee pays off only for units over about 2 t a day with re-processing above about 5% (`03-market-3`) | Hunter's "vendors sell only equipment" contradicted | Moderate L1 (instruments, software, brand programmes) | Weak L1 | **Go, with caution.** Invention must not be another consulting programme |
| 4 | Idle hospital oxygen plants | Multi-brand upkeep (`01-hunt-B.md` T3) | Many plants idle because they are not needed (2022 capacity far above demand); public contracts small and yearly; no private payment evidence; a plant is cheaper only for high-use, grid-powered hospitals (`03-market-4`) | Hunter under-weighted weak demand | Weak | Weak L1 | **Drop.** Why-unsolved is largely category (a), weak demand |
| 5 | Lift accountability for housing societies | Sensor monitoring at ₹500 per lift a month (`01-hunt-C.md` T3) | Pain real and recent; society AMCs about ₹48,000 to 1,25,000 per lift a year, so the hunter's price ratio was wrong; no society pays for monitoring; products sold to makers; independent maintenance and audit firms abroad were bought by incumbents in 2026 (`03-market-5`) | Hunter's AMC figure wrong | Moderate L1 (AMC spend, legal exposure) | Weak L1 | **Go, with caution.** Device access and committee buying are the risks |

## Selected for invention (3, unrelated industries)

1. **Gold metal loss** (jewellery manufacturing). Buyer: in-house manufacturers and job-work workshop owners who keep the savings.
2. **Re-dyeing** (textile dyeing). Buyer: mid-size and large job-work dye houses; consider the brands and exporters who already fund programmes.
3. **Lift accountability** (residential property services). Buyer: housing society committees; consider facility managers and insurers.

None passes G1 yet on the proposed services. Invention is asked to find solutions aligned with where money already flows. The final decision will apply all six gates.

## Dropped
- **Pharma shared audits:** small market, regulator acting directly, shared-report acceptance unknown.
- **Oxygen plant upkeep:** idle because unneeded; weak payers.
