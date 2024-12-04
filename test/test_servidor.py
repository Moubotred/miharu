# import asyncio
# import httpx
# import aiofiles
# import base64
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import Optional
# from apis.Luzdelsur import LuzdelsurRecibo

# # Crea una instancia de la aplicación FastAPI
# app = FastAPI()


# class SuministroRequest(BaseModel):
#     suministro: str


# # Endpoint de FastAPI que recibe el suministro y devuelve la imagen
# @app.post("/obtener-boleta/")
# async def obtener_boleta(suministro_request: SuministroRequest):
#     suministro = suministro_request.suministro
#     archivo = await (suministro)

#     if archivo:
#         return {"mensaje": f"Imagen guardada como: {archivo}"}
#     else:
#         raise HTTPException(status_code=400, detail="No se pudo obtener la boleta o imagen válida.")

