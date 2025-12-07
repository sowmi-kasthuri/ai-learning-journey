# Week-7 Architectural Trade-offs Document

## 1. Prefect on Host vs Prefect in Docker

### Prefect on Host
**Pros**
- Simple orchestration setup; no Docker-in-Docker.
- Full access to local filesystem and Docker daemon.
- Easy debugging through host logs.
- Trainer containers can be launched directly.

**Cons**
- Relies on Docker networking/compose network to reach MLflow.
- Slightly less portable than containerizing Prefect.

### Prefect Inside Docker (Alternative)
**Pros**
- Fully isolated environment.
- Networking is deterministic if everything is inside the same compose project.

**Cons**
- Requires Docker-in-Docker or socket mounting.
- More operational complexity.
- Harder to debug.

### Decision
Running **Prefect on the host** is the correct choice for this workflow.  
This keeps orchestration simple and avoids unnecessary Docker complexity.

---

## 2. Trainer Container: Stateless vs Stateful

### Stateless Trainer (Current Design)
**Pros**
- Clean start on every run; no leftover data.
- Fully reproducible training.
- Supports horizontal scaling.
- All outputs flow into MLflow, not inside the container.

**Cons**
- Hard dependency on MLflow availability.
- No caching inside the container.

### Stateful Trainer (Alternative)
**Pros**
- Could store datasets or checkpoints internally.

**Cons**
- Breaks reproducibility.
- Containers accumulate state and become inconsistent.
- Hard to scale or debug.

### Decision
A **stateless trainer** is the correct architecture for pipeline-driven ML systems.

---

## 3. MLflow as a Long-Running Service

### Why MLflow Must Be Persistent
**Pros**
- Central record of metrics, params, and artifacts.
- UI always available for inspection.
- Trainer containers stay simple.
- Supports history across many runs.

### Why Not Start MLflow Per Run
**Cons**
- Slow and unnecessary.
- No persistence; artifacts disappear on exit.
- Loses comparison across runs.

### Decision
MLflow stays in Docker Compose as a persistent service.

---

## 4. Volume Mounts: Why They Matter

### With Volumes
- MLflow artifacts and DB persist.
- Host can view artifacts in `./mlruns`.
- Runs survive container restarts.

### Without VolVolumes
- MLflow starts with a fresh DB on restart.
- All history disappears.
- Artifacts remain trapped inside the container.
- Local `./mlruns` stays unchanged.

### Decision
The volume mount  
`./mlruns:/mlflow`  
is **mandatory** for durability.

---

## 5. Failure Modes & Observed Behavior

### Failure Mode 1: MLflow Down
- Trainer throws connection errors.
- Prefect flow completes but logs nothing.
- No runs appear in UI.  
**Takeaway:** MLflow availability is required.

### Failure Mode 2: Port Mismatch
- Trainer cannot reach MLflow.
- MLflow runs fine, trainer logs fail.  
**Takeaway:** Ports must stay consistent.

### Failure Mode 3: Volume Removed
- Training runs but no artifacts appear in host.
- Restart wipes all run history.  
**Takeaway:** Persistence = volumes.

### Failure Mode 4: Docker Network Reset
- Trainer cannot resolve `mlflow`.
- Logging breaks even when MLflow is running.  
**Takeaway:** Trainer requires compose network stability.

---

## 6. Overall Architectural Trade-offs

### Simplicity vs Flexibility
Host-based Prefect + compose-based MLflow keeps the system simple while supporting clean orchestration.

### Stateless vs Stateful
Stateless trainers ensure repeatability and scalability.

### Durability vs Isolation
Host-mounted volumes give persistence but couple MLflow to filesystem layout.

### Compose Coupling
MLflow relies on compose to provide network + persistence.  
Trainer relies on compose network for service discovery (`mlflow:5000`).

### Final Position
The architecture balances simplicity, durability, and clarity:
- **Prefect on host**
- **MLflow in compose**
- **Trainer as stateless containers**
- **Compose network for service communication**
- **Volumes for persistence**

---

## Nano TLDR
- Prefect runs locally and uses Docker to launch stateless trainer jobs.  
- MLflow runs as a persistent compose service with durable storage.  
- Trainer logs to MLflow over the compose network (`mlflow:5000`).  
- Removing volumes or changing ports breaks persistence and connectivity.  
- Architecture is simple, reproducible, and aligned with real MLOps patterns.
