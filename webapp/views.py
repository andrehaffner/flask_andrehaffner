from .models import Experience, Education, Certificate
from flask import Blueprint, render_template


Views = Blueprint("views", __name__)


@Views.route("/")
def home():
    return render_template("home.html")


@Views.route("/professional")
def professional():
    data = Experience.query.order_by(Experience.id).all()
    for experience in data:
        experience.description = experience.description.split("<br>")
    return render_template("professional.html", data=data)


@Views.route("/education")
def education():
    data = Education.query.order_by(Education.id).all()
    for education in data:
        education.description = education.description.split("<br>")
    return render_template("education.html", data=data)


@Views.route("/certificates")
def certificates():
    data = Certificate.query.order_by(Certificate.id).all()
    return render_template("certificates.html", data=data)


@Views.route("/data")
def data_page():
    professional_table = Experience.query.order_by(Experience.id).all()
    education_table = Education.query.order_by(Education.id).all()
    certificates_table = Certificate.query.order_by(Certificate.id).all()
    return render_template("data_page.html", professional_table=professional_table,
                           education_table=education_table, certificates_table=certificates_table)
