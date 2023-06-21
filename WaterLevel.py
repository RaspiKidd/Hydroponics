from machine import ADC, Pin
from time import sleep

WaterLevel = ADC(28)

min = 30000

while True:
    value = WaterLevel.read_u16()
    if value > min:
        print ("I need more water!")
    sleep(500)