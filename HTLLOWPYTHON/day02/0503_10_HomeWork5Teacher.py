# 첫번째 숫자 입력
# 두번째 숫자 입력
# 홀수의 합

first   = int(input("첫번째 숫자를 입력하시오"))
second  = int(input("두번째 숫자를 입력하시오"))
sum = 0

arr = range(first,second+1)

for i in arr:
    if i%2 == 1:
        sum += i

print("홀수의 합은 {} 입니다.".format(sum))

