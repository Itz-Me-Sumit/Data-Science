class Compare:
    def __init__(self , x):
        self.x = x
    def __str__(self):
        return f"Welcome to Calculator"
    def __eq__(self,other):
        return self.x == other.x



c1 = Compare(2)
c2 = Compare(4)

c3 = Compare(2)
c4 = Compare(2)

print(c1==c2)
print(c3==c4)