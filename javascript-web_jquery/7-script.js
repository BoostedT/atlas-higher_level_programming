$(document).ready(function() {
    const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  
    $.getJSON(apiUrl, function(data) {
      $('#character').text(data.name);
    }).fail(function() {
      console.error('An error occurred while fetching the character data.');
    });
  });  