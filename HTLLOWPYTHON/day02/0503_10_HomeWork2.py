# 첫번쨰 숫자를 입력
# 두번째 숫자를 입력
# 첫번째부터 두번째 숫자까지 출력

first   = input("첫번째 숫자를 입력하시오")
second  = input("두번째 숫자를 입력하시오")
result = 0

rang = range(int(first),(int(second)+1))

for i in rang:
    result = result + i

print("result",result)

