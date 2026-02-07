from abc import ABC, abstractmethod
class Image(ABC):
    @abstractmethod
    def display(self):
        pass
class RealImage(Image):
    def __init__(self,filename):
        self.filename=filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading Image: {self.filename}")
    
    def display(self):
        print(f"Displaying Image: {self.filename}")

class ProxyImage(Image):
    def __init__(self,filename):
        self.real_image=None
        self.filename=filename

    def display(self):
        if self.real_image is None:
            self.real_image=RealImage(self.filename)
        
        self.real_image.display()
    
if __name__=="__main__":
    image=ProxyImage("example.jpg")

    image.display()
    image.display()