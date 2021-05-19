from flask import Flask, request

#get, post 방식 접근
# myFlask03.html 에서 입력한 값을 result.html에 출력
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    a = request.form.get("a", "홍길동")
    return 'hello {}'.format(a)

if __name__ == '__main__':
    app.run(debug=True)