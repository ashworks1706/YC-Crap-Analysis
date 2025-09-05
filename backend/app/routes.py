# FastAPI app logic goes here
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}
# Download yc data
@router.get("/download_yc_data")
def download_yc_data():
    # Call the download script or function here
    return {"status": "data downloaded"}
