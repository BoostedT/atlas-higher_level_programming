#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeId = '18';

if (!apiUrl) {
  console.error('Usage: node count_wedge_movies.js <API_URL>');
  process.exit(1);
}

request(apiUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error('Error fetching data:', err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error('Failed to retrieve data. Status code:', res.statusCode);
    return;
  }

  const filmsWithWedge = body.results.filter(film =>
    film.characters.some(url => url.endsWith(`/people/${wedgeId}/`))
  );

  console.log(filmsWithWedge.length);
});
