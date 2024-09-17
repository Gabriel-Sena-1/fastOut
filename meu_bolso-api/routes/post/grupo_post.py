from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from model.Grupo import Grupo
from fastapi.responses import JSONResponse

router = APIRouter()

class GrupoCreate(BaseModel):
    nome: str
    id_user: int

@router.post("")
def criar_grupo(grupo_data: GrupoCreate) -> JSONResponse:
    try:
        # Criando o objeto Grupo com o nome fornecido
        grupo = Grupo(nome=grupo_data.nome)

        # Salvando o grupo no banco de dados e associando ao usuário
        sucesso = grupo.salvar(id_user=grupo_data.id_user)
        
        if not sucesso:
            raise HTTPException(status_code=400, detail="Falha ao criar o grupo.")
        
        return JSONResponse(content={"message": "Grupo criado e associado com sucesso!"})
    
    except Exception as e:
        # Captura qualquer exceção e gera uma resposta de erro
        print(f"Erro ao criar o grupo: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")
