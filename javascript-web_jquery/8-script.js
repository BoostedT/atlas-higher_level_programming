$(document).ready(function() {
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

  $.getJSON(apiUrl, function(data) {
    const movies = data.results;
    const $listMovies = $('#list_movies');

    movies.forEach(function(movie) {
      const $listItem = $('<li></li>').text(movie.title);
      $listMovies.append($listItem);
    });
  }).fail(function() {
    console.error('An error occurred while fetching the movie data.');
  });
});