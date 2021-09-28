#!/usr/bin/python3
'''Module to restrive top 10 hot posts of a subreddit'''
import requests


def top_ten(subreddit):
    '''Function to get top 10 hot post from api'''
    url = "https://reddit.com/r/"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)\
                              Gecko/20100101 Firefox/15.0.1"}
    response = requests.get(url + subreddit + "/hot.json",
                            headers=headers)
    try:
        ret = response.json()['data']
        for obj in ret['children']:
            print(obj['data']['title'])
    except:
        print("None")
