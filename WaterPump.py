from machine import Pin # Pico Library this stores all the important code to interact with the pins
from time import sleep # Time library helps us to add pauses to the code to make sure things are running correctly

pump = Pin(26, Pin.OUT) # Water Pump - I circulate water and food to the plants
pin = Pin("LED", Pin.OUT) # I am for testing purposes
# I am a function that get's called to water the plants when the substrate is too dry
def pump_on():
    pin.on()
    # pump.value(0)
    sleep (1)
    print("I am watering the plants")

# I am another function. I turn off the pump once the plants have enough moisture
def pump_off():
    pin.off()
    #pump.value (1)
    sleep (1)
    print ("Plants have been watered")


    