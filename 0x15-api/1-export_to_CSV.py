#!/usr/bin/python3
'''Script uses a REST API for todo lists of employees, for a given employee ID'''

import requests
import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = f"{baseUrl}/{employeeId}"

    try:

        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        username = response.json().get('username')


        todoUrl = f"{url}/todos"
        response = requests.get(todoUrl)
        response.raise_for_status()  # Raise an exception for HTTP errors
        tasks = response.json()

 
        with open(f'{employeeId}.csv', 'w') as file:
            for task in tasks:
                file.write('"{}","{}","{}","{}"\n'.format(
                    employeeId, username, task.get('completed'), task.get('title')))

        print(f"Data exported to '{employeeId}.csv' successfully.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
