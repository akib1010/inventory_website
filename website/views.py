from flask import Blueprint, render_template

views = Blueprint('views',__name__)

#creating routes
@views.route('/')
def home():
    return render_template("home.html")
