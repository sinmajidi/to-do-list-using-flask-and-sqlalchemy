from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SECRET_KEY']='jhvhijghlkbvhjvjkjhvcj'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.Text)
    password = db.Column(db.Text)
    does = db.relationship('Do', backref='author', lazy=True)
    def __repr__(self):
        return f'acant({self.username},{self.password})'
class Do(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    subject=db.Column(db.Text)
    date = db.Column(db.Text)
    time = db.Column(db.Text)
    t = db.Column(db.Text)
    details = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    def __repr__(self):
        return f'Do({self.id},{self.subject},{self.date},{self.time},{self.time})'

