from flask import Flask
from random import randint
from flask import render_template

#create the app
app = Flask(__name__)

@app.get("/")
def home():
    return render_template('pages/home.jinja')

@app.get("/random/")
def random():
    return str(randint(1, 1000))

@app.get("/about/")
def about():
    return render_template('pages/about.jinja')