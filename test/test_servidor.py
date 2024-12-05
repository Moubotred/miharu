# Agregar la raíz del proyecto al PATH

from fastapi import FastAPI, HTTPException
from apis.Luzdelsur import LuzdelsurRecibo
import os

app = FastAPI()

@app.get("/recibo")
async def obtener_recibo(suministro: str):
    if not suministro:
        raise HTTPException(status_code=400, detail="No se proporcionó el número de suministro")
    
    resultado = await LuzdelsurRecibo(suministro)

    # Verifica si el archivo se generó
    if resultado and os.path.exists(os.path.join(os.getcwd(),resultado)):

        return {"suministro": resultado}
    
    else:
        raise HTTPException(status_code=500, detail="No se pudo generar el archivo")

