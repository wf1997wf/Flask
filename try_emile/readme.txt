首先，看一下使用Flask的基本步骤：
1.创建一个新项目，里面创建一个.py文件：

from flask import Flask

#importing flask module
app = Flask(__name__)

#decorating index function with the app.route
@app.route('/')
def index():
    response = make_response(render_template('tmp_map.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # 取消缓存
    response.headers['Pragma'] = 'no-cache'  # 禁止缓存
    return response

@app.route('/hh')
def index():
    return render_template('hh.html')

@app.route('/hhh')
def index():
    return "hhh"

if __name__ == '__main__':
    app.run()

2.工程中的html需要“交流”时：
工程文件夹里建templates文件夹，文件夹里包含login.html和success.html

login.html如下：（需要交流的内容为emile）
<body>
<form method="post" action="/success">
	<input type="text" name="email" placeholder="Enter Email Address">
	<br><br>
	<input type="password" name="pass" placeholder="Password">
	<input type="submit" value="Submit" name="ok">
</form>
</body>

因为使用了html，所以要导入reder_template
.py文件先如下：
from flask import Flask,render_template，request

app = Flask(__name__)

@app.route('/login')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()

而要将按钮与success.html连接起来，先设计success.html
<body>
<h2>You have successfully registered with email {{ email }}</h2>
</body>

{{email}}是login.html发送的值。

再扩充.py文件：
@app.route('/success' ,method=['POST'])
def success():
    if request.method == 'POST':
	email = request.form['email']    #从请求中的login.html的form中的name='email'中读取email的内容
	return render_template('success.html',email=email)#送给success.html
    else:
	pass


推荐一个很好的教程：
https://baijiahao.baidu.com/s?id=1578181786711427689&wfr=spider&for=pc

