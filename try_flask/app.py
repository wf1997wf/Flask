from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/<email>/success')
def success(email):
    return render_template('success.html',email=email)

if __name__ == '__main__':
    app.run()
