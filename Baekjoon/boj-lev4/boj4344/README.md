---
title: (백준/python3) 4344번 평균은 넘겠지
tags: [boj]
author: 김경수
---

### (백준/python3) 
## 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.


### 입력 : 첫째 줄에는 테스트 케이스의 개수 C가 주어진다. 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

### 출력 : 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
#### 📌 제출번호: 46832768
``` python
num = int(input())

for _ in range(num):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:]) / nums[0]   # nums[0] : 학생수, nums[1:] : 점수
    count = 0
    for score in nums[1:]:
        if score > avg:
            count += 1  # 평균 이상인 학생 수
    rate = count/nums[0]*100
    print(f'{rate:.3f}%')
```

#### 📌 풀이
1. 상단 for문에서 점수의 평균을 구함.
2. 하단 for문에서 평균 이상인 학생 수를 구함.
4. 평균보다 높은 점수를 받은 학생 비율을 구하고 출력문 작성