#!/usr/bin/python3
""" apiarda """

import json
import requests
from sys import argv

if __name__ == '__main__':
    path = "https://jsonplaceholder.typicode.com/"
    users = requests.get(path + "users/{}".format(argv[1])).json()
    all = requests.get(path + "todos/", params={"userId":argv[1]}).json()
        
    res = {}
    with open('{}.json'.format(str(argv[1])), mode='w') as f:
        json.dump(res, f)
