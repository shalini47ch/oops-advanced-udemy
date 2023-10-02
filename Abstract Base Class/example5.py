#Abstract classes no instantiation and we can force method implementations 
from abc import ABC
from abc import abstractmethod

class Shape(ABC):
    def __init__(self,x,y):
        self.x=x
        self.y=y 
    @abstractmethod
    def render(self):
        pass
        
class Circle(Shape):
    def render(self):
        return f"Rendering circle at x {self.x}  and y is {self.y}"
    
class Rectangle(Shape):
    def render(self):
        return f"Rendering rectangle at x {self.x} at y is {self.y}"
    
class Ellipse(Shape):
    def render(self):
        return f"Rendering ellipse at x{self.x} and y at {self.y}"
    
    

shapes=[
    Circle(12,13),
    Rectangle(14,15),
    
]

#doing this way will give us the error as shape has no attribute as render

for ele in shapes:
    print(ele.render())
    
#a class becomes abstract when atleast one method becomes abstract with the @abstractmethod decorator and we can make classes as abstract classes using ABC 
