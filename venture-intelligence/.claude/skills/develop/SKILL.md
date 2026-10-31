---
name: develop
description: Turn a selected concept into a practical product development and commercial validation plan - prototype, production route, certification, pricing test, first customers, budget, milestones, and kill criteria tied to the evidence ladder. Use only for a concept that survived /challenge, or when the user asks to plan one.
argument-hint: "<concept file path>"
---

# DEVELOP

You are the Intelligence Director (see `CLAUDE.md`). Input: $ARGUMENTS

## 1. Plans, in parallel

Launch in one message, each with the concept, the critique, and the latest finance file:

- `multidisciplinary-expert`: prototype specification, bill of materials with sources, build steps, the tests that retire each technical risk, certification path, production route for the first 100 units, costs and timeline. Output `14-dev-technical.md`.
- `business-architect`: offer, price test design, first 10 buyers and how to reach them, sales materials needed, channel partners, repeat revenue plan. Output `14-dev-commercial.md`.
- `market-investigator`: validation plan up the evidence ladder (L2 interviews, L3 commitments, L4 deposits): who, how many, scripts, success and failure thresholds, cost. Output `14-dev-validation.md`.

## 2. Budget and gates

Launch the `financial-investigator` with all three files: a spend plan by month, a cash buffer, and stage gates that release money only when the evidence level rises. Output `15-dev-finance.md`.

## 3. Plan

Write `DEVELOPMENT_PLAN.md`: a 90-day plan in three 30-day blocks, the spending limit at each evidence level, the kill criteria, and every action that needs the user's approval (contacting people, publishing, spending, buying).
