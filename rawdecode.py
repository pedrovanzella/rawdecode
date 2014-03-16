from __future__ import print_function
from sys import argv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def demosaic(rfile):
    """Demosaics a raw image file"""
    return rfile


def whitebalance(rfile):
    """Whitebalances a demosaiced image file"""
    return rfile


def gammacompress(rfile):
    """Applies gamma compression to a demosaiced image file"""
    return rfile


if __name__ == "__main__":
    if len(argv) <= 1:
        print("Usage: %s filename.tiff", argv[0])
        print("To convert from dng to tiff, use 'dcraw -D -T <image.dng>")
        exit()

    _, filename = argv

    img = mpimg.imread(filename)
    print(img)

    # Show Grayscale image
    plt.imshow(img, cmap='gray')
    plt.show()
