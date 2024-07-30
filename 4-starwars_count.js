#!/usr/bin/node

const request = require('request');
const filmsUrl = process.argv[2];
let count = 0;

request(filmsUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body);
    const filmsArray = filmsData.results;

    for (const film of filmsArray) {
      if (film.characters.some(character => character.includes('/18/'))) {
        count++;
      }
    }
    console.log(count);
  }
});
