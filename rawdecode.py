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
        print "Usage: %s filename.dng" % argv[0]
        exit()

    _, filename = argv

    try:
        rawfile = open(filename)
    except IOError:
        print "Could not open file named %s" % filename
        exit()

    demosaiced_file = demosaic(rawfile)
    whitebalanced_file = whitebalance(demosaiced_file)
    gammacompressed_file = gammacompress(whitebalanced_file)

    rawfile.close()
