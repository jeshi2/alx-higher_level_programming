#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to
the URL and displays the body of the response.
"""
import requests
import sys


def fetch_url_content(url):
    """
    Sends a request to the specified URL and
    displays the body of the response
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        print(content)
    except requests.exceptions.RequestException as e:
        if hasattr(e.response, 'status_code'):
            print(f"Error code: {e.response.status_code}")
        else:
            print(e)


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else 'http://0.0.0.0:5000'
    fetch_url_content(url)
