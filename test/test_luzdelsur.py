import pytest
from apis.Luzdelsur import LuzdelsurRecibo

@pytest.mark.asyncio
async def test_LuzdelsurRecibo_simple():
    # Número de suministro de prueba
    suministro = "1274983"  # Este número debe ser válido en la API
    
    # Llamar a la función
    resultado = await LuzdelsurRecibo(suministro)
    # print(resultado)

    # Verificar si se devuelve el archivo esperado
    assert resultado.endswith('.png')