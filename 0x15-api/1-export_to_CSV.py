import csv
import requests
import sys

if __name__ == '__main__':
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1]))
    user = user.json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(sys.argv[1]))
    todo = todo.json()
    with open("{}.csv".format(sys.argv[1]), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            taskwriter.writerow([int(sys.argv[1]), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
