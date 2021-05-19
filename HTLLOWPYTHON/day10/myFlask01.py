from flask import Flask

# http://127.0.0.1:5000 접속 시 Hellow World 출력
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)