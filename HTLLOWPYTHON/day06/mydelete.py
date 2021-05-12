import pymysql

# DB 데이터 삭제
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor() # java에서의 statement
 
sql = """DELETE FROM hello WHERE col01 = 1"""
cnt = curs.execute(sql)
print("cnt : ",cnt);
conn.commit()
 
conn.close()