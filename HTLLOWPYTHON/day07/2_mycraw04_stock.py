import urllib.request
import pymysql

from bs4 import BeautifulSoup

# 주식 사이트 크롤링하여 DB에 저장
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


conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    
    html = response_body.decode('euc-kr')
    soup = BeautifulSoup(html, 'html.parser')
    
    text = soup.select_one(".t_11_black").get_text()
    crawl_date = "2021"+text.replace(".","").replace(" ",".").replace(":","")
    
    items = soup.select(".st2")
    
    tuts = []
    for i,item in enumerate(items):
        s_name = item.a.get_text()
        s_price = item.find_next_sibling("td").get_text().replace(",","")
        s_code = item.a['title']
        
        tuts.append((
                s_code,
                s_name,
                s_price,
                crawl_date,
                ))
    
    cnt = insertStock(tuts)
    print("cnt : ",cnt)
else:
    print(response.status_code)