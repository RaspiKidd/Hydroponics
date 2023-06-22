from machine import Pin
from neopixel import NeoPixel

# Define the lights pin number (17) and number of LEDs (X)
lights = NeoPixel(Pin(17), X)

def lights_white():
        # iterate over 15 leds
    for i in range(15):
        # Set each LED in the range to yellow
        lights[i] = (255,255,255)

def lights_red():
    for i in range(15):
        lights[i] = (255,0,0)


# Send the data to the strip
lights_white.write()