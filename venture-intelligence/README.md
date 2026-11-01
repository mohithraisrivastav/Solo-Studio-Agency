# Venture Intelligence

A team of Claude Code specialist agents that finds, invents, challenges, and develops commercial opportunities. Claude does the reasoning and research. Two small scripts do what reasoning should not: money arithmetic and citation checks.

## Start

```bash
cd venture-intelligence
claude
```

Starting Claude Code inside this folder loads the agents in `.claude/agents/`, the skills in `.claude/skills/`, and the Director rules in `CLAUDE.md`.

## The four operations

| Command | What it does | Example |
|---|---|---|
| `/discover <objective>` | Three Opportunity Hunters search unrelated industries in parallel through different lenses. The Director triages. Independent Market Investigators verify each candidate. Returns a ranked shortlist with evidence levels. | `/discover Find high-margin opportunities a two-person team could start with ₹5 lakh` |
| `/invent <opportunity>` | The Inventor produces substantially different concepts. The Multidisciplinary Expert and Business Architect assess them in parallel. The Financial Investigator models the best two. Returns a concept slate. | `/invent runs/2026-10-31-x/04-shortlist.md opportunity 2` |
| `/challenge <concept>` | The Independent Critic tries to kill the concept with its own research. One revision loop at most. Verdict against seven gates. | `/challenge runs/2026-10-31-x/09-slate-2.md` |
| `/develop <concept>` | Prototype and production plan, go-to-market and pricing test, validation plan up the evidence ladder, budget with stage gates. | `/develop runs/2026-10-31-x/12-revision-2.md` |
| `/venture <objective>` | All four in sequence. Develops only a concept that passes every gate. Says so when nothing passes. | `/venture Independently discover three commercially promising opportunities in unrelated industries` |

Each run writes numbered files to `runs/<date>-<slug>/`, ending in `DECISION.md`.

## The specialists

| Agent | Responsibility |
|---|---|
| `opportunity-hunter` | Finds costly, poorly served problems where money is already spent; asks why each is unsolved; kills weak ones. |
| `market-investigator` | Verifies buyers, current alternatives, real prices, competitors including failed ones, and willingness to pay, with its own research. Designs the cheapest real demand test. |
| `inventor` | Generates concepts with eight distinct methods, clusters out cosmetic variants, checks prior art, keeps the commercial hook in from the start. |
| `multidisciplinary-expert` | Assembles the disciplines a concept needs, researches them, calculates, compares production routes, flags certification and safety, plans the cheapest technical test. |
| `business-architect` | Buyer and trigger, offer, price anchored to observed alternatives, route to the first 10 and 100 customers, acquisition cost, model choice, defensibility. |
| `financial-investigator` | Verifies the inputs that move profit most, then runs `tools/econ.py` for three scenarios: contribution after founder time, peak cash, payback, founder earnings per hour. |
| `independent-critic` | Steelmans, then attacks every line with independent research. Grades objections fatal, major, or minor. Kill, revise, or proceed. |
| Intelligence Director | The main Claude session running a skill. Coordinates, keeps specialists independent, weighs disagreements by evidence quality, applies the gates. Rules in `CLAUDE.md`. |

## Rules that keep it honest

- Every factual statement carries a tag: `[S#]` sourced, `[I]` inference, `[A]` assumption, `[K]` background knowledge (never for prices, markets, or competitors). See `standards/EVIDENCE.md`.
- No agent may invent buyers, quotes, orders, market sizes, prices, or sources. Gaps are reported as gaps.
- Demand evidence follows a ladder from L0 to L5. Desk research reaches L1 at most.
- Specialists receive other specialists' claims labelled "unverified" and check them independently.
- Seven gates decide a recommendation, and a commercial screen comes before any invention. If nothing passes, the system says so.
- Contacting people, publishing, buying, and spending are never done by agents. Plans list them for the user to approve.

## Tools

- `tools/econ.py input.json`: unit economics, three scenarios, monthly cash curve, peak cash, payback, founder earnings, and warning flags. `--help` shows the input format.
- `tools/check_evidence.py file.md`: finds untagged numbers, citations without a source row, and sources without a URL or date. Prints the sourced share of claims.

Python 3 standard library only.

## Notes

- Defaults when the user gives none: ₹5,00,000 founder capital, founder time at ₹750 per hour, India first.
- In a session started elsewhere, the agent types are not registered. The Director then runs each role as a general-purpose agent that reads its role file as its full instructions. Same rules, separate context.
- This project does not use any other folder in this repository.

## Standards

`standards/EVIDENCE.md` sets the evidence tags. `standards/OUTPUT.md` sets file layout. `standards/OPPORTUNITY.md` sets what an exceptional opportunity is: seven headings argued in plain sentences, a novelty search, an even-if-true test, and an exploration standard. No scores.
