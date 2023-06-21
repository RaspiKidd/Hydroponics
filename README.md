# Smart Garden Project

## Background of the Project

Kerry Kidd from RaspiKidd the Orchestra conductor making sure all the code and electronics work together in harmony.  Has been helping the Maxwell Community Garden explore smart garden technology with the help of Morgan Academy and the Central Library Code club. The project was funded by the Institute of Physics. 

We originally thought about integrating smart sensors into some of the existing structures of the garden, but after speaking to some of the garden volunteers we seen that we could create a hydroponics system that people could have at home. This is where the hydroponics in a box was born.

## What is hydroponics?

Hydroponics is a method of growing plants without soil, using nutrient-rich water instead. The plants are grown in a controlled environment, typically indoors or in a greenhouse, and the water is carefully monitored and adjusted to provide the necessary nutrients. This method has become increasingly popular in recent years due to its sustainability and efficiency. Within our system we are still using a substrate to hold the plants.

## Hydroponics in a Box

The hydroponics in a box consists of:

* **A plastic box** - while the system is not in use it can be packed down and stored in the box. (£3)
* **A water pump** - I circulate the water and food around the plants. (£3.00)
* **A water level sensor** - I sense the level of the water and when it gets too low I communicate with the LEDs to turn red and alert a human that we need more water. (£7.80)
* **LED strips** - I am stuck to the lid of the box and help the plant grow where there is not enough natural light. (£7.50 per meter)
* **A wooden frame** - I am made up of scrap bits of wood and sit on top of the box to allow the plants to have enough room to grow between the box and the lights.
* **A seed tray** - I hold the substrate and the plants. (£2.00)
* **A moisture sensor** - I detect when the substrate is too dry and communicate with the pump that the plants need more water.
* **Raspberry Pi Pico** - I am the brain of the system. I hold all the code to communicate with all the electronics and power the whole system through my microUSB power cable. (£7.20)
* **A breadboard** - I have wires that run through me and connect all the electronics to the brain. (£4.50)

**Total Price: £38.40**

This is the base of our hydroponics system in a box. There are some things that we would like to integrate in the future like:

* A solar panel to power the system rather than electricity
* PH sensor so we can measure the PH of the water and make sure is optimum for the type of plant we are growing.

## Next Steps

Now that we have got the base of the system up and running we are going to develop a Web app so we can monitor the system remotely and anyone will be able to go to the dashboard and check-in to see how the hydroponics system is running.

We would also like to eventually use the system with different substrates, lighting and plants. We will also be thinking of different ways that we could encase the system to make it usable all year round to prolong growing seasons. If this happens we will document what plants grow best when through [www.dundeebots.uk/smartgarden](http://www.dundeebots.uk/smartgarden) where you can also find all the information required to build your own hydroponics in a box system.

## Parts List

* 1 x Half-sized breadboard
* 1 x Raspberry Pi Pico W
* 1 x Plastic Storage box
* 1 x Moisture Sensor
* 1 x Water Level Sensor
* 1 x Water Pump
* 1 x Temperature Sensor (**Optional**)
* 1 x Seed Tray
* 1 x Solar Panel (**Optional**)
* Some wood and Dowel rods for the frame

## To Do List

- [X] Write Water Pump Code
- [X] Write code for the moisture sensor
- [X] Write code for the water level sensor
- [] Write code for the LEDs

## Testing

- [] Water Pump
- [] Moisture Sensor
- [] Water Level Sensor
- [] LEDs
