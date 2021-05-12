import urllib.request
from bs4 import BeautifulSoup
import pymysql

# 네이버 API 를 사용하여 검색 크롤링 후 DB 저장
def insertChicken(tups):
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
     
    curs = conn.cursor() # java에서의 statement
    
    sql = """insert into chicken(
            title
            ,link
            ,description
            ,bloggername
            ,bloggerlink
            ,postdate
            )
         values (%s, %s, %s, %s, %s, %s)"""
    cnt = curs.executemany(sql, tups)
    
    conn.commit()
    conn.close()
    return cnt


conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')

client_id = "eWj8drgkHgjyO6APRHlC"
client_secret = "t5l653Q7V2"
encText = urllib.parse.quote("치킨")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    curs = conn.cursor()
    response_body = response.read()
    
    html = response_body.decode('utf-8') # enclipse : 암호화 거는것
    soup = BeautifulSoup(html, 'xml') # parser에 따라 데이터가 읽어올 수 있음 원본 자료 참고할 것
    
    tuts = []
    items = soup.select("item")
    for i,item in enumerate(items):
        title       = item.title.text
        link        = item.link.text
        description = item.description.text
        bloggername = item.bloggername.text
        bloggerlink = item.bloggerlink.text
        postdate    = item.postdate.text
        
        tuts.append((
            title,
            link,
            description,
            bloggername,
            bloggerlink,
            postdate
            ))

    
    
    cnt = insertChicken(tuts)
    print("cnt : ",cnt)
else:
    print("Error Code:" + rescode)