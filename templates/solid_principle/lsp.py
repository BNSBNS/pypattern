# liskov substitution principle
# objects of a superclass shall be replaceable with objects of its subclasses without breaking the application

from abc import ABC, abstractmethod
import unittest


class HouseholdItem(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Light(HouseholdItem):
    def turn_on(self):
        print(f"{self.name} light is on")

    def turn_off(self):
        print(f"{self.name} light is off")


class Fan(HouseholdItem):
    def turn_on(self):
        print(f"{self.name} fan is on")

    def turn_off(self):
        print(f"{self.name} fan is off")


def operate_item(item):
    item.turn_on()
    item.turn_off()


light = Light("Living room")
fan = Fan("Bedroom")

operate_item(light)
operate_item(fan)

# The operate_item function takes a HouseholdItem object as a parameter.
# The Light and Fan classes inherit from the HouseholdItem class and implement the turn_on and turn_off methods.
# We can pass objects of the Light and Fan classes to the operate_item function without breaking the application.
# This is an example of the Liskov Substitution Principle.
# The Light and Fan classes are substitutable for the HouseholdItem class.
# The operate_item function can work with objects of the Light and Fan classes without any issues.
# This makes the code more flexible and easier to maintain.
# The Liskov Substitution Principle helps to ensure that the code is robust and reliable.
# It allows us to create code that is more modular and reusable.
# By following this principle, we can write code that is easier to test and debug.


class TestHouseholdItem(unittest.TestCase):
    def test_light(self):
        light = Light("Living room")
        self.assertEqual(light.turn_on(), "Living room light is on")
        self.assertEqual(light.turn_off(), "Living room light is off")

    def test_fan(self):
        fan = Fan("Bedroom")
        self.assertEqual(fan.turn_on(), "Bedroom fan is on")
        self.assertEqual(fan.turn_off(), "Bedroom fan is off")


if __name__ == "__main__":
    unittest.main()


# another example


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


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def get_area(shape):
    return shape.area()


rectangle = Rectangle(10, 20)
square = Square(10)

print(get_area(rectangle))
print(get_area(square))
# The get_area function takes a Shape object as a parameter.
# The Rectangle and Square classes inherit from the Shape class and implement the area method.
# We can pass objects of the Rectangle and Square classes to the get_area function without breaking the application.
# This is an example of the Liskov Substitution Principle.
# The Rectangle and Square classes are substitutable for the Shape class.
# The get_area function can work with objects of the Rectangle and Square classes without any issues.
# This makes the code more flexible and easier to maintain.
# The Liskov Substitution Principle helps to ensure that the code is robust and reliable.
# It allows us to create code that is more modular and reusable.
# By following this principle, we can write code that is easier to test and debug.
# The Liskov Substitution Principle is an important part of object-oriented design and helps to create code that is more maintainable and scalable.
