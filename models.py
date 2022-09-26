from webapp import database


class Experience(database.Model):
    __tablename__ = 'professional_experience'
    id = database.Column(database.Integer, primary_key=True)
    company = database.Column(database.String)
    location = database.Column(database.String)
    charge = database.Column(database.String)
    resume = database.Column(database.String)
    remote = database.Column(database.String)
    dt_start = database.Column(database.Date)
    dt_finish = database.Column(database.Date)


class Certificate(database.Model):
    __tablename__ = 'certificates'
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String)
    subtitle = database.Column(database.String)
    file = database.Column(database.String)
    display_order = database.Column(database.Integer)
