import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor() # java에서의 statement
 
data = [
    (4, '4', '4'),
    (5, '5', '5'),
    (6, '6', '6'),
]

data.append(('1','1','1'))

sql = """insert into hello(col01,col02,col03)
         values (%s, %s, %s)"""
cnt = curs.executemany(sql, data)
print("cnt : ",cnt);
conn.commit()
 
conn.close()