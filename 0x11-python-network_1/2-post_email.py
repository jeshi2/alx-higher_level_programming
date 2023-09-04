#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the e
mail as a parameter, and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter
    """
    try:
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # print("Your email is:", email)
    post_email(url, email)
