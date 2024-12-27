from flask import render_template
from app import app

# These lines cause an empty URL and the /index URL to be mapped to the index() view function
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Default Page', header='Main Header')

# This line causes the /help URL to be mapped to the help() view function
@app.route('/help')
def help():
    return 'Help page'