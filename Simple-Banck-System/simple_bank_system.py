'''
    Simple Bank System
            - Create Client (name, age)
            - deposit
            - withdraw
            - show details 
            - show balance 

'''

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: '{self.name}'\nAge: {self.age}")


class Bank(User):
    def __init__(self, name, age, balance=0):
        super().__init__(name, age)
        self.balance = balance
        print(f"Welcome '{self.name}' created account successfully with balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Hello '{self.name}' Deposit balance accomplished successfully\nYour Current balance : {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Your balance does not allow you to withdraw this amount Balance = {self.balance}")
            return
        self.balance -= amount
        print(f"Hello '{self.name}' withdraw balance accomplished successfully\nYour Current balance : {self.balance}")
    
    def show_balance(self):
        print(f'Current Balance: {self.balance}')
    


client1 = Bank('Mohamed Samy', 24, 1500)
# client1.deposit(2000)
# client1.withdraw(5000)
# client1.withdraw(1500)
# client1.show_details()



