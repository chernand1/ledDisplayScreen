#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse
import numpy as np
from imageImport import imageImport

# LED strip configuration:
LED_COUNT      = 1      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 125     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    myImage = imageImport()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        np = myImage.get_image_data()
        print(int(np[5][0][0]))
        print(int(np[5][0][1]))
        print(int(np[5][0][2]))
        strip.setPixelColorRGB(0, int(np[5][0][1]), int(np[5][0][0]), int(np[5][0][2]))
        #GRB
        #strip.setPixelColorRGB(0, 0, 0, 255, 0)
        strip.show()

        time.sleep(5)
        print ('Color wipe animations.')
        for i in range(255):
            colorWipe(strip, Color(i, 0, 0))  # Red wipe
            time.sleep(0.2)
            #colorWipe(strip, Color(0, i, 0))  # Blue wipe
            time.sleep(0.2)
            #colorWipe(strip, Color(0, 0, i))  # Green wipe
            time.sleep(0.2)
            print("i = " + str(i))

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0))
