# Observer pattern
# The Observer pattern is a behavioral pattern that defines a one-to-many dependency between objects so that when one object changes state, 
# all its dependents are notified and updated automatically.
# The Observer pattern is used when a class needs to notify other classes when its state changes.
# The Observer pattern is used when a class needs to notify multiple classes when its state changes.

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class Subject:
    def __init__(self):
        self.observers = []
        
    def add_observer(self, observer):
        self.observers.append(observer)
        
    def remove_observer(self, observer):
        self.observers.remove(observer)
        
    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

class MessageBoard(Subject):
    def post_message(self, message):
        self.notify_observers(message)

class User(Observer):
    def __init__(self, name):
        self.name = name
        
    def update(self, message):
        print(f"{self.name} received message: {message}")

message_board = MessageBoard()
user1 = User("Alice")
user2 = User("Bob")

message_board.add_observer(user1)
message_board.add_observer(user2)

message_board.post_message("Hello, world!")

# In this example, we have defined an Observer interface with an update method.
# The Subject class maintains a list of observers and provides methods to add, remove, and notify observers.
# The MessageBoard class extends the
# Subject class and provides a method to post messages to observers.
# The User class implements the Observer interface and provides an update method to receive messages.
# We create a MessageBoard instance and two User instances.
# We add the User instances as observers to the MessageBoard instance.

