# Frontend

Next.js 13+ application using the App Router and TypeScript. Tailwind CSS is configured.

Primary locations:
- frontend/app/layout.tsx — root layout
- frontend/app/page.tsx — home page
- frontend/app/components — reusable UI components
- frontend/tailwind.config.js — Tailwind configuration

2nd-round priorities (frontend)
1. Complete core pages: project dashboard, circuit editor, BOM viewer — HIGH
2. Implement authentication flows (login, register, token refresh) and connect to backend — HIGH
3. Integrate realtime UI (WebSocket updates for agent progress) — MEDIUM
4. Add file upload UI and download links (schematics, PDFs) — MEDIUM
5. Add E2E tests (Playwright) and component tests — MEDIUM

Notes:
- Use environment variables for API URL and feature flags.
- Follow existing TypeScript and linting rules (ESLint, Prettier, Airbnb style).
