#!/usr/bin/node

const fs = require('fs');

function myWriteFile (filepath) {
  fs.writeFile(filepath, theStr, function (err) {
    if (err) {
      console.error(err);
    }
  });
}

const filepath = process.argv[2];
const theStr = process.argv[3];

myWriteFile(filepath);
