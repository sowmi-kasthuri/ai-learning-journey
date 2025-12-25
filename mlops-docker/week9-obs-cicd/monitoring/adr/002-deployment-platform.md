# ADR 002: Deployment Platform

## Context

The system consists of multiple services:

- FastAPI backend
- Streamlit frontend
- MLflow tracking server

The deployment platform should allow fast iteration with minimal infrastructure overhead.

## Decision

Use Railway as the deployment platform.

Each service is deployed independently with environment-based configuration.

## Consequences

- Fast setup and low operational overhead
- Easy multi-service deployment
- Limited control over low-level infrastructure
- Acceptable trade-off for scope and learning goals
