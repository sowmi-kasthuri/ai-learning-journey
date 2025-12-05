# Week 7 — Containerized ML Training Pipeline  
### MLflow Tracking + Docker Compose + Prefect Orchestration

This module delivers a production-style MLOps training workflow using:

- Docker & Docker Compose  
- MLflow Tracking Server  
- Prefect (running on host)  
- Python training job running inside a container  
- Persisted experiment tracking (SQLite + artifacts)

The design mirrors real-world MLOps setups such as AWS ECS + Prefect Cloud, or Kubernetes Jobs feeding into a centralized MLflow server.

---

## 🚀 High-Level Architecture

```
               ┌────────────────────────┐
               │      Prefect (Host)    │
               │   orchestrator.py       │
               │   docker run trainer    │
               └───────────┬────────────┘
                           │
                           ▼
         ┌──────────────────────────────────┐
         │         Trainer Container        │
         │ • Loads data                     │
         │ • Trains LogisticRegression      │
         │ • Logs metrics + params → MLflow │
         │ • Logs artifact model.pkl        │
         └───────────────────┬──────────────┘
                             │
                             ▼
         ┌──────────────────────────────────┐
         │    MLflow Tracking Server        │
         │ • Runs at http://localhost:5000  │
         │ • Stores mlflow.db               │
         │ • Stores artifact files          │
         │ • Backed by local ./mlruns/      │
         └──────────────────────────────────┘
```

---

## 📦 Directory Layout

```
week7-ml-pipeline/
│
├── README.md
├── orchestrator.py
├── docker-compose.yml
│
├── docker_context/
│   ├── Dockerfile
│   ├── train.py
│   ├── requirements.txt
│   └── data/iris.csv
│
├── mlflow_server/
│   └── Dockerfile
│
└── mlruns/         ← MLflow DB + artifacts (created on first run)
```

---

## 🔧 Components Explained

### **MLflow Server (Container)**
- Runs as a long-lived service  
- Tracking URI: `http://mlflow:5000`
- Backend store: `mlflow.db` (SQLite)
- Artifact store: `/mlflow`

### **Training Job (Container)**
- Stateless container  
- Loads iris dataset  
- Performs validation + training + evaluation  
- Logs:
  - Parameter (`model=LogisticRegression`)
  - Metric (`accuracy`)
  - Artifact (`model.pkl`)  
- Writes artifacts into MLflow’s mounted volume

### **Prefect Orchestrator (Host)**
- Executes `docker run week7-trainer`
- External orchestrator mimicking Prefect Cloud or Airflow
- Separates control plane (Prefect) from data plane (containers)

---

## 🏁 Running the System

### 1. Start MLflow + training ecosystem
```bash
docker compose up --build
```

Access MLflow UI:

```
http://localhost:5000
```

---

### 2. Trigger Training via Prefect
```bash
python orchestrator.py
```

This will:

1. Launch trainer container  
2. Train model  
3. Log metrics + artifacts  
4. Save everything under `mlruns/`  
5. Create a run visible in MLflow UI  

---

## 📈 Expected Output in MLflow

### Logged Parameters
- `model = LogisticRegression`

### Logged Metrics
- `accuracy = <value>`

### Artifacts
```
model.pkl
MLmodel
conda.yaml
requirements.txt
```

### UI
Click the run → artifacts → `model.pkl`

---

## 🗂 Production Parallels

| Local Component             | Real Production Equivalent               |
|----------------------------|-------------------------------------------|
| docker-compose             | Kubernetes / ECS task definition          |
| Prefect orchestrator       | Prefect Cloud / Airflow / Argo            |
| Trainer container          | Fargate Job / Cloud Run Job               |
| MLflow container           | MLflow on EKS/EC2 / Databricks Tracking   |
| mlruns (local)             | S3 / GCS / Azure Blob                     |

---

## 📚 Lessons Learned

- How to break an ML system into **microservices**
- How Docker Compose provides **networking + service discovery**
- How MLflow behaves with **containerized clients**
- How Prefect orchestrates external workloads
- Why trainer containers must remain **stateless**
- Tracking + versioning of models with MLflow

---

## ▶ Next Step — Week 8

- Add inference service (FastAPI + Docker)
- Serve model from MLflow registry
- Add Prometheus metrics + Grafana dashboards
- Add Evidently data drift monitors
- Add GitHub Actions CI/CD pipeline

---

# ✔ TLDR (Trainer-Ready)

- MLflow server container with persisted storage  
- Training container logs metrics & artifacts to MLflow  
- Prefect orchestrator triggers training via Docker  
- End-to-end flow works: training → logging → tracking  
- Architecture mirrors production (control plane + data plane)  

