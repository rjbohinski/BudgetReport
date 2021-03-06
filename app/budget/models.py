from app.base_model import Base
from app import db

class Budget(Base):

    __tablename__ = 'budget'
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    name = db.Column(db.String(128), nullable=False)

    amount = db.Column(db.Float)

    intial_amount = db.Column(db.Float)

    expenses = db.relationship('Expense')

    def __init__(self, user_id, name, amount, intial_amount):
        self.user_id = user_id
        self.name = name
        self.amount = amount
        self.intial_amount = intial_amount