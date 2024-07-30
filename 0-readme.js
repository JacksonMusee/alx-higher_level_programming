#!/usr/bin/node

const fs = require('fs');

function myReadFile (filepath) {
  fs.readFile(filepath, 'utf8', function (err, data) {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

const filepath = process.argv[2];
myReadFile(filepath);
