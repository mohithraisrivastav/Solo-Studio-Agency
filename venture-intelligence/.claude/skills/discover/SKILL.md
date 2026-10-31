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

## 4. Verify independently, in parallel

Launch one `market-investigator` per candidate in one message. Give each only: the problem statement in one paragraph, the target buyer, and the hunter file path labelled "unverified hypotheses, do your own research". Output `03-market-<n>-<short-name>.md`.

## 5. Shortlist

Write `04-shortlist.md`: for each candidate, the hunter's claim, the investigator's verdict, where they disagree, the evidence level, and go / hold / drop. Choose up to 3 for invention, from unrelated industries. If fewer pass, take fewer. Never pad.

Report to the user: the shortlist, what was dropped and why, and what was not checked.
