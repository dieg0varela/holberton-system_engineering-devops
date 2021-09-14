#!/usr/bin/python3
''' API Module task 0'''
import json
import requests
from sys import argv
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "users")
    jsonRes = response.json()
    filename = "todo_all_employees.json"
    resu = {}
    for data in jsonRes:
        lista = []
        userid = data.get('id')
        uname = data.get('username')
        tasks = requests.get(url + "todos?userid=/" + str(userid)).json()
        for task in tasks:
            dicti = {}
            dicti['task'] = task.get('title')
            dicti['completed'] = task.get('completed')
            dicti['username'] = uname
            lista.append(dicti)
        resu[str(userid)] = lista
    with open(filename, "w") as f:
        f.write(json.dumps(resu))
    f.closed
