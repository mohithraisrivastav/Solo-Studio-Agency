---
name: discover
description: Autonomous opportunity discovery with no starting idea. Use when the user gives a broad objective such as "find commercially promising opportunities". Runs three Opportunity Hunters in parallel with different lenses, triages their findings, sends each shortlisted opportunity to an independent Market Investigator, and returns a ranked shortlist with evidence levels.
argument-hint: "<broad objective, optional budget and geography>"
---

# DISCOVER

You are the Intelligence Director (see `CLAUDE.md`). Objective: $ARGUMENTS

## 1. Brief

Create `runs/<YYYY-MM-DD>-<slug>/`. Write `00-brief.md`: the objective in the user's words, date, budget, geography, and the decision gates from `CLAUDE.md`. Use the defaults in `CLAUDE.md` for anything the user did not state, and say so.

## 2. Hunt, in parallel

Launch three `opportunity-hunter` agents in one message. Each gets a different lens and chooses its own industries. Lenses steer where they look; they do not name industries.

- **Lens A, money wasted:** costly inefficiencies, workarounds, losses, spoilage, rework, downtime, and middlemen in operations-heavy industries.
- **Lens B, something changed:** new regulations or standards, scientific or technical capabilities that became cheap, input cost shifts, behaviour shifts.
- **Lens C, underserved and premium:** specialised buyers nobody serves well, poor product experiences, unmet premium demand.

Brief each hunter: the objective, its lens, the date, "choose at least 3 unrelated industries outside common startup themes", and its output path `01-hunt-A.md`, `01-hunt-B.md`, `01-hunt-C.md`.

## 3. Triage

Run `python3 tools/check_evidence.py` on the three files. Read them. Write `02-triage.md`:

- A table of every kept thesis: industry, problem, payer, evidence of spend, why-unsolved category, entry way for a small firm, evidence level.
- Pick 4 to 6 candidates from at least 3 unrelated industries. Judge on: strength of spending evidence, cost of the problem to the buyer, a beatable reason it is unsolved, a way in for a small firm, room for real differentiation, and early economics. Do not judge by how many sources a thesis cites.
- Drop theses whose reason-unsolved is weak demand, unless contrary evidence is strong. Say why each drop happened.

## 3b. Kill probe, to find fatal flaws and set research priorities

Before full investigations, launch one `market-investigator` per candidate in one message. Brief: "Kill probe. Name the one assumption that must hold. Check it against a primary source where one exists. Look for existing sellers, bundlers, subsidies, failed entrants, and the cheapest rival. Recompute the buyer's economics. Give an outcome: REJECT only for strong contradicting evidence or impractical figures, INVESTIGATE with the cheapest test, or ADVANCE. Say what the next research should be. Search as much as the question needs." Output `03-probe-<n>-<short-name>.md`. Drop REJECT. Send INVESTIGATE and ADVANCE candidates on, with the probe's priorities.

## 4. Verify independently, in parallel (survivors only)

Launch one `market-investigator` per surviving candidate in one message. Give each only: the problem statement in one paragraph, the target buyer, and the hunter file path labelled "unverified hypotheses, do your own research". Output `03-market-<n>-<short-name>.md`.

## 5. Commercial screen, in parallel

For each candidate whose problem spend is at least weak L1, launch a `business-architect` with a short brief: "Screen this opportunity before any invention. Who keeps the savings when it is fixed? How much money flows to the problem each year in one reachable cluster or segment (bottom-up)? What share could a small entrant plausibly capture, and what would it earn per customer over a customer's life after acquisition and founder time? What asset could accumulate that a copier could not buy in 12 months? Give a ceiling estimate with `tools/econ.py` if useful. No concept design." Output `04-screen-<n>.md`. Search as much as the question needs.

## 6. Shortlist

Write `04-shortlist.md`: for each candidate, the hunter's claim, the investigator's two verdicts (problem spend, solution demand), the screen's ceiling, where they disagree, and go / hold / drop.

**Pass rule for "go":** problem spend strong L1, or weak L1 with a decisive test under ₹50,000; a payer whose profit improves; a beatable reason it is unsolved; a ceiling that pays the founder above the stated hourly value at a scale reachable in 24 months; and room for an accumulating asset. Drop an idea only when strong evidence shows its demand is weak. Missing demand evidence makes it INVESTIGATE, with a cheap test, not a drop.

Rank INVESTIGATE ideas by upside if true divided by test cost, and name the best 3 tests with INR cost and time. Choose up to 3 for invention, from unrelated industries. If fewer pass, take fewer. Never pad. If every survivor is a service intermediary, run one more `opportunity-hunter` with the lens "new capability into products: materials, processes, devices, or technology that became cheap or possible, applied to a costly problem" before inventing.

Report to the user: the shortlist, what was dropped and why, and what was not checked.
