import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    user_id: int
    
@router.delete("/user/{user_id}")
def deletaUser()->str:
    value = {}
    #! começa uma transaction com o banco e deleta o conteúdo
    return json.dumps(value)

