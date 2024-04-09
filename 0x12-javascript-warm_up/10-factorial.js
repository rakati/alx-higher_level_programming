#!/usr/bin/node
const { argv } = require('node:process');

function fact (a) {
  if (Number.isNaN(a) || a === 1) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
console.log(fact(parseInt(argv[2])));
