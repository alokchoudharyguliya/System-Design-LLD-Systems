from __future__ import annotations
from abc import ABC, abstractmethod

class Abstraction:
    def __init__(self,implemetnation:Implementation)->None:
        self.implemetnation=implemetnation
    def operation(self)->str:
        return (f"Abstraction : Base operation"
                f"{self.implemetnation.operation_implementation()}")

class ExtendedAbstraction(Abstraction):
    def operation(self)->str:
        return (f"ExtendedAbstraction : Extended operation"
                f"{self.implemetnation.operation_implementation()}")

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self)->str:
        pass
    
class ConcreteImplementationA(Implementation):
    def operation_implementation(self)->str:
        return "ConcreteImplementationA"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self)->str:
        return "ConcreteImplementationB"

def client_code(abstraction:Abstraction)->None:
    print(abstraction.operation(),end="")

if __name__=="__main__":
    implemetnation=ConcreteImplementationA()
    abstraction=Abstraction(implemetnation)
    client_code(abstraction)

    print("\n")

    implemetnation=ConcreteImplementationB()
    abstraction=ExtendedAbstraction(implemetnation)
    client_code(abstraction)