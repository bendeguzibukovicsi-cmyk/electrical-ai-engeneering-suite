# Backend

This directory contains the FastAPI backend for the Electrical AI Engineering Suite. It implements API endpoints, AI agent integration hooks, database models and migrations, background workers (Celery), and core utilities.

Primary locations:
- backend/app/main.py — FastAPI entrypoint
- backend/app/api/v1 — versioned API routers and endpoints
- backend/app/agents — AI agents (electrical_engineering.py present as example)
- backend/app/core — configuration, security, MCP client
- backend/app/db — SQLAlchemy models, session, repositories, Alembic
- backend/tests — pytest test suite

2nd-round priorities (backend)
1. Resolve Python dependency conflicts (pydantic/pydantic-core mismatches) — HIGH
   - Pin compatible versions, run full test suite, and update requirements.txt
2. Implement remaining AI agents (Firmware, PCB, Simulation, Datasheet, BOM, Docs) — HIGH
   - Define agent interfaces, add unit tests and integration tests
3. Add WebSocket support in backend for real-time agent interactions — MEDIUM
   - Decide on protocol (WebSocket / Socket.IO / WebHooks) and implement
4. Implement file upload/download and storage hardening (schematics, BOM, datasheets) — MEDIUM
   - Support S3-compatible backends and local storage in dev
5. Improve test coverage and CI pipelines (unit, integration, e2e) — MEDIUM

Notes:
- Keep configuration in environment variables; don't commit secrets.
- Before merging to main, ensure migrations are deterministic and CI runs migrations in a disposable DB.