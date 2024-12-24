# Dependency Inversion Principle
# The Dependency Inversion Principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions. In addition, abstractions should not depend on details. Details should depend on abstractions.
# The Dependency Inversion Principle helps to decouple the code and make it more flexible and maintainable. It allows us to change the implementation details without affecting the high-level modules.
# The Dependency Inversion Principle is often implemented using dependency injection. Dependency injection is a design pattern that allows us to inject dependencies into a class rather than creating them inside the class.
# Let's see an example of the Dependency Inversion Principle in Python:

from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def detect(self):
        pass

class TemperatureSensor(Sensor):
    def detect(self):
        return 25
    
class InfraRedSensor(Sensor):
    def detect(self):
        return "Movement detected"
    
class Robot:
    def __init__(self, *sensors):
        self.sensors = sensors
        
    def detect(self):
        for sensor in self.sensors:
            print(sensor.detect())

temperature_sensor = TemperatureSensor()
infrared_sensor = InfraRedSensor()

robot = Robot(temperature_sensor, infrared_sensor)
robot.detect()

# The Robot class is open for extension because we can add new sensors without modifying the Robot class.
# For example, if we want to add a new sensor that detects sound, we can create a new class that inherits from the Sensor class and implement the detect method.
# The Robot class does not need to be modified to accommodate the new sensor.



#  another example

class Switchable(ABC):
    @abstractmethod
    def press_switch(self):
        pass

class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.press_switch()
            self.on = False
        else:
            self.client.press_switch()
            self.on = True

class Light(Switchable):
    def press_switch(self):
        print("Light is on")

class Fan(Switchable):
    def press_switch(self):
        print("Fan is on")

light = Light()
fan = Fan()

switch = ElectricPowerSwitch(light)
switch.press()
switch.press()

switch = ElectricPowerSwitch(fan)
switch.press()
switch.press()

# In this example, we have defined two interfaces: Switchable and ElectricPowerSwitch.
# The Switchable interface has a press_switch method, and the ElectricPowerSwitch class takes a Switchable object as a parameter.
# The Light and Fan classes implement the Switchable interface and provide the press_switch method.
# The ElectricPowerSwitch class controls the on/off state of the Switchable object by calling the press_switch method.
# We can easily add new Switchable objects without modifying the ElectricPowerSwitch class.
# This example demonstrates the Dependency Inversion Principle by decoupling the high-level ElectricPowerSwitch class from the low-level Light and Fan classes.
