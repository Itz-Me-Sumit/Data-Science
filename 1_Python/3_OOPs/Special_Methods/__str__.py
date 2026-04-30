# __str__() ka use object ko human-readable (user-friendly) string me convert karke print karne ke liye hota hai.

class person:
    def __init__(self , name , age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return f"{self.__name} is {self.__age} years old"

p = person("Sumit" , 21)
print(p)