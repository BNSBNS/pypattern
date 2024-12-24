# Interface Segregation Principle
# many client-specific interfaces are better than one general-purpose interface
# The Interface Segregation Principle states that a class should not be forced to implement interfaces it does not use.
# Instead of creating a single interface with multiple methods, we should create multiple interfaces with fewer methods.
# This makes the interfaces more specific and easier to implement.
# The Interface Segregation Principle helps to keep the code clean and maintainable.
# It prevents classes from becoming too complex and tightly coupled.

# Example
# Let's consider an example of a Document class that can be printed and scanned.
# We can create a single interface with two methods: print and scan.
# However, not all classes that implement this interface may need both methods.
# Some classes may only need the print method, while others may only need the scan method.
# In this case, the single interface violates the Interface Segregation Principle.
# We can refactor the code to create separate interfaces for printing and scanning.
# This way, classes can implement only the interfaces they need, and the code remains clean and flexible.
# Let's see how this can be implemented in Python:

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass


class Document:
    def __init__(self, content):
        self.content = content


class SimplePrinter(Printer):
    def print_document(self, document):
        print("Printing document:", document.content)


class SimpleScanner(Scanner):
    def scan_document(self, document):
        print("Scanning document:", document.content)


class Photocopier(Printer, Scanner):
    def print_document(self, document):
        print("Printing document:", document.content)

    def scan_document(self, document):
        print("Scanning document:", document.content)


document = Document("Sample document")

simple_printer = SimplePrinter()
simple_printer.print_document(document)

simple_scanner = SimpleScanner()
simple_scanner.scan_document(document)

photocopier = Photocopier()
photocopier.print_document(document)
photocopier.scan_document(document)

# In this example, we have defined three interfaces: Printer, Scanner, and Document.
# The Printer interface has a print_document method, and the Scanner interface has a scan_document method.
# The Document class represents a document with some content.
# We have implemented two classes: SimplePrinter and SimpleScanner that implement the Printer and Scanner interfaces, respectively.
# The Photocopier class implements both the Printer and Scanner interfaces.

