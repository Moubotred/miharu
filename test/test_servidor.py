# Agregar la raíz del proyecto al PATH

from fastapi import FastAPI, HTTPException
from apis.Luzdelsur import LuzdelsurRecibo
from apis.Envioshasber import SistemaEnviosHasber
import os

app = FastAPI()

descargas = '/home/kimshizi/Proyects/miharu/descargas/png'

@app.get("/recibo")
async def obtener_recibo(suministro: str):
    if not suministro:
        raise HTTPException(status_code=400, detail="No se proporcionó el número de suministro")
    
    resultado = await LuzdelsurRecibo(suministro)

    # Verifica si el archivo se generó
    if resultado and os.path.exists(os.path.join(descargas,resultado)):

        return {"suministro": resultado}
    
    else:
        raise HTTPException(status_code=500, detail=resultado)

@app.get("/actividad")
async def obtener_recibo(suministro: str):
    if not suministro:
        raise HTTPException(status_code=400, detail="No se proporcionó el número de suministro")
    
    resultado = await SistemaEnviosHasber(suministro)

    # Verifica si el archivo se generó
    if resultado and os.path.exists(os.path.join(descargas,resultado)):

        return {"suministro": resultado}
    
    else:
        raise HTTPException(status_code=500, detail=resultado)
