import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    grupo_id: int
    
@router.delete("/grupo/{grupo_id}")
def deletaGrupo()->str:
    #! começa uma transaction com o banco e deleta o conteúdo
    return "essa eh a funcao 4"

