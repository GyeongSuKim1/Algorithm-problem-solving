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