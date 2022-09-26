from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import Experience, Certificate
from sqlalchemy import asc

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return redirect(url_for('views.about_me'))


@views.route("/about-me")
def about_me():
    return render_template("about_me.html")


@views.route("/professional-experience")
def professional_experience():
    experiences = Experience.query.all()
    for experience in experiences:
        experience.resume = experience.resume.split("/^")
    return render_template("professional_experience.html", experiences=experiences)


@views.route("/certificates")
def certificates():
    certificates = Certificate.query.order_by(asc(Certificate.display_order)).all()
    return render_template("certificates.html", certificates=certificates)
