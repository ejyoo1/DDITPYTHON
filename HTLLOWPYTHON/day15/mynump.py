import numpy as np

# nump의 장점 : 선형대수학을 쉽게 해주는 것
# ones와 zeros 만으로도 모든 숫자를 표시할 수 있음.
a = np.zeros((2))
b = np.zeros((100,100))
c = np.ones((5,5))*4

print(a)
print(b)
print(c)
print(a.shape)
print(b.shape)
print(c.shape)

d = np.zeros((4,4))
e = d.reshape(16) #4*4를 1줄로
print(e)