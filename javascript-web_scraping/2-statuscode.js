#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Please provide a URL as an argument.');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
