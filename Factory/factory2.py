from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    # this method will associate to the product, by returning the respective product
    @abstractmethod
    def factory_method(self):
        pass
    #  the common operation 
    def some_operation(self)->str:
        product=self.factory_method()
        result=f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

class ConcreteCreator1(Creator):
    def factory_method(self)->Product:
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self)->Product:
        return ConcreteProduct2()

class Product(ABC):
    @abstractmethod
    def operation(self)->str:
        pass
    
class ConcreteProduct1(Product):
    def operation(self)->str:
        return "{Result of ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self)->str:
        return "{Result of ConcreteProduct2}"

def client_code(creator:Creator)->None:
    print(f"Client: Not aware of the creator's class, but it still works\n")
    print(f"{creator.some_operation()}")

if __name__=="__main__":
    # Supply the concretecreator-type and use its' some_operation, Creator will handle select the Product, it is responsible for and will be calling the respective 
    print("App: Launched with ConcreteCreator1")
    client_code(ConcreteCreator1())
    print("\n")
    print("App: Launched with ConcreteCreator2")
    client_code(ConcreteCreator2())

#  flow => creator.some_operation() -> creator.factory_method(), will return the respective product -> product.operation()