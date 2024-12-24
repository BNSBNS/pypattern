# Strategy pattern
# The Strategy pattern is a behavioral pattern that defines a family of algorithms, encapsulates each algorithm, and makes the algorithms 
# interchangeable within that family.
# The Strategy pattern is used when a class needs to perform a task in multiple ways.
# The Strategy pattern is used when a class needs to perform a task using different algorithms.

from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

class Context:
    def __init__(self, strategy):
        self.strategy = strategy
        
    def execute_strategy(self):
        self.strategy.execute()

class CashPayment(Strategy):
    def execute(self):
        print("Executing CashPayment A")

class MastercardPayment(Strategy):
    def execute(self):
        print("Executing MastercardPayment B")

class AmexPayment(Strategy):
    def execute(self):
        print("Executing AmexPayment C")       

context = Context(CashPayment())
context.execute_strategy()

context.strategy = MastercardPayment()
context.execute_strategy()

context.strategy = AmexPayment()
context.execute_strategy()

# In this example, we have defined a Strategy interface with an execute method.
# The Context class maintains a reference to a Strategy object and provides a method to execute the strategy.
# The CashPayment, MastercardPayment, and AmexPayment classes implement the Strategy interface and provide concrete implementations of the execute method.
# We create a Context instance with a CashPayment object and execute the strategy.
# We change the strategy to MastercardPayment and execute the strategy again.
# We change the strategy to AmexPayment and execute the strategy again.
# The Strategy pattern allows us to define a family of algorithms, encapsulate each algorithm, and make the algorithms interchangeable within that family.
# The Strategy pattern is useful when a class needs to perform a task in multiple ways, with different algorithms or configurations.
# The Strategy pattern is useful when a class needs to perform a task using different algorithms, depending on the context or requirements.
# The Strategy pattern allows for more flexibility and reusability in algorithm selection and execution.
