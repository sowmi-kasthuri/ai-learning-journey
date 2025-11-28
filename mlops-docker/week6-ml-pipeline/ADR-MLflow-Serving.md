# ADR: Choice of MLflow for Model Tracking, Registry, and Serving

## Status
Accepted — Week 6 (Nov 2025)

## Context
The project requires:
- Tracking model experiments and metrics.
- Versioning multiple models (baseline, improved).
- A central Model Registry for promotion/rollback.
- A way to load the current Production model dynamically in the inference API.

Multiple options were considered:
- **MLflow**
- **SageMaker Model Registry**
- **KServe**
- **Custom file-based versioning**

## Decision
We chose **MLflow** because:
1. It provides experiment tracking, model registry, and serving in one tool.
2. It supports model versioning with simple API calls.
3. The FastAPI inference service can load the Production model using:
         mlflow.pyfunc.load_model("models:/iris-classifier/Production")
4. Easy local setup for Week-6 development.
5. Smooth transition to Docker + CI/CD in Week-7.

## Consequences
### Positive
- Simple promotion/rollback workflow.
- Central registry for all model versions.
- Reproducible training runs.
- Easy integration with containerized inference.

### Negative
- Local filesystem registry is deprecated; will migrate to SQLite or Docker-based MLflow in Week-7.
- Model environments need to be aligned (handled through updated requirements).

## Notes
This ADR covers only the model tracking and registry part.  
Serving and monitoring ADRs will be added in Week-7.
