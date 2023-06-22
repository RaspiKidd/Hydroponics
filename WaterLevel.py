from machine import ADC
from time import sleep
from Lights import lights_red

WaterLevel = ADC(28)

min = 30000

while True:
    value = WaterLevel.read_u16()
    if value > min:
        lights_red.write()
        print ("I need more water!")
    sleep = 500