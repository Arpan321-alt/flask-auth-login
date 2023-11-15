from flask import Flask,render_template,request,flash,redirect,url_for
from models import db,User 
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///user2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='auth-flask'

db.init_app(app)

@app.route('/',methods=['GET','POST'])
def login_page():
    return render_template('login.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/auth_data',methods=['GET','POST'])
def auth():
    db.create_all()
    username=request.form.get('username')
    password=request.form.get('password')
    email=User.query.filter_by(username=username).first()
    if email:
        flash('email or username already registered')
        return redirect('/login')
    userModel=User(username=username,password=password)
    db.session.add(userModel)
    db.session.commit()
    return 'data is registered'

@app.route('/register_template',methods=['GET','POST'])
def registeration():
    return render_template('register.html')
    

if __name__=='__main__':
    app.run('0.0.0.0',port=5002)