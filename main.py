from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

# 用户数据库
user_database = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    # 使用SHA-256加密密码
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # 将用户名和加密后的密码存储到用户数据库
    user_database[username] = hashed_password

    return "注册成功！"


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # 使用SHA-256加密密码
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # 检查用户名和密码是否匹配
    if username in user_database and user_database[username] == hashed_password:
<<<<<<< HEAD
        return "登录成功！!!@Q@"
    else:
        return "登录失败！!!@Q@"
=======
        return "登录成功！"
    else:
        return "登录失败！"
>>>>>>> parent of 9b59df7 (test1)


if __name__ == '__main__':
    app.run(debug=True)
