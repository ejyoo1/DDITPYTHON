import numpy as np

# array를 np형태로 변경
arr = [1,2,3,4,5]
arr_n = np.array(arr) # 배열이 아닌 nump 형태로 바꾸어주라.

print(arr)
print(arr_n)

# 배열과 동일하지만 nump만의 장점이 있음.

# arr arr_n의 장점 구분
# nump를 사용하면 수학적 계산을 편리하게 하고
#arr = arr * 5
#print(arr) # 1,2,3,4,5,1,2,3,4,5,1,2,3,4,5

#arr_n = arr_n * 5
#print(arr_n) # 5 10 15 20 25

#arr_n = arr_n - 5
#print(arr_n)

arr_n = arr_n % 2
print(arr_n)

# opencv : computer vision
# opency AI에서도 많이 쓰임
# AI 
# 구글 tensorflow
# 구글 kenas