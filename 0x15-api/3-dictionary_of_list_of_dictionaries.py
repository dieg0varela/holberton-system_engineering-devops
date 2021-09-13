#!/usr/bin/python3
''' API Module task 0'''
import json
import requests
from sys import argv
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "todos")
    jsonRes = response.json()
    filename = "todo_all_employees.json"
    resu = {}
    dicti = {
        "task": "",
        "completed": "",
        "username": ""
    }
    for data in jsonRes:
        userid = data.get('userId')
        resu[str(userid)] = []
    for data in jsonRes:
        userId = data.get('userId')
        user = requests.get(url + "users/" + str(userId)).json()
        uname = user.get('username')
        dicti['task'] = data.get('title')
        dicti['completed'] = data.get('completed')
        dicti['username'] = uname
        resu[str(userId)].append(dicti)
    with open(filename, "w") as f:
        f.write(json.dumps(resu))
    f.closed
    print(resu)
