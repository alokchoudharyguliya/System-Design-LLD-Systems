from abc import ABC, abstractmethod
class Coffee(ABC):
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_cost(self):
        pass

class PlainCoffee(Coffee):
    def get_description(self):
        return "Plain Coffee"
    
    def get_cost(self):
        return 2.0
    
class CoffeeDecorator(Coffee):
    def __init__(self,decorated_coffee):
        self.decorated_coffee=decorated_coffee
    
    def get_description(self):
        return self.decorated_coffee.get_description()

    def get_cost(self):
        return self.decorated_coffee.get_cost()
    
class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        return self.decorated_coffee.get_description() + " Milk"
    def get_cost(self):
        return self.decorated_coffee.get_cost()+ 0.5
    
