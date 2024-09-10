import uvicorn

from fastapi import FastAPI
from routes.post.user_post import router as user_post_router            # C
from routes.get.user_get import router as user_get_router               # R
from routes.put.user_put import router as user_put_router               # U
from routes.delete.user_delete import router as user_delete_router      # D

from routes.post.gasto_post import router as gastos_post_router         # C
from routes.get.gasto_get import router as gastos_get_router            # R
from routes.put.gasto_put import router as gastos_put_router            # U
from routes.delete.gasto_delete import router as gastos_delete_router   # D

from routes.post.grupo_post import router as grupos_post_router         # C
from routes.get.grupo_get import router as grupos_get_router            # R
from routes.put.grupo_put import router as grupos_put_router            # U
from routes.delete.grupo_delete import router as grupos_delete_router   # D

# Inicialização do FastAPI
app = FastAPI()

app.include_router(user_post_router, prefix="/user", tags=["User"])     #* OK
app.include_router(user_get_router, prefix="/user", tags=["User"])      #* OK
app.include_router(user_put_router, prefix="/user", tags=["User"])      #* OK
app.include_router(user_delete_router, prefix="/user", tags=["User"])   #* OK

app.include_router(gastos_post_router, prefix="/gasto", tags=["Gasto"])   #* OK
app.include_router(gastos_get_router, prefix="/gasto", tags=["Gasto"])    #* OK
app.include_router(gastos_put_router, prefix="/gasto", tags=["Gasto"]) 
app.include_router(gastos_delete_router, prefix="/gasto", tags=["Gasto"]) 

app.include_router(grupos_post_router, prefix="/grupos", tags=["Grupos"]) 
app.include_router(grupos_get_router, prefix="/grupos", tags=["Grupos"]) 
app.include_router(grupos_put_router, prefix="/grupos", tags=["Grupos"]) 
app.include_router(grupos_delete_router, prefix="/grupos", tags=["Grupos"]) 

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
