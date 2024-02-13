#!/usr/bin/node
const { argv } = require('node:process');
const n = argv.length;

if (n < 3) {
  console.log('No argument');
} else if (n === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
