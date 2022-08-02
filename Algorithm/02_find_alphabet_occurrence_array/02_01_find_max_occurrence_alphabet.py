'''
각 알파벳마다 문자열을 돌면서 몇 글자 나왔는지 확인합니다. 
만약 그 숫자가 저장한 알파벳 빈도 수보다 크다면, 그 값을 저장하고 
제일 큰 알파벳으로 저장합니다. 이 과정을 반복하다보면 
가장 많이 나왔던 알파벳을 알 수 있습니다.
'''

def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]
    
    max_occurrence = 0
    max_alphabet = alphabet_array[0]
    
    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1
        
        if occurrence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurrence
    
    return max_alphabet


result = find_max_occurred_alphabet
print("정답 = e \n현재 풀이 값 =", result("Hello my name is gueongsu"))
print("정답 = g \n현재 풀이 값 =", result("gueongsu"))
print("정답 = e \n현재 풀이 값 =", result("best of best gueongsu"))