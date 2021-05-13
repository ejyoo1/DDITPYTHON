from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql

# 전체 주가 구현 곡선 굴곡 (10개 데이터) 선생님 코드
def getPrices(s_name):
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    
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
        ret.append(row[0])
        
    conn.close()
    return np.array(ret)

def getNames():
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    curs = conn.cursor()
    
    sql = """SELECT s_name 
                FROM stock 
                GROUP BY s_name limit 5;"""
    
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        ret.append(row[0])
    
    return ret

arr_name = getNames()
print(arr_name)

arrz = []
for i in range(len(arr_name)):
    arrz.append(getPrices(arr_name[i]))

arr_per_z = []
for i in range(len(arr_name)):
    imsi = (arrz[i] / arrz[i][0]) * 100 # nump라서 한번만 해도 가능
    arr_per_z.append(imsi)

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.array([1,1,1,1,1,1,1,1,1,1]) # 가로
y = np.array([0,1,2,3,4,5,6,7,8,9]) # 세로

for i in range(len(arr_name)):
    ax.plot3D(x+i, y, arr_per_z[i])

ax.set_title('3D line plot')
plt.show()