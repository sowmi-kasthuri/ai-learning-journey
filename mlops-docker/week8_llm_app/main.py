import os
from dotenv import load_dotenv
load_dotenv()     # <-- ensures .env loads inside Docker


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from utils import call_llm
import logging
import time
import mlflow

import uuid
import json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

app = FastAPI()

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
mlflow.set_experiment(os.getenv("MLFLOW_EXPERIMENT_NAME", "llm-app"))

class GenReq(BaseModel):
    prompt: str
    model: str = "groq"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
async def generate(req: GenReq):

    # NEW trace_id
    trace_id = str(uuid.uuid4())

    if not req.prompt:
        raise HTTPException(status_code=400, detail="prompt required")

    start = time.time()
    result = await call_llm(req.prompt, req.model)
    latency = int((time.time() - start) * 1000)

    #MLFlow logging
    mlflow.log_param("prompt", req.prompt)
    mlflow.log_param("model", req.model)

    mlflow.log_metric("tokens", result["tokens"])
    mlflow.log_metric("latency_ms", latency)

    mlflow.log_text(result["text"], "response.txt")

    # NEW STRUCTURED LOG
    log_record = {
        "trace_id":trace_id,
        "event": "generate_request",
        "model": req.model,
        "tokens": result["tokens"],
        "latency_ms": latency,
        "status": "success"
    }

    logging.info(json.dumps(log_record))

    return {
        "trace_id": trace_id,
        **result
    }
    