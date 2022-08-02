'''
각 char에 따른 arr_index를 구하고 
그 arr_index를 가진 alphabet_occurrence_array값을 1씩 증가시켜 줌으로써
알파벳 별 빈도수를 업데이트할 수 있다.
'''

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