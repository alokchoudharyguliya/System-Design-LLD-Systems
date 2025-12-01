# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def printVehicle(self):
#         pass

# class TwoWheeler(Vehicle):
#     def printVehicle(self):
#         print("I am two wheeler")

# class FourWheeler(Vehicle):
#     def printVehicle(self):
#         print("I am four wheeler")

# class Client:
#     def __init__(self,type):
#         if type==1:
#             self.pVehicle=TwoWheeler()
#         elif type==2:
#             self.pVehicle=FourWheeler()
#         else:
#             self.pVehicle=None
        
#     def cleanup(self):
#         if self.pVehicle is not None:
#             self.pVehicle=None
        
#     def getVehicle(self):
#         return self.pVehicle

# def main():
#     pClient=Client(1)
#     pVehicle=pClient.getVehicle()
#     if pVehicle is not None:
#         pVehicle.printVehicle()
#     pClient.cleanup()

# if __name__=="__main__":
#     main()


## WITH FACTORY METHOD DESIGN PATTERN
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def printVehicle(self):
        pass

class TwoWheeler(Vehicle):
    def printVehicle(self):
        print("I am two wheeler")

class FourWheeler(Vehicle):
    def printVehicle(self):
        print("I am four wheeler")


class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self):
        pass
    
class TwoWheelerFactory(VehicleFactory):
    def createVehicle(self):
        return TwoWheeler()
    
class FourWheelerFactory(VehicleFactory):
    def createVehicle(self):
        return FourWheeler()

class Client:
    def __init__(self,factory:VehicleFactory):
        self.pVehicle=factory.createVehicle()

    def getVehicle(self):
        return self.pVehicle

def main():
    twoWheelerFactory=TwoWheelerFactory()
    twoWheelerClient=Client(twoWheelerFactory)
    twoWheeler=twoWheelerClient.getVehicle()
    twoWheeler.printVehicle()

    fourWheelerFactory=FourWheelerFactory()
    fourWheelerClient=Client(fourWheelerFactory)
    fourWheeler=fourWheelerClient.getVehicle()
    fourWheeler.printVehicle()

if __name__=="__main__":
    main()