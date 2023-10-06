#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <API-URL>');
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
    console.error(`Error: Unable to retrieve movie details. Status code: ${response.statusCode}`);
  } else {
    // Parse the JSON response
    const data = JSON.parse(body);

    // Filter movies where "Wedge Antilles" (character ID 18) is present
    const moviesWithWedge = data.results.filter((movie) =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );

    // Print the number of movies where Wedge Antilles is present
    console.log(moviesWithWedge.length);
  }
});
