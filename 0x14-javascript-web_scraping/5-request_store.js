#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Check if both URL and file path arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file-path>');
  process.exit(1);
}

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, print the error
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the response status code is not 200, print an error message
    console.error(`Error: Unable to retrieve content. Status code: ${response.statusCode}`);
  } else {
    // Write the response body to the specified file
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        // If an error occurs while writing to the file, print the error
        console.error(err);
      } else {
        // console.log(`Content saved to ${filePath}`);
      }
    });
  }
});
