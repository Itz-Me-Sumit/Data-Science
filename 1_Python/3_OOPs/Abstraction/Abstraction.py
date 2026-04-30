from abc import ABC , abstractmethod

class Bank(ABC):
    def database(self):
        print("Connected to database")
    
    @abstractmethod
    def security(self):
        pass

class MobileApp(Bank):
    def mobile_login():
        print("Login")
    def security(self):
        print("Security Assured")

mob = MobileApp()
mob.security()