#In python the constructor is a combination of dunder new and dunder __init__ so init is alone not the constructor the order is like new followed by init
class Song:
    #this __init__ part is the one which acts as the constructor
    def __init__(self,id,name):
        self.id=id  #self.id is the attribute which stores the id
        self.name=name 
        
    #now create a helper function to get the id 
    def get_id(self):
        return f"{self.id}"
    
    def get_name(self):
        return f"{self.name}"
    
obj1=Song(1,"night changes")
obj2=Song(2,"Senorita")
print(obj1.get_id())
print(obj1.get_name())
print(obj2.get_id())
print(obj2.get_name())
