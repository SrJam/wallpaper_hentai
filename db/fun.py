import time
import requests
import json
import math
from colorthief import ColorThief
from PIL import Image
import ctypes
from pathlib import Path
import os



class NekosFun:
    def __init__(self):
        self.url = requests.get('http://api.nekos.fun:8080/api/hentai')
        self.url = json.loads(self.url.content)['image']
        self.image = requests.get(self.url)
        open('photo/image.png', 'wb').write(self.image.content)
        self.path = Path().resolve()
        self.path = os.path.join(self.path, "photo\image.png")

    def find_color(self):
        try:
            color_thief = ColorThief(self.path)

            dominant_color = color_thief.get_color(quality=1)
            return dominant_color
        
        except TypeError:
            return (0)


    def resize_canvas(self, dominant_color, old_image_path="photo/image.png", new_image_path="photo/image.png",
                      canvas_width=1920, canvas_height=1080):

        im = Image.open(old_image_path)
        
        old_width, old_height = im.size
        if old_width / old_height < 1.35:
            # Center the image
            x1 = int(math.floor((canvas_width - old_width) / 2))
            y1 = int(math.floor((canvas_height - old_height) / 2))

            mode = im.mode
            if len(mode) == 1:  # L, 1
                new_background = dominant_color
            if len(mode) == 3:  # RGB
                new_background = dominant_color
            if len(mode) == 4:  # RGBA, CMYK
                new_background = dominant_color

            newImage = Image.new(mode, (canvas_width, canvas_height), new_background)
            newImage.paste(im, (x1, y1, x1 + old_width, y1 + old_height))
            newImage.save(new_image_path)
        else:
            pass
    def define(self):
        with open('./config.json', 'r') as f:
            tempo = json.load(f)
            tempo = int(tempo['tempo'])
        time.sleep(tempo-2)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.path, 0)



while True:
    ma = NekosFun()
    ma.resize_canvas(dominant_color=ma.find_color())
    ma.define()

