class Rectangle:
    def __init__(self , length , breath):
        print("Inside the constructor")
        self.lenght = length
        self.breath = breath

    @classmethod # ye class me changes karne ke liye use kiya jata hai
    def setVal(cls,len,brth): # jaise baki me self(object) waise hi esme cls khud class hota hai
        print("Inside the class method")
        return cls(len,brth)
    
    def area(self):
        return self.lenght * self.breath
    
    def is_square(self):
        return self.lenght == self.breath

r = Rectangle.setVal(3,3)
print(r.is_square())
print(r.area())