import uvicorn
from fastapi import FastAPI, HTTPException
from routes.get.user_get import router as user_router  # Importe o roteador de usuários
# Inicialização do FastAPI
app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
