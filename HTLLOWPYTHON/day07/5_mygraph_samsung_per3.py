from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql
import random

# 전체 주가 구현 곡선 굴곡 (10개 데이터)
conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
curs = conn.cursor()
def getNames():
    arr_name = []
    sql = """SELECT s_name 
                FROM stock 
                GROUP BY s_name;"""
    
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        arr_name.append(row[0])
    
    return arr_name

def getPrices(s_name):
    arr_z = []
    curs = conn.cursor()
    sql = """SELECT
                s_price 
            FROM stock 
            WHERE s_name= '{}'
            ORDER BY crawl_date;""".format(s_name)
    
    print(sql)
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        arr_z.append(row[0])
    return arr_z

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    color = (r,g,b,1)
    return color

names = getNames();
print("names",names)

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.array([1,1,1,1,1,1,1,1,1,1]) # 가로
y = np.array([0,1,2,3,4,5,6,7,8,9]) # 세로

z = []
for i,name in enumerate(names):
    z_np = np.array(getPrices(name)) #z 축 수정
    color = random_color()
    print(i,z_np)
    
    z = (z_np / z_np[0]) * 100
    print(i,z)
    ax.plot3D(x, y, z, c = color)

    ax.set_title('3D line plot')
plt.show()
conn.close()