#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sI "$1" | grep -q "HTTP/1.1 200 OK" && curl -s "$1" || true
