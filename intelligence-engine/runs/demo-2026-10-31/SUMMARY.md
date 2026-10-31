# First live cycle: open discovery, 31 October 2026

Question given to the engine: "Find a credible business opportunity in industries I have not considered. No starting idea." Budget set for the demo: ₹3,00,000 (a demo assumption you can change).

Full engine output: `report.md`. Database: `home/iie.db` (open it with `iie --home runs/demo-2026-10-31/home serve`). Every operator answer: `operator/`. Screenshots: `screens/`.

## How this run was produced, plainly

- The engine chose the industries itself by seed: **parenting and childcare**, **homebrewing and fermentation**, and **woodworking and furniture making**.
- This cloud session blocks every research host (Wikipedia, OpenAlex, arXiv, Stack Exchange and others) and every model download (ollama.com, Hugging Face). The engine tried each connector, recorded each failure as a research gap, and then asked for an operator source bundle.
- I (the Claude Code session) acted as the research operator. I ran real web searches and submitted 58 sources with URLs and retrieval dates. Page fetching was also blocked, so each source's text is the search tool's summary of that page, not verbatim page text. Every source is labelled this way. Treat all of it as leads to verify.
- No local model could be installed, so I also answered the engine's structured model requests through the operator queue (53 answers, all signed). The engine wrote every prompt, validated every answer against its schema, checked every quote against stored text, computed every number, and applied every gate and verdict itself.
- With a local model on your machine and open network access, the same cycle runs without an operator.

## Research evidence

- 58 sources, 90 verified claims, 0 claims with quotes that failed verification.
- Contradiction caught: India's 2024 kombucha market is $39.3 million in one report (MarketsandMarkets) and $102.6 million in another (IMARC), a 2.6x gap. Both stay in the record; neither is used as fact.
- Strongest signals by industry:
  - Childcare: establishments with 50+ employees must now provide a crèche (Section 67, Social Security Code), shared or outsourced crèches are allowed, companies have roughly doubled childcare budgets since 2022 (ProEves), and a July 2025 Bengaluru crèche abuse case shook parents' trust.
  - Fermentation: batter takes 6 to 8 hours in warm weather but up to 24 hours in winter and is sometimes thrown away; Indian ambient heat of 30 to 45°C makes brewing ferment too hot; an imported temperature controller is listed at ₹7,200.
  - Furniture: local carpenters make 80 to 85% of furniture by volume, counterfeit plywood is a known problem, consumer cases allege boards sold as termite proof failed within two years, and surface termite treatment weakens where boards are cut or drilled.

## Opportunities (7), ranked by breadth of evidence

| Opportunity | Industry | Independent sources | Why the gap exists |
|---|---|---|---|
| **Verifiable plywood and termite treatment for carpenter-made furniture** (selected) | Furniture | 8 | technical barrier |
| Climate-stable fermentation for idli/dosa batter and curd | Fermentation | 6 | overlooked segment |
| Shared crèche capacity for mid-size employers under the new labour code | Childcare | 5 | new enabler (regulation) |
| Lower-cost logistics for baby gear rental and resale | Childcare | 3 | distribution barrier |
| Independent crèche safety verification | Childcare | 3 | overlooked segment |
| Damage-resistant packing for online solid-wood furniture | Furniture | 2 | unknown |
| Hot-climate fermentation control for brewers and kombucha makers | Fermentation | 9 | weak demand (ranked last) |

The brewing opportunity had the most sources but ranked last, because the evidence pointed to weak demand: home brewing is legal for personal use only and selling needs a licence.

## Concepts (7 methods, 7 distinct solution families)

| Concept | Method | Principle | Originality verdict | Outcome |
|---|---|---|---|---|
| Traceable edge-seal treatment applied after cutting | First principles | chemical | related work found | shortlisted |
| Colour-change swab kit for board treatment | Cross-disciplinary (lab spot tests) | chemical | **close match**: patent application US 2018/0095042 and published standards | set aside |
| Five-year termite and board warranty | Inversion | business model | **close match**: Duroply lifetime guarantee (since 2016), CenturyPly 25-year warranty | set aside |
| Termite-break standoff mounting for built-ins | Constraint transformation | material/structural | related work found (ant caps on buildings) | shortlisted |
| Delivery-day material inspection visit | Unmet need | informational | related work found (inspection agencies) | shortlisted |
| Board passport: licence lookup plus photo trail | Combination | software | **close match**: the free BIS Care app already verifies licence numbers | set aside |
| Bait-cartridge plinth | Radical | biological | related work found (perimeter baiting, licensed use only) | not shortlisted |

## Commercial analysis (base case, all inputs are labelled assumptions)

| | Edge-seal kit | Standoff mounting set | Inspection visit |
|---|---|---|---|
| Price to buyer, incl. GST | ₹1,499 | ₹2,499 | ₹2,500 |
| Net revenue per unit | ₹967 | ₹1,507 | ₹1,624 |
| Contribution per unit, founder time paid at ₹600/h | -₹138 | -₹196 | -₹1,098 |
| Monthly cash profit | -₹5,984 | -₹7,019 | ₹23,545 |
| Peak cash need | ₹7,68,857 | ₹4,89,689 | ₹39,000 |
| Founder earnings per hour | negative | negative | ₹168 |
| Days to first revenue | 233 | 112 | 24 |
| Verdict | not viable | not viable | weak |
| What a 25% margin would need | price ≥ ₹2,550 | price ≥ ₹4,354 | price ≥ ₹6,220, or ≤ 0.56 h per visit |

## Critical objections that decided it

- Edge-seal kit: each kit loses money once founder time is paid; peak cash is about 2.6 times the budget; a termiticide sealant is probably a regulated pesticide product; board makers already advise edge treatment and Greenply moves treatment into the board core.
- Standoff mounting: the dealer margin, acquisition cost, and courier erase the margin; termite shields mainly make infestations visible rather than prevent them; carpenters' trims would bridge the gap; tall units on brackets need load and tipping tests.
- Inspection visit: a labour trap at about ₹168 an hour and about 30 visits a month; inspection agencies already exist; boards can be swapped after the visit; the licence check is already free in the BIS Care app.

## Decision

**No concept is worth building yet.** The edge-seal kit and the standoff set are rejected. The inspection visit goes back for revision.

Cheapest next actions, in order of cost:

1. Ask 5 interior designers whether they would refer clients (₹0).
2. Interview 5 pest-control technicians about how termites reach built-in furniture (₹0).
3. Offer a ₹499 30-minute video verification of delivered boards through two designers; success is 5 paying homeowners out of 20 (₹2,000). Messages and any booking page need your approval first.
4. One paid consultation on whether a termiticide edge sealant needs registration (₹5,000).

Spending limit from the evidence gate: at most ₹15,000 until real buyers confirm the problem (demand level 2).

## Problems this run exposed, all fixed and covered by tests

1. Bundle sources were not mapped to their industries, so discovery saw no evidence and silently moved on. Fixed; added a fallback and a rerun-from-stage command.
2. Originality judging ran only above a word-overlap threshold, so the BIS Care app was missed for the board passport. Fixed: the judge now sees each concept's own search results and the closest sources, and rates the match.
3. Several stages wrote records before pausing for answers, so a resume could write them twice. Fixed: model requests are batched first, writes come after.
4. Prompts listed evidence by age, not relevance, so the plywood claims were missing from the commercial prompts. Fixed: evidence is ranked by relevance to the concept.
5. The hazard scan missed plural words ("brackets", "wardrobes") and flagged false hazards ("laser-cut", "kitchen"). Fixed.
6. The cash model charged a prepaid first batch twice and overstated peak cash (₹9.5 lakh became ₹7.7 lakh for the edge-seal kit). Fixed, with a test.
7. Reruns left old experiments and objections active. Fixed: superseded outputs are marked and ignored.

The stage log in `report.md` shows each superseded run and its reason. Nothing was deleted.

## Limits of this run

- Source text is search-tool summaries, not page text. Some sources marked `_multi` summarise several results, and their page attribution is not confirmed.
- The model steps were answered by me, a large model. A small local model would make more errors. The quote checks and schema checks would catch some of them, not all.
- Every price, cost, and volume is an assumption. No buyer was contacted. Demand is level 1 for everything.
- The hazard scan is keyword based and still makes mistakes (it flagged "structural" for the edge-seal kit because a plan mentioned a work bench).
- No patent database or Indian design registry was searched; the engine says so in each originality record.
