from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    image_id: int
    correct_classification: str

@router.get("/user")
def func1()->str:
    return "essa eh a funcao 1"

@router.get("/user/{id_user}")
def func2()->str:
    return "essa eh a funcao 2"

