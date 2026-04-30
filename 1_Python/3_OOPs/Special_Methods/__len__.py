class List:
    def __init__(self , l):
        self.l = l
    def __str__(self):
        return self.l
    def __len__(self):
        return len(self.l)
    
a = [1,2,3,4]
l = List(a)
print(len(l))