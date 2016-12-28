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

    try:
        product_list = shop.find_products(list)
    except Exception as e:
        return HttpResponse(e)

    total_price = 0
    for item in product_list:
        total_price += int(item["price"])

    try:
        if shop.isDepositEnough(total_price , username):
            shop.shopController.update_database(product_list)
            return HttpResponse(shop.bankController.buy(username,password1,password2,total_price))
        else:
            return HttpResponse("Your bank account is not enough")
    except Exception as e:
        return HttpResponse(e)


    return HttpResponse(product_list)
