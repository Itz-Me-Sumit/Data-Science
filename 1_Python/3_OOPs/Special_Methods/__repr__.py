class person:
    def __init__(self , name , age):
        self.__name = name
        self.__age = age
    def __repr__(self):
        return f"{self.__name} is {self.__age} years old"

p = person("Sumit" , 21)
print(p)