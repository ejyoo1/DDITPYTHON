import random

test = "홀", "짝"
com = random.choice(test)
result = ""

mine = input("홀/짝을 선택하세요")

if mine == com:
    result="이김"
else:
    result="짐"
    
print("com",com)
print("mine",mine)
print("result",result)

