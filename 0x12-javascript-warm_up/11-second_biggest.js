#!/usr/bin/node
const { argv } = require('node:process');

let mx = 0;
let mx1 = 0;

for (let i = 1; i < argv.length; i++) {
  if (parseInt(argv[i]) > mx) {
    mx1 = mx;
    mx = parseInt(argv[i]);
  } else if (parseInt(argv[i]) > mx1) {
    mx1 = parseInt(argv[i]);
  }
}
console.log(mx1);
