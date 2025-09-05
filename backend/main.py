# YC Crap Analysis Backend - FastAPI Skeleton

from fastapi import FastAPI
from app.routes import router

app = FastAPI()
app.include_router(router)

# Entry point for FastAPI app
