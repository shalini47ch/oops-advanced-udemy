from abc import ABC 
from abc import abstractmethod 

class Shape(ABC):
    def __init__(self,x:float,y:float)->None:
        self.x=x 
        self.y=y 
    
    @abstractmethod
    def render(self):
        pass 

class Circle(Shape):
    def render(self)->str:
        return f"Rendering circle at x={self.x} at y {self.y}"
    
class Rectangle(Shape):
    def render(self)->str:
        return f"Rendering rectangle at x={self.x} at y {self.y}"
    
class Ellipse(Shape):
    def render(self)->str:
        return f"Rendering ellipse at x={self.x} at y {self.y}"
    
shapes=[
    Circle(12,20),
    Rectangle(10,20),
    Ellipse(11,12)
    ]
for ele in shapes:
    print(ele.render())
    
#this is an example of type abstract base class,with the help of static type checkers interfaces are implemented in python
 
    

        