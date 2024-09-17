
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from model.Grupo import Grupo

router = APIRouter()

class Request(BaseModel):
    id_grupo: int
    
@router.get("/grupo")
def retornaTodosGrupos()->JSONResponse:
    value = {}
    #TODO: acumula todos os grupos em value
    return JSONResponse(value) #? retorna os grupos em json

@router.get("/grupo/{id_grupo}")
def retornaUmGrupo()->JSONResponse:
    value = {}
    #TODO: acumula um grupo em value
    return JSONResponse(value) #? retorna os grupos em json

