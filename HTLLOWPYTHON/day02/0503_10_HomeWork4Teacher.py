# 첫번째 숫자 입력
# 두번째 숫자 입력
# 짝수의 합

first   = int(input("첫번째 숫자를 입력하시오"))
second  = int(input("두번째 숫자를 입력하시오"))
sum = 0

arr = range(first,second+1)

for i in arr:
    if i%2 == 0:
        sum += i

print("2의 배수의 합은 {} 입니다.".format(sum))
