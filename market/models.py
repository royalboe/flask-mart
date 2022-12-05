from market import db
from market import bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email_address = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer, nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email_address}', '{self.budget}')"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plaintext):
        self.password_hash = bcrypt.generate_password_hash(plaintext).decode('utf-8')


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
