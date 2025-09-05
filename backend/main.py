# YC Crap Analysis Backend - FastAPI Skeleton

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# TODO: Add /analyze endpoint and ML integration
