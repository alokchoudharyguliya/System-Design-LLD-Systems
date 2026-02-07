from abc import ABC, abstractmethod
# Target Interface
class Printer(ABC):
    @abstractmethod
    def print(self):
        pass
# Adaptee
class LegacyPrinter:
    def print_document(self):
        print("Legacy Printer is printing a document.")
# Adapter        
class PrintAdapter(Printer):
    def __init__(self):
        self.legacy_printer=LegacyPrinter()
        
    def print(self):
        self.legacy_printer.print_document()
# Client Code        
def client_code(printer):
    printer.print()
    
if __name__=="__main__":
    adapter=PrintAdapter()
    client_code(adapter)