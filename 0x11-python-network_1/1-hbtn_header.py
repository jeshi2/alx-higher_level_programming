#!/usr/bin/python3
"""
Python script that takes in a URL, sends a
request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id header from the URL's response
    """
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader("X-Request-Id")
            return x_request_id
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = fetch_x_request_id(url)

    if x_request_id:
        print(x_request_id)
