# Week 7 Prefect flow outline
from prefect import flow, task
import pandas as pd
from sklearn.linear_model import LogisticRegression

@task
def load_data():
    # read csv
    df = pd.read_csv("week7-ml-pipeline/data/iris.csv")
    return df

@task
def validate_data(data):
    # check columns
    expected_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    if not all(col in data.columns for col in expected_cols):
        raise ValueError("Missing required columns in dataset")
    
    # check nulls
    if data.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains null values")
    return data

@task
def train_model(data):
    X = data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    y = data["species"]

    model = LogisticRegression(max_iter=200)
    model.fit(X,y)
    return model

@task
def evaluate_model(model,data):
    X = data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    y = data["species"]

    accuracy = model.score(X, y)
    return accuracy


@task
def register_model(model,metrics):
    pass

@flow
def ml_pipeline():
    d = load_data()
    v = validate_data(d)
    m = train_model(v)
    e = evaluate_model(m,v)
    register_model(m,e)

if __name__ == "__main__":
    ml_pipeline()