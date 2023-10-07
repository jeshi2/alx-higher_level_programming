// Use jQuery's $.get() method to make an AJAX request and fetch the translation
$.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
  // Extract the translation from the fetched data
  const helloTranslation = data.hello;

  // Display the translation in the <div> with id 'hello'
  $('#hello').text(helloTranslation);
});
