之前的里面两个网页的交流，限于form里的action属性的帮忙，但一般的交流难以直接套用，现做出改进：

.py文件中：
@app.route('/<email>/success')
def success(email):
    return render_template('success.html',email=email)
#其中，<>中的东西的默认数据类型为string，如果要指定类型时，可以写为：
<type:name>,其中type为类型名，有
int，
float，
path（同string，但可以接受/），
uuid（唯一识别码），
any（多种路径）eg：<any(article,blog):url_path>,即url_path的值可以为article,blog中任何一个。

如果需要传递的参数在login.html中为email：
login.html文件如下：
var email="123@163.com";
function c(){
    self.location.href="http://127.0.0.1:5000/"+email+"/success";
}

则实现email的传递。


另补充：
1.让其他电脑可以访问：
app.run(host='0.0.0.0')

2.route()的作用：把函数绑定在这个URL上，注意.py中的函数不可重名。

3.URL重定向：
from flask import redirect
@app.route('/about/aa')
def aa():
    return redirect('/projects/')
