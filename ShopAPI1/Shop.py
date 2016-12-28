import json
from ShopAPI1.Interfaces import Order, Product
from ShopAPI1.callWS import callWS

__author__ = 'mahshid'


class ShopAPI1:
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
        list = []
        if response.code == 406:
            return list
        for i in response.data:
            if Product(i["name"] , i["price"] , i["amount"]).amount != None :
                list.append(Product(i["name"] , i["price"] , i["amount"]))
        return list

'''
shop = ShopAPI()
order1 = Order("mahshid" , 2)
list = []
list.append(order1.__dict__)

list2 = []
list2.append("mahshid")
list2.append("test")
list2.append("test2")

# res = shop.buy(list)
res2 = shop.menu(list2)

for i in res2:
    print(i.name , i.price , i.amount)
'''