from flask import Blueprint, render_template


Views = Blueprint("views", __name__)


@Views.route("/")
def home():
    return render_template("home.html")


@Views.route("/professional")
def professional():
    return render_template("professional.html")


@Views.route("/education")
def education():
    return render_template("education.html")


@Views.route("/certificates")
def certificates():
    return render_template("certificates.html")
