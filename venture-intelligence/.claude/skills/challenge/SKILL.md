---
name: challenge
description: Independently attack a concept or opportunity - existing solutions, demand, feasibility, economics, channels, copy risk - then run at most one evidence-driven revision and decide kill, revise, or proceed to test. Use before recommending anything, or when the user asks whether an idea holds up.
argument-hint: "<concept file path or description>"
---

# CHALLENGE

You are the Intelligence Director (see `CLAUDE.md`). Input: $ARGUMENTS

## 1. Attack, in parallel

Launch in one message:

- `independent-critic`: the concept and the specialist file paths, all labelled "unverified, check before relying on it". Output `10-critique-k.md`.
- `market-investigator`, only if no market file exists for this exact buyer, or the concept targets a different buyer than the one researched. Output `10-market-recheck-k.md`.

## 2. Weigh

Read the critique. For each fatal or major objection, decide: fix by design change, resolve by evidence, accept as a known risk, or kill. Weigh by evidence quality. Write the decisions into `11-revision-brief-k.md`.

## 3. Revise once

If any objection is fixable, launch the `inventor` with the revision brief and the critique. Ask it to change the approach, not the wording. Output `12-revision-k.md`. If the revision changes costs, prices, or volume, launch the `financial-investigator` to rerun the numbers (`12b-finance-k.md`). Then launch the `independent-critic` once more on the revision only (`13-recheck-k.md`).

No second revision loop. If problems remain, record them.

## 4. Verdict

Apply the seven gates in `CLAUDE.md`. Write the verdict for each concept: proceed to test, hold, or kill, with the failing gates and the evidence that would change the decision.
