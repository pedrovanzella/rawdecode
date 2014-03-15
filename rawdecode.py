from __future__ import print_function
from sys import argv


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
        print("Usage: %s filename.dng", argv[0])
        exit()

    _, filename = argv

    try:
        with open(filename) as f:
            image_binary = f.read()
    except IOError:
        print("Could not open file named %s", filename)
        exit()
