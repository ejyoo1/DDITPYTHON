from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# 그래프 그리기 샘플 코드
fig = plt.figure()
ax = plt.axes(projection='3d')
z = np.linspace(0, 1, 100) # 선형대수학 ( 0에서부터 1까지 100조각 )
x = z * np.sin(30 * z) # 원 하나에 6조각이라 쳣을 때 30이면 5번 돌림
y = z * np.cos(30 * z) 

ax.plot3D(x, y, z, 'maroon')
ax.set_title('3D line plot')
plt.show()