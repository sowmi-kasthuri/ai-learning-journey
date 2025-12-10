import os
from dotenv import load_dotenv
load_dotenv()     # <-- ensures .env loads inside Docker

DEFAULT_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

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
    # model: str = "groq"
    # model: str = "llama-3.1-8b-instant"
    model: str = DEFAULT_MODEL

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
    try:

        result = await call_llm(req.prompt, req.model)
        latency = int((time.time() - start) * 1000)

        #MLFlow logging - Success only
        with mlflow.start_run():
            mlflow.log_param("prompt", req.prompt)
            mlflow.log_param("model", req.model)

            mlflow.log_metric("tokens", result["tokens"])
            mlflow.log_metric("latency_ms", latency)
            mlflow.log_metric("cost", result["cost"])

            mlflow.log_text(result["text"], "response.txt")

        formatted_cost = float(f"{result['cost']:.6f}")

        # STRUCTURED SUCCESS LOG
        success_log = {
            "trace_id": trace_id,
            "event": "generate_request",
            "model": req.model,
            "tokens": result["tokens"],
            "latency_ms": latency,
            "cost": f"{formatted_cost:.6f}",    # <–– fix
            "status": "success"
        }

        logging.info(json.dumps(success_log))

        return {
            "trace_id": trace_id,
            "text": result["text"],
            "tokens": result["tokens"],
            "latency_ms": result["latency_ms"],
             "cost": f"{formatted_cost:.6f}"   # formatted cost
        }
    
    except Exception as e:
        # ERROR PATH
        latency = int((time.time() - start) * 1000)

        error_log = {
            "trace_id": trace_id,
            "event": "generate_request",
            "model": req.model,
            "tokens": 0,
            "latency_ms": latency,
            "cost": 0,
            "status": "error",
            "error_message": str(e)
        }
        
        logging.error(json.dumps(error_log))
        raise HTTPException(status_code=500, detail="LLM call failed")
