#!/usr/bin/python3
''' API Module task 0'''
import requests
from sys import argv
import json
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "todos?userId=" + argv[1])
    json = response.json()
    userId = json[0].get('userId')
    total_task = len(json)
    user = requests.get(url + "users/" + str(userId)).json()
    uname = user.get('username')
    filename = str(userId) + ".json"
    lista = []
    for data in json:
        dicti = {}
        dicti['task'] = data.get('title')
        dicti['completed'] = data.get('completed')
        dicti['username'] = uname
        lista.append(dicti)
    with open(filename, "w") as f:
        res = {}
        res[str(userId)] = lista
        f.write(str(res))
    f.closed
