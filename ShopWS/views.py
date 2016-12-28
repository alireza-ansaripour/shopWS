import json
from django.http import HttpResponse
from ShopWS.models import *

__author__ = 'mahshid'


def home(request):
    username = request.POST.get("user" , None)
    list = request.POST.get("names" , None)
    password1 = request.POST.get("password1" , None)
    password2 = request.POST.get("password2" , None)

    list = json.loads(list)

    shop = Shop()

    product_list = shop.find_products(list)

    total_price = 0
    for item in product_list:
        total_price += int(item["price"])

    # print("tital price : " , total_price)
    try:
        if shop.isDepositEnough(total_price , username):
            return HttpResponse(shop.bankController.buy(username,password1,password2,total_price))
        else:
            return HttpResponse("Your bank account is not enough")
    except Exception as e:
        return HttpResponse(e)
    # print("res:" , res)
    return HttpResponse(product_list)
