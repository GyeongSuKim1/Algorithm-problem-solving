---
title: (백준/node.js) 1330번 두 수 비교하기
tags: [boj]
author: 김경수
---

### (백준/node.js) 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
#### 📌 제출번호: 40946381
``` js
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');

const num1 = parseInt(input[0]);
const num2 = parseInt(input[1]);

if (num1 > num2) {
    console.log('>');
} else if (num1 < num2)
    console.log('<');
else
    console.log('==');
```

#### 📌 풀이
1. 간단한 조건문 문제
2. num1 과 num2 를 비교
3. num1 이 크면 '>' 출력
4. num2 가 크면 '<' 출력
5. 그 외 '==' 출력