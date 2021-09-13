#!/usr/bin/python3
''' API Module task 0'''
import requests
from sys import argv
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "todos?userId=" + argv[1])
    json = response.json()
    userId = json[0].get('userId')
    user = requests.get(url + "users/" + str(userId)).json()
    name = user.get('name')
    task_done = 0
    total_task = len(json)
    for data in json:
        if data.get("completed"):
            task_done += 1
    print("Employee {} is done with tasks({:d}/{:d}):".format(name, task_done,
                                                              total_task))
    for data in json:
        if data.get("completed"):
            print("\t " + data.get("title"))
