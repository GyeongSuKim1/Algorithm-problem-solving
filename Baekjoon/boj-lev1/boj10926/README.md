---
title: (백준/node.js) 10926번 ??!
tags: [boj]
author: 김경수
---

### (백준/node.js) 준하는 사이트에 회원가입을 하다가 joonas라는 아이디가 이미 존재하는 것을 보고 놀랐다. 준하는 놀람을 ??!로 표현한다. 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어졌을 때, 놀람을 표현하는 프로그램을 작성하시오.
#### 📌 제출번호: 40850426
``` js
const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim(); 
console.log(`${input}??!`);
```

#### 📌 풀이
1. 간단한 출력문제.
2. trim() 을 넣어서 앞, 뒤 공백을 제거