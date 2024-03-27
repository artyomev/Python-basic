
from fastapi import APIRouter

router = APIRouter()


@router.get("/ping/")
def send_pong():
    return {"message": "pong"}