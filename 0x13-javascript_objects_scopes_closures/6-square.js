#!/usr/bin/node

const baseSquare = require('./5-square');

class Square extends baseSquare {
  charPrint (c) {
    let symbol = 'X';
    let i = 0;

    if (c) {
      symbol = c;
    }

    while (i < this.width) {
      console.log(`${symbol}`.repeat(this.width));
      i++;
    }
  }
}

module.exports = Square;
