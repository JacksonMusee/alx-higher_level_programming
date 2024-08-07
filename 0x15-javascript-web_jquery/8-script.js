// Fetches and lists the title for all movies by using this
// + URL: https://swapi-api.alx-tools.com/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const filmsArray = data.results;
  $.each(filmsArray, function (i, film) {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
});
});