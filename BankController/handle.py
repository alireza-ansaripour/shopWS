from BankAPI1.API import BankAPI1
from BankAPI2.API import BankAPI2

__author__ = 'alireza'


class BankHandler:

    def __init__(self):
        self.api1 = BankAPI1()
        self.api2 = BankAPI2()

    def get_user_balance(self, name):
        response1 = self.api1.getBalance(name)
        response2 = self.api2.getBalance(name)
        if response2.code == 406 and response1.code == 406:
            raise Exception(response1.details)
        if response2.code == 406:
            return float(response1.details), 0
        if response1.code == 406:
            return 0, float(response2.details)
        return float(response1.details), float(response2.details)

    def buy(self, name, password1, password2, amount):
        amount1, amount2 = self.get_user_balance(name)
        res1 = self.api1.getId(name)
        res2 = self.api2.getId(name)
        id1 = None
        id2 = None
        if res1.code == 200:
            id1 = int(res1.details)
        if res2.code == 200:
            id2 = int(res2.details)

        if id1 is not None and password1 is not None and (amount1 > amount):
            res1 = self.api1.withdraw(id1, password1, amount)
            if res1.code == 406:
                raise Exception(res1.details)
            return res1.details

        if id2 is not None and password2 is not None and (amount2 > amount):
            res = self.api2.withdraw(id2, password2, amount)
            if res.code == 406:
                    raise Exception(res.details)
            return res.details

        if (amount1 + amount2) > amount:
            res1 = self.api1.withdraw(id1, password1, amount1)
            res2 = self.api2.withdraw(id2, password2, amount - amount1)
            return res1, res2
        return Exception("Amount is not enough")