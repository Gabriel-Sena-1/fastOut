from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    image_id: int
    correct_classification: str
    
@router.delete("/grupo/{grupo_id}")
def func4()->str:
    return "essa eh a funcao 4"

