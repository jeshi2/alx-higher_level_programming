// Wait for the document to be ready
$(document).ready(function() {
  // Attach a click event handler to the button with id 'btn_translate'
  $('#btn_translate').click(function() {
    // Get the language code entered by the user from the input with id 'language_code'
    const languageCode = $('#language_code').val();

    // Make an AJAX request to fetch the translation
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
      // Extract the translation from the fetched data
      const translation = data.hello;

      // Display the translation in the <div> with id 'hello'
      $('#hello').text(translation);
    });
  });
});
