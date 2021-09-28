#!/usr/bin/python3
'''Module to restrive number of subscribers of a subreddit'''
import requests


def number_of_subscribers(subreddit):
    '''Function to get data from reddit api'''
    url = "https://reddit.com/r/"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)\
                              Gecko/20100101 Firefox/15.0.1"}
    response = requests.get(url + subreddit + "/about.json",
                            headers=headers)
    try:
        ret = response.json()['data'].get('subscribers')
        return(ret)
    except:
        return (0)
