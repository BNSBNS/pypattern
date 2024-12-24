# Factory pattern is a creational pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.
# The Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate.
# The Factory Method lets a class defer instantiation to subclasses.
# The Factory Method Pattern is also known as Virtual Constructor.
# The Factory Method Pattern is used when a class can't anticipate the class of objects it must create.
# The Factory Method Pattern is used when a class wants its subclasses to specify the objects it creates.
# The Factory Method Pattern is used when a class needs control over the creation of objects.
# The Factory Method Pattern is used when a class needs to centralize object creation.
# The Factory Method Pattern is used when a class needs to defer object creation to its subclasses.
# The Factory Method Pattern is used when a class needs to defer instantiation to its subclasses.
# The Factory Method Pattern is used when a class needs to delegate object creation to its subclasses.
# The Factory Method Pattern is used when a class needs to defer the responsibility of object creation to its subclasses.
# The Factory Method Pattern is used when a class needs to defer the responsibility of object instantiation to its subclasses.
# The Factory Method Pattern is used when a class needs to defer the responsibility of object construction to its subclasses.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()
    
class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()
    
dog_factory = DogFactory()
dog = dog_factory.create_animal()
print(dog.speak())

cat_factory = CatFactory()
cat = cat_factory.create_animal()

print(cat.speak())


# In this example, we have defined an Animal interface with a speak method.
# The Dog and Cat classes implement the Animal interface and provide the speak method.  

# Another example

class Dog
    def __init__(self):
        self.name = "Dog"

class Cat:
    def __init__(self):
        self.name = "Cat"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "Dog":
            return Dog()
        elif animal_type == "Cat":
            return Cat()
        else:
            return None
        
animal_factory = AnimalFactory()
dog = animal_factory.create_animal("Dog")

print(dog.name)
