import pymysql

def insertChicken(tups):
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
     
    curs = conn.cursor() # java에서의 statement
    
    sql = """insert into hello(col01,col02,col03)
             values (%s, %s, %s)"""
    cnt = curs.executemany(sql, tups)
    
    conn.commit()
    conn.close()
    return cnt

if __name__ == '__main__': # java에서의 main 처럼 실행해줌
    tups = []
    
    tups.append(('1','1','1'))
    tups.append(('2','1','1'))
    tups.append(('3','1','1'))
    tups.append(('4','1','1'))
    cnt = insertChicken(tups)
    print("cnt:",cnt)
