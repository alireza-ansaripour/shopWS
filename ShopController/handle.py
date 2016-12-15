from ShopAPI1.Shop import ShopAPI1
from ShopAPI2.Shop import ShopAPI2

__author__ = 'mahshid'

class Handle:
    def __init__(self):
        self.shop1 = ShopAPI1()
        self.shop2 = ShopAPI2()

    def find(self , list):
        res1 = self.shop1.menu(list)
        res2 = self.shop2.menu(list)
        return (res1, res2)
