import httpx
import base64
import aiofiles
import sys
sys.path.append('/home/kimshizi/Proyects/miharu/')

from utils import directorio

import asyncio

async def LuzdelsurRecibo(suministro:str) -> str:
    # URL de la API
    url = "https://www.luzdelsur.pe/es/VerPagarRecibo/ObtenerImagenBoletaLibre"

    # Payload con el número de suministro
    payload = {
        "request": {
            "Suministro": f"{suministro}"  # Ajusta el número de suministro
        }
    }

    # Encabezados necesarios (incluye la Cookie si es requerida)
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://www.luzdelsur.pe",
        "Referer": "https://www.luzdelsur.pe/es/VerPagarRecibo"
    }

    # Realiza la solicitud POST de manera asíncrona
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(url, json=payload, headers=headers)

    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta a JSON
        data = response.json()
        
        imagen_base64 = data['datos']['archivoBase64']

        if not imagen_base64:
            return False
        
        # Decodificar y guardar la imagen en un archivo de manera asíncrona
        try:
            archivo = f'{suministro}.png'
            async with aiofiles.open(archivo, "wb") as img_file:
                await img_file.write(base64.b64decode(imagen_base64))
                await directorio(suministro=archivo)
                return f"{suministro}.png"
                
        
        except TypeError:
            return "La API no devolvió una imagen válida en formato base64"