from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    db.__tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    user_pantry = db.relationship('Pantry', backref='user', lazy=True)

    def __repr__(self):
        return "Username: {}, Email: {}".format(self.username, self.email)


class Pantry(db.Model):
    db.__tablename__ = "pantry"
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(40), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer, nullable=True)
    expiration = db.Column(db.DateTime, nullable=True, default='1/1/2049')
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/')
def main():
    return "Please Login!"


if __name__ == '__main__':
    app.run(debug=True)
