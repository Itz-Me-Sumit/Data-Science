# Concept: super() usage

class Parent:
    def __init__(self):
        print("Parent Constructor")

    def show(self):
        print("Parent Method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

    def show(self):
        super().show()
        print("Child Method")

c = Child()
c.show()