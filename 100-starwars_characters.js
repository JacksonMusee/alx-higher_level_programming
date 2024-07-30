#!/usr/bin/node

const request = require('request');

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characterLst = movieData.characters;

    for (const url of characterLst) {
      request(url, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const characterObj = JSON.parse(body);
          const characterName = characterObj.name;

          console.log(characterName);
        }
      });
    }
  }
});
