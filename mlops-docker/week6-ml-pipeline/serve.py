from fastapi import FastAPI
import mlflow.pyfunc
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")

app = FastAPI()

# Load the current Production model from MLflow Registry
model = mlflow.pyfunc.load_model("models:/iris-classifier/Production")

@app.get("/")
def home():
    return {"status": "ok", "model_version": "Production"}

@app.post("/predict")
def predict(features: dict):
    # Expecting: {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
    X = [[
        features["sepal_length"],
        features["sepal_width"],
        features["petal_length"],
        features["petal_width"]
    ]]

    prediction = model.predict(X)
    return {"prediction": int(prediction[0])}
