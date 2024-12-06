from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO
import requests

def waifu(tipo:str,categotia:str):
    url = f"https://api.waifu.pics/{tipo}/{categotia}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        imagen_waifu =  data['url']
        image_response = requests.get(imagen_waifu, timeout=10)
        return image_response

    if response.status_code != 200:
        return None

def recibo_anime(suministro):
    # Abrir la imagen base
    base_image = Image.open(f"{suministro}.png").convert("RGBA")

    # Crear la superposición (puede ser un rectángulo transparente con texto)
    overlay = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    logo_anime = waifu(tipo='sfw',categotia='neko')
    logo = Image.open(BytesIO(logo_anime.content)).convert("RGBA")
    logo = logo.resize((400, 700))  # Redimensionar si es necesario
    overlay.paste(logo, (1050, 760), logo)  # Pegar con transparencia

    # Crear la superposición (puede ser un rectángulo transparente con texto)
    overlay_oficial = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay_oficial)


    logo_oficial = os.path.join('/home/kimshizi/Proyects/miharu/experimental','anime','fracazado.png') 
    logo = Image.open(logo_oficial).convert("RGBA")
    logo = logo.resize((400, 330))  # Redimensionar si es necesario
    overlay_oficial.paste(logo, (1120, 60), logo)  # Pegar con transparencia

    # Combinar imágenes
    combined = Image.alpha_composite(base_image, overlay)
    final_image = Image.alpha_composite(combined, overlay_oficial)

    # Guardar el resultado
    final_image.save(f"{suministro}.png", format="PNG")
