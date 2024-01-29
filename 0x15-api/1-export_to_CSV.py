#!/usr/bin/python3
"""
A Script that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
exporting data in the CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    todos_req = requests.get('{}users/{}/todos'.format(base_url, user_id))
    user_req = requests.get('{}users/{}'.format(base_url, user_id))

    json_req = todos_req.json()
    username = user_req.json()['username']

    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in json_req]
