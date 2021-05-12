import pymysql
 
# DB Update
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
sql = """
        update hello 
        set 
        col02 = '2'
        , col03 = '2'
        where col01 = '3'
    """

cnt = curs.execute(sql)
print("cnt : ", cnt)

conn.commit()
 
conn.close()