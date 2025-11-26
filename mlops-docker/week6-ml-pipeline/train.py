import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib
import mlflow
import mlflow.sklearn

MODEL_NAME = "iris-classifier"

mlflow.set_tracking_uri("http://127.0.0.1:5000")

def load_data():
    df = pd.read_csv("data/iris.csv")
    return df

def train_baseline(df):
    with mlflow.start_run(run_name="baseline"):
        X = df[["sepal_length","sepal_width","petal_length","petal_width"]]
        y = LabelEncoder().fit_transform(df["species"])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)

        from sklearn.metrics import accuracy_score
        preds = model.predict(X_test)
        mlflow.log_metric("accuracy", accuracy_score(y_test, preds))
        mlflow.sklearn.log_model(model, "model")

        mlflow.register_model(
            model_uri=f"runs:/{mlflow.active_run().info.run_id}/model",
            name=MODEL_NAME
        )

        joblib.dump(model, "models/baseline_model.pkl")
        print("Baseline model saved.")
        return model


def train_improved(df):
    with mlflow.start_run(run_name="improved"):
        X = df[["sepal_length","sepal_width","petal_length","petal_width"]]
        y = LabelEncoder().fit_transform(df["species"])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LogisticRegression(max_iter=500, C=0.5)
        model.fit(X_train, y_train)
        
        from sklearn.metrics import accuracy_score
        preds = model.predict(X_test)
        mlflow.log_metric("accuracy", accuracy_score(y_test, preds))

        mlflow.sklearn.log_model(model, "model")

        mlflow.register_model(
            model_uri=f"runs:/{mlflow.active_run().info.run_id}/model",
            name=MODEL_NAME
        )

        joblib.dump(model, "models/improved_model.pkl")
        print("Improved model saved.")
        return model

if __name__ == "__main__":
    df = load_data()
    train_baseline(df)
    train_improved(df)
