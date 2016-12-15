__author__ = 'mahshid'


class Response:
    def __init__(self, data, code):
        self.data = data
        self.code = code


class Order:
    def __init__(self , name , amount):
        self.name = name
        self.amount = amount

class Product:
    def __init__(self , name , price , amount):
        self.amount = amount
        self.name = name
        self.price = price