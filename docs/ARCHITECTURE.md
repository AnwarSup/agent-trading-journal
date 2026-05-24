# Agentic Trading Journal Architecture

## Purpose

Post-trade review engine that turns fills, thesis notes, and market context into measurable behavior loops.

## Runtime loop

1. **Observe** — collect domain signals: risk_reward, max_adverse_excursion, plan_deviation, holding_time_hours, emotion_tag_risk.
2. **Orient** — map the active scenario to specialist agent responsibilities.
3. **Decide** — score severity, confidence, and operator urgency.
4. **Act** — emit next actions that a human operator can verify.
5. **Reflect** — attach trace IDs and deterministic evidence for review.

## Components

- `backend/swarm.py` — pure Python reasoning core, safe for CI and static demos.
- `backend/app.py` — FastAPI wrapper for product integration.
- `cli.py` — terminal demo path for reviewers.
- `index.html` — front-facing dashboard surface.

## Agent responsibilities

- `Trade Ingest Agent`: owns one part of the analysis loop.
- `Thesis Consistency Checker`: owns one part of the analysis loop.
- `Risk Discipline Auditor`: owns one part of the analysis loop.
- `Pattern Miner`: owns one part of the analysis loop.
- `Coaching Plan Generator`: owns one part of the analysis loop.

## Production extension points

- Replace deterministic signals with live connectors.
- Persist reports in Postgres or SQLite.
- Add auth and organization workspaces.
- Add export hooks for Slack, Discord, Telegram, or email.
