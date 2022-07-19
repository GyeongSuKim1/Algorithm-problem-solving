//로컬 주소     ex.txt
//백준주소 /dev/stdin >>>> ex.txt
var fs = require('fs');
var input = fs.readFileSync('ex.txt').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);
console.log(a-b);