#!/bin/bash
# Bash script sends a request to a URL and displays the size of the response body in byte
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
