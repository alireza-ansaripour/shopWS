import requests
import json
from BankAPI1.Interfaces import Response

__author__ = 'alireza'

url = 'http://192.168.43.33:8001/account/'


def callWS(method, params):
    r = requests.post(url + method, data=params)
    data = json.loads(r.text)
    response = Response(data['detail'], r.status_code)
    return response