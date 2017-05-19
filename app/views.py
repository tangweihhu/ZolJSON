# from flask import Flask, render_template
# from flask_sqlalchemy import AQLAlchemy
# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'hard to guess'
# app.config['SQLALCHEMT_DATABAWE_URL'] = 'mysql://root:rootroot@localhost:3306/zol'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
# session = db.session()

# class PhoneInfo(db.Model):
    # __tablename__ = 'zolphone'
    # id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(100))
    # price = db.Column(db.String(100))
    # product_url = db.Column(db.String(100))
    # par_1 = db.Column(db.Text)
    # par_2 = db.Column(db.Text)
    # par_3 = db.Column(db.Text)
    # par_4 = db.Column(db.Text)
    # par_5 = db.Column(db.Text)
    # par_6 = db.Column(db.Text)
    # par_7 = db.Column(db.Text)
    
    # def __repr__(self):
         # return '<PhoneInfo {}> '.format(self.title)

# @app.route('/<int:phone_id>', methods = ['GET'])
# def get_phone():
    # query_result = db.query(zolphone).filter(zolphone.id == "phone_id").all()
    # return jsonify({'PhoneDetails': query_result[0]})