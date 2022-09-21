from main import db


class Description(db.Model):
    __tablename__ = 'descriptions'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
