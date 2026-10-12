# BevQuery

Plain-English analytics for beverage manufacturers. Ask a question about production, warehouse, and depot data; BevQuery writes safe, read-only SQL, runs it, and returns a table, a chart, and a short summary.

> Status: Sprint 1 (core engine) in progress. Sections marked TODO are filled in during later sprints.

## Links

| Item | Link |
|---|---|
| Live app | TODO (Sprint 3) |
| Scrum board (Trello) | TODO (add the shared board link) |
| Design and testing document | TODO: `DESIGN_AND_TESTING.md` (Sprint 3) |
| Sprint review recordings | TODO (one 3-minute recording per sprint) |
| Final video | TODO (Sprint 3) |

## What it does

- Takes a plain-English question from a plant user
- Builds a prompt from the customer's schema, concept map, and glossary
- Generates SQL with an LLM, then validates it (SELECT only, single statement, row limit)
- Runs it on a read-only database and shows the SQL, a results table, a chart, and an executive summary
- Supports several customers (tenants) with different schemas; each user only sees their own tenant

## Tech stack

Python, Flask, SQLite, LLM API (OpenAI or Anthropic), Chart.js, pytest, GitHub Actions, Render or Railway.

## Setup

```bash
git clone <your-repo-url>
cd bevquery
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then fill in your keys
```

Never commit `.env`. Only `.env.example` is tracked.

## Run the tests

```bash
pytest
```

## Project layout

```
app/        Flask app and core modules (prompt builder, LLM client, guardrails, executor, charts)
tenants/    One JSON config per customer (concept map and glossary)
seed/       Scripts that generate the sample tenant databases
tests/      pytest suite
data/       Generated databases (not committed)
```

## Sprint plan

| Sprint | Dates | Goal |
|---|---|---|
| 1 | 12 to 25 Oct 2026 | Core engine: command-line questions on two tenant databases |
| 2 | 26 Oct to 8 Nov 2026 | Web app, guardrails, retry loop, charts, summaries |
| 3 | 9 to 22 Nov 2026 | CI, deployment, documentation, final video |

## Author

TODO: name. Built as a solo capstone project (Product Owner, Scrum Master, and developer).
