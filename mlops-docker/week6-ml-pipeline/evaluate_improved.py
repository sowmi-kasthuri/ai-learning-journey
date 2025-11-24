import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load_data():
    df = pd.read_csv("data/iris.csv")
    X = df[["sepal_length","sepal_width","petal_length","petal_width"]]
    y = LabelEncoder().fit_transform(df["species"])
    return X, y

def evaluate_model():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = joblib.load("models/improved_model.pkl")
    preds = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, preds))
    print("Precision:", precision_score(y_test, preds, average="macro"))
    print("Recall:", recall_score(y_test, preds, average="macro"))
    print("F1 Score:", f1_score(y_test, preds, average="macro"))

if __name__ == "__main__":
    evaluate_model()
