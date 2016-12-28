import json
from ShopAPI2.Interfaces import Order, Product
from ShopAPI2.callWS import callWS

__author__ = 'mahshid'


class ShopAPI2:
    def add(self, name, price):
        data = {'name': name, 'price': price}
        response = callWS('add', data)
        return response

    def buy(self , list ):
        json_list = json.dumps(list)
        data = {'list':json_list}
        response = callWS('buy', data)
        return response

    def increase_amount(self , id , amount):
        data = {'id': id, 'amount': amount}
        response = callWS('increase' , data)
        return response

    def menu(self , list ):
        json_list = json.dumps(list)
        data = {'names':json_list}
        response = callWS('menu', data)
        if response.code == 406:
            return []
        list = []
        for i in response.data:
            if Product(i["name"] , i["price"] , i["amount"]).amount != None :
                list.append(Product(i["name"] , i["price"] , i["amount"]))
        return list
