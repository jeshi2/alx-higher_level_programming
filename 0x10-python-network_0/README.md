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

This README provides a foundational understanding of various networking concepts and tools related to HTTP and URL manipulation. Further exploration and hands-on practice are recommended to solidify your knowledge.
