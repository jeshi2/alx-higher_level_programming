// Wait for the document to be ready
$(document).ready(function() {
  // Function to add a new <li> element to the list
  $('#add_item').click(function() {
    const newItem = $('<li>').text('Item');
    $('.my_list').append(newItem);
  });

  // Function to remove the last <li> element from the list
  $('#remove_item').click(function() {
    const listItems = $('.my_list li');
    if (listItems.length > 0) {
      listItems.last().remove();
    }
  });

  // Function to clear all <li> elements from the list
  $('#clear_list').click(function() {
    $('.my_list').empty();
  });
});
