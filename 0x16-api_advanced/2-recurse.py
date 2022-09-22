#!/usr/bin/python3
""" task 2 reddit """

import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {"User-Agent": "benjaxd"}
    url = "https://www.reddit.com/r/{}/hot.json?after={}"\
        .format(subreddit, after)
    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
        for children in request.json().get("data").get("children"):
            hot_list.append(children.get("data").get("title"))

        after = request.json().get("data").get("after")
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)

    else:
        return None
