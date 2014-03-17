from __future__ import print_function
from sys import argv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def demosaic(rfile):
    """Demosaics a raw image file"""
    r = np.empty_like(rfile)
    g = np.empty_like(rfile)
    b = np.empty_like(rfile)
    reconstructed = np.empty([len(rfile), len(rfile[0]), 3])

    for x in range(0, len(rfile)):
        for y in range(0, len(rfile[0])):
            if x % 2 == 0:
                # Even line, Blue-Green
                if y % 2 == 0:
                    # Blue
                    b[x][y] = rfile[x][y]
                else:
                    # Green
                    g[x][y] = rfile[x][y]
            else:
                # Odd line: Green-Red
                if y % 2 == 0:
                    # Green
                    g[x][y] = rfile[x][y]
                else:
                    # Red
                    r[x][y] = rfile[x][y]

    print("RED:")
    print(r)

    print("GREEN:")
    print(g)

    print("BLUE:")
    print(b)

    return reconstructed


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

    desmosaiced_file = demosaic(img)
