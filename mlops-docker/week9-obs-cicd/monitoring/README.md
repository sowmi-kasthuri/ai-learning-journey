# Drift Metrics Contract

## Primary Metric

- Name: model_drift_score
- Type: Gauge
- Range: 0.0 – 1.0
- Source: Evidently
- Meaning: Overall data drift between reference and current window

## Alert Threshold

- Warning: > 0.7
- Action: Investigate data distribution shift

## Notes

- Single metric for Week 9
- No per-feature metrics
- No labels initially

## Alerting Limitation (Local Stack)

### Issue

Grafana alert rule creation is blocked in the local Docker setup due to an
alerting engine limitation:

- Hidden/orphan expression references created internally by Grafana
- No UI support to remove or convert expressions
- Alert rule save fails with evaluator error:
  `invalid command type in expression 'B'`

### Decision

Alerting is intentionally stopped at **metric + visualization** for this
training stack.

### Production Note

In a production environment, drift alerting would be implemented via:

- Prometheus Alertmanager rules on `model_drift_score`, or
- Grafana upgraded to a unified alerting–compatible version

This limitation does not affect drift detection correctness or observability.
