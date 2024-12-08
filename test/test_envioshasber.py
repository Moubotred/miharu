import pytest
from apis.Envioshasber import SistemaEnviosHasber

@pytest.mark.asyncio
async def test_hasber():
    # Número de suministro de prueba
    suministro = "7798"  # Este número debe ser válido en la API
    
    # Llamar a la función
    resultado = await SistemaEnviosHasber(suministro)

    # Verificar si se devuelve el archivo esperado
    assert resultado.endswith('.pdf')
    # assert resultado == None