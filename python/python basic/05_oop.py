from random import randint

class train:

    def __init__(self , trainNo):
        self.trainNo= trainNo

    def book(self ,fro , to):
        print(f"ticket is booked in train no : {self.trainNo} form {fro} to {to}")

    def getstatus(self):
        print(f"train no : {self.trainNo}  is running on time")

    def getfare(self ,fro , to):
        print(f"ticket fare in train no : {self.trainNo} form {fro} to {to} is {randint(100,500)}")


t = train(12399)
t.book("Dhaka ","Usa")
t.getstatus()
t.getfare("Dhaka" , "Usa")