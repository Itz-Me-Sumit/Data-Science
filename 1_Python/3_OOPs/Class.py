class Atm:

    # constructor 
    def __init__(self , pin , balance):
        self.pin = pin
        self.balance = balance
    
    # Setter
    def SetPin(self , pin):
        self.pin = pin
    def SetBalance(self , balance):
        self.balance = balance
    
    # Getter
    def GetPin(self):
        return self.pin
    def GetBalance(self):
        return self.balance


sumit = Atm(122 , 323)
print(sumit.pin , " " , sumit.balance)

sumit.SetPin(121)
sumit.SetBalance(2322)
print(sumit.GetPin() , " " , sumit.GetBalance()) 