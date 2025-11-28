# Week 6 — MLOps: Model Training & Serving (Summary)

## Completed
- Trained baseline and improved models (Iris dataset).
- Evaluated models (accuracy, precision, recall, F1).
- Logged metrics & artifacts to MLflow.
- Registered models in MLflow Model Registry (iris-classifier V1 baseline, V2 improved).
- Promoted V2 → Production and tested rollback.
- Built FastAPI inference service (`serve.py`) that loads `models:/iris-classifier/Production`.
- End-to-end prediction tested successfully.

## How to run (local)
1. Activate venv:
..venv\Scripts\Activate.ps1

2. Start MLflow UI (project root):
mlflow ui --port 5000

3. Start inference API (week6 folder):
cd week6-ml-pipeline
uvicorn serve:app --reload --port 9000

4. Test:
- GET `http://127.0.0.1:9000/` → health
- POST `http://127.0.0.1:9000/predict` with JSON:
  ```json
  {"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}
  ```

## Notes
- MLflow tracking URI used: `http://127.0.0.1:5000`
- Requirements updated to match model environment (`numpy==2.3.4`, `pyarrow==22.0.0`, `psutil==7.1.1`).
- Models saved locally under `week6-ml-pipeline/models/` and registered in MLflow.

## Next (Week-7 / Weekend)
- Build production-ready CI/CD for promotion.
- Containerize inference + MLflow (docker-compose).
- Add monitoring (Prometheus, Grafana) and drift detection.
