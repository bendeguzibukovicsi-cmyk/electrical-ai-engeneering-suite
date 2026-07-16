# 2nd Round: Draft Issues and Work Items

Below are proposed draft issues for the "2nd round" of development. Copy each section into new GitHub issues and assign labels/milestones as appropriate.

1) Resolve Python dependency conflicts
- Priority: High
- Description: There are compatibility issues (notably pydantic/pydantic-core) that prevent runtime tests. Update requirements.txt to pin compatible versions, run the test matrix (Python 3.10/3.11/3.12), and verify Alembic and SQLAlchemy interactions.
- Acceptance criteria:
  - All unit tests pass locally and in CI
  - Requirements file updated and documented

2) Implement Firmware Agent (STM32/ESP32/Arduino)
- Priority: High
- Description: Implement an agent that can generate firmware skeletons, compile (toolchains or dockerized), and suggest peripheral initialization code. Add unit/integration tests and sample projects.
- Acceptance criteria:
  - Agent can scaffold a basic STM32 project and build inside a CI job

3) Implement PCB Agent (KiCad integration)
- Priority: High
- Description: Integrate KiCad for PCB layout automation and generate board files. Provide sanitized output and file export.
- Acceptance criteria:
  - Backend can invoke KiCad CLI or provide guidance for offline KiCad workflows

4) Implement Simulation Agent (LTspice)
- Priority: Medium
- Description: Add agent to run SPICE simulations, parse results, and produce plots/data for the frontend.
- Acceptance criteria:
  - Demo simulation runs with sample circuits

5) File Upload / Storage
- Priority: Medium
- Description: Implement secure file upload and storage (support local dev and S3), size limits, virus scanning optional.
- Acceptance criteria:
  - Upload endpoint with RBAC and storage backend configuration

6) WebSocket / Realtime
- Priority: Medium
- Description: Add realtime agent progress updates and logs via WebSocket or server-sent events.
- Acceptance criteria:
  - Frontend receives agent progress events and displays them

7) Frontend: Project Dashboard & Circuit Editor
- Priority: High
- Description: Build the core pages required for users to create projects, upload schematics, and view BOMs.
- Acceptance criteria:
  - Dashboard page showing projects
  - Circuit editor stub integrated with backend

8) Testing & CI Improvements
- Priority: Medium
- Description: Expand unit and integration tests and ensure GitHub Actions run them across PRs. Add e2e tests.
- Acceptance criteria:
  - CI passes for sample PRs; coverage thresholds documented

9) Security & Production Hardening
- Priority: High
- Description: Ensure JWT secrets, CORS settings, secure cookie handling, and rate limiting are in place. Add Sentry and monitoring.
- Acceptance criteria:
  - Security checklist completed and validated in staging

Estimated effort per issue should be assigned by maintainers. Consider creating smaller subtasks for large items (agents, frontend features).
