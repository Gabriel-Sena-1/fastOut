from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from model.Gasto import Gasto
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# Definindo o modelo Pydantic que será recebido no corpo da requisição (sem id_gasto)
class GastoUpdate(BaseModel):
    nome: str
    valor: float
    data: datetime = None

# Rota PUT que recebe o id_gasto na URL e os dados via corpo da requisição
@router.put("/{id_gasto}")
def editar_gasto(id_gasto: int, gasto_data: GastoUpdate):
    # Se a data não for fornecida, use a data e hora atual
    if gasto_data.data is None:
        gasto_data.data = datetime.now()

    # Formatando a data para o formato SQL
    formatted_data = gasto_data.data.strftime('%Y-%m-%d %H:%M:%S')
    # Buscar o gasto existente pelo ID
    gasto_atual = Gasto.buscar_por_id(id_gasto)
    
    if not gasto_atual:
        raise HTTPException(status_code=404, detail="Gasto não encontrado.")
    
    # Criar o objeto Gasto com os novos dados recebidos
    gasto = Gasto(
        nome=gasto_data.nome,
        valor=gasto_data.valor,
        data=formatted_data  # Se a data não for passada, mantém a original
    )

    # Definir o id_gasto manualmente após a criação
    gasto.id_gasto = gasto_atual.id_gasto

    # Salvar as mudanças no banco de dados
    sucesso = gasto.editar()

    if not sucesso:
        raise HTTPException(status_code=400, detail="Falha ao editar o gasto.")
    
    return JSONResponse(content={"message": "Gasto atualizado com sucesso!"})
