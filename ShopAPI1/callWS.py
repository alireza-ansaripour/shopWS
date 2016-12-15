import requests
import json
from Interfaces import Response

__author__ = 'mahshid'

url = "http://127.0.0.1:8000/product/"


def callWS(method, params):
    r = requests.post(url + method, data=params)
    j = json.loads(r.text)
    if method == 'menu':
        c1 = Response(j, r.status_code)
    else:
        c1 = Response(j['data'], r.status_code)
    return c1
