from BankAPI1.API import BankAPI

__author__ = 'alireza'


class BankHandler:

    def __init__(self):
        self.api = BankAPI()

    def get_user_balance(self, id, password):
        return self.api.withdraw(id, password, 0)

    def buy(self, id, password, amount):
        return self.api.withdraw(id, password, amount)

handler = BankHandler()
print(handler.get_user_balance(335, "32").details)