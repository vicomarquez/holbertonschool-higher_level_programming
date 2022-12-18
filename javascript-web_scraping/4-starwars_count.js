#!/usr/bin/node

// The first argument is the movie ID
// The status code must be printed like this: code: <status code>

const request = require('request');
let counter = 0;

request(process.argv[2], function (error, resp, body) {
  if (error) {
    console.log(error);
  } else {
    const dt = JSON.parse(body);
    for (let i = 0; i < dt.results.length; i++) {
      for (let x = 0; x < dt.results[i].characters.length; x++) {
        if (dt.results[i].characters[x].includes('/18/')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
