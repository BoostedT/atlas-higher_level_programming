#!/usr/bin/node
const Rectangle = require('./rectangle');

const rect = new Rectangle(4, 2);
console.log('Original Rectangle:');
rect.print();

console.log('After rotation:');
rect.rotate();
rect.print();

console.log('After doubling:');
rect.double();
rect.print();

const invalidRect = new Rectangle(0, -5);
console.log('Invalid Rectangle:', invalidRect); // Output: {}
