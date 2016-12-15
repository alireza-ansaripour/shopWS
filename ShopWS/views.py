from django.http import HttpResponse
from ShopAPI1.Shop import ShopAPI
from ShopController.handle import *

__author__ = 'mahshid'


def home(request , list):
    handle = Handle()
    list = []
    list.append("kala1")
    list.append("kala2")
    res = handle.find(list)
    return HttpResponse(res)
