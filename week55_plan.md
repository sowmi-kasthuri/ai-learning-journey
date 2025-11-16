# Week 5.5: MLOps Setup Week
## November 18-23, 2025

**Goal:** Get all MLOps tools installed and working.

**Daily commitment:** 2 hours
- 1 hour: Agentic capstone (continues until Nov 30)
- 1 hour: MLOps tool setup

---

## Tuesday Nov 18 (After Interview)

### Hour 1: Agentic capstone work

### Hour 2: Environment Setup

**Step 1: Create folder**

```bash
cd ~/ai-learning-journey
mkdir week5.5-setup
cd week5.5-setup
```

**Step 2: Install tools**

```bash
pip install mlflow great-expectations evidently prefect prometheus-client
```

**Step 3: Verify installations**

```bash
python -c "import mlflow; print('MLflow:', mlflow.__version__)"
python -c "import great_expectations; print('Great Expectations: OK')"
python -c "import evidently; print('Evidently: OK')"
python -c "import prefect; print('Prefect: OK')"
```

**Step 4: Test Docker**

```bash
docker --version
docker run hello-world
```

**Step 5: Create README**

```bash
echo "# Week 5.5 Setup - All tools installed" > README.md
echo "" >> README.md
echo "- MLflow ✅" >> README.md
echo "- Great Expectations ✅" >> README.md
echo "- Evidently ✅" >> README.md
echo "- Prefect ✅" >> README.md
echo "- Docker ✅" >> README.md
```

**Step 6: Commit**

```bash
git add .
git commit -m "Week 5.5 Day 1: MLOps tools installed"
git push
```

**✅ Done for Tuesday Nov 18**

---

## Wednesday Nov 19

### Hour 1: Agentic capstone work

### Hour 2: Great Expectations Hello World

**Step 1: Create demo folder**

```bash
cd ~/ai-learning-journey/week5.5-setup
mkdir ge-demo
cd ge-demo
```

**Step 2: Initialize Great Expectations**

```bash
great_expectations init
```

**Step 3: Create sample CSV**

```bash
echo "name,age,city" > data.csv
echo "Alice,30,Chennai" >> data.csv
echo "Bob,25,Mumbai" >> data.csv
echo "Charlie,35,Delhi" >> data.csv
```

**Step 4: Create expectation suite**

```bash
great_expectations suite new
```

- Choose option 1 (manual)
- Name it: `basic_suite`

**Step 5: Run validation**

```bash
great_expectations checkpoint new my_checkpoint
```

- Select your suite
- Select your data file

**Step 6: Check HTML report created** ✅

**Step 7: Update README**

```bash
cd ~/ai-learning-journey/week5.5-setup
echo "" >> README.md
echo "## Wednesday Nov 19: Great Expectations" >> README.md
echo "- Created expectation suite ✅" >> README.md
echo "- Ran validation ✅" >> README.md
```

**Step 8: Commit**

```bash
git add .
git commit -m "Week 5.5 Day 2: Great Expectations hello world"
git push
```

**✅ Done for Wednesday Nov 19**

---

## Thursday Nov 20

### Hour 1: Agentic capstone work

### Hour 2: MLflow Hello World

**Step 1: Create demo folder**

```bash
cd ~/ai-learning-journey/week5.5-setup
mkdir mlflow-demo
cd mlflow-demo
```

**Step 2: Start MLflow UI** (keep running in terminal)

```bash
mlflow ui
```

**Step 3: Open browser**

http://localhost:5000

**Step 4: Create test script** (`test_mlflow.py`)

```python
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
import numpy as np

# Start MLflow run
with mlflow.start_run():
    # Log parameters
    mlflow.log_param("model_type", "linear_regression")
    mlflow.log_param("test", "hello_world")
    
    # Simple model
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Log metrics
    score = model.score(X, y)
    mlflow.log_metric("r2_score", score)
    
    # Log model
    mlflow.sklearn.log_model(model, "model")
    
    print(f"✅ MLflow run complete. Score: {score}")
    print("Check MLflow UI at http://localhost:5000")
```

**Step 5: Run script**

```bash
python test_mlflow.py
```

**Step 6: Check MLflow UI** - see your run? ✅

**Step 7: Update README**

```bash
cd ~/ai-learning-journey/week5.5-setup
echo "" >> README.md
echo "## Thursday Nov 20: MLflow" >> README.md
echo "- Logged experiment ✅" >> README.md
echo "- Tracked metrics ✅" >> README.md
```

**Step 8: Commit**

```bash
git add .
git commit -m "Week 5.5 Day 3: MLflow hello world"
git push
```

**✅ Done for Thursday Nov 20**

---

## Friday Nov 21

### Hour 1: Agentic capstone work

### Hour 2: Evidently Hello World

**Step 1: Create demo folder**

```bash
cd ~/ai-learning-journey/week5.5-setup
mkdir evidently-demo
cd evidently-demo
```

**Step 2: Create test script** (`test_evidently.py`)

```python
import pandas as pd
import numpy as np
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Reference data (baseline)
np.random.seed(42)
reference = pd.DataFrame({
    'feature1': np.random.normal(0, 1, 1000),
    'feature2': np.random.normal(5, 2, 1000),
    'target': np.random.randint(0, 2, 1000)
})

# Current data (with drift)
current = pd.DataFrame({
    'feature1': np.random.normal(0.5, 1, 1000),  # Mean shifted
    'feature2': np.random.normal(5, 2, 1000),
    'target': np.random.randint(0, 2, 1000)
})

# Generate drift report
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=reference, current_data=current)
report.save_html('drift_report.html')

print("✅ Drift report generated")
print("Open drift_report.html in browser")
```

**Step 3: Run script**

```bash
python test_evidently.py
```

**Step 4: Open `drift_report.html`** - see drift detected? ✅

**Step 5: Update README**

```bash
cd ~/ai-learning-journey/week5.5-setup
echo "" >> README.md
echo "## Friday Nov 21: Evidently" >> README.md
echo "- Generated drift report ✅" >> README.md
```

**Step 6: Commit**

```bash
git add .
git commit -m "Week 5.5 Day 4: Evidently hello world"
git push
```

**✅ Done for Friday Nov 21**

---

## Saturday Nov 22

### Hour 1: Agentic capstone work

### Hour 2: Docker Basics

**Step 1: Create demo folder**

```bash
cd ~/ai-learning-journey/week5.5-setup
mkdir docker-demo
cd docker-demo
```

**Step 2: Create FastAPI app** (`app.py`)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Docker!", "status": "working"}

@app.get("/health")
def health():
    return {"status": "healthy"}
```

**Step 3: Create `requirements.txt`**

```txt
fastapi
uvicorn
```

**Step 4: Create `Dockerfile`**

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Step 5: Build and run**

```bash
docker build -t fastapi-demo .
docker run -p 8000:8000 fastapi-demo
```

**Step 6: Test**

Open http://localhost:8000 - see the message? ✅

**Step 7: Stop container**

Press Ctrl+C

**Step 8: Update README**

```bash
cd ~/ai-learning-journey/week5.5-setup
echo "" >> README.md
echo "## Saturday Nov 22: Docker" >> README.md
echo "- Built Docker image ✅" >> README.md
echo "- Ran container ✅" >> README.md
```

**Step 9: Commit**

```bash
git add .
git commit -m "Week 5.5 Day 5: Docker hello world"
git push
```

**✅ Done for Saturday Nov 22**

---

## Sunday Nov 23

### Hour 1: Agentic capstone work

### Hour 2: Docker Compose

**Step 1: Create demo folder**

```bash
cd ~/ai-learning-journey/week5.5-setup
mkdir docker-compose-demo
cd docker-compose-demo
```

**Step 2: Copy files from Saturday**

Copy these from `docker-demo/`:
- `app.py`
- `requirements.txt`
- `Dockerfile`

**Step 3: Create `docker-compose.yml`**

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - MLFLOW_TRACKING_URI=http://mlflow:5000

  mlflow:
    image: ghcr.io/mlflow/mlflow:latest
    ports:
      - "5000:5000"
    command: mlflow server --host 0.0.0.0 --port 5000
```

**Step 4: Run both services**

```bash
docker-compose up
```

**Step 5: Test both services**

- FastAPI: http://localhost:8000
- MLflow: http://localhost:5000

Both working? ✅

**Step 6: Stop services**

Press Ctrl+C, then:

```bash
docker-compose down
```

**Step 7: Update README**

```bash
cd ~/ai-learning-journey/week5.5-setup
echo "" >> README.md
echo "## Sunday Nov 23: Docker Compose" >> README.md
echo "- Multi-container setup ✅" >> README.md
echo "- Services communicating ✅" >> README.md
```

**Step 8: Commit**

```bash
git add .
git commit -m "Week 5.5 Day 6: Docker Compose hello world"
git push
```

**✅ Done for Sunday Nov 23**

---

## Week 5.5 Summary

**Create this on Sunday Nov 23 evening:**

```bash
cd ~/ai-learning-journey/week5.5-setup
code WEEK_SUMMARY.md
```

**Content:**

```markdown
# Week 5.5 Summary (Nov 18-23, 2025)

## What I Learned
- Great Expectations: Data validation
- MLflow: Experiment tracking
- Evidently: Drift detection
- Docker: Containerization
- Docker Compose: Multi-container apps

## What I Built
- GE validation suite
- MLflow experiment
- Evidently drift report
- Dockerized FastAPI app
- Multi-container stack

## Tools Verified
- MLflow ✅
- Great Expectations ✅
- Evidently ✅
- Prefect ✅
- Docker ✅
- Docker Compose ✅

## Status
- Tools installed: ✅
- Basics understood: ✅
- Ready for Week 6: ✅

## Stats
- Days: 6
- Commits: 6
- New streak total: 38 days

## Next Week
**Week 6: ML Training Pipeline + Model Registry**
Starts: Monday, November 24, 2025
```

**Commit:**

```bash
git add WEEK_SUMMARY.md
git commit -m "Week 5.5 complete - all tools ready"
git push
```

---

## Week 5.5 Complete Checklist

By Sunday Nov 23 evening, you should have:

- [ ] MLflow installed and tested
- [ ] Great Expectations installed and tested
- [ ] Evidently installed and tested
- [ ] Prefect installed
- [ ] Docker working (hello-world test passed)
- [ ] Docker Compose working (multi-container test passed)
- [ ] 6 commits (one per day)
- [ ] Agentic capstone progressing (1h/day)
- [ ] Week summary written

**If all checked: Ready for Week 6** ✅

---

## Troubleshooting

### If Docker doesn't work:
- Make sure Docker Desktop is running
- Check: `docker --version` shows version number
- Restart Docker Desktop if needed

### If pip install fails:
- Try: `pip install --upgrade pip` first
- Then retry the installations

### If Great Expectations init fails:
- Make sure you're in an empty folder
- Try: `great_expectations --version` to verify installation

### If MLflow UI doesn't open:
- Check port 5000 is not in use
- Try: `mlflow ui --port 5001` (use different port)

### If ports conflict in docker-compose:
- Change ports in `docker-compose.yml`
- Example: `"8001:8000"` instead of `"8000:8000"`

---

## Daily Routine Template

**Each day this week:**

1. Open terminal
2. Navigate to `~/ai-learning-journey/week5.5-setup`
3. Follow the day's instructions
4. Test that it works
5. Update README
6. Commit and push
7. Check GitHub - green square appears ✅

**Time per day:** 2 hours (1h Agentic + 1h MLOps)

---

## After Week 5.5

**Monday Nov 24:** Week 6 begins - ML Training Pipeline + Model Registry

You'll use all these tools together to build a real ML system.

---

## Notes

- **Don't skip days** - tools build on each other
- **Commit daily** - keeps your streak alive
- **Test everything** - make sure it actually works
- **Ask if stuck** - don't waste time struggling alone

---

**Week 5.5 Plan: Nov 18-23, 2025**  
**Status: Ready to Execute**  
**Start: Tuesday Nov 18 (after interview Monday Nov 17)**

🚀