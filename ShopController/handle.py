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
        price = 0
        item1_amount = 0
        item2_amount = 0
        item1 = None
        for item in list1:
            if item.name == name:
                item1 = item
                item1_amount = item1.amount
                break

        item2 = None
        for item in list2:
            if item.name == name:
                item2 = item
                item2_amount = item2.amount
                break

        #item1 and item2 is not None ( shop1 and shop2 has item with 'name')
        if item1!=None and item2!=None:
            if amount > (item2.amount + item1.amount):
                raise Exception("The Product Amount is Not Enough")

            if item1.price <= item2.price:
                if item1.amount >= amount :
                    price = amount * item1.price
                    item1.amount -= amount
                # If item1 and item2 amounts are more than amount
                elif (item2.amount + item1.amount) >= amount :
                    price = item1.amount * item1.price + (amount - item1.amount) * item2.price
                    item2.amount -= (amount-item1.amount)
                    item1.amount = 0
            elif item1.price > item2.price:

                if item2.amount >= amount :
                    price = amount * item2.price
                    item2.amount -= amount

                elif item1.amount >= (amount - item2.amount):
                    price = item2.amount * item2.price + (amount - item2.amount) * item1.price
                    item1.amount -= (amount - item2.amount)
                    item2.amount = 0
        #item1 is not None and item2 is None ( shop1 has not item with 'name' and shop2 has item with 'name' )
        elif item1!=None and item2 == None:
            if amount > item1.amount:
                raise Exception("The Product Amount is Not Enough")
            elif amount <= item1.amount :
                price = amount * item1.price
                item1.amount -= amount

        #item2 is not None and item1 is None ( shop2 has not item with 'name' and shop1 has item with 'name' )
        elif item1 == None and item2 != None:
            if amount > item2.amount :
                raise Exception("The Product Amount is Not Enough")
            elif amount <= item2.amount :
                price = amount * item2.price
                item2.amount -= amount
        #item2 is None and item1 is None
        elif item1 == None and item2 == None :
            raise Exception("The product doesn't exist")

        amount1 = 0
        amount2 = 0
        if item1 is not None:
            amount1 = item1.amount
        if item2 is not None:
            amount2 = item2.amount

        return (price, item1_amount - amount1, item2_amount - amount2 )

    def update_database(self,list):

        shop1_buy_list = []
        shop2_buy_list = []

        for item in list:
            shop1_buy_list.append({"name":item["name"],"amount":int(item["shop1"])})
            shop2_buy_list.append({"name":item["name"],"amount":int(item["shop2"])})

        res1 = self.shop1.buy(shop1_buy_list)
        res2 = self.shop2.buy(shop2_buy_list)

        # return (res1 , res2)
