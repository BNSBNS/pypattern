# Builder pattern
# The Builder pattern is a creational pattern that separates the construction of a complex object from its representation.
# The Builder pattern is used when a class needs to create an object with many optional parameters.
# The Builder pattern is used when a class needs to create an object with many possible configurations.

from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass
    
    @abstractmethod
    def build_part_b(self):
        pass
    
    @abstractmethod
    def build_part_c(self):
        pass


class Product:
    def __init__(self):
        self.parts = []
        
    def add_part(self, part):
        self.parts.append(part)
        
    def show_parts(self):
        print("Product parts:")
        for part in self.parts:
            print(part)


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()
        
    def build_part_a(self):
        self.product.add_part("Part A1")
        
    def build_part_b(self):
        self.product.add_part("Part B1")
        
    def build_part_c(self):
        self.product.add_part("Part C1")
        
    def get_product(self):
        return self.product
    

class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()
        
    def build_part_a(self):
        self.product.add_part("Part A2")
        
    def build_part_b(self):
        self.product.add_part("Part B2")
        
    def build_part_c(self):
        self.product.add_part("Part C2")

    def build_part_d(self):
        self.product.add_part("Part C3")
        
    def get_product(self):
        return self.product
    

class Director:
    def __init__(self, builder):
        self.builder = builder
        
    def construct(self, sequence=None):
        """Construct the product using a specific sequence of steps."""
        if sequence is None:
            # Default sequence
            sequence = ['build_part_a', 'build_part_b', 'build_part_c']

        for step in sequence:
            getattr(self.builder, step)()


builder1 = ConcreteBuilder1()
director1 = Director(builder1)
director1.construct()
product1 = builder1.get_product()
product1.show_parts()

builder2 = ConcreteBuilder2()
director2 = Director(builder2)
director2.construct(['build_part_a', 'build_part_b', 'build_part_c', 'build_part_d'])
product2 = builder2.get_product()
product2.show_parts()

# In this example, we have defined a Builder interface with methods to build parts of a product.
# The Product class maintains a list of parts and provides methods to add and show parts.
# The ConcreteBuilder1 and ConcreteBuilder2 classes implement the Builder interface and provide methods to build specific parts of a product.
# The Director class takes a builder instance and constructs a product using the builder's methods.
# We create two builder instances and two director instances.
# We construct products using the directors and get the final products from the builders.
# The Builder pattern allows us to create complex objects step by step, with different configurations and options.
# The Builder pattern separates the construction of an object from its representation, allowing for more flexibility and reusability in object creation.
# The Builder pattern is useful when a class needs to create objects with many optional parameters or configurations.
# The Builder pattern is useful when a class needs to create objects with many possible variations or combinations of parts.
# The Builder pattern is useful when a class needs to create objects with complex initialization logic or dependencies.
# The Builder pattern is useful when a class needs to create objects with different representations or formats.
# The Builder pattern is useful when a class needs to create objects with different configurations or options.

# Output
# Product parts:
# Part A1
