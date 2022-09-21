#!/usr/bin/python3
""" task 1 reddit"""

import json
import requests


def top_ten(subreddit):
    user = {"User-Agent": "benjaxd"}
    request = requests.get("https://www.reddit.com/r/{}/hot/.json"
                           .format(subreddit), headers=user)

    if request.status_code == 200:
        for i in request.json().get("data").get("children")[:10]:
                print(i.get("data").get("title"))
    else:
        print(None)
