#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys


def get_github_user_id(username, personal_access_token):
    """
    Uses Basic Authentication to access the
    GitHub API and fetches the user ID.
    """
    try:
        url = 'https://api.github.com/user'
        response = requests.get(url, auth=(username, personal_access_token))
        if response.status_code == 200:
            user_data = response.json()
            return str(user_data.get('id'))
        else:
            return None
    except Exception as e:
        return None


if __name__ == "__main__":
    username = sys.argv[1]
    personal_access_token = sys.argv[2]
    github_user_id = get_github_user_id(username, personal_access_token)
    print(github_user_id)
