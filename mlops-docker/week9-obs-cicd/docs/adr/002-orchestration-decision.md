# ADR-002: Orchestration Decision (Prefect)

## Context

As the system evolves, certain workflows may need coordination beyond a single API call,
such as:

- scheduled retraining
- batch evaluation or backfills
- periodic data validation and drift checks

An orchestration tool may be required to manage retries, scheduling, and visibility.

## Decision

Prefect is selected as the preferred orchestration framework.

Prefect is chosen for:

- Python-first API and low cognitive overhead
- Easy local execution and cloud transition
- Clear task and flow abstractions suitable for ML workflows

Orchestration is **not implemented** in Week 9.

## Consequences

- Clear orchestration direction without premature implementation
- No operational overhead added to the current stack
- Future workflows can be introduced incrementally
- Scheduling and retries remain manual for now

This decision defers complexity while keeping the system extensible.
