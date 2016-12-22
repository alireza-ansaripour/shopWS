from BankAPI2.callWS import callWS

__author__ = 'alireza'


class BankAPI2:
    def createAccount(self, name, password):
        data = {'name': name, 'password': password}
        response = callWS('create', data)
        return response

    def changePassword(self, id, current_password, new_password):
        data = {'id': id, 'current_password': current_password, 'new_password': new_password}
        response = callWS('changePassword', data)
        return response

    def withdraw(self, id, password, amount):
        data = {'id': id, 'password': password, 'amount': amount}
        response = callWS('withdraw', data)
        return response

    def deposit(self, id, password, amount):
        data = {'id': id, 'password': password, 'amount': amount}
        response = callWS('deposit', data)
        return response

