# Evaluation results, 31 October 2026

Environment: cloud container, 4 CPU cores, 15 GB RAM, no GPU. Research hosts and model downloads are blocked by the session's network policy, so no local model and no live connector could be tested here.

| # | Test | Status | Evidence | What is still weak |
|---|---|---|---|---|
| 1 | Independent discovery | **Run once live**, with operator research and operator answers | Engine picked 3 unrelated industries by seed; 7 opportunities, each citing verified claims; ranking explained by source count and gap type. `runs/demo-2026-10-31/` | One run. Sources are search summaries. Needs a run with live connectors and a local model. |
| 2 | Original invention | **Run once live**, plus automated logic tests | 7 methods gave 7 distinct families; 3 close matches to existing products found and set aside. `tests/test_diversity.py` checks cosmetic variants and same-principle merges | Diversity uses word overlap (TF-IDF), which misses paraphrase. Embeddings are not built. |
| 3 | Premium physical product (₹5 lakh) | **Partial**: economics and premium checks only | `evals/results/t3_premium_object_report.md`: verdict "revise" with `FEW_COMPARABLES_AT_PRICE`, `NO_QUALIFIED_INTEREST_AT_PRICE`, `CAPITAL_EXCEEDS_BUDGET` | No live research on comparable prices, galleries, or buyers was run. Inputs are test assumptions. |
| 4 | Low capital business | **Not run as a dedicated test** | The demo's inspection visit is a low-capital case (₹39,000 peak, 24 days to revenue) and was judged a labour trap | Needs its own run with research on acquisition cost and real channels. |
| 5 | Commercial rejection | **Passed** (automated and live) | Teak speaker rejected with the price a 25% margin needs (₹28,788). Live demo rejected two concepts with numbers. `tests/test_business_reality.py` | The "stronger direction" is numeric (price, hours, materials) plus a generic model change. It does not yet research alternative models. |
| 6 | Knowledge challenge | **Not run as a dedicated test** | The demo touched unfamiliar fields (wood preservative spot tests, termite shields) and flagged limits rather than claiming expertise | Needs a designed test with an unfamiliar technical principle and live academic search. |
| 7 | Evidence integrity | **Passed** (automated) | With research disabled and a test model that fabricates sources, quotes, prices, and customer interest: 0 sources, 0 verified claims, 0 claims above L0, fabricated price references downgraded, no direct evidence, 13 research gaps recorded. `tests/test_evidence_integrity.py`, `evals/results/offline_evals.json` | Fabricated text in free fields (for example a concept description) is not fact-checked; only claims, quotes, prices, and evidence levels are. |
| 8 | Persistence and recovery | **Passed** (automated) | A subprocess is killed with SIGKILL during research; on restart the job is marked interrupted, completed sources, decisions, and approvals are intact, and the run resumes to completion. `tests/test_persistence.py` | Single machine only. No backup or export command yet. |
| 9 | Independence | **Passed** (automated) | Static scan of imports and source text; file access limited to the engine's own storage; excluded systems blocked even with approval; URL policy; fresh database with no attached data; an audit hook records every file opened during a full cycle and finds none outside the engine. `tests/test_independence.py` | The project lives inside a git repository that shares a name with an excluded system (on an empty, separate branch). Moving it to its own repository would make this cleaner. |
| 10 | Business reality | **Passed** (automated) | A ₹2.5 lakh object with materials at 1/22 of price is called "marginal", not profitable; the engine shows materials are 6.5% of real unit cost and flags labour, channel, delivery, tax, rejects, returns, tooling, volume, and cash flow. `tests/test_business_reality.py`, `evals/results/offline_evals.json` | Tax handling is a single GST rate input; HSN-specific rates are not looked up. |

## What improved during this evaluation

Seven defects found in the live run were fixed and given tests (see `runs/demo-2026-10-31/SUMMARY.md`). The most important: originality judging that missed a free government app, a cash model that charged a prepaid batch twice, and stage writes that could repeat after a pause.

## Run them yourself

```bash
python -m pytest -q
python evals/run_offline_evals.py
```

For tests 1 to 4 and 6 with live research, install Ollama and a model, allow outbound HTTPS, then:

```bash
iie benchmark
iie new "Find a credible business opportunity in industries I have not considered" --workflow full --budget 300000
iie new "Is a ₹5 lakh collectible object credible?" --workflow evaluate --concept-json concept.json --budget 500000
iie run <project_id>
```
