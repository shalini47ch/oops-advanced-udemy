#Generally inheritance has two roles one is to allow polymorphism and the other is to prevent duplicate code 
#but in python it has only one role that is to prevent duplicate code 

class Employee:
    def __init__(self,name,salary):
        self.name=name  
        self.salary=salary 
        
    def get_info(self):
        return f"Employee {self.name} {self.salary}"
    
#now Manager is also an employee and they will inherit the init method 
class Manager(Employee):
    #the manager inherits the init from the employee
    def get_info(self):
        return f"Manager {self.name} {self.salary}"
    
class Programmer(Employee):
    #here Programmer will inherit from Employee 
    def get_info(self):
        return f"Programmer {self.name} {self.salary}"
    

employees=[
    Manager("Veera",2000),
    Programmer("Hanna",1000),
    Programmer("Raina",1500),
   
]
#iterate through the employees
for emp in employees:
    print(emp.get_info())
    
#the manager is inheriting the properties of Employee
#here the get_info method is getting overridden this is an example of overriding

    