from flask import Flask, render_template, request

#parameter list => templates\index.html
# render_template을 사용해서 templates 안의 index.html에 출력하기
app = Flask(__name__)

@app.route('/')
def a():
    title = "리스트 보기"
    mylist = ["최윤성","김이현","공슬기","김민지"]
    
    objlist =[]
    objlist.append({"e_id":"1","e_name":"1","e_birth":"1"})
    objlist.append({"e_id":"1","e_name":"1","e_birth":"1"})

    return render_template('index.html',mylist=mylist, title=title, objlist=objlist)
if __name__ == '__main__':
    app.run(debug=True)