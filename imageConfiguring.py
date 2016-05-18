"""
File: pgmProj6.py
Author: Chris Bruns
Description: Program that creates 3 new versions of the image "smokey.gif".
It allows the user to lighten the picture, darken the picture, and then set
adjust the colors with a color filter.
"""

from images import Image


def lighten(image, light):
    for y in xrange(image.getHeight()):
        for x in xrange(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            if (r + light) <= 255:
                r += light
            else:
                r == 255
            if (g + light) <= 255:
                g += light
            else:
                g == 255
            if (b + light) <= 255:
                b += light
            else:
                b == 255
            image.setPixel(x, y, (r, g, b))
    return light

def darken(image, dark):
    for y in xrange(image.getHeight()):
        for x in xrange(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            if r >= dark:
                r -= dark
            else:
                r == 0
            if g >= dark:
                g -= dark
            else:
                g == 0
            if b >= dark:
                b -= dark
            else:
                b == 0
            image.setPixel(x, y, (r, g, b))
    return dark

def colorFilter(image, (red, green, blue)):
    for y in xrange(image.getHeight()):
        for x in xrange(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            if r + red >= 255:
                r = 255
            elif r + red <= 0:
                r = 0
            else:
                r += red
            if g + green >= 255:
                g = 255
            elif g + green <= 0:
                g = 0
            else:
                g += green
            if b + blue >= 255:
                b = 255
            elif b + blue <= 0:
                b = 0
            else:
                b += blue
            image.setPixel(x, y, (r, g, b))
    return (red, green, blue)

def main(filename = "smokey.gif"):
    light = input("Enter the amount you wish to lighten the image value (0-255) with 255 being white: ")
    image1 = Image(filename)
    lighten(image1, light)
    print "Close the image window to continue. "
    image1.draw()
    dark = input("Enter the amount you wish to darken the image (0-255) with 0 being black: ")
    image2 = Image(filename)
    darken(image2, dark)
    print "Close the image window to continue. "
    image2.draw()
    red = input("Enter the amount you wish to adjust the r value (use - to decrease the value): ")
    green = input("Enter the amount you wish to adjust the g value (use - to decrease the value): ")
    blue = input("Enter the amount you wish to adjust the b value (use - to decrease the value): ")
    image3 = Image(filename)
    colorFilter(image3, (red, green, blue))
    print "close the window to quit. "
    image3.draw()


main()
