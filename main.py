import sqlite3
from flask import *
app = Flask(__name__)

def connect_db():
    return sqlite3.connect('/path/to/database.db')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = request.form['user_name']
        p = request.form['password']
        n = request.form['email']
        with connect_db() as con
            cur = con.cursor()
            cur.execute('SELECT password FROM account WHERE user_name = %s',(u,))
            if u == cur.fetchone():
                return render_template('login.html', state="登陆成功")
            else:
                return render_template('login.html', state="未登陆")
    else:
       return render_template('login.html', state="未登陆")

if __name__ == '__main__':
    app.run(debug=True)