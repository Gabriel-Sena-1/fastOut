import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    grupo_id: int
    gasto_id: int

@router.delete("/grupo/{grupo_id}/gasto/{gasto_id}")
def deletaGasto()->str:
    value = {"message": 'sucess'} # ? -> faz a transação e de acordo com o retorno muda a mensagem
    #! começa uma transaction com o banco e deleta o conteúdo
    return json.dumps(value)

