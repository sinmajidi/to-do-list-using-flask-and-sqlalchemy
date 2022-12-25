from flask import render_template,request,redirect,make_response,flash
from database import db
from database import app
from database import Do,Users
import datetime
db.create_all()

@app.route("/add",methods=['POST','GET'])
def add():
    if request.cookies.get("user"):
        if request.method=='POST':
            subject = request.form.get('subject')
            date = request.form.get('date')
            time = request.form.get('time')
            details = request.form.get('details')
            flash("add to Do list", "primary")
            x = datetime.datetime.now()
            admin=Do(subject=subject,time=time,date=date,t=x.strftime("%c"),author=Users.query.filter_by(username=request.cookies.get("user")).first(),details=details)
            db.session.add(admin)
            db.session.commit()
            return redirect('/')
        else:
            return render_template('add.html')
    else:
        return redirect('/login')
@app.route("/",methods=['POST','GET'])
def home():
    return render_template('index.html',user=request.cookies.get("user"),subject=Do.query.all(),items=len(Do.query.all()))
@app.route("/delete/<int:post_id>",methods=['POST','GET'])
def delete(post_id):
    if request.cookies.get("user"):
         do=Do.query.get(post_id)
         db.session.delete(do)
         db.session.commit()
         return redirect("/")
    else:
        return redirect('/login')
@app.route("/show_details/<int:post_id>",methods=['POST','GET'])
def show_details(post_id):
    if request.cookies.get("user"):
         do=Do.query.get(post_id)
         return render_template('details.html',user=request.cookies.get("user"),subject=do)

    else:
        return redirect('/login')
@app.route("/logout")
def logout():
    flash("user log out","danger")
    response = make_response(redirect('/login'))
    response.delete_cookie("user")
    return response
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user = request.form.get('user')
        pas = request.form.get('pas')
        found=False
        for u in range(len(Users.query.all())):
            if user==Users.query.all()[u].username and pas==Users.query.all()[u].password:
                flash("user login","success")
                response=make_response(redirect('/'))
                response.set_cookie("user",user)
                found = True
                return response
        if found==False:
                flash("user or pass wrong", "danger")
                return render_template('login.html')
    return render_template('login.html')
@app.route('/register',methods=['POST','GET'])
def Register():
    if request.method=='POST':
        user_name1 = request.form.get('user')
        password1 = request.form.get('pas')
        re_password = request.form.get('pass')
        if password1==re_password:
            admin1=Users(username=user_name1,password=password1)
            db.session.add(admin1)
            db.session.commit()
            flash("user Register","success")
            return redirect('/add')
        else:
            flash("password or re_password wrong","danger")
            return render_template('Register.html')
    else:
        return render_template('Register.html')
if __name__=='__main__':
    app.run(host='0.0.0.0',port=80)
