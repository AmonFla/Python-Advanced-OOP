
class AccountError(Exception):
    pass

class SingleBankAccount():

    def __init__(self, number) -> None:
        self.__number = number
        self.__balance = 0
    
    @property
    def account_number(self):
        return self.__number
    
    @account_number.setter
    def account_number(self,number):
        raise AccountError('Do not change Account Number')
    
    @account_number.deleter
    def account_number(self):
        if self.balance > 0:
            raise AccountError('You hace some money at the account')
        self.__number = None
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise AccountError('Invalid balance amount')
        self.__balance = amount
    
        
    def operation(self,amount):
        if abs(amount) > 100000:
            print("Operation over 100000")
        self.balance += amount

account = SingleBankAccount("123")

account.balance = 1000
# account.balance = -200
# account.account_number = 234
account.operation(1000000)
# del account.account_number
account.operation(-account.balance)
del account.account_number
print(account.account_number)