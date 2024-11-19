#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);
const firstNum = parseInt(args[0], 10);
const secondNum = parseInt(args[1], 10);

if (isNaN(firstNum) || isNaN(secondNum)) {
  console.log('NaN');
} else {
  console.log(add(firstNum, secondNum));
}
