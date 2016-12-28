from django.db import models
from BankController.handle import BankHandler
from ShopController.handle import Handle

__author__ = 'mahshid'

class Shop:
    bankController = BankHandler()
    shopController = Handle()

    def find_products(self,list):
        name = []
        amount = []

        name = list.keys()
        amount = list.values()

        names = []
        for item in name:
            names.append(item)

        amounts = []
        for item in amount:
            amounts.append(item)

        list1,list2 = self.shopController.find(names)

        order_list = []
        for x in range(0,len(name)):
            price ,shop1_amount , shop2_amount = self.shopController.getMinimumPrice(list1 , list2 , names[x] , amounts[x])
            order_list.append({"name" : names[x] , "price" : price , "shop1" : shop1_amount , "shop2" : shop2_amount})

        return order_list

    def isDepositEnough(self,price,name):
        bank1 , bank2 = self.bankController.get_user_balance(name)
        if bank1 + bank2 >= int(price):
            return True
        return False

