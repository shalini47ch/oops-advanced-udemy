class Product:
    def __init__(self,productid,name,price):
        self.productid=productid  
        self.name=name 
        self.price=price 
    
    def __str__(self):
        return f" {self.name} {self.productid}"
    
    def __repr__(self):
        return f"{self.name}({self.productid})"
products=[
        Product(1,"Headphone",40.10),
        Product(2,"Speakers",45.10),
        Product(3,"Soundcard",78.5)
    ]
for ele in products:
    print(ele)
    #using this way we can get the outputs for both str and repr by calling them
    print(str(ele))
    print(repr(ele))
    print()
    
    
#print(ele)
#__str__
#__repr__
#these are the two ways to represent object representation

#in case our class doesnt have these these then some addresses are returned
#in dunder string is present before dunder repr then the dunder string class will be implemented instead of repr
#the above is the order in which the function is executed