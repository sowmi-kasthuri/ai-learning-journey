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
