# Senior MLOps Engineer Plan v2.1 FINAL
## 25-Year Veteran → Senior MLOps Engineer by Jan 1, 2026

**Version:** 2.1 FINAL (Incorporating Senior Readiness Requirements)  
**Start:** Tuesday, November 19, 2025  
**End:** December 31, 2025  
**Duration:** 6.5 weeks  
**Status:** FROZEN AND LOCKED

---

## CRITICAL: Senior Readiness Checklist

Before declaring "complete," you MUST have these 7 deliverables in your portfolio:

### The 7 Non-Negotiables for Senior Roles

| # | Deliverable | Week | Hours | Status |
|---|------------|------|-------|--------|
| 1 | **Model Training Evidence** (train+eval+retrain with metrics) | Week 6 | 3-4h | [ ] |
| 2 | **Prefect Flow Artifact** (DAG file + run logs) | Week 7 | 1-2h | [ ] |
| 3 | **MLflow Model Registry Demo** (register→promote→rollback) | Week 6 | 1-2h | [ ] |
| 4 | **Evidently→Prometheus Bridge** (drift metrics in Grafana) | Week 7 | 1-2h | [ ] |
| 5 | **Senior Readiness ADR** (cloud mapping, scale, trade-offs) | Week 9 | 2-3h | [ ] |
| 6 | **Demo Documentation** (bulletproof 5-min demo steps) | Week 9 | 0.5h | [ ] |
| 7 | **Demo GIF/Video** (30-60 sec quick preview) | Week 9 | 0.5-1h | [ ] |

**Total additional time: 10-15 hours (spread across 4 weeks)**

---

## Your Profile & Target

### Who You Are
- 48, Chennai, India
- 25 years IT, 8 years DevOps
- 32-day coding streak
- Target: Senior MLOps Engineer (₹25-55 LPA)

### Your Advantage
**Production expertise + leadership experience**
- 25 years running production systems
- Team leadership & incident management
- Know what breaks at scale

### The Gap
- 90% ready (technical + architecture + leadership)
- 10% missing: ML-specific tool depth at scale
- **This plan closes the gap for senior roles**

---

## The 70/20/10 Framework

### 70% - Technical Execution (Weeks 5.5-8)
Build 3 production MLOps projects

### 20% - Architecture & Design (Week 9)
Document decisions, trade-offs, senior thinking

### 10% - Leadership Positioning (Week 10)
Emphasize 25 years, position for senior roles

---

## Week 5.5: Foundation Setup
### November 18-24, 2025

**Daily: 2h (1h Agentic + 1h MLOps)**

Same as before:
- Install all tools (MLflow, Great Expectations, Evidently, Prefect)
- Run hello-world for each
- Verify Docker, docker-compose

**No changes to this week.**

---

## Week 6: ML Training Pipeline + Model Registry
### November 25 - December 1, 2025

**Daily: 2h (1h Agentic until Nov 30, then full 2h MLOps)**

**UPDATED: Now includes explicit senior deliverables**

### Monday Nov 25: Model Training Evidence (Senior Deliverable #1)
**Focus:** Train Model from Scratch with Full Evaluation

**Requirements (EXPLICIT):**
- Choose dataset (Iris, Wine, or Titanic)
- Implement proper train/test split (80/20)
- Train baseline model (Logistic Regression)
- Calculate metrics:
  - Accuracy, Precision, Recall, F1-score
  - Confusion matrix (save as PNG)
  - Classification report
- Train second model with different hyperparameters
- Compare results (baseline vs improved)
- **Save all artifacts:** model files, metrics JSON, plots

**Deliverable File Structure:**
```
week6-ml-pipeline/
├── data/
│   └── dataset.csv
├── models/
│   ├── baseline_model.pkl
│   └── improved_model.pkl
├── results/
│   ├── confusion_matrix_baseline.png
│   ├── confusion_matrix_improved.png
│   ├── metrics_baseline.json
│   └── metrics_improved.json
├── train.py
├── evaluate.py
└── README.md (with results comparison)
```

**README must show:**
- Training command
- Metrics comparison table
- Why improved model is better

**Commit:** "Model training evidence - baseline + improved with full metrics"

**Time:** 3-4 hours (This is the extra time from feedback)

---

### Tuesday Nov 26: Data Validation
Same as before - Great Expectations validation

**Commit:** "Data validation pipeline"

---

### Wednesday Nov 27: MLflow Model Registry Demo (Senior Deliverable #3)
**Focus:** Complete Model Registry Pattern

**Requirements (EXPLICIT):**
- Log both models (baseline + improved) to MLflow
- **Register both in MLflow Model Registry**
- Tag baseline as "Staging"
- Tag improved as "Production"
- Create script that loads "Production" model dynamically
- Test: Change production tag, script loads new model without code change

**Deliverable:**
```python
# load_production_model.py
import mlflow

def load_production_model():
    """Load current production model from registry"""
    client = mlflow.tracking.MlflowClient()
    model_name = "sentiment-classifier"
    
    # Get production version
    prod_version = client.get_latest_versions(
        model_name, 
        stages=["Production"]
    )[0]
    
    model = mlflow.pyfunc.load_model(
        f"models:/{model_name}/{prod_version.version}"
    )
    return model, prod_version.version

# Test it
model, version = load_production_model()
print(f"Loaded model version: {version}")
```

**Rollback Test:**
```python
# rollback.py
"""Demonstrate rollback capability"""
import mlflow

client = mlflow.tracking.MlflowClient()

# Get all versions
versions = client.search_model_versions(
    f"name='sentiment-classifier'"
)

# Promote previous version to Production
previous_version = versions[-2]  # Second to last
client.transition_model_version_stage(
    name="sentiment-classifier",
    version=previous_version.version,
    stage="Production"
)

print(f"Rolled back to version {previous_version.version}")
```

**README section:**
```markdown
## Model Registry Workflow

### Promotion
1. Train model → logs to MLflow
2. Register in Model Registry
3. Tag as "Staging" for testing
4. After validation, promote to "Production"

### Rollback
If production model has issues:
```bash
python rollback.py  # Promotes previous version
```

### Load Production Model
```bash
python load_production_model.py  # Always loads current Production
```
```

**Commit:** "MLflow Model Registry with promotion and rollback"

**Time:** 1-2 hours (This is the extra time from feedback)

---

### Thursday Nov 28: Inference API
Same as before - FastAPI loading from registry

**But now it uses the `load_production_model()` function**

**Commit:** "Inference API with dynamic model loading"

---

### Friday Nov 29: Model Promotion Workflow
Same as before - document promotion criteria

**Commit:** "Model promotion workflow documented"

---

### Saturday Nov 30: Documentation
**Agentic Capstone DONE ✅**

Polish Week 6 project README

**Commit:** "Week 6 complete - training + registry + API"

---

### Sunday Dec 1: Architecture Decision Record
Create `docs/adr/001-model-registry-choice.md`

**Commit:** "ADR for model registry decision"

---

**Week 6 Deliverables:**
✅ Model training evidence (baseline + improved)  
✅ MLflow Model Registry with rollback  
✅ Inference API loading from registry  
✅ ADR documenting decision

---

## Week 7: Orchestrated Containerized MLOps Stack
### December 2-8, 2025

**Daily: 2-3h (full focus)**

**UPDATED: Now includes explicit Prefect + Evidently deliverables**

### Monday Dec 2: Prefect Flow Artifact (Senior Deliverable #2)
**Focus:** Complete Workflow Orchestration

**Requirements (EXPLICIT):**
- Create Prefect flow file: `ml_pipeline_flow.py`
- Tasks:
  1. Load data
  2. Validate with Great Expectations
  3. Train model
  4. Evaluate metrics
  5. Register in MLflow if improved
- Run flow and capture logs
- Save flow run output

**Deliverable File:**
```python
# workflows/ml_pipeline_flow.py
from prefect import flow, task
import mlflow
from great_expectations.checkpoint import SimpleCheckpoint

@task
def load_data():
    """Load training data"""
    # Implementation
    return data

@task
def validate_data(data):
    """Validate with Great Expectations"""
    checkpoint = SimpleCheckpoint(...)
    results = checkpoint.run()
    
    if not results.success:
        raise ValueError("Data validation failed")
    
    return data

@task
def train_model(data):
    """Train model and log to MLflow"""
    with mlflow.start_run():
        model = train(data)
        mlflow.log_metrics({"accuracy": 0.95})
        mlflow.sklearn.log_model(model, "model")
    return model

@task
def evaluate_model(model, test_data):
    """Evaluate model"""
    metrics = evaluate(model, test_data)
    return metrics

@task
def register_model(model, metrics):
    """Register if improved"""
    if metrics['accuracy'] > 0.90:
        mlflow.register_model(
            f"runs:/{mlflow.active_run().info.run_id}/model",
            "sentiment-classifier"
        )

@flow(name="ml-training-pipeline")
def ml_pipeline():
    """End-to-end ML training pipeline"""
    data = load_data()
    validated_data = validate_data(data)
    model = train_model(validated_data)
    metrics = evaluate_model(model, test_data)
    register_model(model, metrics)

if __name__ == "__main__":
    ml_pipeline()
```

**Run and capture output:**
```bash
python workflows/ml_pipeline_flow.py > flow_run_log.txt
```

**README section:**
```markdown
## Workflow Orchestration

### Run Pipeline
```bash
python workflows/ml_pipeline_flow.py
```

### Flow Structure
```
load_data → validate_data → train_model → evaluate_model → register_model
```

### Successful Run Log
See `flow_run_log.txt` for example execution.
```

**Commit:** "Prefect workflow orchestration with DAG artifact"

**Time:** 1-2 hours (This is the extra time from feedback)

---

### Tuesday Dec 3: Containerize ML Service
Same as before - Dockerfile

**Commit:** "Containerized ML service"

---

### Wednesday Dec 4: Docker Compose Stack
Same as before - multi-container setup

**Commit:** "Multi-container setup"

---

### Thursday Dec 5: Prometheus
Same as before - add Prometheus

**Commit:** "Prometheus metrics collection"

---

### Friday Dec 6: Grafana
Same as before - add Grafana

**Commit:** "Grafana monitoring dashboards"

---

### Saturday Dec 7: Evidently→Prometheus Bridge (Senior Deliverable #4)
**Focus:** Complete Observability Loop

**Requirements (EXPLICIT):**
- Evidently generates drift reports
- Export drift metrics to Prometheus format
- Visualize in Grafana dashboard
- Set up alert for high drift

**Deliverable File:**
```python
# monitoring/drift_exporter.py
"""Export Evidently drift metrics to Prometheus"""
from prometheus_client import Gauge, start_http_server
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import time

# Define Prometheus metrics
drift_score = Gauge('model_drift_score', 'Overall data drift score')
feature_drift = Gauge('feature_drift_count', 'Number of features with drift')

def calculate_drift(reference_data, current_data):
    """Calculate drift using Evidently"""
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference_data, current_data=current_data)
    
    # Extract metrics
    result = report.as_dict()
    drift_share = result['metrics'][0]['result']['drift_share']
    n_drifted = result['metrics'][0]['result']['number_of_drifted_columns']
    
    return drift_share, n_drifted

def export_metrics():
    """Continuously export drift metrics"""
    start_http_server(8001)  # Prometheus scrapes this
    
    while True:
        # Get latest data
        reference = load_reference_data()
        current = load_current_predictions()
        
        # Calculate drift
        drift_share, n_drifted = calculate_drift(reference, current)
        
        # Export to Prometheus
        drift_score.set(drift_share)
        feature_drift.set(n_drifted)
        
        time.sleep(60)  # Update every minute

if __name__ == "__main__":
    export_metrics()
```

**Add to docker-compose.yml:**
```yaml
  drift-exporter:
    build: ./monitoring
    ports:
      - "8001:8001"
    depends_on:
      - ml-service
```

**Add to prometheus.yml:**
```yaml
scrape_configs:
  - job_name: 'drift-exporter'
    static_configs:
      - targets: ['drift-exporter:8001']
```

**Grafana Dashboard Panel:**
- Create panel: "Model Drift Score"
- Query: `model_drift_score`
- Add alert: `model_drift_score > 0.7`
- Take screenshot: `grafana_drift_dashboard.png`

**README section:**
```markdown
## Drift Monitoring

### How It Works
1. Evidently calculates drift every minute
2. Metrics exported to Prometheus
3. Visualized in Grafana dashboard
4. Alert triggers if drift > 0.7

### View Dashboard
Open Grafana at http://localhost:3000
Navigate to "MLOps Monitoring" dashboard

### Drift Metrics
- `model_drift_score`: Overall drift (0-1)
- `feature_drift_count`: Number of drifted features

![Drift Dashboard](docs/images/grafana_drift_dashboard.png)
```

**Commit:** "Evidently→Prometheus drift monitoring integrated"

**Time:** 1-2 hours (This is the extra time from feedback)

---

### Sunday Dec 8: Documentation & Demo
Same as before - polish and demo video

**Commit:** "Week 7 complete - orchestrated containerized stack"

---

**Week 7 Deliverables:**
✅ Prefect flow artifact with run logs  
✅ Evidently→Prometheus bridge working  
✅ Grafana dashboard showing drift  
✅ Complete containerized stack

---

## Week 8: Production Pipeline with CI/CD
### December 9-15, 2025

**Daily: 3-4h**

Same as before - no major changes to this week.

Focus on:
- End-to-end pipeline
- CI/CD with GitHub Actions
- Deployment to Railway/Render
- Full monitoring

**Week 8 Deliverable:** Production-grade ML pipeline

---

## Week 9: Architecture Documentation + Senior Readiness
### December 16-22, 2025

**Daily: 2-3h**

**UPDATED: Now includes Senior Readiness ADR**

### Monday Dec 16: Architecture Decision Records
Same as before - write ADRs for all decisions

**Commit:** "ADRs for all major decisions"

---

### Tuesday Dec 17: Senior Readiness ADR (Senior Deliverable #5)
**Focus:** Cloud Mapping, Scale, Trade-offs

**Requirements (EXPLICIT):**
Create `docs/adr/SENIOR_READINESS.md`

**Required Sections:**

#### 1. Cloud Mapping (AWS/GCP/Azure)
```markdown
## How This Stack Maps to Cloud

### Current (Local Development)
- Docker Compose → **Production: Kubernetes (EKS/GKE/AKS)**
- Local PostgreSQL → **Production: RDS/Cloud SQL**
- Local MLflow → **Production: MLflow on EC2/GCE or managed (Databricks)**
- Prefect local → **Production: Prefect Cloud or self-hosted on K8s**
- Prometheus/Grafana → **Production: Managed Prometheus + Grafana Cloud**

### Architecture Diagram
```
[Current: Docker Compose]
     ↓
[AWS Example]
EKS (K8s) → RDS PostgreSQL → S3 (artifacts) → CloudWatch (monitoring)

[GCP Example]
GKE (K8s) → Cloud SQL → GCS (artifacts) → Cloud Monitoring

[Azure Example]
AKS (K8s) → Azure Database → Blob Storage → Azure Monitor
```

### Migration Path
1. Phase 1: Lift docker-compose to single VM (Railway/Render)
2. Phase 2: Convert to K8s manifests, deploy to managed K8s
3. Phase 3: Add managed services (RDS, S3, etc.)
4. Phase 4: Multi-region, auto-scaling
```

#### 2. Rollout/Rollback Strategy
```markdown
## Deployment Strategies

### Current (Simple)
- Blue/Green: New container replaces old
- Rollback: `docker-compose down && git checkout previous && docker-compose up`

### Production (Graduated)

**Canary Deployment:**
- Deploy new model to 5% of traffic
- Monitor metrics for 1 hour
- If success: gradually increase to 100%
- If failure: instant rollback to 100% old version

**Blue/Green:**
- Blue: Current production (100% traffic)
- Green: New version (0% traffic)
- Test green, then switch traffic
- Keep blue for instant rollback

**Implementation:**
- K8s: Use Deployments with readiness probes
- Istio/LinkerD: Traffic splitting
- AWS: ECS with ALB target groups
- MLflow: Model Registry stages (Staging → Production)

**Rollback SLA:** <30 seconds to previous version
```

#### 3. Cost & Scaling Considerations
```markdown
## Cost Analysis

### Training Costs
- Current: Free (CPU local)
- Production scale:
  - Small models (<1GB): $10-50/month (spot instances)
  - Large models (>10GB): $500-2000/month (GPU instances)
  - Optimization: Use spot/preemptible, schedule off-peak

### Inference Costs
- Current: Free (local)
- Production scale:
  - 100 req/min: ~$50-100/month (2-3 CPU containers)
  - 1000 req/min: ~$500-800/month (10-15 containers + load balancer)
  - 10000 req/min: ~$3000-5000/month (K8s cluster + autoscaling)

### Storage Costs
- Models: $0.023/GB/month (S3 Standard)
- Logs: $0.03/GB/month (S3 IA after 30 days)
- Metrics: Included in monitoring service

### Optimization Strategies
1. Model compression (quantization, pruning)
2. Batch inference where possible
3. Caching frequent predictions
4. Spot instances for training
5. Serverless for low-volume endpoints

### When to Scale
- 100 req/min → Docker Compose OK
- 1000 req/min → Move to K8s
- 10000 req/min → Multi-region K8s + CDN
```

#### 4. Feature Store Trade-offs
```markdown
## Feature Store: Build vs Buy vs Skip

### When You DON'T Need Feature Store
- Team < 5 data scientists
- < 50 features
- Batch inference only
- Simple feature transformations

**Solution:** Versioned feature scripts + S3

### When You NEED Feature Store
- Team > 20 data scientists
- > 200 features
- Real-time inference (<100ms)
- Complex feature sharing across teams
- Training/serving skew problems

### Options

**1. Feast (Open Source)**
- Pros: Free, flexible, good for <50 data scientists
- Cons: Self-hosted, maintenance overhead
- Cost: Infrastructure only (~$200-500/month)

**2. Tecton (Managed)**
- Pros: Fully managed, enterprise features
- Cons: Expensive ($20k-100k/year)
- Best for: Large teams (>50 DS)

**3. Lightweight (DIY)**
- Versioned feature generation scripts
- Features stored in S3/GCS
- Feature metadata in PostgreSQL
- Good for: Small teams, batch inference

**My Recommendation (Based on 25 Years):**
- Start lightweight (scripts + S3)
- Add Feast when team hits 10-15 data scientists
- Consider Tecton only at enterprise scale (>50 DS)

**Anti-pattern I've seen:** Companies building custom feature stores. It becomes a 2-year project that delays actual ML work.
```

#### 5. Data Versioning Trade-offs
```markdown
## Data Versioning: DVC vs LakeFS vs Simple

### When You DON'T Need It
- Datasets < 10GB
- < 10 model versions to reproduce
- Short data retention needs

**Solution:** Timestamped data in S3 + metadata in MLflow

### When You NEED It
- Datasets > 100GB
- Need to reproduce models from 6+ months ago
- Regulatory compliance (audit trails)

### Options

**1. DVC (Data Version Control)**
- Pros: Git-like workflow, free
- Cons: Learning curve, requires discipline
- Best for: Teams comfortable with Git

**2. LakeFS**
- Pros: Git-like branches for data lakes
- Cons: Additional infrastructure
- Best for: Large data lakes (>1TB)

**3. Simple (Timestamped + Metadata)**
```python
# Store data with timestamp
s3://bucket/data/2024-11-15/dataset.csv

# Log in MLflow
mlflow.log_param("data_version", "2024-11-15")
mlflow.log_param("data_path", "s3://bucket/data/2024-11-15/")
```

**My Recommendation:**
- Start simple (timestamps + MLflow metadata)
- Add DVC when datasets > 50GB or team > 10
- Consider LakeFS only for data lake scenarios (>1TB)
```

**Commit:** "Senior Readiness ADR - cloud, scale, trade-offs"

**Time:** 2-3 hours (This is the extra time from feedback)

---

### Wednesday Dec 18: System Design Documentation
Same as before - create SYSTEM_DESIGN.md

**Commit:** "System design documentation"

---

### Thursday Dec 19: Trade-off Analysis
Same as before - create TRADEOFFS.md

**Commit:** "Trade-off analysis"

---

### Friday Dec 20: Technical Blog
Same as before - architecture-focused blog post

**Publish:** Medium/dev.to

---

### Saturday Dec 21: Demo Documentation (Senior Deliverable #6)
**Focus:** Bulletproof 5-Minute Demo

**Requirements (EXPLICIT):**
Create `docs/DEMO.md`

**Content:**
```markdown
# 5-Minute Live Demo Script

## Prerequisites
```bash
# Clone repo
git clone https://github.com/your-username/mlops-pipeline
cd mlops-pipeline

# Install dependencies (if not using Docker)
pip install -r requirements.txt
```

## Demo Flow (5 minutes)

### Part 1: One-Command Deployment (30 seconds)
```bash
# Start entire stack
docker-compose up -d

# Wait for services (10 seconds)
# All services ready
```

**What to say:** "This is a production MLOps stack. One command deploys 5 services: ML API, MLflow, Prometheus, Grafana, and drift monitoring."

### Part 2: Service Tour (2 minutes)

**FastAPI Service (30 sec)**
```bash
# Open browser
http://localhost:8000/docs

# Make prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This is amazing!"}'

# Response: {"prediction": "positive", "confidence": 0.95}
```

**What to say:** "API loads model from MLflow Registry. Production version served automatically. No hardcoded paths."

**MLflow Registry (30 sec)**
```bash
# Open browser
http://localhost:5000

# Show Models → sentiment-classifier
# Point out: Staging and Production versions
```

**What to say:** "Models registered here. Staging for testing, Production for serving. Rollback is changing this tag."

**Grafana Dashboard (30 sec)**
```bash
# Open browser
http://localhost:3000

# Navigate to MLOps Monitoring dashboard
# Point out panels: requests/sec, latency, drift score
```

**What to say:** "Complete observability. System metrics, model metrics, drift detection. Alert fires if drift > 0.7."

**Drift Detection (30 sec)**
```bash
# Trigger drift
python scripts/simulate_drift.py

# Watch Grafana drift panel increase
```

**What to say:** "Evidently detects distribution shift. Exports to Prometheus. Visible in Grafana. Auto-alert configured."

### Part 3: MLOps Workflow (1.5 minutes)

**Training Pipeline (30 sec)**
```bash
# Run Prefect flow
python workflows/ml_pipeline_flow.py

# Shows: data load → validate → train → register
```

**What to say:** "Prefect orchestrates training. Great Expectations validates data. If model improves, registers automatically."

**Model Promotion (30 sec)**
```bash
# In MLflow UI, promote model to Production
# Restart API or wait for hot-reload
# Make prediction - new model served
```

**What to say:** "No code deploy. Change registry tag, API loads new model. Blue/green deployment pattern."

**Rollback Test (30 sec)**
```bash
# Run rollback script
python scripts/rollback_model.py

# Shows: Previous version promoted to Production
# Make prediction - old model served
```

**What to say:** "Incident response: one command rolls back. <30 second recovery time."

### Part 4: Architecture (1 minute)

**Show diagram** (from README)

**What to say:** 
"Local: Docker Compose for speed.
Production: This maps to K8s on AWS/GCP.
Prefect → managed Prefect or K8s CronJob.
MLflow → EC2 or Databricks.
Monitoring → CloudWatch or Grafana Cloud.

Scaling: 100 req/min stays here. 1000+ req/min moves to K8s with autoscaling. I've documented the migration path and cost estimates."

## Troubleshooting

**Services don't start:**
```bash
docker-compose logs
# Check port conflicts (8000, 5000, 9090, 3000)
```

**Model not found:**
```bash
# Register initial model
python scripts/register_initial_model.py
```

**Drift not showing:**
```bash
# Ensure drift-exporter is running
docker-compose ps | grep drift-exporter
```

## Demo Checklist

Before demo:
- [ ] All services running: `docker-compose ps`
- [ ] Initial model registered in MLflow
- [ ] Grafana dashboard created
- [ ] Test all endpoints work
- [ ] Have terminal and browser ready
- [ ] Clear browser cache (fresh look)
```

**Commit:** "5-minute demo documentation"

**Time:** 0.5 hours (This is the extra time from feedback)

---

### Saturday Dec 21 (continued): Demo GIF/Video (Senior Deliverable #7)
**Focus:** Quick Visual Preview

**Requirements:**
- 30-60 second GIF or video
- Shows: docker-compose up → services running → prediction → dashboard
- Tool: Use ScreenToGif (Windows), Kap (Mac), or Peek (Linux)

**Deliverable:**
```
docs/images/demo.gif
```

**Add to main README:**
```markdown
## Quick Demo

![MLOps Pipeline Demo](docs/images/demo.gif)

**Full demo:** See [DEMO.md](docs/DEMO.md) for 5-minute walkthrough.
```

**Commit:** "Demo GIF added"

**Time:** 0.5-1 hour (This is the extra time from feedback)

---

### Sunday Dec 22: Final Review
Same as before - verify everything works

**Commit:** "Week 9 complete - senior-ready portfolio"

---

**Week 9 Deliverables:**
✅ All ADRs written  
✅ Senior Readiness ADR (cloud, scale, trade-offs)  
✅ Demo documentation (bulletproof 5-min script)  
✅ Demo GIF/video  
✅ Portfolio polished

---

## Week 10: Interview Prep & Applications
### December 23-29, 2025

Same as before - no changes.

**Week 10 Deliverable:** Interview-ready, applications sent

---

## The 7 Senior Deliverables - Final Checklist

Before applying to senior roles, verify you have ALL 7:

### ✅ Checklist

| # | Deliverable | Location | Verified |
|---|-------------|----------|----------|
| 1 | **Model Training Evidence** | `week6/results/` + README | [ ] |
| 2 | **Prefect Flow Artifact** | `workflows/ml_pipeline_flow.py` + logs | [ ] |
| 3 | **MLflow Model Registry Demo** | README section + scripts | [ ] |
| 4 | **Evidently→Prometheus Bridge** | `monitoring/drift_exporter.py` + Grafana screenshot | [ ] |
| 5 | **Senior Readiness ADR** | `docs/adr/SENIOR_READINESS.md` | [ ] |
| 6 | **Demo Documentation** | `docs/DEMO.md` | [ ] |
| 7 | **Demo GIF/Video** | `docs/images/demo.gif` | [ ] |

**When all checked: READY FOR SENIOR ROLES** ✅

---

## Time Investment Summary

### Original Plan
- Weeks 5.5-10: ~140 hours

### Additional Senior Items
- Model training evidence: 3-4h (Week 6)
- Prefect flow artifact: 1-2h (Week 7)
- MLflow registry demo: 1-2h (Week 6)
- Evidently→Prometheus: 1-2h (Week 7)
- Senior Readiness ADR