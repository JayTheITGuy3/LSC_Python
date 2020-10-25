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
            (r,g,b) = image.getPixel(x, y)

            newR = (0.393 * r + 0.769 * g + 0.189 * b)
            newG = (0.349 * r + 0.686 * g + 0.168 * b)
            newB = (0.272 * r + 0.534 * g + 0.131 * b)

            if newR > 255: newR = 255
            if newG > 255: newG = 255
            if newB > 255: newB = 255

            image.setPixel(x,y,(newR,newG,newB))

    image.draw()


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
