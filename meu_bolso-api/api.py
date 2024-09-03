import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="db",
  password="&b7Lq!Xy29D#Wj4N"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE meubolso")

#@app.get("/")
#async def homepage():
#    return FileResponse("static/index.html")

if __name__ == "__main__":
    uvicorn.run(router, port=8000)