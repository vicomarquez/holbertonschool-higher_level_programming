#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, resp, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (er) => {
      if (er) {
        console.log(er);
      }
    });
  }
});
