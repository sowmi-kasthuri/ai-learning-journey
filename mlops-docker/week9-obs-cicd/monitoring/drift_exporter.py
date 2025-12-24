from prometheus_client import Gauge, start_http_server
import pandas  as pd
import time

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

REFERENCE_PATH = "data/reference.csv"
CURRENT_PATH = "data/current.csv"

model_drift_score = Gauge(
    "model_drift_score",
    "Overall data drift score computed by Evidently"
)

def load_data():
    reference = pd.read_csv(REFERENCE_PATH)
    current = pd.read_csv(CURRENT_PATH)
    return reference, current

def compute_drift(reference, current):
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference, current_data=current)

    result = report.as_dict()
    drift_score = result["metrics"][0]["result"]["dataset_drift"]
    
    return float(drift_score)


def update_metric():
    reference, current = load_data()
    drift_score = compute_drift(reference, current)
    model_drift_score.set(drift_score)

if __name__ == "__main__":
    start_http_server(8001)

    while True:
        update_metric()
        time.sleep(30)