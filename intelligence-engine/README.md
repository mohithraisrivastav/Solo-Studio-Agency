# Independent Intelligence Engine

A local system for finding opportunities, inventing different solutions, and judging whether they make commercial sense. It keeps evidence with sources and dates, does its own calculations, and is built to reject weak ideas.

It starts from zero. It has its own code, database, configuration, and memory. It does not read, import, or connect to any earlier personal system, memory, or repository. `iie/guard.py` enforces this in code, and `tests/test_independence.py` checks it.

## What works today

| Capability | Status | Where |
|---|---|---|
| Persistent store with version history | Working | `iie/db.py` |
| Jobs that survive a hard kill and resume from checkpoints | Working, tested with SIGKILL | `iie/orchestrator.py`, `tests/test_persistence.py` |
| Rerun from any stage, with old outputs kept and marked superseded | Working | `iie rerun` |
| Research connectors: Wikipedia, OpenAlex, Crossref, arXiv, Semantic Scholar, Stack Exchange, Hacker News, World Bank, SearXNG, Brave, PatentsView, single public pages | Built and tested against documented response formats. Not tested live here: this cloud session blocks those hosts | `iie/research/connectors.py` |
| Operator source bundles (a person or agent supplies sources with URL and retrieval date) | Working, used in the demo | `iie/research/engine.py` |
| Quote verification: every claim must quote its stored source text | Working | `iie/evidence.py` |
| Contradiction detection between numeric claims | Working (caught a 2.6x market-size conflict in the demo) | `iie/evidence.py` |
| Evidence ladder L0 to L5; only the user can record L2 and above | Working, enforced in code | `iie/evidence.py` |
| Seven invention methods with structured outputs | Working with a model or operator | `iie/invention/methods.py` |
| Diversity check: overlap, cosmetic variants, solution families | Working | `iie/invention/diversity.py` |
| Originality search and judgement, never claims "novel" | Working | `iie/invention/originality.py` |
| Unit economics, three scenarios, sensitivity, cash curve, break-even, founder time, "what it would take" | Working, deterministic | `iie/commercial/economics.py` |
| Premium-price checks and business model fit | Working | `iie/commercial/fit.py` |
| Twelve commercial questions with evidence levels computed in code | Working | `iie/commercial/demand.py` |
| Technical plans, keyword hazard flags, OpenSCAD concept CAD, BOM CSV | Working (hazard scan is keyword based) | `iie/engineering.py` |
| Critical review: fixed rules plus model review; disputes recorded | Working | `iie/critique.py` |
| Evidence gates, spending limits by demand level, experiments | Working | `iie/decision.py` |
| Approval gate for messages, publishing, purchases, spending, private files | Working, enforced in code | `iie/approvals.py`, `iie/tools.py` |
| Ollama and OpenAI-compatible local servers, hardware detection, model benchmark | Built. Not run here: no model could be installed in this container | `iie/llm/` |
| Web interface with all nine areas plus approvals, operator queue, settings | Working | `iie/web/` |
| CLI | Working | `iie/cli.py` |

## Not built yet

- Embedding-based similarity. Overlap and originality ranking use TF-IDF word overlap, which misses paraphrase. A model judges the closest sources to compensate.
- Patent and industrial design search without an API key. Indian patent and design registries have no connector.
- Price scraping of marketplaces. Prices come from observed listings in sources, user quotes, or labelled assumptions.
- Multi-user access and authentication for the web interface. Run it on localhost only.

## Quick start

```bash
cd intelligence-engine
pip install -e .            # or: pip install fastapi uvicorn jinja2 httpx pydantic python-multipart
iie init                    # creates ./var with a fresh database
iie hardware                # what this machine can run
```

Local model (recommended):

```bash
ollama pull qwen2.5:7b      # pick a size that fits your RAM; `iie hardware` suggests one
iie benchmark               # measures speed, JSON validity, and correctness; sets the default
```

Run a cycle:

```bash
iie new "Find an overlooked opportunity" --workflow full --budget 300000
iie run <project_id>
iie report <project_id> --out report.md
iie serve                   # web interface at http://127.0.0.1:8765
```

Workflows: `full`, `discovery`, `invention`, `evaluate` (pass `--concept-json`), `commercial` (pass `--concept-json` and `--economics-json`).

Modes: `fresh` (idea generation sees no stored concept history) and `evidence` (uses stored test results and outcomes from earlier projects).

## Without a model

With no model the engine still researches, stores sources, extracts rule-based claims, computes economics from your inputs, applies critique rules and gates, and records gaps. It marks every model step as "not performed" and writes method worksheets. It never fills the gap with invented text.

To have a person or an external agent answer the model steps, use the operator provider:

```bash
iie --provider operator run <project_id>
iie operator list
iie operator show <task_id>
iie operator answer <task_id> answer.json --by "Your Name"
```

Answers are checked against the schema and stored with the name of whoever answered.

## Research access

The free connectors need outbound HTTPS. Optional keys come from environment variables only and are never stored:

- `IIE_BRAVE_API_KEY` for Brave Search
- `IIE_SEARXNG_URL` for a self-hosted SearXNG
- `IIE_PATENTSVIEW_API_KEY` for USPTO PatentsView

`iie connectors` probes each one. Add `--operator-research` to let an operator supply source bundles when connectors fail.

## Evidence rules

- Public sources can lift a demand claim to L1 at most.
- L2 to L5 need direct evidence (interviews, commitments, deposits, orders, repeat orders) recorded by you with a counterparty and a date. Models, agents, and operators are refused in code.
- A price is "observed" only if it references a verified claim of a price. Otherwise it is an assumption, and the economics flag `PRICE_UNSUPPORTED`.
- Spending limits follow the demand level: 5% of budget until L2, 15% until L3, 40% until L4.

## Approvals

Tools that send messages, publish, buy, spend, change external accounts, or read private files stop with an approval request. You approve the exact payload once, in the web interface or with `iie approvals approve <id>`. Agents cannot approve. Excluded personal systems stay blocked even with approval.

## Tests and evaluations

```bash
python -m pytest -q                      # 48 tests
python evals/run_offline_evals.py        # scenarios that need no model or network
```

See `evals/RESULTS.md` for the ten evaluation tasks and their status, and `runs/demo-2026-10-31/SUMMARY.md` for the first full live cycle.

## Layout

```
iie/
  config.py guard.py db.py util.py schema.py text.py evidence.py approvals.py tools.py context.py roles.py
  llm/            providers (ollama, openai_compat, operator, none), hardware detection and benchmark
  research/       fetcher (robots.txt, cache, limits), connectors, research workflow
  invention/      methods, diversity, originality
  commercial/     economics, twelve questions, premium and fit checks
  engineering.py  hazards, plan schema, OpenSCAD and BOM output
  critique.py decision.py memory.py report.py
  stages/         the eleven stages and the workflows
  orchestrator.py jobs, recovery, reruns
  web/            FastAPI app, templates, CSS
tests/            unit, integration, recovery, independence, web
evals/            offline evaluation runner and results
runs/             recorded runs with their database, operator answers, report, and screenshots
```
