#!/usr/bin/python3
""" task 0 """
import requests


def number_of_subscribers(subreddit):
    user = {"User-Agent": "benjaxd"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user)

    if request.status_code != 200:
        return 0
    else:
        return request.json().get("data").get("subscribers")
