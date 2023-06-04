# Write a Python class called BankAccount with methods for depositing, withdrawing,and checking the account balance.
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        
        '''
        Agrega la cantidad especificada al saldo de la cuenta.
        '''

        self.balance += amount

    def withdraw(self, amount):
        '''
        Verifica si el saldo de la cuenta es suficiente para realizar el retiro. 
        Si es así, resta la cantidad especificada al saldo utilizando.
        '''
        if self.balance >= amount:
            self.balance -= amount

    def check_balance(self):
        '''
        Devuelve el valor del atributo balance, que representa el saldo de la cuenta.
        '''
        return self.balance


account = BankAccount()
print("Account balance:", account.check_balance()) 
account.deposit(1000)
print("Account balance:", account.check_balance())  
account.withdraw(50)
print("Account balance:", account.check_balance()) 
account.withdraw(200)
print("Account balance:", account.check_balance())  