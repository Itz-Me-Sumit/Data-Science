# Super Method ka use parent ke methods and data accrss karne ek liye use hota hai

class Phone:
    
    def __init__(self , price , brand , camera):
        print("Inside Phone Cunstructor")
        self.price = price 
        self.barnd = brand
        self.camera = camera  

    def buy(self):
        print("Buying A Phone")

class Smartphone(Phone):

    def __init__(self,price , brand , camera , os , ram):
        self.os = os
        self.ram = ram
        super().__init__(price , brand , camera)

    def buy(self):
        print("Buying A Smartphone")
        super().buy()

sp = Smartphone(120000 , "Apple" , "42 MP" , "IOS" , 16)
sp.buy()