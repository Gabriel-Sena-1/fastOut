import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


#@app.get("/")
#async def homepage():
#    return FileResponse("static/index.html")

if __name__ == "__main__":
    uvicorn.run(router, port=8000)