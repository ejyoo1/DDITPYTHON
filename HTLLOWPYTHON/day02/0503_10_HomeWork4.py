# 첫번째 숫자 입력
# 두번째 숫자 입력
# 짝수의 합

first = input("첫번째 숫자를 입력하세요")
second = input("두번째 숫자를 입력하세요")
result = 0

rang = range(int(first), int(second)+1)

for i in rang:
    if i % 2 == 0:
        result = result + i
    else:
        pass
        
print("result",result)
