---
title: (백준/python3) 10869번 사칙연산
tags: [boj]
author: 김경수
---

### (백준/python3) 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, AxB, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
#### 📌 제출번호: 42767325
``` python
num, num2 = map(int, input().split())
print(num + num2)
print(num - num2)
print(num * num2)
print(num // num2)
print(num % num2)
```

#### 📌 풀이
1. num1, num2를 변수로 선언
2. map을 이용하여 int, input(), split()을 적용 시켜줌
4. 사칙연산 진행



<hr>

---
title: (백준/node.js) 10869번 사칙연산
tags: [boj]
author: 김경수
---

### (백준/node.js) 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, AxB, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
#### 📌 제출번호: 40074217
``` js
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let a = parseInt(input[0]);
let b = parseInt(input[1]);
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(Math.floor(a / b));
console.log(a % b);
```

#### 📌 풀이
1. Node.js의 fs모듈을 이용하여 ps를 진행.
2. '표준 입력장치'의 값을 읽어 input에 저장
3. console.log 로 결과 출력
4. a/b 를 하였는데 나머지가 무수히 나오는경우 오류가 있다. 그래서 Matg.floor을 추가
5. Math.floor() 는 나머지를 버리는 즉 정수만을 출력하는 명령어 이다.