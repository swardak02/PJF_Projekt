from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class Pracownik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    stanowisko = db.Column(db.String(150))
    wyplata = db.Column(db.Integer)
class Oferta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    oferta = db.Column(db.String(600))
    stanowisko = db.Column(db.String(150))
    stawka = db.Column(db.Integer)
class Uzytkownik(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    password = db.Column(db.String(150))
    stanowisko = db.Column(db.String(150))
