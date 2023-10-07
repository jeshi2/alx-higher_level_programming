// Wait for the document to be ready
$(document).ready(function() {
  // Attach a click event handler to the div with id 'toggle_header'
  $('#toggle_header').click(function() {
    // Toggle the 'red' and 'green' classes on the <header> element
    $('header').toggleClass('red green');
  });
});
