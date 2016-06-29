import sqlite3
from flask import *
app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

def get_db():
    db = getattr(g, '_db', None)
    if db is None:
        db = g._db = connect_db()
    return db

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        print(request.form['user_name'])
        db =  get_db()
        cursor = db.cursor()
        cursor.execute('SELECT password FROM account WHERE name = ?',(user_name,))
        pw = cursor.fetchone()
        if password == pw:
            return render_template('login.html', state="登陆成功")
        return render_template('login.html', state="用户名或者密码错误")
    else:
        return render_template('login.html', state="未登陆")

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)