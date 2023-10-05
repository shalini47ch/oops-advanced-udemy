#Polymorphism same function name just different implementations 
class Circle:
    def render(self):
        return f"Circle geometry"
    
#similarly create a rectangle geometry
class Rectangle:
    def render(self):
        return f"Rectangle geometry"
    
shapes=[Circle(),Rectangle()]
for s in shapes:
    print(s.render())