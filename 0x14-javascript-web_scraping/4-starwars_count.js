#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <API-URL>');
  process.exit(1);
}

// Get the API URL from the command line argument
const apiUrl = process.argv[2];

// Function to make a GET request to the API URL
function makeRequest(url, callback) {
  request(url, (error, response, body) => {
    if (error) {
      // If an error occurs during the request, call the callback with an error
      callback(error);
    } else if (response.statusCode !== 200) {
      // If the response status code is not 200, call the callback with an error
      callback(`Error: Unable to retrieve movie details. Status code: ${response.statusCode}`);
    } else {
      // Parse the JSON response
      const data = JSON.parse(body);

      // Call the callback with the parsed data
      callback(null, data);
    }
  });
}

// Function to count movies with Wedge Antilles
function countMoviesWithWedge(apiUrl, callback, moviesWithWedge = []) {
  makeRequest(apiUrl, (error, data) => {
    if (error) {
      // If there is an error, call the callback with the error
      callback(error);
    } else {
      // Filter movies where "Wedge Antilles" (character ID 18) is present
      const movies = data.results.filter((movie) =>
        movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );

      // Add filtered movies to the array
      moviesWithWedge = moviesWithWedge.concat(movies);

      // Check if there are more pages of results
      if (data.next) {
        // If there are more pages, recursively call the function with the next URL
        countMoviesWithWedge(data.next, callback, moviesWithWedge);
      } else {
        // If there are no more pages, call the callback with the count of movies
        callback(null, moviesWithWedge.length);
      }
    }
  });
}

// Call the countMoviesWithWedge function to get the count of movies with Wedge Antilles
countMoviesWithWedge(apiUrl, (error, count) => {
  if (error) {
    // If there is an error, print the error message
    console.error(error);
  } else {
    // Print the count of movies with Wedge Antilles
    console.log(count);
  }
});
