#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movieJsonData = JSON.parse(body);

  for (let i = 0; i < movieJsonData.characters.length; i++) {
    request.get(movieJsonData.characters[i], (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      const characterJsonData = JSON.parse(body);
      console.log(characterJsonData.name);
    });
  }
});
