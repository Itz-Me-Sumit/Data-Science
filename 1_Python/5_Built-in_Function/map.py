def square(x):
    return x**2
lis = list(range(1,11))
map_of_list = map(square , lis)
print(list(map_of_list)) 



lis2 = list(range(1,11))
map_of_list = map(lambda x:x**2 , lis2)
print(list(map_of_list))