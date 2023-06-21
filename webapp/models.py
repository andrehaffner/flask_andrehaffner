from . import db


class Certificate(db.Model):
    __tablename__ = 'certificates'
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String)
    institution = db.Column(db.String)
    date_period = db.Column(db.String)
    image = db.Column(db.String)


class Education(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True)
    diploma = db.Column(db.String)
    institution = db.Column(db.String)
    date_period = db.Column(db.String)
    image = db.Column(db.String)
    description = db.Column(db.String)


class Experience(db.Model):
    __tablename__ = 'professional'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)
    company = db.Column(db.String)
    date_period = db.Column(db.String)
    image = db.Column(db.String)
    description = db.Column(db.String)
