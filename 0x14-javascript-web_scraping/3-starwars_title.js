#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const jsonData = JSON.parse(body);
  console.log(jsonData.title);
});
