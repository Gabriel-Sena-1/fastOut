import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    id_user: int

@router.get("/user")
def retornaTodosUsuarios()->json:
    usuarios = {}
    #todo: acumula todos os usuarios em value
    return json.dumps(usuarios) #? retorna usuarios 

@router.get("/user/{id_user}")
def retornaUmUsuario()->json:
    usuario = {}
    #todo: acumula o usuario em value
    return json.dumps(usuario) #? retorna o usuario

