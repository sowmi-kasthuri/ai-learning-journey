import pandas as pd
from sklearn.linear_model import LogisticRegression
import mlflow
import mlflow.sklearn
import pickle

def load_data():
    df = pd.read_csv("data/iris.csv")
    return df

def validate_data(df):
    if df.isnull().any().any():
        raise ValueError("Data contains null values")
    return df

def train_model(df):
    X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    y = df["species"]

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model

def evaluate_model(model, df):
    X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    y = df["species"]
    accuracy = model.score(X, y)
    return accuracy

def log_results(model, accuracy):
    import pickle
    mlflow.set_tracking_uri("http://mlflow:5000")
    with mlflow.start_run():
        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_metric("accuracy", accuracy)
        with open("model.pkl", "wb") as f:
            pickle.dump(model, f)
        mlflow.log_artifact("model.pkl")


if __name__ == "__main__":
    df = load_data()
    df = validate_data(df)
    model = train_model(df)
    accuracy = evaluate_model(model, df)
    log_results(model, accuracy)

