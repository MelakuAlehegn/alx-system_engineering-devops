#!/usr/bin/python3
'''
    a python script that use rest api for a given employee
    and returns for his/her to do status
'''

import requests
import sys

if __name__ == '__main__':
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1]))
    user = user.json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(sys.argv[1]))
    todo = todo.json()
    completed_tasks = []
    for i in todo:
        if i.get('completed') is True:
            completed_tasks.append(i.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed_tasks), len(todo)))
    for i in completed_tasks:
        print('\t {}'.format(i))
