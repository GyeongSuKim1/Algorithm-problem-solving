---
title: (백준/node.js) 9498번 시험 성적
tags: [boj]
author: 김경수
---

### (백준/node.js) 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
#### 📌 제출번호: 40948851
``` js
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();

const num = parseInt(input);

if (100 >= num && num >= 90) {
    console.log('A');
} else if (89 >= num && num >= 80) {
    console.log('B')
} else if (79 >= num && num >= 70) {
    console.log('C')
} else if (69 >= num && num >= 60) {
    console.log('D')
} else
    console.log('F')
```

#### 📌 풀이
1. 조건문, 논리연산자 문제
2. num이 100과 같거나 작다 그리고 90보다 크거나 같다.
- 아래도 마찬가지로 작성.