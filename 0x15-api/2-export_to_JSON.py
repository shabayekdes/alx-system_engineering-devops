#!/usr/bin/python3
"""
A sript that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the JSON format.
"""

import requests
import json
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    todos_req = requests.get('{}users/{}/todos'.format(base_url, user_id))
    user_req = requests.get('{}users/{}'.format(base_url, user_id))

    json_req = todos_req.json()
    username = user_req.json()['username']

    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": username,
            })
    updateUser[user_id] = totalTasks

    file_Json = user_id + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
