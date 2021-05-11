import urllib.request
from bs4 import BeautifulSoup
import pymysql

def insertStock(tups):
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
     
    curs = conn.cursor() # java에서의 statement
    
    sql = """insert into stock2(
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
if(rescode==200):
    curs = conn.cursor()
    response_body = response.read()
    
    html = response_body.decode('euc-kr') 
    soup = BeautifulSoup(html, 'html.parser') 
    
    tuts = []
    #items = soup.select(".st2")
    #print(items)
    
    # s_name : tag
    #items = soup.select_one(".st2")
    #s_name_item = items.a
    #s_name = s_name_item.get_text()
    #print(s_name)
    
    # s_name : contents
    #items = soup.select_one(".st2")
    #s_name_item_tag_arr = items.contents
    #s_name_item_tag = s_name_item_tag_arr[0]
    #s_name_item_arr = s_name_item_tag.contents
    #s_name = s_name_item_arr[0]
    #print(s_name)
    
    # s_name : children
    #items = soup.select_one(".st2")
    #s_name_item_tag_arr = items.contents
    #s_name_item_tag = s_name_item_tag_arr[0]
    #for s_name_item in s_name_item_tag.children:
    #    print(s_name_item)
    
    # s_name : descendants
    #items = soup.select_one(".st2")
    #for s_name_item in items.descendants:
    #    print(s_name_item)
    
    # s_name : children 과 descendants 비교
    #items = soup.select_one(".st2")
    #print(len(list(items.children)))
    #print(len(list(items.descendants)))
    
    # s_name : next_element [<> previous_elements]
    #items = soup.select_one(".st2")
    #s_name_item_tag_arr = items.contents
    #s_name_item_tag = s_name_item_tag_arr[0]
    #s_name = s_name_item_tag.next_element
    #print(s_name)
    
    # s_name : next_sibling : a 태그 옆 출력 : 아무것도 없음.
    #items = soup.select_one(".st2")
    #s_name_item_tag_arr = items.contents
    #s_name_item_tag = s_name_item_tag_arr[0]
    #s_name = s_name_item_tag.next_sibling
    #print(s_name)
    
    # s_name : find_all(tag)
    #items = soup.select_one(".st2")
    #s_name_tag_arr = items.find_all("a")
    #s_name_tag = s_name_tag_arr[0]
    #s_name = s_name_tag.get_text()
    #print(s_name)
    
    #s_name : 태그 호출
    #items = soup.select_one(".st2")
    #s_name_tag_arr = items("a")
    #s_name_tag = s_name_tag_arr[0]
    #s_name = s_name_tag.get_text()
    #print(s_name)
    
    # s_name : find
    #items = soup.select_one(".st2")
    #s_name_tag = items.find("a")
    #s_name = s_name_tag.get_text()
    #print(s_name)
    

    # s_code
    #items = soup.select_one(".st2")
    #print(items)
    #s_code_item = items.a
    #print(s_code_item)
    #s_code = s_code_item['title']
    #print(s_code)
    

    # s_price : string
    #items = soup.select_one(".st2")
    #test = items.a.next_element.next_element.next_element.string
    #print(test)
    
    # s_price : find_next_sibling()
    #items = soup.select_one(".st2")
    #s_price_tag = items.find_next_sibling("td")
    #s_price = s_price_tag.get_text()
    #print(s_price)
    
    
    date = soup.select_one(".t_11_black").get_text()
    crawl_date = "2021"+date.replace(".","").replace(" ",".").replace(":","")
    
    items = soup.select(".st2")
    tuts = []
    for i,item in enumerate(items):
        print(item)
        s_code = item.a['title']
        print(s_code)
        s_name = item.a.get_text()
        print(s_name)
        s_price = item.find_next_sibling("td").get_text().replace(",","")
        print(s_price)
    
        tuts.append((
            s_code,
            s_name,
            s_price,
            crawl_date,
        ))

    cnt = insertStock(tuts)
    print("cnt : ",cnt)
else:
    print("Error Code:" + rescode)