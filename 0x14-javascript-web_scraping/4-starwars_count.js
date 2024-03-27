#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  let count = 0;
  const jsonData = JSON.parse(body);
  const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

  for (let i = 0; i < jsonData.results.length; i++) {
    const movie = jsonData.results[i];
    if (movie.characters.includes(characterUrl)) {
      count++;
    }
  }
  console.log(count);
});
