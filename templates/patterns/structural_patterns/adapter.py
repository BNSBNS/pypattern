# Adapter pattern
# The Adapter pattern is a structural pattern that allows objects with incompatible interfaces to work together.
# The Adapter pattern is used when a class needs to interact with another class that has a different interface.


class Dog:
    def __init__(self):
        self.name = "Dog"
        
    def bark(self):
        return "Woof!"
    
class Cat:
    def __init__(self):
        self.name = "Cat"
        
    def meow(self):
        return "Meow!"
    
class DogAdapter:
    def __init__(self, dog):
        self.dog = dog
        
    def speak(self):
        return self.dog.bark()
    
class CatAdapter:
    def __init__(self, cat):
        self.cat = cat
        
    def speak(self):
        return self.cat.meow()
    
dog = Dog()
dog_adapter = DogAdapter(dog)
print(dog_adapter.speak())

cat = Cat()
cat_adapter = CatAdapter(cat)

print(cat_adapter.speak())

class MultiAdapter:
    def __init__(self, obj, adapter):
        self.obj = obj
        self.adapter = adapter
        
    def speak(self):
        return self.adapter.speak()
    
multi_adapter = MultiAdapter(dog, dog_adapter)
print(multi_adapter.speak())

multi_adapter = MultiAdapter(cat, cat_adapter)
print(multi_adapter.speak())


# In this example, we have defined Dog and Cat classes with bark and meow methods, respectively.
# The DogAdapter and CatAdapter classes are adapters that wrap the Dog and Cat classes, respectively.
# The DogAdapter and CatAdapter classes provide a speak method that calls the bark and meow methods of the Dog and Cat classes, respectively.
# We create instances of the Dog and Cat classes and pass them to the DogAdapter and CatAdapter classes, respectively.
# The speak method of the DogAdapter and CatAdapter classes calls the bark and meow methods of the Dog and Cat classes, respectively.
# The Adapter pattern allows objects with incompatible interfaces to work together by providing a common interface that can be used by clients.
# The Adapter pattern is used when a class needs to interact with another class that has a different interface.


