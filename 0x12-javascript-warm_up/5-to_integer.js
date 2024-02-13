#!/usr/bin/node

const num = process.argv[2];
const str = isNaN(num) ? 'Not a number' : ('My number: ' + num);
console.log(str);
