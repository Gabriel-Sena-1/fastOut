from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from model.User import User
from pydantic import BaseModel

router = APIRouter()

# Definindo o modelo Pydantic que será recebido no corpo da requisição
class UserCreate(BaseModel):
    nome: str
    sobrenome: str
    email: str
    senha: str

# Rota POST que recebe os dados via corpo da requisição
@router.post("")
def criar_usuario(user: UserCreate):
    # Aqui você pode processar os dados recebidos
    usuario = User(
        nome=user.nome,
        sobrenome=user.sobrenome,
        email=user.email,
        senha=user.senha
    )
    # Salvar o usuário no banco de dados
    cria_usuario = usuario.salvar()

    if not cria_usuario:
        raise HTTPException(status_code=404, detail="Falha ao criar o usuário.")
    return JSONResponse(content={"message": "Sucesso ao cadastrar o usuário!"})
