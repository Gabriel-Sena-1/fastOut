import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    id_grupo: int
    id_gasto: str
    
@router.get("/grupo/{id_grupo}/gasto")
def exibeTodosGastos()->json:
    value = {}
    #! faz uma chamada de select nos gastos
    #! acumula e armazena em uma variável
    return json.dumps(value)

@router.get("/grupo/{id_grupo}/gasto/{id_gasto}")
def exibeUmGasto()->json:
    value = {}
    #! faz uma chamada de select no gasto especifico
    #! acumula e armazena em uma variável
    return json.dumps(value)

