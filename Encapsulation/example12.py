#Encapsultation limits direct access to class data and methods
#you can't make things private in python but you can atleast hint that they are private by using single underscore.
class Employee:
    def __init__(self,firstname,lastname,salary):
        self._firstname=firstname 
        self._lastname=lastname 
        self._salary=salary 
        
    def get_full_name(self):
        return f"Her name is {self._firstname}{self._lastname}" 
    
    def raise_salary(self,percentage):
        self._salary=self._salary+(100*percentage)//100
    
    def get_year_salary(self):
        return self._salary*12 
    
e=Employee("Veera","Schmidth",2000)
e.raise_salary(10)
print(e.get_full_name())
print(e.get_year_salary())