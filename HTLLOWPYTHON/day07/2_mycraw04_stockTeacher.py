import urllib.request
import pymysql
import time

from bs4 import BeautifulSoup
from datetime import datetime

#주식사이트 주식 정보 크롤링하여 DB에 저장 (선생님 코드)
def insertStock(tuts):
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
    cnt = curs.executemany(sql, tuts)
    
    conn.commit()
    conn.close()
    return cnt


for i in range(10):
    url = "https://vip.mk.co.kr/newSt/rate/item_all.php"
    
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        html = response_body.decode('euc-kr')
        soup = BeautifulSoup(html, 'html.parser')
        
        now = datetime.now()
        crawl_date = now.strftime("%Y%m%d.%H%M")
    
        tuts = []
        
        items = soup.select(".st2")
        for i, item in enumerate(items):
            #print(item)
            #print(item.text)
            #print(item.a['title'])
            #print(item.parent)
            #print(item.parent.td)
            #print(item.parent.select('td'))
            #print(item.parent.select('td')[1])
            #print(item.parent.select('td')[1].text)
            #print(item.parent.select('td')[1].text.replace(",",""))
            
            s_code = item.a['title']
            s_name = item.text
            s_price = item.parent.select('td')[1].text.replace(',','')
    
            tuts.append((s_code,s_name,s_price,crawl_date))
            
        cnt = insertStock(tuts)
        print("cnt :",cnt) 
    
        
    else:
        print(response.status_code)
        
    time.sleep(60)