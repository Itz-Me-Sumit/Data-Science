# Concept: Method Overriding

class Parent:
    def show(self):
        print("Parent Method")

class Child(Parent):
    def show(self):
        print("Child Method")

c = Child()
c.show()