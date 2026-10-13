#write a class train which has methods to book a 
#ticket , get status( no.of seats) and get fare
#information of train running under indian railways.
from random import randint
class train():
    
    def __init__(self, trainNo):
        self.trainNo = trainNo  
                       
    def book(self, fro , to ):  
        print (f"ticket is booked in train no. {self.trainNo} from {fro} to {to}") 
                   
    def getStatus(self, ):
        print (f"train No. {self.trainNo} is running on time ")

    def getFare(self,  fro, to):
        print(f"ticket fare in train no ;{self.trainNo} from {fro} to {to} is {randint (222 ,5555 )}")

t = train(12399)
t.book ("bhagalpur " ,"haldia ")
t.getStatus()
t.getFare("bhagalpur " ,"haldia ")
