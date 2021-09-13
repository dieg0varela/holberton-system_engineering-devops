#!/usr/bin/python3
''' API Module task 0'''
import requests
from sys import argv
import json
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "todos?userId=" + argv[1])
    jsonRes = response.json()
    userId = jsonRes[0].get('userId')
    total_task = len(jsonRes)
    user = requests.get(url + "users/" + str(userId)).json()
    uname = user.get('username')
    filename = str(userId) + ".json"
    resu = {str(userId): []}
    for data in jsonRes:
        dicti = {
            "task": "",
            "completed": "",
            "username": ""
        }
        dicti['task'] = data.get('title')
        dicti['completed'] = data.get('completed')
        dicti['username'] = uname
        resu[str(userId)].append(dicti)
    print(resu)
