import asyncio
from utils.syncro import syncro_temporal

async def Directorio(suministro):
    loop = asyncio.get_running_loop()
    Directorio = await loop.run_in_executor(None, syncro_temporal,suministro)
