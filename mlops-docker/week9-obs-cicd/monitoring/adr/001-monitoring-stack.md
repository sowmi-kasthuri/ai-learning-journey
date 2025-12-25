# ADR 001: Monitoring Stack

## Context

The LLM service requires basic production-grade observability to track:

- request volume
- latency and cost (LLM-specific)
- data drift over time

The solution must be lightweight, local-first, and suitable for a learning MLOps stack.

## Decision

Use:

- Prometheus for metrics scraping
- Grafana for visualization
- Evidently for data drift computation

Metrics are exposed via `/metrics` and scraped by Prometheus.
Drift is computed in a separate exporter service and exposed as a Prometheus gauge.

## Consequences

- Simple and explainable observability stack
- Easy to run locally via Docker Compose
- Limited alerting in local Grafana setup (documented)
- Production alerting would move to Alertmanager or managed Grafana
