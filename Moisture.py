from machine import ADC, Pin
from time import sleep
# from WaterPump import pump_on, pump_off

substrate = ADC(Pin(26)) # Substrate moisture pin reference

# Calibrating the sensor
max_moisture = 11700 # Maximum moisture level
min_moisture = 11500 # Minimum moisture level

while True:
    # Test Code
    '''
    if substrate.read_u16() <= min_moisture:
        #pump_on()
        print("Plants need watered")
        sleep(0.5)
    else:
        print("Enough Water")
    
    value=substrate.read_u16()
    print(value)
    sleep(1)
    '''
    
    if substrate.read_u16() <= min_moisture:
        #pump_on()
        print("Plants need watered")
        sleep(0.5)
    elif substrate.read_u16() >= max_moisture:
        #pump_off()
        print ("Enough Water")
        sleep(0.5)