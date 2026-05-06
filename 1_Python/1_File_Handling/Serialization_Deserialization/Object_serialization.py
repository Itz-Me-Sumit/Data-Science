import json

class Person:
    def __init__(self, name , age , gender):
        self.name=name
        self.age=age
        self.gender=gender

class car:
    def __init__(self,brand,price,milage):
        self.brand = brand
        self.price=price
        self.milage=milage

p1 = Person("Sumit",21,"male")
c1 = car("Spelender" , 80000 , 30)

def format(obj):
    if isinstance(obj,Person):
        return f"{obj.name} -> {obj.age} -> {obj.gender}"
    else:
        raise ValueError("This is not Person instance")

with open("objectData.json" , "w") as f:
    json.dump(p1 , f , default=format)

with open("objectData.json" , "r") as f:
    print(json.load(f))