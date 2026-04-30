class Phone:
    def __init__(self):
        pass
    def buy(self):
        print("Buying A Phone")

class Smartphone(Phone):
    def buy(self):
        print("Buying A Smartphone")

sp = Smartphone()
sp.buy()