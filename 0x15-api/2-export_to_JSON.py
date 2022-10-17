#!/usr/bin/python3
'''
    a python script that use rest api for a given employee
    and exports to json
'''

import json
import requests
import sys

if __name__ == '__main__':
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1]))
    user = user.json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(sys.argv[1]))
    todo = todo.json()
    username = user.get('username')
    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    jsonobj = {}
    jsonobj[sys.argv[1]] = tasks
    with open("{}.json".format(sys.argv[1]), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
