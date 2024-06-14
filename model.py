from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    steps = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Step {self.date} - {self.steps}>'
