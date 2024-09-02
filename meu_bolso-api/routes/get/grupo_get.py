import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    id_grupo: int
    
@router.get("/grupo")
def retornaTodosGrupos()->json:
    value = {}
    #TODO: acumula todos os grupos em value
    return json.dumps(value) #? retorna os grupos em json

@router.get("/grupo/{id_grupo}")
def retornaUmGrupo()->json:
    value = {}
    #TODO: acumula um grupo em value
    return json.dumps(value) #? retorna os grupos em json

