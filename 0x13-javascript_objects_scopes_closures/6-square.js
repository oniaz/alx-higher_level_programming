#!/usr/bin/node

const BaseSquare = require('./5-square.js');

class Square extends BaseSquare {
  charPrint (c) {
    if (!c) c = 'X';
    for (let h = 0; h < this.height; h++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
