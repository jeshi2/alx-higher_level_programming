#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API-URL>');
  process.exit(1);
}

// Get the API URL from the command line argument
const apiUrl = process.argv[2];

// Make a GET request to the specified API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, print the error
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the response status code is not 200, print an error message
    console.error(`Error: Unable to retrieve task data. Status code: ${response.statusCode}`);
  } else {
    // Parse the JSON response
    const tasks = JSON.parse(body);

    // Create an object to store the number of completed tasks per user
    const completedTasksByUser = {};

    // Iterate through the tasks and count completed tasks per user
    for (const task of tasks) {
      if (task.completed) {
        const userId = task.userId.toString();
        if (completedTasksByUser[userId]) {
          completedTasksByUser[userId]++;
        } else {
          completedTasksByUser[userId] = 1;
        }
      }
    }

    // Print the completed tasks count for each user
    console.log(completedTasksByUser);
  }
});
