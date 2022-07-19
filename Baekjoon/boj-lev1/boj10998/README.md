---
title: (백준/node.js) 10998번 A*B
tags: [boj]
author: 김경수
---

### (백준/node.js) 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
#### 📌 제출번호: 39990675
``` js
var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);
console.log(a * b);
```

#### 📌 풀이
1. Node.js의 fs모듈을 이용하여 ps를 진행.
2. '표준 입력장치'의 값을 읽어 input에 저장
3. console.log 로 결과 출력