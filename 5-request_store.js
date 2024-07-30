#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const webUrl = process.argv[2];
const filePath = process.argv[3];

request(webUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
