# JavaScript - Web scraping

This repository contains a set of Node.js scripts that demonstrate various tasks using external APIs and modules.

## Requirements

Before running these scripts, make sure you have Node.js installed. You can download it from [nodejs.org](https://nodejs.org/).

Install the necessary modules using npm:

```bash
npm install request
```

## Scripts

1. **Read and Print File Content (`0-readme.js`)**: This script reads and prints the content of a file. It takes a file path as an argument and prints the file's content in UTF-8 encoding. If an error occurs during reading, it prints the error object.

   Usage:
   ```bash
   ./0-readme.js <file-path>
   ```

2. **Write String to File (`1-writeme.js`)**: This script writes a string to a file. It takes a file path and a string as arguments and writes the string to the specified file in UTF-8 encoding. If an error occurs while writing, it prints the error object.

   Usage:
   ```bash
   ./1-writeme.js <file-path> <string-to-write>
   ```

3. **Get Status Code of a URL (`2-statuscode.js`)**: This script makes a GET request to a URL and prints the status code of the response. It takes a URL as an argument.

   Usage:
   ```bash
   ./2-statuscode.js <URL>
   ```

4. **Count Completed Tasks by User (`6-completed_tasks.js`)**: This script makes a GET request to a JSON API URL and counts the number of completed tasks for each user. It only prints users with completed tasks.

   Usage:
   ```bash
   ./6-completed_tasks.js <API-URL>
   ```

5. **Print Characters of a Star Wars Movie (`100-starwars_characters.js`)**: This script prints all characters of a Star Wars movie based on the Movie ID. It uses the Star Wars API and the `request` module to fetch and print character names.

   Usage:
   ```bash
   ./100-starwars_characters.js <Movie-ID>
   ```

6. **Print Characters of a Star Wars Movie (In Order) (`101-starwars_characters.js`)**: This script prints all characters of a Star Wars movie based on the Movie ID, ensuring that the characters are displayed in the same order as the list "characters" in the `/films/` response. It uses the Star Wars API and the `request` module to fetch and print character names in order.

   Usage:
   ```bash
   ./101-starwars_characters.js <Movie-ID>
   ```

## Resources

- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object](https://www.w3schools.com/js/js_json_syntax.asp)
- [request module](https://www.npmjs.com/package/request)
- [Modern JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  
## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use request and fetch API
- How to read and write a file using fs module

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var

## More Info

- Install Node 14
  ```bash
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```

- Install semi-standard
  Documentation:
  ```bash
  $ sudo npm install semistandard --global
  ```

- Install request module and use it
  Documentation:
  ```bash
  $ sudo npm install request --global
  $ export NODE_PATH=/usr/lib/node_modules
  ```
  
Notes: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s

## Author

These scripts were created by Antony Evans.

Feel free to explore, modify, and use these scripts for your own projects.
