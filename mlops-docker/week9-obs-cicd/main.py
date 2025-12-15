import os
from dotenv import load_dotenv
load_dotenv()     # <-- ensures .env loads inside Docker

DEFAULT_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

from fastapi import FastAPI,HTTPException, Response
from pydantic import BaseModel
from utils import call_llm
from prometheus_client import Counter
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

import logging
import time
import mlflow

import uuid
import json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

stats = {
    "total_requests": 0,
    "total_errors": 0,
    "total_cost": 0.0,
    "avg_latency_ms": 0.0
}
app = FastAPI()
http_requests_total = Counter("http_requests_total", "Total HTTP requests")

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

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.post("/generate")
async def generate(req: GenReq):

    http_requests_total.inc()
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

            mlflow.log_metric("input_tokens", result["input_tokens"])
            mlflow.log_metric("output_tokens", result["output_tokens"])
            mlflow.log_metric("total_tokens", result["total_tokens"])
            mlflow.log_metric("latency_ms", latency)
            mlflow.log_metric("cost", result["cost"])

            mlflow.log_text(result["text"], "response.txt")

        formatted_cost = float(f"{result['cost']:.6f}")

        # STRUCTURED SUCCESS LOG
        success_log = {
            "trace_id": trace_id,
            "event": "generate_request",
            "model": req.model,
            "input_tokens": result["input_tokens"],
            "output_tokens": result["output_tokens"],
            "total_tokens": result["total_tokens"],
            "latency_ms": latency,
            "cost": f"{formatted_cost:.6f}",
            "status": "success",
            "stats": {
                 "total_requests": stats["total_requests"] + 1,
                "total_errors": stats["total_errors"],
                "avg_latency_ms": stats["avg_latency_ms"],
                "total_cost": stats["total_cost"] + formatted_cost
            }
        }

        logging.info(json.dumps(success_log))

        # Update stats
        stats["total_requests"] += 1
        stats["total_cost"] += formatted_cost

        # rolling avg latency
        stats["avg_latency_ms"] = (
            (stats["avg_latency_ms"] * (stats["total_requests"] - 1)) + latency
        ) / stats["total_requests"]

        return {
            "trace_id": trace_id,
            "text": result["text"],
            "input_tokens": result["input_tokens"],
            "output_tokens": result["output_tokens"],
            "total_tokens": result["total_tokens"],
            "latency_ms": latency,     # consistent
            "cost": f"{formatted_cost:.6f}"
        }
    
    except Exception as e:
        # ERROR PATH
        latency = int((time.time() - start) * 1000)

        error_log = {
            "trace_id": trace_id,
            "event": "generate_request",
            "model": req.model,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "latency_ms": latency,
            "cost": 0,
            "status": "error",
            "error_message": str(e),
            "stats": {
                "total_requests": stats["total_requests"],
                "total_errors": stats["total_errors"] + 1,
                "avg_latency_ms": stats["avg_latency_ms"],
                "total_cost": stats["total_cost"]

            }
        }
        
        logging.error(json.dumps(error_log))
        stats["total_errors"] += 1
        raise HTTPException(status_code=500, detail="LLM call failed")

@app.get("/stats")
def get_stats():
    return {
        "total_requests": stats["total_requests"],
        "total_errors": stats["total_errors"],
        "total_cost": float(f"{stats['total_cost']:.6f}"),
        "avg_latency_ms": int(stats["avg_latency_ms"])
    }