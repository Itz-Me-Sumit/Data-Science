class User:
    def __name__(self):
        pass
    def login(self):
        print("Login")

class Student(User):
    # def __init__(self):
    #     pass
    def enroll(self):
        print("Enrolled")

u = User()
s = Student()

s.login()