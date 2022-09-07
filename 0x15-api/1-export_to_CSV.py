#!/usr/bin/python3
""" apiarda """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    path = "https://jsonplaceholder.typicode.com/"
    users = requests.get(path + "users/{}".format(argv[1])).json()
    all = requests.get(path + "todos/", params={"userId": argv[1]}).json()

with open('{}.csv'.format(str(argv[1])), mode='w') as f:
    writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)

    for i in all:
        writer.writerow([argv[1], users["username"],
                        i["completed"], i["title"]])
