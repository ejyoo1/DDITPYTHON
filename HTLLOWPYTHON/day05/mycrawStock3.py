import urllib.request
from bs4 import BeautifulSoup
import pymysql

def insertTest(tups):
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
     
    curs = conn.cursor() 
    
    sql = """insert into test(
            one_td_Title
            ,one_td_txt
            ,two_td_txt
            )
         values (%s, %s, %s)"""
    cnt = curs.executemany(sql, tups)
    
    conn.commit()
    conn.close()
    return cnt

conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')

url = "웹 사이트 경로 입력"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    curs = conn.cursor()
    response_body = response.read()
    
    html = response_body.decode('euc-kr') 
    soup = BeautifulSoup(html, 'html.parser') 
    
    items = soup.select(".one")
    tuts = []
    for i,item in enumerate(items):
        print(item)
        one_td_Title = item.a['title']
        print(one_td_Title)
        one_td_txt = item.a.get_text()
        print(one_td_txt)
        two_td_txt = item.find_next_sibling("td").get_text().replace(",","")
        print(two_td_txt)
    
        tuts.append((
            one_td_Title,
            one_td_txt,
            two_td_txt,
        ))

    cnt = insertTest(tuts)
    print("cnt : ",cnt)
else:
    print("Error Code:" + rescode)
    
    
    # one_td_txt : tag
    #items = soup.select_one(".st2")
    #one_td_txt_item = items.a
    #one_td_txt = one_td_txt_item.get_text()
    #print(one_td_txt)
    
    # one_td_txt : contents
    #items = soup.select_one(".st2")
    #one_td_txt_item_tag_arr = items.contents
    #one_td_txt_item_tag = one_td_txt_item_tag_arr[0]
    #one_td_txt_item_arr = one_td_txt_item_tag.contents
    #one_td_txt = one_td_txt_item_arr[0]
    #print(one_td_txt)
    
    # one_td_txt : children
    #items = soup.select_one(".st2")
    #one_td_txt_item_tag_arr = items.contents
    #one_td_txt_item_tag = one_td_txt_item_tag_arr[0]
    #for one_td_txt_item in one_td_txt_item_tag.children:
    #    print(one_td_txt_item)
    
    # one_td_txt : descendants
    #items = soup.select_one(".st2")
    #for one_td_txt_item in items.descendants:
    #    print(one_td_txt_item)
    
    # one_td_txt : children 과 descendants 비교
    #items = soup.select_one(".st2")
    #print(len(list(items.children)))
    #print(len(list(items.descendants)))
    
    # one_td_txt : next_element [<> previous_elements]
    #items = soup.select_one(".st2")
    #one_td_txt_item_tag_arr = items.contents
    #one_td_txt_item_tag = one_td_txt_item_tag_arr[0]
    #one_td_txt = one_td_txt_item_tag.next_element
    #print(one_td_txt)
    
    # one_td_txt : next_sibling : a 태그 옆 출력 : 아무것도 없음.
    #items = soup.select_one(".st2")
    #one_td_txt_item_tag_arr = items.contents
    #one_td_txt_item_tag = one_td_txt_item_tag_arr[0]
    #one_td_txt = one_td_txt_item_tag.next_sibling
    #print(one_td_txt)
    
    # one_td_txt : find_all(tag)
    #items = soup.select_one(".st2")
    #one_td_txt_tag_arr = items.find_all("a")
    #one_td_txt_tag = one_td_txt_tag_arr[0]
    #one_td_txt = one_td_txt_tag.get_text()
    #print(one_td_txt)
    
    #one_td_txt : 태그 호출
    #items = soup.select_one(".st2")
    #one_td_txt_tag_arr = items("a")
    #one_td_txt_tag = one_td_txt_tag_arr[0]
    #one_td_txt = one_td_txt_tag.get_text()
    #print(one_td_txt)
    
    # one_td_txt : find
    #items = soup.select_one(".st2")
    #one_td_txt_tag = items.find("a")
    #one_td_txt = one_td_txt_tag.get_text()
    #print(one_td_txt)
    

    # one_td_Title
    #items = soup.select_one(".st2")
    #print(items)
    #one_td_Title_item = items.a
    #print(one_td_Title_item)
    #one_td_Title = one_td_Title_item['title']
    #print(one_td_Title)
    

    # two_td_txt : string
    #items = soup.select_one(".st2")
    #test = items.a.next_element.next_element.next_element.string
    #print(test)
    
    # two_td_txt : find_next_sibling()
    #items = soup.select_one(".st2")
    #two_td_txt_tag = items.find_next_sibling("td")
    #two_td_txt = two_td_txt_tag.get_text()
    #print(two_td_txt)