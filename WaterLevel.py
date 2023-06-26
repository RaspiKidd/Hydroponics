from machine import ADC
from time import sleep
# from Lights import lights_red, lights_white

WaterLevel = ADC(28)

# max = 10626
# min = 10514

# Testing purposes
while True:
    value=WaterLevel.read_u16()
    print(value)
    sleep(1)
'''
while True:

    value = WaterLevel.read_u16()
    if value >= min:
        lights_red.write()
        print ("I need more water!")
    sleep(0.5)
    if value <= max:
        lights_white.write()
        print ("I am full!")
'''