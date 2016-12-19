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
        shopList = []
        return (res1, res2)

    def getMinimumPrice(self , list1 , list2 , name , amount):
        item1 = None
        for item in list1:
            if item.name == name:
                item1 = item

        item2 = None
        for item in list2:
            if item.name == name:
                item2 = item
        '''
        if item1!=None and item2!=None:
            if item1.price < item2.price:
                if item1.amount
        '''
handler = Handle()
list = handler.find(["table"])
list1 = list[0]
list2 = list[1]
print(list1)
print(list2)