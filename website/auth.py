from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

#creating more routes
@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signUp')
def signUp():
    return render_template("signUp.html")