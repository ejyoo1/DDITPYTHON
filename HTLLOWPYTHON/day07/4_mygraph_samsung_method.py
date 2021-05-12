import pymysql

# 삼성전자 주가 구현 곡선 굴곡 (10개 데이터)
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
    return ret

if __name__ == '__main__':
    ret = getPrices("삼성전자")
    print(ret)