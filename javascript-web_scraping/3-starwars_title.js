#!/usr/bin/node

// The first argument is the movie ID
// The status code must be printed like this: code: <status code>

const request = require('request');

request(('https://swapi-api.hbtn.io/api/films/' + process.argv[2]), function (error, resp, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
