#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    """
    Sends a request to the specified URL, handles HTTP errors
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    fetch_url_content(url)
