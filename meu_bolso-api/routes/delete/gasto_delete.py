# routes/delete/gasto_delete.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from model.Gasto import Gasto

router = APIRouter()

class Request(BaseModel):
    grupo_id: int
    gasto_id: int

@router.delete("/grupo/{grupo_id}/gasto/{gasto_id}")
async def deletaGasto(grupo_id: int, gasto_id: int):
    try:
        # Busca o gasto pelo ID
        gasto = Gasto.buscar_por_id(gasto_id)
        
        if gasto is None:
            raise HTTPException(status_code=404, detail="Gasto não encontrado")
        
        # Aqui você pode adicionar uma verificação para garantir que o gasto pertence ao grupo correto
        # Por exemplo:
        # if gasto.grupo_id != grupo_id:
        #     raise HTTPException(status_code=400, detail="O gasto não pertence ao grupo especificado")
        
        # Deleta o gasto
        gasto.deletar()
        
        value = {"message": "Gasto deletado com sucesso"}
        return value
    except Exception as e:
        # Log the exception for debugging
        print(f"Erro ao deletar gasto: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor ao tentar deletar o gasto")