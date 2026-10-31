# Director's running notes on agent behaviour (for the improvement step)

Observed during the acceptance run. Each item cites the file where it shows.

## What worked

- Independence produced corrections. Market investigators overturned hunter claims on the payer (gold: `03-market-1`), the competitor landscape (re-dyeing: `03-market-3` found Archroma's right-first-time programme), the price benchmark (lifts: `03-market-5` corrected the AMC range), and the cause of idleness (oxygen: `03-market-4` found plants idle because unneeded).
- Evidence discipline held: every file passed `check_evidence.py` with 0 problems; "not found after N searches" appears where evidence was missing; no invented interviews or prices were seen.
- Hunters killed most candidates with reasons (9 to 12 raw candidates each, 3 kept).

## Weaknesses

1. **Wrong payer.** Hunter A sold the gold audit to the party that does not keep the savings (`01-hunt-A.md` T1 vs `03-market-1`). Hunters do not trace whose profit improves when the problem is fixed.
2. **Missed incumbent services.** Hunter A said instrument vendors sell equipment, not outcomes; dye makers already sell outcome programmes (`03-market-3`). Hunters search for startups and equipment, not for service offerings by large suppliers in the value chain.
3. **Mismatched benchmark.** Hunter C used home-lift AMC prices for housing societies (`03-market-5`). Price benchmarks are not checked for segment fit.
4. **Under-weighted weak demand.** Hunter B kept oxygen upkeep although capacity far exceeded need (`03-market-4`). Hunters do not check utilisation or actual need against installed base.
5. **Search budget.** Every investigator stopped at 35 to 44 searches, some before the deciding question (private hospital payment in `03-market-4`; refining charges in `03-market-1`). Agents are not told to plan searches around the deciding questions first.
6. **Gate ambiguity.** G1 does not separate spending on the problem from demand for the proposed solution (`04-shortlist.md`).
7. **Undefined shortlist rule.** `/discover` says "if fewer pass" without defining pass.
8. **Out-of-role action.** The gold investigator queued a user-facing task suggestion for unchecked items instead of only listing them in its file. Specialists should not create tasks, messages, or notifications.
9. **Environment.** All sources came through search summaries; page fetching was blocked. Figures could not be confirmed at source.
