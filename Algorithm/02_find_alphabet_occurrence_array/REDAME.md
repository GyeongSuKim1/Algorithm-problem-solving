---
title: 최빈값 찾기
tags: [Algorithm]
---

### 다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오
#### 📌 : "hello my name is gyeongsu"
``` python
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():  # 알파벳인지 확인
            continue    # 알파벳이 아니라면 다음 문자로 넘어감
        arr_index = ord(char) - ord("a")    # 배열의 인덱스 값이 됨
        alphabet_occurrence_array[arr_index] += 1
        
    return alphabet_occurrence_array

print("정답 = [1, 1, 0, 0, 2, 0, 0, 0, 1, 0, 2, 2, 2, 1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0] \n풀이 =", find_alphabet_occurrence_array("Hello my name is kks"))
print("정답 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] \n풀이 =", find_alphabet_occurrence_array("kks"))
print("정답 = [0, 2, 0, 0, 2, 1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0] \n풀이 =", find_alphabet_occurrence_array("best of best kks"))
```

#### 📌 풀이
1. 각 char에 따른 arr_index를 구한다.
2. arr_index를 가진 alphabet_occurrence_array값을 1씩 증가시켜준다.