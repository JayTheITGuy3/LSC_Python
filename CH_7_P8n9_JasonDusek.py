"""
Author: Jason Dusek, Peggy Walsh, Jeremy Hinz
Date: 10/25/2020
Project: sepia.py

"""

from images import Image

def sepia():
    picture = Image("smokey.gif")

    for y in range(picture.getHeight()):
        for x in range(picture.getWidth()):
            (red,green,blue) = picture.getPixel(x, y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192
                 red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)

            picture.setPixel(x,y,(red,green,blue))

    picture.draw()

sepia()
