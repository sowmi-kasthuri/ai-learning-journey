# Senior Readiness – Production Thinking

This document captures how the Week 8–9 system would evolve in a real
production environment and the trade-offs involved.

---

## 1. Cloud Mapping (Local → Production)

### Compute

- Local: Docker Compose
- Production: Managed containers (ECS, GKE, AKS)

Each service (API, frontend, MLflow, monitoring) maps cleanly to its own
container with independent scaling characteristics.

### Observability

- Local: Prometheus + Grafana
- Production: Managed Prometheus / Grafana or cloud-native monitoring

Metrics contracts remain unchanged; only the hosting layer differs.

### Experiment Tracking

- Local: MLflow container
- Production: Managed MLflow or hosted tracking server with object storage

---

## 2. Rollout and Rollback Strategy

### Deployment

- Blue/green or rolling deployments at the container level
- No in-place mutations of running services

### Rollback

- Revert to previous container image
- MLflow experiments remain immutable and auditable
- No schema migrations in Week 9 scope

---

## 3. Cost and Scaling Considerations

### Cost Drivers

- LLM inference cost (primary)
- Request volume
- Monitoring overhead (minimal)

### Scaling

- Horizontal scaling of FastAPI service
- External LLM provider absorbs model-scale complexity
- No autoscaling configured in Week 9 (intentional)

---

## 4. Feature Store Trade-offs

### Current State

- No feature store
- Prompt-based inference only

### Production Option

- Introduce feature store only if:
  - repeated feature reuse exists
  - offline/online consistency is required

Feature stores are intentionally excluded to avoid premature complexity.

---

## 5. Data Versioning Trade-offs

### Current State

- Reference and current datasets versioned manually
- Drift detection focused on correctness, not automation

### Production Option

- Dataset versioning via object storage + metadata
- Tight integration with MLflow runs

This was deferred to keep Week 9 focused on observability fundamentals.
