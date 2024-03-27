#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const statusCode = response.statusCode;
  console.log('code:', statusCode);
});
