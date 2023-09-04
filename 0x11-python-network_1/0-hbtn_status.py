#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/statu
"""
import urllib.request


def fetch_and_display_status(url):
    """
    fetch content
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            utf8_content = content.decode('utf-8')

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", utf8_content)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_and_display_status(url)
