class student :
    def check_pass_fail(self):
        if self.marks >=40 :
            return True
        else :
            return False
        
    def __init__(self, name ,marks):
        self.name=name
        self.marks=marks
        
        
student1=student( "Ariyan", 31)


did_pass=student1.check_pass_fail()
print(did_pass)