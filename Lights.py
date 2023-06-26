from machine import Pin
from neopixel import NeoPixel

# Define the lights pin number (17) and number of LEDs (X)
lights = NeoPixel(Pin(17), X)

# RGB colour values
white = 255,255,255
red = 255,0,0

def lights_white():
        # iterate over 15 leds
    for i in range(15):
        # Set each LED in the range to yellow
        lights[i] = (white)

def lights_red():
    for i in range(15):
        lights[i] = (red)


# Send the data to the strip for testing only
while True:
    lights_white.write()
    sleep = 1000
    lights_red.wirte()