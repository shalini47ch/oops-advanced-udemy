class Employee:
    def __init__(self,firstname,middlename,lastname,salary):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname  
        self.salary=salary 
    #self.name and self.salary are the data attributes the data attributes need not be declared 
    
    def get_fullname(self):
        return f"{self.firstname}{self.middlename}{self.lastname}"
    
    #create a helper function to raise the salary of an employee by specific percentage
    def raise_salary(self,percent):
        self.salary=self.salary*(100+percent)/100
        
    #create a helper function to add the bonus
    def add_bonus(self,amount):
        self.salary=self.salary+amount 
         
#now the next step is to instantiate the class 
e1=Employee("hanna","de","er",1500)
# e2=Employee("ema","we","ma",2000)
# e3=Employee("roni","re","ta",2500)
# print(e1.firstname,e1.middlename,e1.lastname,e1.salary)
# print(e2.firstname,e2.middlename,e2.lastname,e2.salary)
# print(e3.firstname,e3.middlename,e3.lastname,e3.salary)
print(e1.get_fullname())
# print(e2.get_fullname())
# print(e3.get_fullname())
e1.raise_salary(12)
print(e1.salary)
e1.add_bonus(10)
print(e1.salary)



# # print(e1.name,e1.salary)
# print(e2.name,e2.salary)
# print(e3.name,e3.salary)