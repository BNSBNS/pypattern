# Chain of responsibility pattern
# The Chain of Responsibility pattern is a behavioral pattern that allows an object to pass a request along a chain of handlers until the request is handled.
# The Chain of Responsibility pattern is used when a class needs to handle a request in multiple ways.
# The Chain of Responsibility pattern is used when a class needs to pass a request to multiple handlers.
# The Chain of Responsibility pattern is used when a class needs to decouple the sender and receiver of a request.
# The Chain of Responsibility pattern is used when a class needs to avoid specifying the receiver explicitly.
# The Chain of Responsibility pattern is used when a class needs to allow multiple objects to handle a request without the sender knowing the handler.
# The Chain of Responsibility pattern is used when a class needs to allow multiple objects to handle a request without the handler knowing the sender.
# The Chain of Responsibility pattern is used when a class needs to allow multiple objects to handle a request without the sender or handler knowing each other.
# The Chain of Responsibility pattern is used when a class needs to allow multiple objects to handle a request without coupling the sender and receiver.

from abc import ABC, abstractmethod

class Handler:
    
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

    def __repr__(self):
        class_name = self.__class__.__name__
        if self.successor:
            return f"class_name {class_name} -> successor{self.successor}"
        return class_name

class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            print("Handler A processing request A.")
        else:
            print(f'else A {request}')
            super().handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            print("Handler B processing request B.")
        else:
            print(f'else B {request}')
            super().handle_request(request)

class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request == "C":
            print("Handler C processing request C.")
        else:
            print(f'else C {request}')
            super().handle_request(request)

class Client:
    def __init__(self):
        self.handler_chain = ConcreteHandlerA(ConcreteHandlerB(ConcreteHandlerC()))
        print(f'self handler chain {self.handler_chain}')

    def make_request(self, request):
        self.handler_chain.handle_request(request)


client = Client()
client.make_request("C")
client.make_request("B")
client.make_request("A")
# self handler chain class_name ConcreteHandlerA -> successorclass_name ConcreteHandlerB -> successorConcreteHandlerC
# else A C
# else B C
# Handler C processing request C.
# else A B
# Handler B processing request B.
# Handler A processing request A.


# In this example, we have defined a Handler interface with a set_next and handle method.
# The AbstractHandler class implements the Handler interface and provides a default implementation for the set_next method.
# The ConcreteHandler1, ConcreteHandler2, and ConcreteHandler3 classes extend the AbstractHandler class and provide concrete implementations of the handle method.
# We create instances of the ConcreteHandler classes and chain them together using the set_next method.
# We send requests to the first handler in the chain, which will pass the request
# along the chain until a handler is found that can handle the request.
# The Chain of Responsibility pattern allows an object to pass a request along a chain of handlers until the request is handled.
# The Chain of Responsibility pattern allows for more flexibility in handling requests, as the chain can be reconfigured dynamically.
# The Chain of Responsibility pattern allows for more flexibility in adding or removing handlers from the chain.
# The Chain of Responsibility pattern allows for more flexibility in defining the order of handlers in the chain.
# The Chain of Responsibility pattern allows for more flexibility in handling requests based on different criteria or conditions.
# The Chain of Responsibility pattern allows for more flexibility in handling requests based on the state of the system or environment.
# The Chain of Responsibility pattern allows for more flexibility in handling requests based on the type or content of the request.
# The Chain of Responsibility pattern allows for more flexibility in handling requests based on the context or requirements of the system.
# The Chain of Responsibility pattern allows for more flexibility in handling requests based on the configuration or settings of the system.
# The Chain of Responsibility pattern allows for more flexibility in handling requests based on the user input or interaction with the system.
# The Chain of Responsibility pattern allows for more flexibility in handling requests based on the user preferences or behavior.