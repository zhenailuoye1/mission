from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import *
from flask_script import Manager

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
app = Flask(__name__)
manager = Manager(app)
# 以上全部为 1

# 2
class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer,Sequence('account_id_seq'), primary_key=True)
    name = Column(Integer)
    password = Column(String)
    email = Column(String)
    def __repr__(self):
        return '<Account %r>' % self.name

    def check_password(self, input_pw):
        #import pdb; pdb.set_trace()
        return  input_pw == self.password

@app.route('/')
def index():
    return render_template('index.html')

# 2
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db_session = Session()
        form_pw = request.form['password']
        form_un = request.form['user_name']   
        account = db_session.query(Account).filter_by(name=form_un).first()
        if account and account.check_password(form_pw):
            #import pdb; pdb.set_trace()
            session['username'] = form_un
            return 'ok'
        else:
            return "error"
    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return 'ok'

# 3 
@app.route('/account')
def account():
    if need_login():
        return redirect(url_for('login'))
    return render_template('account.html')

def need_login():
    return 'username' not in session
        
# 1
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    manager.run()