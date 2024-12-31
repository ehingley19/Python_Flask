# Code based on "The New and Improved Flask Mega-Tutorial (2024 Edition)" by Miguel Grinberg
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# ====================================================================================================


# These lines cause an empty URL and the /index URL to be routed to the index() view function
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home Page", header="Welcome")


# ====================================================================================================


# This line causes the /help URL to be routed to the help() view function
@app.route("/help")
def help():
    return render_template("help.html", title="Help Page", header="Help")


# ====================================================================================================


# This line causes the /login URL to be routed to the login() view function, and that it accepts GET and POST requests.
# Note: HTTP GET requests return information to the client. HTTP POST requests are typically used to return form data to the server.
@app.route("/login", methods=["GET", "POST"])
def login():
    # Use LoginForm class defined in app/forms.py
    form = LoginForm()

    # The validate_on_submit() method does the form procesising work. When submit is pressed it gathers the data, runs the
    # attached validators and if everything is OK it will return true, otherwise it returns false.
    if form.validate_on_submit():
        # Login has passed validations so generate message to be displayed
        flash(
            "Login requested for user {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )

        # User has logged in so redirect to the home page
        return redirect(url_for("index"))

    # User has failed to loging to direct back to the login page
    return render_template("login.html", title="Sign In", form=form)
