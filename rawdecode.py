from __future__ import print_function
from sys import argv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


def demosaic(rfile):
    """Demosaics a raw image file"""
    reconstructed = np.empty([len(rfile), len(rfile[0]), 3])

    for x in range(0, len(rfile)):
        for y in range(0, len(rfile[0])):
            if x % 2 == 0:
                # Even line, Blue-Green
                if y % 2 == 0:
                    # Blue
                    reconstructed[x][y][0] = interpolate_red_blue(rfile, x, y)
                    reconstructed[x][y][1] = interpolate_green(rfile, x, y)
                    reconstructed[x][y][2] = rfile[x][y]
                else:
                    # Green
                    reconstructed[x][y][0] = interpolate_red_blue(rfile, x, y)
                    reconstructed[x][y][1] = rfile[x][y]
                    reconstructed[x][y][2] = interpolate_red_blue(rfile, x, y)
            else:
                # Odd line: Green-Red
                if y % 2 == 0:
                    # Green
                    reconstructed[x][y][0] = interpolate_red_blue(rfile, x, y)
                    reconstructed[x][y][1] = rfile[x][y]
                    reconstructed[x][y][2] = interpolate_red_blue(rfile, x, y)
                else:
                    # Red
                    reconstructed[x][y][0] = rfile[x][y]
                    reconstructed[x][y][1] = interpolate_green(rfile, x, y)
                    reconstructed[x][y][2] = interpolate_red_blue(rfile, x, y)

    return reconstructed


def interpolate_red_blue(rfile, x, y):
    r = 0

    topleft = 0
    if x > 0 and y > 0:
        # There is a pixel to the top left
        topleft = int(rfile[x - 1][y - 1])

    bottomleft = 0
    if x > 0 and y < len(rfile[0]) - 1:
        # There is a pixel to the bottom left
        bottomleft = int(rfile[x - 1][y + 1])

    topright = 0
    if x < len(rfile) - 1 and y > 0:
        # There is a pixel to the top right
        topright = int(rfile[x + 1][y - 1])

    bottomright = 0
    if x < len(rfile) - 1 and y < len(rfile[0]) - 1:
        # There is a pixel to the bottom right
        bottomright = int(rfile[x + 1][y + 1])

    r = (topleft + bottomleft + topright + bottomright) / 4

    return r


def interpolate_green(rfile, x, y):
    g = 0

    top = 0
    if y > 0:
        top = int(rfile[x][y - 1])

    left = 0
    if x > 0:
        left = int(rfile[x - 1][y])

    bottom = 0
    if y < len(rfile[0]) - 1:
        bottom = int(rfile[x][y + 1])

    right = 0
    if x < len(rfile) - 1:
        right = int(rfile[x + 1][y])

    g = (top + left + bottom + right) / 4

    return g


def whitebalance(rfile):
    """Whitebalances a demosaiced image file"""
    # We'll be using the hardcoded pixel value of (871, 558)
    print(rfile)
    result = [(r, g, b) for r in rfile[:, :, 0] for g in rfile[:, :, 1] for b in rfile[:, :, 2]]
    print(result)
    return result


def gammacompress(rfile):
    """Applies gamma compression to a demosaiced image file"""
    result = np.exp(rfile, 1 / 2.2)
    return result


if __name__ == "__main__":
    if len(argv) <= 1:
        print("Usage: %s filename.tiff", argv[0])
        print("To convert from dng to tiff, use 'dcraw -D -T <image.dng>")
        exit()

    _, filename = argv

    img = mpimg.imread(filename)

    # Show Grayscale image
    plt.imshow(img, cmap='gray')
    plt.show()

    # demosaiced_file = demosaic(img)
    # plt.imshow(demosaiced_file)
    # plt.show()

    debayer = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)
    resized = cv2.resize(debayer, (0, 0), fx=0.3, fy=0.3)
    cv2.imshow('debayered', resized)

    #whitebalanced = whitebalance(debayer)
    #resized = cv2.resize(whitebalanced, (0, 0), fx=0.3, fy=0.3)
    #cv2.imshow('whitebalanced', resized)

    #gammacorrected = gammacompress(debayer)
    #resized = cv2.resize(gammacorrected, (0, 0), fx=0.3, fy=0.3)
    #cv2.imshow('gammacorrected', resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
