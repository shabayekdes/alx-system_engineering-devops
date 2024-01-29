#!/usr/bin/python3
"""
A Script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'
    todos_req = requests.get('{}users/{}/todos'.format(base_url, argv[1]))
    user_req = requests.get('{}users/{}'.format(base_url, argv[1]))

    json_req = todos_req.json()
    name = user_req.json()['name']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
