# Python Network 1 Scripts for Web Requests and GitHub API

This repository contains a collection of Python scripts for making web requests and interacting with the GitHub API. Each script addresses a specific task and demonstrates how to perform various network-related operations using Python.

## Table of Contents

1. [Requirements](#requirements)
2. [Scripts](#scripts)
   - [1-hbtn_status.py](#1-hbtn_statuspy)
   - [2-post_email.py](#2-post_emailpy)
   - [3-error_code.py](#3-error_codepy)
   - [4-hbtn_status.py](#4-hbtn_statuspy)
   - [5-hbtn_header.py](#5-hbtn_headerpy)
   - [6-post_email.py](#6-post_emailpy)
   - [7-error_code.py](#7-error_codepy)
   - [8-json_api.py](#8-json_apipy)
   - [10-my_github.py](#10-my_githubpy)
   - [100-github_commits.py](#100-github_commitspy)

## Requirements

To run these scripts, you need to have Python installed on your system. Additionally, some scripts may require specific packages like `requests`.

You can install the required packages using `pip`:

```bash
pip install requests
```

## Scripts

### 1-hbtn_status.py

This script fetches the status of the website https://alx-intranet.hbtn.io/status using the `urllib` package and displays information about the response, including its content type and content.

Usage:

```bash
./1-hbtn_status.py
```

### 2-post_email.py

This script takes a URL and an email address as arguments, sends a POST request to the URL with the email as a parameter, and displays the response. It uses the `urllib` package for making the request.

Usage:

```bash
./2-post_email.py <URL> <email>
```

### 3-error_code.py

This script takes a URL as an argument, sends a request to the URL, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints an error message.

Usage:

```bash
./3-error_code.py <URL>
```

### 4-hbtn_status.py

This script fetches the status of the website https://alx-intranet.hbtn.io/status using the `requests` package and displays information about the response, including its content type and content.

Usage:

```bash
./4-hbtn_status.py
```

### 5-hbtn_header.py

This script takes a URL as an argument, sends a request to the URL, and displays the value of the `X-Request-Id` variable in the response header. It uses the `requests` package for making the request.

Usage:

```bash
./5-hbtn_header.py <URL>
```

### 6-post_email.py

This script takes a URL and an email address as arguments, sends a POST request to the URL with the email as a parameter, and displays the response. It uses the `requests` package for making the request.

Usage:

```bash
./6-post_email.py <URL> <email>
```

### 7-error_code.py

This script takes a URL as an argument, sends a request to the URL, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints an error message. It uses the `requests` package for making the request.

Usage:

```bash
./7-error_code.py <URL>
```

### 8-json_api.py

This script takes a letter as an argument, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter, and displays the response. It checks if the response body is valid JSON and prints the id and name if available, or an error message if the JSON is invalid or empty. It uses the `requests` package for making the request.

Usage:

```bash
./8-json_api.py <letter>
```

### 10-my_github.py

This script takes your GitHub username and personal access token as arguments, uses Basic Authentication to access the GitHub API, and displays your GitHub user id. It uses the `requests` package for making the API request.

Usage:

```bash
./10-my_github.py <username> <token>
```

### 100-github_commits.py

This script lists 10 most recent commits (or a specific number) from a GitHub repository by a user. It takes the repository name and owner name as arguments and uses the GitHub API to fetch and display commit information.

Usage:

```bash
./100-github_commits.py <repository_name> <owner_name>
```

# How each line of code works in each script:

### 1-hbtn_status.py

```python
import urllib.request

# Send a GET request to the specified URL
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    # Read the response and decode it as UTF-8
    content = response.read().decode("utf-8")

# Print the content type and content of the response
print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
```

1. We import the `urllib.request` module to make HTTP requests.

2. We use a `with` statement to open a connection to the URL `https://alx-intranet.hbtn.io/status`.

3. Inside the `with` block, we send a GET request to the URL using `urllib.request.urlopen`. This returns a response object.

4. We read the content of the response using `response.read()`, which gives us the raw response body as bytes.

5. We decode the response body as UTF-8 using `.decode("utf-8")` to convert it to a string.

6. Finally, we print the content type (data type) and the content of the response.

### 2-post_email.py

```python
import urllib.request
import sys

# Get the URL and email from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email data
data = {'email': email}

# Encode the data and convert it to bytes
data = urllib.parse.urlencode(data).encode('utf-8')

# Send a POST request with the email data to the specified URL
with urllib.request.urlopen(url, data=data) as response:
    # Read and decode the response
    content = response.read().decode('utf-8')

# Print the response content
print("Your email is:", content)
```

1. We import `urllib.request` for making HTTP requests and `sys` for handling command-line arguments.

2. We retrieve the URL and email from the command-line arguments.

3. We create a dictionary `data` to hold the email data, where the key is 'email' and the value is the email address.

4. We encode the `data` dictionary and convert it to bytes using `urllib.parse.urlencode(data).encode('utf-8')`.

5. We send a POST request to the specified URL using `urllib.request.urlopen`. We pass the encoded `data` as the request body.

6. After receiving the response, we read and decode it as UTF-8.

7. Finally, we print the response content, which is the email address.

### 3-error_code.py

```python
import urllib.request
import sys

# Get the URL from command-line arguments
url = sys.argv[1]

try:
    # Send a GET request to the specified URL
    with urllib.request.urlopen(url) as response:
        # Check the HTTP status code
        if response.status >= 400:
            print("Error code:", response.status)
        else:
            # Read and decode the response
            content = response.read().decode('utf-8')
            print(content)
except urllib.error.HTTPError as e:
    # Handle HTTP errors and print the error code
    print("Error code:", e.code)
```

1. We import `urllib.request` for making HTTP requests, `urllib.error.HTTPError` for handling HTTP errors, and `sys` for handling command-line arguments.

2. We retrieve the URL from the command-line arguments.

3. We use a `try` block to handle potential errors during the request.

4. Inside the `try` block, we send a GET request to the specified URL using `urllib.request.urlopen`.

5. We check the HTTP status code of the response. If it's greater than or equal to 400, we print an error message with the HTTP status code. Otherwise, we read and decode the response content and print it.

6. If an HTTP error occurs (e.g., 404 Not Found), we catch the `urllib.error.HTTPError` exception and print the error code.

### 4-hbtn_status.py

```python
import requests

# Send a GET request to the specified URL
response = requests.get("https://alx-intranet.hbtn.io/status")

# Extract and print information from the response
print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
```

1. We import the `requests` package for making HTTP requests.

2. We send a GET request to the URL "https://alx-intranet.hbtn.io/status" using `requests.get()`. The response is stored in the `response` variable.

3. We extract and print information from the response. This includes the data type of the response content and the content itself.

### 5-hbtn_header.py

```python
import requests
import sys

# Get the URL from command-line arguments
url = sys.argv[1]

# Send a GET request to the specified URL
response = requests.get(url)

# Extract and print the value of the X-Request-Id header
print(response.headers.get('X-Request-Id'))
```

1. We import the `requests` package for making HTTP requests and `sys` for handling command-line arguments.

2. We retrieve the URL from the command-line arguments.

3. We send a

 GET request to the specified URL using `requests.get()`, and the response is stored in the `response` variable.

4. We extract and print the value of the `X-Request-Id` header from the response headers.

### 6-post_email.py

```python
import requests
import sys

# Get the URL and email from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email data
data = {'email': email}

# Send a POST request with the email data to the specified URL
response = requests.post(url, data=data)

# Extract and print the response content
print("Your email is:", response.text)
```

1. We import the `requests` package for making HTTP requests and `sys` for handling command-line arguments.

2. We retrieve the URL and email from the command-line arguments.

3. We create a dictionary `data` to hold the email data, with the key 'email' and the email address as the value.

4. We send a POST request to the specified URL using `requests.post()`, passing the `data` dictionary as the request body.

5. We extract and print the response content, which contains the email address.

### 7-error_code.py

```python
import requests
import sys

# Get the URL from command-line arguments
url = sys.argv[1]

# Send a GET request to the specified URL
response = requests.get(url)

# Check the HTTP status code
if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response.text)
```

1. We import the `requests` package for making HTTP requests and `sys` for handling command-line arguments.

2. We retrieve the URL from the command-line arguments.

3. We send a GET request to the specified URL using `requests.get()`, and the response is stored in the `response` variable.

4. We check the HTTP status code of the response. If it's greater than or equal to 400, we print an error message with the HTTP status code. Otherwise, we print the response content.

### 8-json_api.py

```python
import requests
import sys

# Get the letter from command-line arguments (default to empty string if not provided)
letter = sys.argv[1] if len(sys.argv) > 1 else ""

# Send a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
response = requests.post("http://0.0.0.0:5000/search_user", data={'q': letter})

try:
    # Parse the JSON response
    data = response.json()

    # Check if the response is not empty and contains 'id' and 'name' keys
    if data and 'id' in data and 'name' in data:
        print("[{}] {}".format(data['id'], data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
```

1. We import the `requests` package for making HTTP requests and `sys` for handling command-line arguments.

2. We retrieve the letter from the command-line arguments, defaulting to an empty string if not provided.

3. We send a POST request to "http://0.0.0.0:5000/search_user" with the letter as a parameter using `requests.post()`.

4. We attempt to parse the JSON response using `response.json()`.

5. We check if the response is not empty and contains 'id' and 'name' keys. If so, we print the id and name. Otherwise, we print appropriate error messages for invalid JSON or no result.

### 10-my_github.py

```python
import requests
import sys

# Get the GitHub username and personal access token from command-line arguments
username = sys.argv[1]
token = sys.argv[2]

# Set up the Basic Authentication using the token
auth = (username, token)

# Send a GET request to the GitHub API to retrieve user information
response = requests.get('https://api.github.com/user', auth=auth)

# Print the user id or None if authentication fails
if response.status_code == 200:
    user_info = response.json()
    print(user_info['id'])
else:
    print(None)
```

1. We import the `requests` package for making HTTP requests and `sys` for handling command-line arguments.

2. We retrieve the GitHub username and personal access token from the command-line arguments.

3. We set up Basic Authentication by creating a tuple `auth` containing the username and token.

4. We send a GET request to the GitHub API to retrieve user information using `requests.get()`, and we pass the `auth` tuple for authentication.

5. If the response status code is 200 (OK), we parse the JSON response and print the user id. Otherwise, we print `None` to indicate authentication failure.

### 100-github_commits.py

```python
import requests
import sys

# Get the repository name and owner name from command-line arguments
repository_name = sys.argv[1

]
owner_name = sys.argv[2]

# Construct the URL for retrieving commits
url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

# Send a GET request to the GitHub API to retrieve commit information
response = requests.get(url)

# Check if the response is successful (status code 200)
if response.status_code == 200:
    commits = response.json()
    for commit in commits[:10]:  # Get the first 10 commits
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
else:
    print("Error: Unable to fetch commits")
```

1. We import the `requests` package for making HTTP requests and `sys` for handling command-line arguments.

2. We retrieve the repository name and owner name from the command-line arguments.

3. We construct the URL for retrieving commits by interpolating the repository name and owner name into the URL template.

4. We send a GET request to the GitHub API to retrieve commit information using `requests.get()`.

5. We check if the response status code is 200 (OK). If it is, we parse the JSON response, iterate over the first 10 commits, and print the SHA and author name of each commit. If the request is not successful, we print an error message.
