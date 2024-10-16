class Employee:

    name    = "Ariyan"  #this is a class attribute
    language= "py"
    salary  = 1200000


    def __init__(self , name , salary , language):  #Dunder method which is automatically called
        print("I am creating an object")
        self.name= name
        self.salary= salary
        self.language = language


    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")


    def greet():
        print("GOOD MORNING")   

        



Ariyan = Employee( "Hridoy" , 1500000 , "Java script")  
Ariyan.name ="ariyan" #instance attribude
print(Ariyan.name , Ariyan.salary , Ariyan.language)
# Employee.getinfo(Ariyan)
 #13 14 line will give same result


