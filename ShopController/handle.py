from ShopAPI1.Shop import ShopAPI

__author__ = 'mahshid'

class Handle:
    def __init__(self):
        self.shop = ShopAPI()

    def find(self , list):
        res = self.shop.menu(list)
        return (res)
