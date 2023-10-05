class Employee:
    def __init__(self,firstname:str,lastname:str,salary:float):
        self.firstname=firstname 
        self.lastname=lastname
        self.salary=salary  
    
    def get_fullname(self)->str:
        return f"{self.firstname} {self.lastname}"
        
    #similarly write a helper function to raise_salary
    def raise_salary(self,percentage:float)->None:
        self.salary=self.salary*(100+percentage)/100
        
        
        
e=Employee("Vera","schemidth",2000)
print(e.get_fullname())
e.raise_salary(10)
print(e.salary)

#we can perform type checking by specifying the data type directly
#using the type for the self parameter is Optional