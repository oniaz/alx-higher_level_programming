// Fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
    response.results.forEach(function (movie) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
