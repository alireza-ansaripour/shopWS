import requests
import json
from BankAPI1.Interfaces import Response

__author__ = 'alireza'

url = 'http://127.0.0.1:8002/account/'


def callWS(method, params):
    r = requests.post(url + method, data=params)
    data = json.loads(r.text)
    response = Response(data['detail'], r.status_code)
    return response

res = callWS("create", {'name': "ali", 'password': '123'})
