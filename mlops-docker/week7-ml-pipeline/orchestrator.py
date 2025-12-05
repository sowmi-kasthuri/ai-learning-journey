from prefect import flow, task
import subprocess

@task
def run_training_container():
    result = subprocess.run(
        ["docker", "run", "--rm", "week7-trainer"],
        capture_output = True,
        text = True
    )

    print(result.stdout)
    print(result.stderr)

@flow(name="week7-training-orchestrator")
def training_orchestrator():
    run_training_container()


if __name__ == "__main__":
    training_orchestrator()