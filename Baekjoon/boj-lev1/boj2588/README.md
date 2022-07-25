---
title: (백준/python3) 2588번 곱셈
tags: [boj]
author: 김경수
---

### (백준/python3) (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
#### 📌 제출번호: 42770640
``` python
import math

a = int(input())
b = int(input())

b_one = b % 10
b_ten = math.floor((b % 100)/10)
b_hundred = math.floor(b / 100)

print(a * b_one)
print(a * b_ten)
print(a * b_hundred)
print(a * b)
```

#### 📌 풀이
1. 1의 자리: 10으로 나눈 나머지
2. 10의 자리: 100으로 나눈 나머지에서 10으로 나눗셈
3. 100의 자리: 100으로 나눗셈

<hr>


---
title: (백준/node.js) 2588번 곱셈
tags: [boj]
author: 김경수
---

### (백준/node.js) (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
#### 📌 제출번호: 40338105
``` js
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const num1 = parseInt(input[0]);
const num2 = parseInt(input[1]);

const oneNum2 = num2 % 10;
const tenNum2 = Math.floor((num2 % 100)/10);
const hundredNum2 = Math.floor(num2 / 100)

console.log(num1 * oneNum2);
console.log(num1 * tenNum2);
console.log(num1 * hundredNum2);
console.log(num1 * num2);
```

#### 📌 풀이
1. 1의 자리: 10으로 나눈 나머지
2. 10의 자리: 100으로 나눈 나머지에서 10으로 나눗셈
3. 100의 자리: 100으로 나눗셈
4. split(\n) 을 넣음으로써 한줄 띄어 씀.