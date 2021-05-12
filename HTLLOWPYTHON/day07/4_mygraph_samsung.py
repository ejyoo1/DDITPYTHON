from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql

# 삼성전자, 삼성전자우, 두산 주가 구현 곡선 굴곡 (10개 데이터)
# 사용자에게 보이는 영역은 자동으로 세팅된다.
def getPrices(s_name):
    arr_z = []
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
        arr_z.append(row[0])
        
    conn.close()
    return arr_z

fig = plt.figure()
ax = plt.axes(projection='3d')
z1 = np.array(getPrices("삼성전자")) #z 축 수정
z2 = np.array(getPrices("삼성전자우")) #z 축 수정
z3 = np.array(getPrices("두산")) #z 축 수정

x = np.array([1,1,1,1,1,1,1,1,1,1]) # 가로
y = np.array([0,1,2,3,4,5,6,7,8,9]) # 세로

ax.plot3D(x, y, z1, 'red')
ax.plot3D(x, y, z2, 'yellow')
ax.plot3D(x, y, z3, 'green')
ax.set_title('3D line plot')
plt.show()