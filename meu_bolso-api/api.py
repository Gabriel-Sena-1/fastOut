import uvicorn
from fastapi import FastAPI, HTTPException
from routes.get.user_get import router as user_router  
from routes.delete.user_delete import router as user_delete_router  
from routes.get.gasto_get import router as gastos_router  


# Inicialização do FastAPI
app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(user_delete_router, prefix="/users", tags=["Users"])
app.include_router(gastos_router, prefix="/gastos", tags=["Gastos"])

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
