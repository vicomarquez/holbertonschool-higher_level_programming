#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, resp, body) {
  if (error) {
    console.log(error);
  } else {
    const complete = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; i++) {
      const id = body[i].userId;
      const completed = body[i].completed;
      if (completed && !complete[id]) {
        complete[id] = 0;
      }
      if (completed) ++complete[id];
    }
    console.log(complete);
  }
});
