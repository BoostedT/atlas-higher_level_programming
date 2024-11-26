#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide an API URL as an argument.');
  process.exit(1);
}

request(apiUrl, { json: true }, (error, response, body) => {
    if (err) {
        console.error('Error fetching data:', err);
        return;
    }
});
