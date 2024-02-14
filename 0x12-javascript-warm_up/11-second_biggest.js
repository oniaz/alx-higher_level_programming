#!/usr/bin/node

const size = process.argv.length - 2;

if (size < 2) {
  console.log(0);
} else {
  /* making a new array with the numbers and parsing them to ints */
  const arr = process.argv.slice(2).map(function (x) {
    return parseInt(x, 10);
  });

  const max = Math.max(...arr);
  let secondMax = Math.min(...arr);

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < max && arr[i] > secondMax) {
      secondMax = arr[i];
    }
  }

  console.log(secondMax);
}
