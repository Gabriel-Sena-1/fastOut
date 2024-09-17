from datetime import datetime
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from model.Gasto import Gasto
from model.User import User
from pydantic import BaseModel

router = APIRouter()

# Definindo o modelo Pydantic que será recebido no corpo da requisição
class GastoCreate(BaseModel):
    nome: str
    valor: float
    data: datetime = None
    id_user: int
    id_grupo: int

@router.post("")
def criar_gasto(gasto_data: GastoCreate):
    # Se a data não for fornecida, use a data e hora atual
    if gasto_data.data is None:
        gasto_data.data = datetime.now()

    # Formatando a data para o formato SQL
    formatted_data = gasto_data.data.strftime('%Y-%m-%d %H:%M:%S')

    # Criando uma instância do gasto
    gasto = Gasto(
        nome=gasto_data.nome,
        valor=gasto_data.valor,
        data=formatted_data
    )

    try:

        # Salvando o gasto e associando ao usuário e grupo
        sucesso = gasto.salvar_gasto(id_user=gasto_data.id_user, id_grupo=gasto_data.id_grupo)

        if not sucesso:
            raise HTTPException(status_code=400, detail="Falha ao criar o gasto.")
        
        return JSONResponse(content={"message": "Gasto criado e associado com sucesso!"})
    
    except Exception as e:
        # Captura qualquer exceção e gera uma resposta de erro
        print(f"Erro ao salvar o gasto: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")
