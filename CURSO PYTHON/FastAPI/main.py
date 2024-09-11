from fastapi import FastAPI
app = FastAPI()

@app.get("")
async def Inicio():
    return "Inicio"



@app.get("/rut")
async def rut():
    return "Rut"
