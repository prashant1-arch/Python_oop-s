# Abstraction-
from abc import ABC, abstractmethod
class Bankapp(ABC):
    def database(self):
        print("Database connected")
    @abstractmethod
    def security(self):
        pass
    
class MobileApp(Bankapp):
    def mobile_login(self):
        print("Mobile login successful")
    def security(self):
        print("Mobile App security")
        
        
        
# Object
mob = MobileApp()
mob.database()
mob.mobile_login()