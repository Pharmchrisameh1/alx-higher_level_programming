$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    for (const result of data.results) { $('UL#list_movies').append($('<li></li>').text(result.title)); }
  });
});
