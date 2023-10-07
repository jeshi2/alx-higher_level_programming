// Wait for the document to be ready
$(document).ready(function() {
  // Define the URL for the movies data
  const moviesUrl = "https://swapi-api.alx-tools.com/api/films/?format=json";
  
  // Use jQuery's $.get() method to make an AJAX request and fetch the movies data
  $.get(moviesUrl, function(data) {
    // Extract the array of movie objects from the fetched data
    const movies = data.results;

    // Select the <ul> element with id 'list_movies'
    const listMovies = $('#list_movies');

    // Iterate through the movie objects and add each movie title as an <li> element to the <ul>
    $.each(movies, function(index, movie) {
      const movieTitle = movie.title;
      const listItem = $('<li>').text(movieTitle);
      listMovies.append(listItem);
    });
  });
});
