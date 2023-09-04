#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email
as a parameter, and finally displays the body of the response.
"""
import requests
import sys


def post_email(url, email):
    """
    Sends a POST request to the specified URL with the
    email as a parameter
    """
    try:
        data = {'email': email}
        response = requests.post(url, data=data)
        # print("Your email is:", email)
        print(response.text)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = sys.argv[1] if len(
        sys.argv) > 1 else 'http://0.0.0.0:5000/post_email'
    email = sys.argv[2] if len(sys.argv) > 2 else 'hr@holbertonschool.com'
    post_email(url, email)
