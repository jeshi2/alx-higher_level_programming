#!/usr/bin/node

const fs = require('fs');

// Check if the file path is provided as an argument
if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

// Get the file path from the command line argument
const filePath = process.argv[2];

// Read the file content in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurred during reading, print the error object
    console.error(err);
  } else {
    // If reading was successful, print the file content
    console.log(data);
  }
});
