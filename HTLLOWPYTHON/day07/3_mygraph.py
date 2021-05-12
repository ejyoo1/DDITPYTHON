from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# 그래프 그리기 샘플코드 활용한 코드
fig = plt.figure()
ax = plt.axes(projection='3d')

#직선
#z = np.array([0,1,2,3,4])
#x = np.array([1,1,1,1,1])
#y = np.array([1,2,3,4,5])
#print(z)

#직선 : 점찍어서 직선됨
#x = z
#y = z

#for i in z:
#    print(i)

#print(z)

# 곡선 굴곡
#z = np.array([2,1,2,1,4]) #z 축 수정
#x = np.array([1,1,1,1,1])
#y = np.array([1,2,3,4,5])

# 삼성전자 주가 구현 곡선 굴곡 (10개 데이터)
z = np.array([2,1,2,1,4,2,1,2,1,4]) #z 축 수정
x = np.array([1,1,1,1,1,1,1,1,1,1]) # 가로
y = np.array([0,1,2,3,4,5,6,7,8,9]) # 세로
print(z)

ax.plot3D(x, y, z, 'maroon')
ax.set_title('3D line plot')
plt.show()