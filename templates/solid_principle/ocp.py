# open/close principle
# open for extension, closed for modification

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


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total


shapes = [Rectangle(2, 3), Circle(5), Circle(7)]

calculator = AreaCalculator(shapes)

print(calculator.total_area())  # 3.14 * 5 * 5 + 3.14 * 7 * 7 + 2 * 3 = 153.86
# 153.86

# Now, if we want to add a new shape, we can do so without modifying the AreaCalculator class.
# We can simply create a new class that inherits from the Shape class and implement the area method.
# This is the open/closed principle in action. The AreaCalculator class is open for extension but closed for modification.
