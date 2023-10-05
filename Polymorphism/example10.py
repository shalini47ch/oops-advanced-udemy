class Text:
    def __init__(self,text):
        self.text=text  

class Header(Text):
    def format(self):
        return f"{self.text}\n{'=' *len(self.text)}"
    
#similarly create another class called as Paragraph and inherit from Text
class Paragraph(Text):
    def format(self):
        return f"\n{self.text}"
#now the next step is to add uppercase characters 

class UpperCaseParagraph(Text):
    def format(self):
        return f"{self.text.upper()}"

document=[
    Header("Polymorphism"),
    Paragraph("The secret weapon of software engineering is polymorphism"),
    UpperCaseParagraph("Polymorphism is an important concept when learning about software engineering")
]
 
for ele in document:
    print(ele.format())
    
#here in this example we need a base case and had to use Inheritance to obtain polymorphism but generally it is not always the case
#Code has three parts models,data creation and reporting 
#we can modify the models and the data creation code but the reporting code is left untouched so here we also achieved polymorphism and even the open close principle was not violated

#In statically typed languages polymorphism requires inheritance but in languages like python which are dynamically typed polymorphism can be achieved without inheritance
#just changing the function name helps to achieve polymorphism in python