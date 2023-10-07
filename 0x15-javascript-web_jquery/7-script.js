// Wait for the document to be ready
$(document).ready(function() {
  // Define the URL for the character data
  const characterUrl = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
  
  // Use jQuery's $.get() method to make an AJAX request and fetch the character data
  $.get(characterUrl, function(data) {
    // Extract the character name from the fetched data
    const characterName = data.name;

    // Display the character name in the <div> with id 'character'
    $('#character').text(characterName);
  });
});
