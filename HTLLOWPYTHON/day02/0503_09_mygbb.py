# 유저 입력
# 컴퓨터 랜덤
# 3가지 경우 0.33으로 나누기
import random

mine = input("가위/바위/보를 입력하세요")
com = ""
result = ""

rand = random.random()

if 0 < rand and rand < 0.33:
    com = "가위"
elif 0.33 < rand and rand < 0.66:
    com = "바위"
else:
    com = "보"
    
if mine == com:
    result = "비김"
else: 
    if mine == "가위" and com == "보" or mine == "바위" and com == "가위" or mine == "보" and com == "바위":
        result = "이김"
    elif mine == "가위" and com == "바위" or mine == "바위" and com == "보" or mine == "보" and com == "가위":
        result = "짐"
    else:
        pass

print("mine:",mine);
print("com:",com);
print("result:",result);