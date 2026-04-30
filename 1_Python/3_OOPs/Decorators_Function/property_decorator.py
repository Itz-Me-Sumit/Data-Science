class Person:
    def __init__(self , name , phoneNo):
        self.__name = name
        self.__phoneNo = phoneNo
        
    @property
    def name(self):
        if not hasattr(self , "_Person__name"): # check karta hai ki object me koi perticular attribute hai ki nhi
            return "Name deleted"
        return self.__name
    
    @name.setter
    def name(self , new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        if self.__name == '':
            raise ValueError("Name doesn't exist")
        else:
            del self.__name

    @property
    def phone_no(self):
        if not hasattr(self , "_Person__phoneNo"):
            return "Number Deleted"
        return self.__phoneNo

    @phone_no.setter
    def phone_no(self , new_phone_no):
        self.__phoneNo = new_phone_no
    
    @phone_no.deleter
    def phone_no(self):
        if not hasattr(self , "_Person__phoneNo"):
            return "Phone Number Doesn't exist"
        del self.__phoneNo

person = Person("Sumit")

# Getter
print(person.name)

# Setter
person.name = "Shivam"
print(person.name)

# Deleter
del person.name
print(person.name)

person.name ="Sumit"
print(person.name)