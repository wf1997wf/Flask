���ȣ���һ��ʹ��Flask�Ļ������裺
1.����һ������Ŀ�����洴��һ��.py�ļ���

from flask import Flask

#importing flask module
app = Flask(__name__)

#decorating index function with the app.route
@app.route('/')
def index():
    response = make_response(render_template('tmp_map.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # ȡ������
    response.headers['Pragma'] = 'no-cache'  # ��ֹ����
    return response

@app.route('/hh')
def index():
    return render_template('hh.html')

@app.route('/hhh')
def index():
    return "hhh"

if __name__ == '__main__':
    app.run()

2.�����е�html��Ҫ��������ʱ��
�����ļ����ｨtemplates�ļ��У��ļ��������login.html��success.html

login.html���£�����Ҫ����������Ϊemile��
<body>
<form method="post" action="/success">
	<input type="text" name="email" placeholder="Enter Email Address">
	<br><br>
	<input type="password" name="pass" placeholder="Password">
	<input type="submit" value="Submit" name="ok">
</form>
</body>

��Ϊʹ����html������Ҫ����reder_template
.py�ļ������£�
from flask import Flask,render_template��request

app = Flask(__name__)

@app.route('/login')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()

��Ҫ����ť��success.html���������������success.html
<body>
<h2>You have successfully registered with email {{ email }}</h2>
</body>

{{email}}��login.html���͵�ֵ��

������.py�ļ���
@app.route('/success' ,method=['POST'])
def success():
    if request.method == 'POST':
	email = request.form['email']    #�������е�login.html��form�е�name='email'�ж�ȡemail������
	return render_template('success.html',email=email)#�͸�success.html
    else:
	pass


�Ƽ�һ���ܺõĽ̳̣�
https://baijiahao.baidu.com/s?id=1578181786711427689&wfr=spider&for=pc

