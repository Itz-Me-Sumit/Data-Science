class Atm:

    __counter = 1 # Static Variable(Subject to Class not to Object)

    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.cid = Atm.__counter # Static Variable called by Class_Name
        Atm.__counter+=1
    
    def Menu(self):
        while True:
            command = int(input("""
                Select Following options
                Press 1 to Create a pin
                press 2 to Change pin
                press 3 to Check balance
                press 4 to withdraw
                press 5 to Debit Amount
                press 6 to exit
            """))
            if command == 1:
                self.CreatePin()
            elif command == 2:
                self.ChangePin()
            elif command == 3:
                self.CheckBalance()
            elif command == 4:
                self.Withdraw()
            elif command == 5:
                self.deposit()
            elif command == 6:
                break
            else:
                print("Invalid Option")

    @staticmethod
    def get_counter():
        return Atm.__counter

    def is_pin_set(self):
        if self.__pin == '':
            print("Please Create Pin First")
            return False
        return True

    def CreatePin(self):
        pin = input("Enter Your Pin: ")
        self.__pin = pin
        print("Pin Created Successfully")
        

    def ChangePin(self):
        if not self.is_pin_set():
            return
        old_pin = input("Enter Old Pin: ")
        if old_pin == self.__pin:
            new_pin = input("Enter New Pin: ")
            self.__pin = new_pin
            print("Pin Successfuly changed")
        else:
            print("Wrong Pin")

    def CheckBalance(self):
        if not self.is_pin_set():
            return
        entered_pin = input("Enter Your Pin: ")
        if entered_pin == self.__pin:
            print("Your Balance: ",self.__balance)
        else:
            print("Wrong Pin")

    def deposit(self):
        if not self.is_pin_set():
            return
        entered_pin = input("Enter Your pin: ")
        if entered_pin == self.__pin:
            amount = int(input("Enter Amount: "))
            if amount>0:
                self.__balance = self.__balance + amount
                print("Amount Deposited Successfully")
            else:
                print("You Entered Amount less then or equal to 0")
        else:
            print("Wrong pin")

    def Withdraw(self):
        if not self.is_pin_set():
            return
        entered_pin = input("Enter Your Pin: ")
        if entered_pin == self.__pin:
            amount = int(input("Enter Amount: "))
            if amount<=self.__balance:
                self.__balance -= amount
                print(amount ," Amount Withdraw get Successfull")
            else:
                print("Insufficient Balance")
        else:
            print("Wrong Pin")

SumitAccount = Atm()
print(SumitAccount.cid)
print(Atm._Atm__counter)
SumitAccount.Menu()