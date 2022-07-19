const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const num1 = parseInt(input[0]);
const num2 = parseInt(input[1]);

const oneNum2 = num2 % 10;
const tenNum2 = Math.floor((num2 % 100)/10);
const hundredNum2 = Math.floor(num2 / 100);

console.log(num1 * oneNum2);
console.log(num1 * tenNum2);
console.log(num1 * hundredNum2);
console.log(num1 * num2);