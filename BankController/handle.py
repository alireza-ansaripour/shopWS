from BankAPI1.API import BankAPI1
from BankAPI2.API import BankAPI2

__author__ = 'alireza'


class BankHandler:

    def __init__(self):
        self.api1 = BankAPI1()
        self.api2 = BankAPI2()

    def get_user_balance(self, id, password):
        response1 = self.api1.withdraw(id, password, 0)
        response2 = self.api2.withdraw(id, password, 0)
        if response2.code == 406 and response1.code == 406:
            raise Exception(response1.details)
        if response2.code == 406:
            return response1.details
        if response1.code == 406:
            return response2.details
        return response1.details, response2.details

    def buy(self, id, password, amount):
        response1 = self.api1.withdraw(id, password, 0)
        response2 = self.api2.withdraw(id, password, 0)
        amount1 = 0
        amount2 = 0
        if response1.code == 200:
            amount1 = response1.details
        if response2.code == 200:
            amount2 = response2.details
        if response1.code == 406 and response2.code == 406:
            raise Exception(response1.details)

        if amount1 > amount:
            return self.api1.withdraw(id, password, amount)
        if amount2 > amount:
            return self.api2.withdraw(id, password, amount)
        if (amount1 + amount2) > amount:
            self.api1.withdraw(id, password, amount1)
            self.api2.withdraw(id, password, amount - amount1)
            return amount
        return Exception("Amount is not enough")