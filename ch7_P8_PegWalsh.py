"""

Program: ch7_P8_PeggyWalsh.py

Authors: Peg Walsh, Jeremy Hinz, Jason Dusek

Description: Write and test a function named sepia that converts a
color image to sepia. Function should first call grayscale to
convert the color image to grayscale.

"""
"""

Program: ch7_P8_PeggyWalsh.py

Authors: 

Description: Write and test a function named sepia that converts a
color image to sepia. Function should first call grayscale to
convert the color image to grayscale.

"""
from images import Image

def grayscale(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))
            
        
def main(filename = "smokey.gif"):
    image = Image(filename)
    print("Close the image window to continue.")
    image.draw()
    grayscale(image)
    print("Close the image window to quit.")
    image.draw()


if __name__ == "__main__":
    main()

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

