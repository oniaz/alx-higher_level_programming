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
  const charRegex = /\/18\/$/;

  for (let i = 0; i < jsonData.results.length; i++) {
    const movie = jsonData.results[i];
    for (let j = 0; j < movie.characters.length; j++) {
      if (charRegex.test(movie.characters[j])) {
        count++;
      }
    }
  }
  console.log(count);
});
