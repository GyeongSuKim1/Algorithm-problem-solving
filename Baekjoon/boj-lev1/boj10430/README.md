---
title: (백준/node.js) 10430번 나머지
tags: [boj]
author: 김경수
---

### (백준/node.js) (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?(A×B)%C는                             ((A%C) × (B%C))%C 와 같을까?                    세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
#### 📌 제출번호: 40851022
``` js
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

let a = parseInt(input[0]);
let b = parseInt(input[1]);
let c = parseInt(input[2]);

console.log((a+b)%c)
console.log(((a%c) + (b%c))%c)
console.log((a*b)%c)
console.log(((a%c) * (b%c))%c)
```

#### 📌 풀이
1. 간단한 연산, 출력 문제