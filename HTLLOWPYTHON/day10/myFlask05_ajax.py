from flask import Flask, render_template, jsonify, request

# 정적인 파일에 ajax 데이터 출력하기. jquery-3.6.0.js 필요
# 원래는 정적인 파일을 올리기 위해서는 static 폴더를 만들어야 함.
# static 폴더를 만들지 않고 static_url_path를 설정하여 정적인 폴더 위치를 알려줌.
# app.route는 java의 servlet url anntaion과 같다고 생각하기.
app = Flask(__name__,static_url_path='')

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.get_json()
    print(data)

    return jsonify(result = "success", result2= data)


if __name__ == '__main__':
    app.run(debug=True)