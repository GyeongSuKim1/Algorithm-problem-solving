let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let a = parseInt(input[0]);
let b = parseInt(input[1]);
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(Math.floor(a / b));     //나머지를 버림 즉 정수만을 출력 Math.floor()
console.log(a % b);