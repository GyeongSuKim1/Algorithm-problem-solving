'''
각 알파벳의 빈도수를 alphabet_occurrence_list 라는 변수에 저장합니다.
그리고 각 문자열을 돌면서 해당 문자가 알파벳인지 확인하고,
알파벳을 인덱스 화 시켜 각 알파벳의 빈도수를 업데이트 합니다.

이후, 알파벳의 빈도수가 가장 높은 인덱스를 찾습니다.
'''
    
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index
    
    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = e \n현재 풀이 값 =", result("Hello my name is gueongsu"))
print("정답 = g \n현재 풀이 값 =", result("gueongsu"))
print("정답 = e \n현재 풀이 값 =", result("best of best gueongsu"))