#!flask/bin/python

#-*- coding:utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from flask import Flask, render_template, json
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from sqlalchemy.ext.serializer import loads, dumps

app.config['SECRET_KEY'] = 'hard to guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootroot@localhost:3306/zol'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
session = db.session()

class PhoneInfo(db.Model):
    __tablename__ = 'zolphone'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.String(100))
    product_url = db.Column(db.String(100))
    par_1 = db.Column(db.Text)
    par_2 = db.Column(db.Text)
    par_3 = db.Column(db.Text)
    par_4 = db.Column(db.Text)
    par_5 = db.Column(db.Text)
    par_6 = db.Column(db.Text)
    par_7 = db.Column(db.Text)
    
    def __repr__(self):
        return '<PhoneInfo {}> '.format(self.title)
    def serialize(self):
        return {
           'id': self.id,
           'title': self.title,
           'price': self.price,
           'product_url': self.product_url,
           'par_1': self.par_1,
           'par_2': self.par_2,
           'par_3': self.par_3,
           'par_4': self.par_4,
           'par_5': self.par_5,
           'par_6': self.par_6,
           'par_7': self.par_7
           }
       
@app.route('/<phone_id>', methods = ['GET'])
def get_phone(phone_id):
    query_result = session.query(PhoneInfo).filter(PhoneInfo.id == phone_id).all()
    return json.dumps(query_result[0].serialize(), indent=4, sort_keys=False,ensure_ascii=False)
app.run(debug = True, host='0.0.0.0')