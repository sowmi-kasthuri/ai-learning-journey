import logging
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from app.utils import timed_stub_response

import json
import uuid
import mlflow
import time

class GenerateRequest(BaseModel):
    prompt: str
    model: Optional[str] = "default"

class GenerateResponse(BaseModel):
    trace_id: str
    text: str
    tokens: int
    latency_ms: int
    cost: float

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("week8-backend-rebiuild")

app = FastAPI(title="Week8 Backend Rebuild")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    
    trace_id = str(uuid.uuid4())

    with mlflow.start_run():
        mlflow.log_param("model", req.model)
        mlflow.log_param("trace_id", trace_id)

        text, tokens, cost, latency_ms = timed_stub_response()

        mlflow.log_metric("tokens", tokens)
        mlflow.log_metric("latency_ms", latency_ms)
        mlflow.log_metric("cost", cost)

        mlflow.log_text(text, "response.txt")
        
        log_event = {
            "trace_id": trace_id,
            "event": "generate_request",
            "model": req.model,
            "tokens": tokens,
            "latency_ms": latency_ms,
            "cost": cost,
            "status": "success",
        }

        logger.info(json.dumps(log_event))
        
        return GenerateResponse(
            trace_id=trace_id,
            text=text,
            tokens=tokens,
            latency_ms=latency_ms,
            cost=cost,
        )

