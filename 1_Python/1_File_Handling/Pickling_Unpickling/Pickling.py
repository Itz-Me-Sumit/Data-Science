# Pickling is a process where a python object hierarchy converted into byte stream

import pickle

class Person:
    def __init__(self, name , age , gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def display_info(self):
        print(f"Hi {self.name} your age is {self.age} and gender is {self.gender}")

p1 = Person("Sumit" , 21 , "male")

with open("Person.pkl" , "wb") as f:
    pickle.dump(p1 , f)