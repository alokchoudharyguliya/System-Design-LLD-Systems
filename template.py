from abc import ABC, abstractmethod

class BeverageMaker(ABC):
    def make_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling Water")

    def pour_in_cup(self):
        print("Pouring into Cup")

    @abstractmethod
    def brew(self):
        pass
    @abstractmethod
    def add_condiments(self):
        pass

class TeaMaker(BeverageMaker):
    def brew(self):
        print("Steeping the tea")
    
    def add_condiments(self):
        print("Adding Lemon")


class CoffeeMaker(BeverageMaker):
    def brew(self):
        print("Dripping coffee through filter")
    
    def add_condiments(self):
        print("Adding sugar and milk")

if __name__=="__main__":
    print("Making Tea")
    tea_maker=TeaMaker()
    tea_maker.make_beverage()

    print("\nMaking Coffee")
    coffee_maker=CoffeeMaker()
    coffee_maker.make_beverage()