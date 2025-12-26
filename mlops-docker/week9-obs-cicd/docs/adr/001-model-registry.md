# ADR-001: Model Registry Choice (MLflow)

## Context

The system requires a way to track model-related artifacts and metrics over time,
including:

- parameters and configuration
- performance metrics (latency, cost, tokens)
- generated outputs for auditability

The solution should be lightweight, developer-friendly, and suitable for both
local development and small production deployments.

## Decision

Use MLflow as the model registry and experiment tracking system.

MLflow is used to:

- log parameters and metrics per request
- store response artifacts (e.g., generated text)
- provide a historical view of model behavior and cost

Model registration and stage promotion are not automated in Week 9.

## Consequences

- Clear experiment traceability and audit trail
- Minimal operational overhead
- No built-in approval workflows or gated promotions
- Model governance is documented but not enforced by tooling

This trade-off is intentional to prioritize observability and learning over
process complexity.
