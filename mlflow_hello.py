import mlflow

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.1)
    mlflow.log_metric("accuracy", 0.95)

print("MLflow hello world completed.")
