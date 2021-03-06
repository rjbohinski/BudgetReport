from app.base_model import Base
from app.extensions import bcrypt
from app import db

from flask_login import UserMixin
class User(Base, UserMixin):

    __tablename__ = 'user'

    # Identification Data: email & password
    email    = db.Column(db.String(128),  nullable=False,
                                            unique=True)
    password = db.Column(db.Binary(128), nullable=False)

    budgets = db.relationship('Budget')

    expenses = db.relationship('Expense')

    # New instance instantiation procedure
    def __init__(self, email, password):

        self.email    = email
        if password:
            self.set_password(password)
        else:
            self.password = None
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)

    def __repr__(self):
        return '<User %r>' % (self.email) 