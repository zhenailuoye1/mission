from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       print(request.form['user_name'])
       return "登陆成功"
    else:
       return render_template('login.html', state="未登陆")

if __name__ == '__main__':
    app.run(debug=True)