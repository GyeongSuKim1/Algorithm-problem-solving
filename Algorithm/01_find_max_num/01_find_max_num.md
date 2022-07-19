---
title: 최대값 찾기
tags: [Algorithm]
---

### 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

``` python
def find_max_num(array):
    # 이 부분을 채워보세요!
    return 1


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))
```

#### 📌 풀이
1. 01_find_max_num : 각 숫자마다 모든 다른 숫자와 비교해서 최대값인지 확인 후 return
2. 02_find_max_num : 배열 내에서 가장 큰 수를 찾아서 큰 수를 다른 변수에 저장하고 return