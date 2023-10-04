#super gives access to the base class we can use the __super__.init() to obtian the features from the base class and then add new properties to our classes
#instead of calling the repetitive __init__ we will use the super to solve this 
class Employee:
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary  
    
    def get_year_salary(self):
        return self.salary*12
    
class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus=bonus  
    
    def get_year_salary(self):
        return super().get_year_salary()+self.bonus
    
e=Employee("ABC",12000)
m=Employee("DEF",24000)
print(e.get_year_salary())
print(m.get_year_salary())
    
        
    