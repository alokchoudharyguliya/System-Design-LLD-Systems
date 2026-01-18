from abc import ABC, abstractmethod

class IVegetarianMenu(ABC):
    # Interface for vegetarian menu
    @abstractmethod
    def getVegetarianItems(self):
        pass
    
class INonVegetarianMenu(ABC):
    # Interface for non-vegetarian menu
    @abstractmethod
    def getNonVegetarianItems(self):
        pass
    
class IDrinkMenu(ABC):
    # Interface for Drink menu
    @abstractmethod
    def getDrinkItems(self):
        pass

class VegetarianMenu(IVegetarianMenu):
    def getVegetarianItems(self):
        return ["Veg","Paneer"]
    
class NonVegetarianMenu(INonVegetarianMenu):
    def getNonVegetarianItems(self):
        return ["Chicken","Egg"]
    
class DrinkMenu(IDrinkMenu):
    def getDrinkItems(self):
        return ['Soda']

def displayVegetarianMenu(menu):
    print("Vegetarian Menu",end=":>\n")
    for i in menu.getVegetarianItems():
        print(f"{i}")

def displayNonVegetarianMenu(menu):
    print("Non Vegetarian Menu",end=":>\n")
    for i in menu.getNonVegetarianItems():
        print(f"{i}")
        
def main():
    
    vegMenu=VegetarianMenu()
    displayVegetarianMenu(vegMenu)
    nonvegMenu=NonVegetarianMenu()
    displayNonVegetarianMenu(nonvegMenu)
    
    drinkMenu=DrinkMenu()
    print(drinkMenu.getDrinkItems())
    
if __name__=="__main__":
    main()
    