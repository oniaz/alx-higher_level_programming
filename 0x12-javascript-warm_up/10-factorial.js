#!/usr/bin/node

function fact (n) {
  if (isNaN(n) || n === 1 || n === 0) {
    return (1);
  } else {
    return (fact(n - 1) * n);
  }
}
console.log(fact(process.argv[2]));
