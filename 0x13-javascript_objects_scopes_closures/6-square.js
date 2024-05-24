#!/usr/bin/node

const BaseSquare = require('./5-square.js');

class Square extends BaseSquare {
  charPrint (c) {
    if (!c) c = 'X';
    console.log((c.repeat(this.width) + '\n').repeat(this.height));
  }
}

module.exports = Square;
