import httpx
import aiofiles
from utils.descargar import Descargar
from utils.convertidor import ConvertirPDF
from utils.directorio import Directorio

async def SistemaEnviosHasber(suministro:str) -> str:
    # URL de la solicitud POST
    url = "https://hasbercourier.easyenvios.com/modulos/controlador/herramientas/con_cargosenvios.php?tabla=congrid_envio_seguimiento"

    # Encabezados de la solicitud
    headers = {
        "Host": "hasbercourier.easyenvios.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://hasbercourier.easyenvios.com",
        "Referer": "https://hasbercourier.easyenvios.com/modulos/seguimiento.php",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Te": "trailers",
        "Connection": "keep-alive"
    }

    # Datos del cuerpo de la solicitud (POST data)
    data = {
        "ciacodigo": "17",
        "succodigo": "001",
        "asenombre": "",
        "codigoenvio": "",
        "codigounico": f"{suministro}",
        "asepropuesta": "",
        "strnrodocumento": "",
        "page": "1",
        "rows": "10",
        "sort": "a.asenumero",
        "order": "asc"
    }

    # Realiza la solicitud POST de manera asíncrona
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, data=data)
            if response.status_code == 200:
                data = response.json()
                # Busca la clave de diccionario especificada

                try:

                    seleccionar = [data['rows'][item]['artnombre'] == 'CARTAS / REEMPLAZO DE MEDIDOR EMPRESAS' for item in range(len(data['rows']))]
                    if seleccionar:
                        UrlImage = str(data['rows'][seleccionar.index(True)].get('imagen1'))
                        response_data = await client.get(UrlImage)
                        formato_TIF = await Descargar(response=response_data,nombre_archivo=suministro)
                        formato_PDF = await ConvertirPDF(suministro=formato_TIF)
                        return formato_PDF
                    
                except Exception as e:
                    print('sinstaxis en espera')
                    return 'la actividad no esta programda aun'

        except httpx.HTTPStatusError as e:
            return f"Error en la solicitud: {e.response.status_code}"
        except httpx.RequestError as e:
            return f"Error de conexión: {e}"