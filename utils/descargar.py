import httpx
import aiofiles


async def Descargar(url, nombre_archivo):

    nombre_archivo = f'{nombre_archivo}.TIF'

    # Realizar la solicitud de descarga asíncrona
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()  # Asegura que la respuesta sea exitosa (200 OK)
        except httpx.HTTPStatusError as e:
            print(f"Error al descargar el archivo: {e.response.status_code}")
            return
        except httpx.RequestError as e:
            print(f"Error de conexión: {e}")
            return

    # Guardar el contenido en un archivo de manera asíncrona
    async with aiofiles.open(nombre_archivo, 'wb') as archivo:
        await archivo.write(response.content)
        return nombre_archivo
    # print(f"Archivo descargado y guardado como {nombre_archivo}")

