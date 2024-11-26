$(document).ready(function() {
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
    $.getJSON(apiUrl, function(data) {
      $('#hello').text(data.hello);
    }).fail(function() {
      console.error('An error occurred while fetching the translation.');
    });
  });  