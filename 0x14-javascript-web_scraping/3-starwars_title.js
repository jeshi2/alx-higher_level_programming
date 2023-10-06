#!/usr/bin/node

const request = require('request');

// Check if the movie ID is provided as an argument
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie-ID>');
  process.exit(1);
}

// Get the movie ID from the command line argument
const movieID = process.argv[2];

// Create the URL for the Star Wars API request
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, print the error
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the response status code is not 200, print an error message
    console.error(`Error: Unable to retrieve movie details. Status code: ${response.statusCode}`);
  } else {
    // Parse the JSON response and print the movie title
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
