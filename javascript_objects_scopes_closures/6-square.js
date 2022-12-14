#!/usr/bin/node

const squareOne = require('./5-square');
module.exports = class Square extends squareOne {
  charPrint (C) {
    if (!C) {
      super.print();
    } else {
      for (let x = 0; x < this.width; x++) {
        console.log(C.repeat(this.width));
      }
    }
  }
};
