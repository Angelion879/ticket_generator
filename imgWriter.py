import os
from PIL import Image, ImageDraw, ImageFont

def img_writer (name,code):
    with Image.open('PASSAPORTE_suricato.png') as img:
        draw = ImageDraw.Draw(img)
        new_font = ImageFont.truetype("arial.ttf", 25)
        draw.text((250,220),name,(61, 52, 235),font=new_font)
        draw.text((300,250),code,(61, 52, 235),font=new_font)

        if os.path.exists('passaporte.jpg'):
            os.remove('passaporte.png')

        img.save('passaporte.png', "PNG")
