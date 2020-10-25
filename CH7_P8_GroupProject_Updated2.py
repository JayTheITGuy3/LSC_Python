"""
Author: Jason Dusek, Peggy Walsh, Jeremy Hinz
Date: 10/25/2020
Project: CH7_P8_GroupProject

Request: To create a program to do photo editing

"""

from images import Image


def sepia(image):


    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (red,green,blue) = image.getPixel(x, y)

            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)

            image.setPixel(x,y,(red,green,blue))


def grayscale(image):
    """Converts the argument image to grayscale."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))

    image.draw()

    sepia(image)


def main(filename = "smokey.gif"):
    image = Image(filename)
    print("Close the image window to continue. ")
    image.draw()
    grayscale(image)
    print("Close the image window to quit. ")
    image.draw()



if __name__ == "__main__":
    main()
