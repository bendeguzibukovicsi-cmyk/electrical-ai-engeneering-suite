# Infra

Infrastructure and deployment-related files: Docker Compose, Nginx reverse proxy, SSL folder, and production considerations.

Primary locations:
- docker-compose.yml — local multi-service orchestration (db, redis, backend, frontend, worker, nginx)
- nginx.conf — reverse-proxy configuration
- Dockerfiles (frontend/, backend/) — container build instructions

2nd-round priorities (infra)
1. Create a production-ready docker-compose or orchestration (Kubernetes / Docker Swarm) manifest — HIGH
2. Add secrets management (HashiCorp Vault / Docker secrets / GitHub Secrets) and avoid committing .env files with secrets — HIGH
3. Harden Nginx configuration (TLS, HSTS, security headers) and add automatic certificate provisioning (Let’s Encrypt) — MEDIUM
4. Add monitoring & logging stack (Prometheus, Grafana, Sentry integration) — MEDIUM
5. Update CI to build images and run tests in PRs; add image scanning for vulnerabilities — MEDIUM

Notes:
- Ensure compose healthchecks are robust and fail fast when dependencies are misconfigured.
- Consider splitting development and production compose files: docker-compose.dev.yml and docker-compose.prod.yml.
