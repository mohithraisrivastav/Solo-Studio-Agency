---
name: venture
description: Full autonomous cycle from a broad objective to a decision - DISCOVER, INVENT, CHALLENGE, then DEVELOP for the winner only. Use when the user asks the system to find, invent, and evaluate opportunities end to end without a starting idea.
argument-hint: "<broad objective>"
---

# VENTURE: full cycle

You are the Intelligence Director (see `CLAUDE.md`). Objective: $ARGUMENTS

1. Run `/discover` (steps in `.claude/skills/discover/SKILL.md`). Stop if nothing survives; report why.
2. For each shortlisted opportunity (at most 3), run `/invent` steps. Run the opportunities in parallel at each step.
3. For each lead concept, run `/challenge` steps, in parallel across concepts.
4. Write `DECISION.md`:
   - A gate table: concept by gate G1a to G6, pass or fail, with the evidence file for each cell.
   - The recommendation: the single strongest opportunity, or "none passes" with the closest candidates and what would change the decision.
   - Unresolved disagreements between specialists.
   - What was not checked, and why.
5. If one concept passes, run `/develop` steps for it alone.
6. Report to the user: the decision, the reasons, the strongest evidence, the biggest risks, and the cheapest next actions. Point to the files.
