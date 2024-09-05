
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from ...model.User import User

router = APIRouter()

class Request(BaseModel):
    id_user: int

@router.get("/user")
def retornaTodosUsuarios() -> JSONResponse:
    usuarios = User.buscar_todos()
    if not usuarios:
        raise HTTPException(status_code=404, detail="Nenhum usuário encontrado.")
    return JSONResponse(content=usuarios)

@router.get("/user/{id_user}")
def retornaUmUsuario(id_user: int) -> JSONResponse:
    usuario = User.buscar_por_id(id_user=id_user)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return JSONResponse(content=usuario)

