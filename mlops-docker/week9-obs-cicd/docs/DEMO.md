# Demo – Production LLM System (MLOps Focus)

## 1. What problem does this solve?

This project demonstrates how to take an LLM-powered API from a simple prototype
to a **production-aware system** with observability, cost tracking, drift awareness,
and CI/CD intent.

The focus is on **operational readiness**, not model training.

---

## 2. Architecture (high level)

- FastAPI backend serving `/generate`
- External LLM provider (Groq / OpenRouter)
- MLflow for experiment and cost tracking
- Prometheus + Grafana for metrics
- Evidently for data drift computation
- Docker-based local stack; Railway-ready deployment

Each service is independently deployable.

---

## 3. Live Flow (5-minute walkthrough)

1. Send a request to `/generate`
2. Observe latency, tokens, and cost logged in MLflow
3. View request metrics via Prometheus
4. Inspect Grafana dashboards for system behavior
5. Review drift metric (`model_drift_score`) exposed via exporter

---

## 4. Observability Highlights

- Request count, latency, and cost treated as first-class metrics
- MLflow provides a full audit trail per request
- Prometheus/Grafana provide system-level visibility
- Drift monitoring implemented with a clear metric contract

Known limitation:

- Local alerting and rate queries are constrained by scrape/window timing
- Documented and acceptable for scope

---

## 5. CI/CD Intent

- GitHub Actions pipeline builds Docker image on push to main
- Deployment intentionally documented but not automated
- Design favors clarity and control over premature automation

---

## 6. Key Trade-offs

- Simplicity over scale
- Clear decisions over tool sprawl
- Documentation over overengineering
- Managerial clarity over IC-level depth

---

## 7. What this demonstrates

- Production thinking for LLM systems
- Practical MLOps observability
- Cost and drift awareness
- Senior-level decision making and trade-offs

 A short demo GIF will be added to visually walk through the system flow.
