#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


def fetch_hbtn_status(url):
    """
    Fetches the specified URL using the requests
    package and displays the response
    """
    try:
        response = requests.get(url)
        response_type = str(type(response.text))
        response_content = response.text
        print("Body response:")
        print("\t- type:", response_type)
        print("\t- content:", response_content)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_hbtn_status(url)
