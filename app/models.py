from app import db

class Stock(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	ticker = db.Column(db.String(50))
	date = db.Column(db.Date)
	price = db.Column(db.String(50))