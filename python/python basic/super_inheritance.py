class Employee:
    def __init__(self):
        print("Constructor of Employee")

    a=1

class programmer(Employee):
    def __init__(self):
        print("Constructor of programmer")    
    b=2

class coder(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of coder")    
    c=3

o=Employee()
print(o.a)

o=programmer()
print(o.a,o.b)

o=coder()   
print(o.a,o.b,o.c)        