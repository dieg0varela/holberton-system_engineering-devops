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
        userid = data.get('id')
        uname = data.get('username')
        resu[str(userid)] = []
        tasks = requests.get(url + "todos?userid=/" + str(userid)).json()
        for task in tasks:
            dicti = {}
            dicti['task'] = task.get('title')
            dicti['completed'] = task.get('completed')
            dicti['username'] = uname
            resu[str(userid)].append(dicti)
    with open(filename, "w") as f:
        f.write(json.dumps(resu))
    f.closed
