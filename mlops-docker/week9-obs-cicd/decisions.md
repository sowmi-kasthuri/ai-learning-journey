# Week 8 – Architecture & Design Decisions

This document captures all key decisions made while building the Week-8 production LLM app.  
Each decision includes the reasoning, alternatives considered, and what would change in a production-grade system.

---

## 1. Choice of Frontend: Streamlit

**Decision:** Use Streamlit as the frontend for the LLM demo.

**Why**

- Fastest way to build a usable UI  
- No JavaScript or frontend build pipeline  
- Easy local testing + simple Railway deployment  
- Good enough for an internal QA/MLOps demo  

**Alternatives**

- React → slower to build, unnecessary complexity  
- Gradio → limited control over layout  
- Custom HTML → more work, no upside for Week-8

**What I’d change for production**

- Replace Streamlit with a lightweight React/Vue SPA  
- Add authentication + request quotas  
- Integrate proper analytics  

---

## 2. Backend Framework: FastAPI

**Decision:** Use FastAPI for the LLM backend service.

**Why**

- Simple, explicit request/response model  
- Async support for external LLM calls  
- Easy to containerize  
- Clear OpenAPI docs  

**Alternatives**

- Flask → synchronous, older pattern  
- Node/Express → not needed, slower for me personally  

**What I’d change for production**

- Add request validation layers  
- Add retries, circuit breaking, timeout logic  
- Replace in-memory stats with Redis  

---

## 3. Deployment Platform: Railway

**Decision:** Deploy all components on Railway.

**Why**

- Simple multi-service deployments  
- Containers supported out of the box  
- Clean environment variable management  
- Free tier sufficient for learning  

**Alternatives**

- Render → slower, occasional cold starts  
- AWS/GCP → overkill for Week-8  
- Docker Compose on cloud VM → too much ops overhead  

**What I’d change for production**

- Migrate to Kubernetes or ECS  
- Add horizontal scaling  
- Add monitoring (Grafana, Loki, Prometheus)  

---

## 4. Observability: MLflow + In-Memory Stats

**Decision:** Use MLflow for metrics + store live stats in memory.

**Why**

- MLflow already part of my pipeline (Week 6–7)  
- Easy metric logging from Python  
- In-memory stats sufficient for short-lived service  

**Alternatives**

- Prometheus + Grafana → too heavy for Week-8  
- Langsmith → paid  
- Custom DB metrics → unnecessary now  

**What I’d change for production**

- Move stats to Redis  
- Add Prometheus metrics endpoint  
- Add structured logging to ELK/Loki stack  

---

## 5. LLM Provider: Groq/OpenRouter

**Decision:** Use Groq/OpenRouter for inference.

**Why**

- Free or cheap usage  
- High performance  
- Supports multiple models  
- Simplifies token/cost tracking  

**Alternatives**

- OpenAI → paid  
- Anthropic → paid  
- Local models → too heavy for the Railway free tier  

**What I’d change for production**

- Formalize model versioning  
- Add fallback models  
- Track per-model cost + latency at scale  

---

## 6. Architecture Simplicity

**Decision:** Use a lightweight 3-service architecture:

- Streamlit → UI  
- FastAPI → logic  
- MLflow → observability  

**Why**

- Easiest path to a real deployed system  
- Clear separation of responsibilities  
- Minimizes moving parts  

**Alternatives**

- Monolithic service → harder to reason about  
- Over-engineered microservices → too complex for Week-8  

**What I’d change for production**

- Add API gateway  
- Authentication  
- Rate limiting  
- Cost-guard rails  

---

## 7. Token, Latency, Cost Tracking

**Decision:** Compute everything manually and log to MLflow.

**Why**

- Forces hands-on understanding of LLM finops  
- Transparent and inspectable  
- Good for interview demonstration  

**Alternatives**

- LangSmith autopilot → paid  
- OpenTelemetry instrumentation → overkill  

**What I’d change for production**

- Use OTel traces  
- Dashboards showing per-endpoint cost  
- Error class analytics  

---

# Summary

Week-8 decisions prioritized:

- **simplicity**
- **speed of execution**
- **production realism**
- **observable LLM behavior**

Perfect foundation for Week-9 (Quality + CI/CD).
