class Employee:
    name    = "Ariyan"  #this is a class attribute
    language= "py"
    salary  = 1200000

    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")



Ariyan = Employee()  
Ariyan.name ="ariyan" #instance attribude
Ariyan.getinfo()
# Employee.getinfo(Ariyan)
 #13 14 line will give same result


