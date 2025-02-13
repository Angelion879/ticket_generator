import os
from PIL import Image, ImageDraw, ImageFont

color = (0,0,0)
y_axis = 1620

def img_writer (name,code):
    with Image.open('PASSAPORTE_suricato.png') as img:
        draw = ImageDraw.Draw(img)
        new_font = ImageFont.truetype("nats.ttf", 100)
        draw.text((70,y_axis),name,color,font=new_font)
        draw.text((1000,y_axis),code,color,font=new_font)

        if os.path.exists('passaporte.jpg'):
            os.remove('passaporte.png')

        img.save('passaporte.png', "PNG")
