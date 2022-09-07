#!/usr/bin/python3
""" apiarda """

import json
import requests

if __name__ == '__main__':
    path = "https://jsonplaceholder.typicode.com/"
    users = requests.get(path + "users").json()
    all = requests.get(path + "todos").json()
    res = {}
    with open("todo_all_employees.json", mode='w') as f:
        json.dump(res, f)
