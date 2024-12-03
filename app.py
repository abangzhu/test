import itchat
from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def qr_code():
    uuid = itchat.get_QRuuid()
    qr_code_url = itchat.get_QR(uuid)
    return render_template('index.html', qr_code_url=qr_code_url)

@app.route('/login')
def login():
    itchat.auto_login(hotReload=True)
    return "登录成功!"

if __name__ == '__main__':
    app.run(debug=True)