class Customer:
    def __init__(self , name , gender , address):
        self.name = name
        self.gender = gender
        self.address = address
    def print_address(self):
        print("Address:",self.address.state , self.address.getCity() , self.address.pin)
    def editProfile(self ,new_name , new_state , new_city , new_pin ):
        self.name = new_name
        self.address.editAddress(new_state , new_city , new_pin)

class Address:
    def __init__(self , state , city , pin ):
        self.state = state
        self.__city = city
        self.pin = pin
    def getCity(self):
        return self.__city
    def editAddress(self , new_state , new_city , new_pin):
        self.state = new_state
        self.__city = new_city
        self.pin = new_pin

add1 = Address("Bihar" , "Begusarai" , "851135")
cust1 = Customer("sumit" , "male" , add1)

cust1.print_address()
cust1.editProfile("Shivam" , "UP" , "Banaras" , "123123")
cust1.print_address()
