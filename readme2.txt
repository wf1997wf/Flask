֮ǰ������������ҳ�Ľ���������form���action���Եİ�æ����һ��Ľ�������ֱ�����ã��������Ľ���

.py�ļ��У�
@app.route('/<email>/success')
def success(email):
    return render_template('success.html',email=email)
#���У�<>�еĶ�����Ĭ����������Ϊstring�����Ҫָ������ʱ������дΪ��
<type:name>,����typeΪ����������
int��
float��
path��ͬstring�������Խ���/����
uuid��Ψһʶ���룩��
any������·����eg��<any(article,blog):url_path>,��url_path��ֵ����Ϊarticle,blog���κ�һ����

�����Ҫ���ݵĲ�����login.html��Ϊemail��
login.html�ļ����£�
var email="123@163.com";
function c(){
    self.location.href="http://127.0.0.1:5000/"+email+"/success";
}

��ʵ��email�Ĵ��ݡ�