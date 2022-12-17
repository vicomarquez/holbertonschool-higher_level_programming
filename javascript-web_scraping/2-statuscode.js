#!/usr/bin/node

// Script that displays the status code of a GET request.
// The first argument is the URL to request (GET)
// The status code must be printed like this: code: <status code>

const request = require('request');

request(process.argv[2], function (error, response) {
    console.log('code:', response.statusCode);
});
