#!/usr/bin/python3
''' API Module task 0'''
import requests
from sys import argv
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "todos?userId=" + argv[1])
    json = response.json()
    userId = json[0].get('userId')
    total_task = len(json)
    user = requests.get(url + "users/" + str(userId)).json()
    uname = user.get('username')
    filename = str(userId) + ".csv"
    with open(filename, "w") as f:
        for data in json:
            res = '"{:d}","{}","{}","{}"\n'.format(userId, uname,
                                                   data.get('completed'),
                                                   data.get('title'))
            f.write(res)
    f.closed
