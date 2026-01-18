class Rectangle:
    def __init__(self,w,h):
        self.width=w
        self.height=h

    def area(self):
        return self.width*self.height
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def setWidth(self,w):
        self.width=w
    
    def setHeight(self,h):
        self.height=h
        
class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size,size)
        
    def setWidth(self, w):
        self.width=self.height=w