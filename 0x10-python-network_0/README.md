# Python Network #0

This project aims to provide a fundamental understanding of various networking concepts and tools related to HTTP and URL manipulation. The following topics are covered in this README:

## Table of Contents
1. [What is a URL?](#what-is-a-url)
2. [What is HTTP?](#what-is-http)
3. [How to Read a URL](#how-to-read-a-url)
4. [HTTP URL Scheme](#http-url-scheme)
5. [Domain Names](#domain-names)
6. [Sub-Domains](#sub-domains)
7. [Defining Port Numbers in a URL](#defining-port-numbers-in-a-url)
8. [Query Strings](#query-strings)
9. [HTTP Requests](#http-requests)
10. [HTTP Responses](#http-responses)
11. [HTTP Headers](#http-headers)
12. [HTTP Message Body](#http-message-body)
13. [HTTP Request Methods](#http-request-methods)
14. [HTTP Response Status Codes](#http-response-status-codes)
15. [HTTP Cookies](#http-cookies)
16. [Making Requests with cURL](#making-requests-with-curl)
17. [Browser Behavior when Typing a URL](#browser-behavior-when-typing-a-url)
18. [Copyright and Plagiarism](#copyright-and-plagiarism)

## What is a URL?

A **Uniform Resource Locator (URL)** is a web address that specifies the location of a resource on the internet. It consists of several components, including the scheme, domain name, path, query string, and fragment identifier.

## What is HTTP?

**HTTP (Hypertext Transfer Protocol)** is a protocol used for transmitting data, particularly for the World Wide Web. It governs how requests and responses are formatted and transmitted between web clients (such as browsers) and servers.

## How to Read a URL

Reading a URL involves breaking it down into its components, understanding each part's purpose, and knowing how to interpret them.

## HTTP URL Scheme

The **scheme** in an HTTP URL indicates how the resource should be accessed. Common schemes include `http` and `https`, where `https` is a secure version of HTTP.

## Domain Names

A **domain name** is a human-readable label used to identify a specific location on the internet. For example, "example.com" is a domain name.

## Sub-Domains

A **sub-domain** is a part of a larger domain. For example, in "blog.example.com," "blog" is a sub-domain of "example.com."

## Defining Port Numbers in a URL

A **port number** in a URL specifies the communication port to use when connecting to the server. For example, `http://example.com:8080` uses port 8080.

## Query Strings

A **query string** allows passing parameters to a web resource. It follows a `?` in the URL and is often used in search and data retrieval.

## HTTP Requests

An **HTTP request** is a message sent by a client (e.g., a web browser) to request a specific resource from a server. It includes information like the requested URL, method, and headers.

## HTTP Responses

An **HTTP response** is the server's reply to an HTTP request. It contains the requested data, along with status information, headers, and a message body.

## HTTP Headers

**HTTP headers** are metadata sent in both requests and responses, providing additional information about the request/response or the server's capabilities.

## HTTP Message Body

The **HTTP message body** carries the actual data being transmitted, such as HTML content in a web page or JSON data in an API response.

## HTTP Request Methods

HTTP defines various **request methods**, such as `GET`, `POST`, `PUT`, and `DELETE`, to specify the action the server should perform.

## HTTP Response Status Codes

**HTTP response status codes** indicate the outcome of an HTTP request. Examples include `200 OK` for success, `404 Not Found` for resource not found, and `500 Internal Server Error` for server issues.

## HTTP Cookies

An **HTTP Cookie** is a small piece of data sent from a server and stored on a user's device. It is often used for session management and user tracking.

## Making Requests with cURL

**cURL** is a command-line tool for making HTTP requests. It allows you to fetch or send data to web servers from the command line.

## Browser Behavior when Typing a URL

When you type a URL like "google.com" into your browser, the browser performs DNS resolution to find the IP address associated with the domain, initiates an HTTP request to that IP, and renders the webpage received in response.

## Copyright and Plagiarism

Respect copyright and avoid plagiarism. Ensure that you create original content and give proper attribution when using external sources. Plagiarism is strictly prohibited.

# Bash Scripts Overview

This repository contains several Bash scripts designed to perform various tasks using the `curl` command-line tool. Each script is designed to solve a specific problem or accomplish a particular task. Below is a brief overview of each script:

## 0-body_size.sh

- **Description**: This script takes a URL as an argument, sends a GET request to that URL using `curl`, and displays the size of the response body in bytes.
- **Usage**: `./0-body_size.sh <URL>`

## 1-body.sh

- **Description**: This script takes a URL as an argument, sends a GET request to that URL using `curl`, and displays the body of the response if the response status code is 200.
- **Usage**: `./1-body.sh <URL>`

## 2-delete.sh

- **Description**: This script takes a URL as an argument, sends a DELETE request to that URL using `curl`, and displays the body of the response.
- **Usage**: `./2-delete.sh <URL>`

## 3-methods.sh

- **Description**: This script takes a URL as an argument, sends an OPTIONS request to that URL using `curl`, and displays the allowed HTTP methods.
- **Usage**: `./3-methods.sh <URL>`

## 4-header.sh

- **Description**: This script takes a URL as an argument, sends a GET request to that URL using `curl` with a custom header, and displays the body of the response.
- **Usage**: `./4-header.sh <URL>`

## 5-post_params.sh

- **Description**: This script takes a URL as an argument, sends a POST request to that URL using `curl` with specified variables in the request body, and displays the body of the response.
- **Usage**: `./5-post_params.sh <URL>`

## 6-peak.py

- **Description**: This script contains a Python function `find_peak` that finds a peak in a list of unsorted integers with a low complexity algorithm (O(log(n))).
- **Usage**: The function `find_peak` can be imported and used in other Python scripts.

## 100-status_code.sh

- **Description**: This script takes a URL as an argument, sends a request to that URL using `curl`, and displays only the status code of the response.
- **Usage**: `./100-status_code.sh <URL>`

## 101-post_json.sh

- **Description**: This script takes a URL and a JSON file as arguments, sends a JSON POST request to the URL with the contents of the JSON file in the request body, and displays whether the JSON content is valid.
- **Usage**: `./101-post_json.sh <URL> <JSON_FILE>`

## 102-catch_me.sh

- **Description**: This script makes a request to `0.0.0.0:5000/catch_me` using `curl` in a way that the server responds with the message "You got me!" in the body of the response.
- **Usage**: `./102-catch_me.sh`

Each script serves a specific purpose and can be used to interact with web services, perform HTTP requests, or manipulate data. Refer to individual script files for detailed usage instructions.



This README provides a foundational understanding of various networking concepts and tools related to HTTP and URL manipulation. Further exploration and hands-on practice are recommended to solidify your knowledge.
