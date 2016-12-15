import json
from django.http import HttpResponse
from ShopController.handle import *

__author__ = 'mahshid'


def home(request):
    list = request.POST.get("names" , None)
    list = json.loads(list)
    print("list" , list)
    handle = Handle()
    # list = []
    # list.append("kala1")
    # list.append("kala2")
    res = handle.find(list)
    return HttpResponse(res)
