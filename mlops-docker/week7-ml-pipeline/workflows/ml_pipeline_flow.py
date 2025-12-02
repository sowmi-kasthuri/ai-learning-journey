# Week 7 Prefect flow outline
from prefect import flow, task

@task
def load_data():
    pass

@task
def validate_data(data):
    pass

@task
def train_model(data):
    pass

@task
def evaluate_model(model):
    pass

@task
def register_model(model,metrics):
    pass

@flow
def ml_pipeline():
    d = load_data()
    v = validate_data(d)
    m = train_model(v)
    e = evaluate_model(m)
    register_model(m,e)

if __name__ == "__main__":
    ml_pipeline()