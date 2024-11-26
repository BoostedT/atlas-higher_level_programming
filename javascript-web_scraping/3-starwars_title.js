#!/usr/bin/node

const request = require('request');
const args = process.argv;
const requestURL = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request(requestURL, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
