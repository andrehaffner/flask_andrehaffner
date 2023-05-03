from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Configuring app ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

load_dotenv()
Views = Blueprint("views", __name__)
postgres_uri = getenv("PostgresURI")
app = Flask(__name__, template_folder='templates')
app.config["SECRET_KEY"] = "as@d145!sidh12*G3478"
app.config["SQLALCHEMY_DATABASE_URI"] = postgres_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Views ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

@Views.route("/")
def home():
    return render_template("home.html")


@Views.route("/professional")
def professional():
    data = Experience.query.order_by(Experience.id).all()
    return render_template("professional.html", professional=data)


@Views.route("/education")
def education():
    data = Education.query.order_by(Education.id).all()
    return render_template("education.html", educations=data)


@Views.route("/certificates")
def certificates():
    data = Certificate.query.order_by(Certificate.id).all()
    return render_template("certificates.html", certificates=data)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Models ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


class Certificate(db.Model):
    __tablename__ = 'certificates'
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String)
    institution = db.Column(db.String)
    date_period = db.Column(db.String)
    image = db.Column(db.String)


class Education(db.Model):
    __tablename__ = 'educations'
    id = db.Column(db.Integer, primary_key=True)
    diploma = db.Column(db.String)
    institution = db.Column(db.String)
    date_period = db.Column(db.String)
    image = db.Column(db.String)


class Experience(db.Model):
    __tablename__ = 'professional'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)
    company = db.Column(db.String)
    date_period = db.Column(db.String)
    image = db.Column(db.String)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

if __name__ == "__main__":
    app.register_blueprint(Views, url_prefix="/")
    app.run(port=5432, debug=True)
