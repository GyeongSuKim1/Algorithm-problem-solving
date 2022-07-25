---
title: 최빈값 찾기
tags: [Algorithm]
---

### 다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오
#### 📌 : "hello my name is gyeongsu"
``` python
def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    return "a"


result = find_max_occurred_alphabet(input)
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))
```

#### 📌 풀이
1. 01_find_max_num : 각 숫자마다 모든 다른 숫자와 비교해서 최대값인지 확인 후 return
2. 02_find_max_num : 배열 내에서 가장 큰 수를 찾아서 큰 수를 다른 변수에 저장하고 return