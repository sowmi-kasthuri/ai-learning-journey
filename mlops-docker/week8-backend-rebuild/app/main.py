from fastapi import FastAPI

app = FastAPI(title="Week8 Backend Rebuild")

@app.get("/health")
def health():
    return {"status": "ok"}
