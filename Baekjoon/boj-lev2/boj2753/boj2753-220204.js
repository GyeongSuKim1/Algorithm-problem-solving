const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf8').toString().split(' ');

const a = parseInt(inputData[0]);

if ((a % 4) == 0 && (a % 100) !== 0 || (a % 400) == 0) {
    console.log(1);
} else {
    console.log(0);
}