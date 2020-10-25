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
            (r,g,b) = picture.getPixel(x, y)

            newR = (0.393 * r + 0.769 * g + 0.189 * b)
            newG = (0.349 * r + 0.686 * g + 0.168 * b)
            newB = (0.272 * r + 0.534 * g + 0.131 * b)

            if newR > 255: newR = 255
            if newG > 255: newG = 255
            if newB > 255: newB = 255

            picture.setPixel(x,y,(newR,newG,newB))

    picture.draw()

sepia()
