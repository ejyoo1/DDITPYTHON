from flask import Flask,request

# http://127.0.0.1:5000 get 방식 출력
# 넘어온 파라미터 a 값이 없으면 '하하하' 출력
app = Flask(__name__)

@app.route('/')
def home():
    a = request.args.get('a', "하하하")
    return 'hello, {}'.format(a)

if __name__ == '__main__':
    app.run(debug=True)