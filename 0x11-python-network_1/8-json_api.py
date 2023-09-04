#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys


def search_user(letter):
    """
    Sends a POST request to the search_user endpoint with the letter
    """
    try:
        url = 'http://0.0.0.0:5000/search_user'
        data = {'q': letter}
        response = requests.post(url, data=data)
        response_json = response.json()

        if response_json:
            print("[{}] {}".format(response_json.get('id'),
                                   response_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
