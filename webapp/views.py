from flask import Blueprint, render_template, redirect, request
from ..main import app

Views = Blueprint("views", __name__)


@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)


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
