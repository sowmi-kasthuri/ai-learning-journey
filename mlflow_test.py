import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

mlflow.set_tracking_uri("file:/app/mlruns")

if __name__ == "__main__":
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    with mlflow.start_run():
        mlflow.log_param("n_estimators", 10)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")

    print("Logged run with accuracy:", acc)
