---
title: (백준/node.js) 14681번 사분면 고르기
tags: [boj]
author: 김경수
---

### (백준/node.js) 흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다. 사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. "Quadrant n"은 "제n사분면"이라는 뜻이다. 예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.
## (출력) 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.
#### 📌 제출번호: 40948851
``` js
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on("line", function (line) {
    input.push(parseInt(line));
}).on("close", function () {

    const x = input[0];
    const y = input[1];

    if (x > 0 && y > 0) {
        console.log(1);
    } else if (x < 0 && y > 0) {
        console.log(2);
    } else if (x < 0 && y < 0) {
        console.log(3);
    } else if (x > 0 && y < 0) {
        console.log(4);
    }

    process.exit();
});
```
#### 📌 풀이
1. 조건문, 논리연산자 문제
2. 0 < x && y > 0
- x,y를 양수로 만들면 사분면 1이 출력