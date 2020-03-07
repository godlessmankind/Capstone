
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

def image_show_API(image_file,stop):
    
    image = Image.open(image_file)

    # Configuration for the matrix
    options = RGBMatrixOptions()
    options.rows = 32
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

    matrix = RGBMatrix(options = options)
    matrix.Clear()
    # Make image fit our screen.
    image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

    matrix.SetImage(image.convert('RGB'))

    try:
        while True:
            pass
            if stop():
                break

    except KeyboardInterrupt:
        sys.exit(0)

#!/usr/bin/env python