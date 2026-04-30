class Calculator:
    def __init__(self , x):
        self.x = x
    def __str__(self):
        return f"Welcome to Calculator"
    def __add__(self,other):
        return (self.x + other.x)
    def __sub__(self,other):
        return (self.x - other.x)
    def __mul__(self,other):
        return (self.x * other.x)
    def __truediv__(self,other):
        return (round(self.x / other.x , 3))

c1 = Calculator(2)
c2 = Calculator(4)

print(c1+c2 , c2-c1 , c1*c2 , c2/c1)