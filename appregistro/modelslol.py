from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#se crean a medida que guardamos en nuestra database
class Pizzeria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)

