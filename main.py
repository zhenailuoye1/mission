import sqlite3
from flask import *
app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

def get_db():
    db = getattr(g, '_db', None)
    if db is None:
        g._db = connect_db()
        db = g._db
    return db

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_un = request.form['user_name']
        form_pw = request.form['password']
        print(request.form['user_name'])
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute('SELECT password FROM account WHERE name = ?',(form_un,))
            account_pw = cursor.fetchone()
            if account_pw and account_pw[0] == form_pw:
                return "ok"
            return "error"
    else:
        return render_template('login.html')

@app.route('/account')
def account():
    return render_template('account.html')

if __name__ == '__main__':
    app.run(debug=True)