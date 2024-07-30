#!/usr/bin/node

const request = require('request');

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

const fetchCharacter = async (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterObj = JSON.parse(body);
        resolve(characterObj.name);
      }
    });
  });
};

request(movieUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characterLst = movieData.characters;

    for (const url of characterLst) {
      const characterName = await fetchCharacter(url);
      console.log(characterName);
    }
  }
});
