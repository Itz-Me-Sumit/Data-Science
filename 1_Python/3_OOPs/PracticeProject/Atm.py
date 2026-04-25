class Atm:

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.Menu()
    
    def Menu(self):
        while True:
            command = int(input("""
                Select Following options
                Press 1 to Create a pin
                press 2 to Change pin
                peess 3 to Check balance
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
                self.debit()
            elif command == 6:
                exit()
            else:
                print("Invalid Option")

    def is_pin_set(self):
        if self.pin == '':
            print("Please Create Pin First")
            return False
        return True

    def CreatePin(self):
        pin = input("Enter Your Pin: ")
        self.pin = pin
        print("Pin Created Successfully")
        

    def ChangePin(self):
        if not self.is_pin_set():
            return
        old_pin = input("Enter Old Pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter New Pin: ")
            self.pin = new_pin
            print("Pin Successfuly changed")
        else:
            print("Wrong Pin")

    def CheckBalance(self):
        if not self.is_pin_set():
            return
        entered_pin = input("Enter Your Pin: ")
        if entered_pin == self.pin:
            print("Your Balance: ",self.balance)
        else:
            print("Wrong Pin")

    def debit(self):
        if not self.is_pin_set():
            return
        entered_pin = input("Enter Your pin: ")
        if entered_pin == self.pin:
            amount = int(input("Enter Anount: "))
            if amount>0:
                self.balance = self.balance + amount
                print("Amount Debited Successfuly")
            else:
                print("You Entered Amount less then or equal to 0")
        else:
            print("Wrong pin")

    def Withdraw(self):
        if not self.is_pin_set():
            return
        entered_pin = input("Enter Your Pin: ")
        if entered_pin == self.pin:
            amount = int(input("Enter Amount: "))
            if amount<=self.balance:
                self.balance = self.balance-amount
                print(amount ," Amount Withdraw get Successfull")
            else:
                print("Insufficient Balance")
        else:
            print("Wrong Pin")

SumitAccount = Atm()