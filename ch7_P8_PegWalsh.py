"""

Program: ch7_P8_PeggyWalsh.py

Author: Peggy Walsh

Description: Write and test a function named sepia that converts a
color image to sepia. Function should first call grayscale to
convert the color image to grayscale.

"""
from images import Image


def grayscale(image):
    image = Image("smokey.gif")
    result = Image.new("RGB", image.getHeight, image.getWidth)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))
            image.draw()
  
    



##def sepia(image, grayscale):
##     (red, green, blue) = image.getPixel(x, y)
##     if red < 63:
##         red = int(red * 1.1)
##         blue = int(blue * 0.9)
##     elif red < 192:
##        red = int(red * 1.15)
##        blue = int(blue * 0.85)
##     else:
##        red = min(int(red * 1.08), 255)
##        blue = int(blue * 0.93)



##def main(image):
##    sepia()
##    grayscale()
##    main()
        