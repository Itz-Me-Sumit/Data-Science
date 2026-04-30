class Values:
    def __init__(self , l):
        self.l = l
    def __getitem__(self , index):
        return self.l[index]

lis = [0,1,2,3,4,5]
Val = Values(lis)
print(Val[2])