let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let a = parseInt(input[0]);
console.log(a - 543);