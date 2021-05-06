# 첫번쨰 숫자를 입력
# 두번째 숫자를 입력
# 첫번째부터 두번째 숫자까지 출력

first   = int(input("첫번째 숫자를 입력하시오"))
second  = int(input("두번째 숫자를 입력하시오"))
sum = 0

arr = range(first,second+1)

for i in arr:
    sum = sum + i

print("숫자의 합은 {} 입니다.".format(sum))

