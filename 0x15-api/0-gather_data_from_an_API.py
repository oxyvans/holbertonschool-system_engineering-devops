#!/usr/bin/python3
""" apiarda """

import requests
from sys import argv

if __name__ == '__main__':
    path = "https://jsonplaceholder.typicode.com/"
    users = requests.get(path + "users/{}".format(argv[1])).json()
    all = requests.get(path + "todos/", params={"userId":argv[1]}).json()

    c = 0
    t = 0
    complit = []
    for w in all:
        if w['completed'] is True:
            c += 1
            t += 1
            complit.append(w["title"])
        else:
            t += 1

    print("Employee " + users["name"] + " is done with tasks({}/{}):".format(c,t))
    for task in complit:
        print("\t {}".format(task))