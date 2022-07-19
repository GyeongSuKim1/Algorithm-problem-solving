let hour = 23;
let min = 40;
let count = 180;

min += count;
// h = 23, min = 290, c = 250

if (min >= 60) {    //가독성을 위해 크거나 같다로 표현
    hour += Math.floor(min / 60);
    // h = 27, min = 290 , c = 250

    min %= 60;
    // h = 27, min = 50, c = 250

    if (hour >= 24)
        hour -= 24;
    // h = 3, min = 50, c = 250
}
console.log(hour + ' ' + min);