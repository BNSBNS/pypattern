# Singleton pattern
# The Singleton pattern is a creational pattern that ensures a class has only one instance and provides a global point of access to that instance.
# The Singleton pattern is used when a class should have
# only one instance and clients should be able to access it easily.
# The Singleton pattern is used when a class needs to have a single instance that is shared across the application.
# The Singleton pattern is used when a class needs to have a single instance that is shared across multiple threads, processes,modules.


class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)

# <__main__.Singleton object at 0x000002254F6D02B0>
# <__main__.Singleton object at 0x000002254F6D02B0>

# In this example, we have defined a Singleton class with a private class attribute _instance.
# The __new__ method is overridden to ensure that only one instance of the class is created.
# The first time the Singleton class is instantiated, the _instance attribute is set to None.
# The __new__ method is called to create a new instance of the class.
# The _instance attribute is set to the newly created instance and returned.
# Subsequent calls to the Singleton class will return the same instance created earlier.

# Another example

class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
class Logger(Singleton):
    def __init__(self):
        self.log = []
        
    def add_log(self, message):
        self.log.append(message)

logger1 = Logger()
logger1.add_log("Log message 1")

logger2 = Logger()
logger2.add_log("Log message 2")

print(logger1.log)
print(logger2.log)

# In this example, we have defined a Logger class that extends the Singleton class.
# The Logger class has an add_log method that adds a message to the log list.
# The Logger class is a singleton, so only one instance of the class is created.
# We create two instances of the Logger class, logger1 and logger2.
# Both logger1 and logger2 share the same log list, as they are instances of the same class.

