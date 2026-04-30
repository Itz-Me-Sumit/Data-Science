# Concept: Multilevel Inheritance

class Grandparent:
    def gp(self):
        print("Grandparent")

class Parent(Grandparent):
    def p(self):
        print("Parent")

class Child(Parent):
    def c(self):
        print("Child")

obj = Child()
obj.gp()
obj.p()
obj.c()