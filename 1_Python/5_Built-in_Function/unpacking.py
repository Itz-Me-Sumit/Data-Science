lis = [1,2,3,4,5]
print(*lis) # output -> 1 2 3 4 5 (not in list)

def add(a,b,c,d,e):
    return a+b+c+d+e

print(add(*lis))

d = {
    1:"Sumit",
    2:"Shivam",
}
print(*d)
print(*d.values())