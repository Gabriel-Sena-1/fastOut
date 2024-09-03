import uvicorn
from fastapi import FastAPI, HTTPException
from database_manager import DatabaseManager

# Configuração do banco de dados
db_manager = DatabaseManager(
    host="localhost",
    user="db",
    password="&b7Lq!Xy29D#Wj4N",
    database="meubolso"
)

# Conectar ao banco de dados
db_manager.connect()

# Criação do banco de dados (se necessário)
db_manager.execute("CREATE DATABASE IF NOT EXISTS meubolso")
db_manager.commit()

# Seleciona o banco de dados
db_manager.execute("USE meubolso")

# Lê e executa o arquivo SQL
with open("schema.sql", "r") as file:
    sql_script = file.read()

for statement in sql_script.split(';'):
    if statement.strip():
        db_manager.execute(statement)

# Confirma as mudanças e desconecta
db_manager.commit()
db_manager.disconnect()

# Inicialização do FastAPI
app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
