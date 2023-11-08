from datetime import datetime

from flask import Flask, render_template, escape, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# PYTHONPATH="static/scripts" environment variable
from mbs import PrivateBank, CurrencyParser
from bk import BunchOfKeys



class Base(DeclarativeBase):
	pass


db = SQLAlchemy(model_class=Base)


class Transactions(db.Model):
	__tablename__ = "Transactions"
	id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
	amount = db.Column(db.Float, nullable=False)
	description = db.Column(db.Text)
	category_id = db.Column(db.Integer, db.ForeignKey("Categories.id"), nullable=False)
	category = db.relationship("Categories", backref=db.backref("category", lazy=True))
	payment_id = db.Column(db.Integer, db.ForeignKey("Storages.id"), nullable=False)
	payment = db.relationship("Storages", backref=db.backref("payment", lazy=True))
	account_id = db.Column	(db.Integer, db.ForeignKey("Accounts.id"), nullable=False)
	account = db.relationship("Accounts", backref=db.backref("account", lazy=True))
	transaction_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return "<Transactions %r>" % self.id


class Transfers(db.Model):
	__tablename__ = "Transfers"
	id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
	from_account = db.Column(db.Text, db.ForeignKey("Storages.id"), nullable=False)
	to_account = db.Column(db.Text, db.ForeignKey("Storages.id"), nullable=False)
	amount = db.Column(db.Float, nullable=False)
	transfer_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return "<Transfers %r>" % self.id


class Categories(db.Model):
	__tablename__ = "Categories"
	id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
	name = db.Column(db.Text, nullable=False)
	icon = db.Column(db.Text, nullable=False)
	transaction_type = db.Column(db.Text, nullable=False) # cost / input

	def __repr__(self):
		return "<Categories %r>" % self.id


class Accounts(db.Model):
	__tablename__ = "Accounts"
	id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
	accountName = db.Column(db.Text, nullable=False) # asneeded, option, reserve_stock
	amount = db.Column(db.Float, nullable=False)
	lastUpdate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return "<Accounts %r>" % self.id


class Debts(db.Model):
	__tablename__ = "Debts"
	id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
	name = db.Column(db.Text, nullable=False)
	amount = db.Column(db.Float, nullable=False)
	dd = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return "<Debts %r>" % self.id


class Storages(db.Model):
	__tablename__ = "Storages"
	id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
	storageName = db.Column(db.Text, nullable=False) # card, pocket, cash
	amount = db.Column(db.Float, nullable=False)
	dateOfUpdate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return "<Storages %r>" % self.id


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///budget.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# with app.app_context():
#     db.create_all()


# Models
bk_model = BunchOfKeys()
bank_model = PrivateBank()
parser_model = CurrencyParser()


# migrations
@app.route('/')
def home():
	# response = parser_model.get("text")
	# print(f"buy: {response[0]}\nsell: {response[1]}")
	return render_template('home.html')


@app.route('/bunch-of-kyes', methods=["POST", "GET"])
def bk():
	if request.method == "POST":
		phrase = request.form.get('phrase')
		mode = request.form.get('mode')

		# if len(phrase) < 16:
		# 	return render_template('bk.html', result="Not enough characters")
		# else:
		return render_template('bk.html', result=bk_model.get_password(phrase))

	return render_template('bk.html')


@app.route('/financial-control', methods=["POST", "GET"])
def fc():
	if request.method == "POST":
		amount = float(request.form["amount"])
		description = request.form["desc"]
		typeOfEntry = request.form["typeOfEntry"]
		category = request.form["category"]

		transaction = Transactions(
			amount=amount,
			description=description,
			category_id=1,
			payment_id=1,
			account_id=1
		)
		try:
			db.session.add(transaction)
			db.session.commit()
		except Exception as e:
			print(f"Error: {e}")

	return render_template('mbs.html', transactions=Transactions.query.all())
	# return render_template('mbs.html')


@app.route('/language-bridge')
def eic():
	return render_template('eic.html')

@app.route('/thoughts')
def thoughts():
	return render_template('thoughts.html')

@app.route('/progress')
def progress():
	return render_template('progress.html')


@app.route('/rewards-system')
def reward():
	return render_template('rs.html')


if __name__ == '__main__':
	app.run(debug=True)
