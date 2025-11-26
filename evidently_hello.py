import pandas as pd
from sklearn.datasets import load_iris
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

data = load_iris(as_frame=True).frame

reference = data.sample(100, replace=True)
current = data.sample(100, replace=True)

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=reference, current_data=current)

report.save_html("evidently_report.html")
print("Evidently report generated.")
