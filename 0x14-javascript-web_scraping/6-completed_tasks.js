#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const jsonData = JSON.parse(body);
  const result = {};

  for (let i = 0; i < jsonData.length; i++) {
    const task = jsonData[i];

    if (task.completed) {
      if (!result[task.userId]) {
        result[task.userId] = 0;
      }
      result[task.userId] += 1;
    }
  }
  console.log(result);
});
