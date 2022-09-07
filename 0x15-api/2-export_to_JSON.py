#!/usr/bin/python3
""" apiarda """

import json
import requests
from sys import argv

if __name__ == '__main__':
    path = "https://jsonplaceholder.typicode.com/"
    users = requests.get(path + "users/{}".format(argv[1])).json()
    all = requests.get(path + "todos/", params={"userId": argv[1]}).json()

    res = {}
    t = []
    for task in all:
        td = {}
        td["task"] = task["title"]
        td["completed"] = task["completed"]
        td["username"] = users["username"]
        t.append(td)

    res[argv[1]] = t
    with open("{}.json".format(str(argv[1])), mode='w') as f:
        json.dump(res, f)
