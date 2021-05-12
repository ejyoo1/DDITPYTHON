import pymysql
 
 # 주식 저장 DB에 데이터 삽입하기
def insertStock(tups):
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
     
    curs = conn.cursor() # java에서의 statement
    
    sql = """insert into stock(
            s_code
            ,s_name
            ,s_price
            ,crawl_date
            )
         values (%s, %s, %s, %s)"""
    cnt = curs.executemany(sql, tups)
    
    conn.commit()
    conn.close()
    return cnt

if __name__ == '__main__':
    tuts = []
    tuts.append((1,1,1,1))
    cnt = insertStock(tuts)
    print("cnt",cnt)