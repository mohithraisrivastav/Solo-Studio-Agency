---
name: invent
description: Develop substantially different solutions for an opportunity, then test each for technical feasibility and business viability. Use with an opportunity from /discover or a problem the user describes. Runs the Inventor, then the Multidisciplinary Expert and Business Architect in parallel, then the Financial Investigator, and returns a concept slate.
argument-hint: "<opportunity file path or problem description>"
---

# INVENT

You are the Intelligence Director (see `CLAUDE.md`). Input: $ARGUMENTS

If no run folder exists, create one and write `00-brief.md`. Use `k` as the opportunity number.

## 1. Invent

Launch an `inventor` with: the problem statement, the market file path (labelled verified buyer research), the hunter file path (labelled unverified), and output `05-invent-k.md`. For several opportunities, launch one inventor each, in one message.

## 2. Feasibility and business design, in parallel

When the inventor finishes, launch in one message:

- `multidisciplinary-expert`: assess the three lead concepts and the wildcard. Output `06-expert-k.md`.
- `business-architect`: design the business for each lead concept and pick the strongest model. Give it the market file. Output `07-business-k.md`.

## 3. Numbers

Launch a `financial-investigator` for the two concepts the business architect and the expert rate highest. Give it both files, labelled unverified inputs to check, and the budget and founder hour value from `00-brief.md`. Output `08-finance-k.md` with its input JSON files beside it.

## 4. Slate

Write `09-slate-k.md`: for each lead concept, the mechanism, the feasibility class, the business model, contribution after founder time, peak cash, and the open questions. Pick the lead concept with reasons. Note where specialists disagree.

Report the slate to the user.
