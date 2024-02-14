#!/usr/bin/node

const size = process.argv[2];
const char = 'X';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const str = char.repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(str);
  }
}
