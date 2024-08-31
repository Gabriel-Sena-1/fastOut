from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    image_id: int
    correct_classification: str

@router.post("/login")
def func1()->str:
    return "essa eh a funcao 1"

@router.post("/user")
def func2()->str:
    return "essa eh a funcao 1"
