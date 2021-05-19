import pymysql

# class를 생성하여 crud 수행
class DaoExam:
    def __init__(self): # 생성자
        self.conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
        
    def myselect(self):
        ret = []
        curs = self.conn.cursor()
        sql = "select e_id,kor,eng,math from exam"
        curs.execute(sql)
         
        rows = curs.fetchall()
        
        for row in rows:
            ret.append({"e_id":row[0],"kor":row[1],"eng":row[2],"math":row[3]})
            
        return ret
    
    def myinsert(self,e_id,kor,eng,math):
        curs = self.conn.cursor()

        sql = """insert into exam(e_id,kor,eng,math)
                 values ('{}', '{}', '{}', '{}')""".format(e_id,kor,eng,math)
                 # values 할 때 ''를 써야함. 한글이 들어갔을 때 문자인 것을 알려줘야함.
        cnt = curs.execute(sql)
        
        self.conn.commit()
        return cnt
    
    def myupdate(self,e_id,kor,eng,math):
        curs = self.conn.cursor()

        sql = f"""
                update exam 
                set 
                e_id = '{e_id}'
                , kor = '{kor}'
                , eng = '{eng}'
                , math = '{math}'
                where e_id = '{e_id}'
            """
        
        cnt = curs.execute(sql)
        
        self.conn.commit()
        return cnt
    
    def mydelete(self,e_id):
        curs = self.conn.cursor()

        sql = f"""DELETE FROM exam WHERE e_id = '{e_id}'"""
        
        cnt = curs.execute(sql)
        
        self.conn.commit()
        return cnt
        
    def __del__(self):
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoExam()
    #list = de.myselect()
    #print(list)
    cnt = de.myinsert("2", "2", "2","2")
    print(cnt)
    #cnt = de.myupdate()
    #print(cnt)
    #cnt = de.mydelete()
    #print(cnt)