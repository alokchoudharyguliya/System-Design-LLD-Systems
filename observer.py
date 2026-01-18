from abc import ABC, abstractmethod
from typing import List
class Observer(ABC):
    @abstractmethod
    def update(self,weather):
        pass
    
class Subject(ABC):
    @abstractmethod
    def add_observer(self,observer:Observer):
        pass

    @abstractmethod
    def remove_observer(self,observer:Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class PhoneDisplay(Observer):
    # def __init__(self):
    #     self.weather=""
        
    def update(self,weather):
        print(f"-{weather}")

class TVDisplay(Observer):
    def update(self,weather):
        print(f"+{weather}")

class WeatherStation(Subject):
    def __init__(self):
        self.observers:List[Observer]=[]
        self.weather=""
        
    def add_observer(self,observer:Observer):
        self.observers.append(observer)
    
    def set_weather(self,weather:str):
        self.weather=weather
        self.notify_observers()
    
    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for obs in self.observers:
            obs.update(self.weather)
            
weather_station=WeatherStation()
phone_display=PhoneDisplay()
tv_display=TVDisplay()

weather_station.add_observer(phone_display)
weather_station.add_observer(tv_display)
weather_station.set_weather("Sunny")

weather_station.set_weather("Cold")