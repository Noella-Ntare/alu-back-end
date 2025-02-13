#!/usr/bin/python3
"""Module to fetch employee tasks and save them as JSON"""

import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]  # Read user ID from command-line argument
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user and todos data
    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    if not user_info or not todos_info:
        print(f"Error: User ID {employee_id} not found")
        sys.exit(1)

    employee_username = user_info.get("username", "Unknown")

    # Create the expected format
    todos_info_sorted = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_username
        }
        for task in todos_info
    ]

    user_dict = {str(employee_id): todos_info_sorted}

    # Write to file with proper JSON formatting
    filename = f"{employee_id}.json"
    with open(filename, "w") as file:
        json.dump(user_dict, file, indent=4)

    print(f"Data saved successfully to {filename}")
