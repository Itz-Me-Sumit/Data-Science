import pickle

class Person:
    def __init__(self, name , age , gender):
        self.name=name
        self.age=age
        self.gender=gender

with open("Person.pkl" , "rb") as f:
    obj = pickle.load(f)
    print(obj.name,obj.age,obj.gender)
