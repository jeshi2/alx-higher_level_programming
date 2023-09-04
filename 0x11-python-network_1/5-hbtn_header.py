#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the value of the variable
X-Request-Id in the response header
"""
import requests
import sys


def get_x_request_id(url):
    """
    Sends a request to the specified URL and displays
    the value of the X-Request-Id header.
    """
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://alx-intranet.hbtn.io'
    get_x_request_id(url)
