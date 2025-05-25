from flask import Flask
from flask import redirect
from random import randint
from flask import render_template
from flask import request

#create the app
app = Flask(__name__)

# Home page - loading a static page
@app.get("/")
def home():
    return render_template('pages/home.jinja')

# About page - loading a static page
@app.get("/about/")
def about():
    return render_template('pages/about.jinja')

# Random number page - passing a value to the template
@app.get("/random/")
def random():
    randNum = randint(1, 100000000000000000)
    return render_template('pages/random.jinja' , number = randNum)

# Number page - getting a value from the root and passing it into the template
@app.get("/number/<int:num>")
def analyseNumber(num):
    print(f"You have entered the number {num}")
    return render_template('pages/number.jinja', number = num)

# Form page - static page with a form
@app.get("/form/")
def form():
    return render_template('pages/form.jinja')

# Handle form submission - processing the form data
@app.post("/processForm/")
def processForm():
    print(f"Form data: ${request.form}")
    return render_template("pages/formData.jinja", name = request.form['name'], email = request.form['email'], age = request.form['age'])

# Error page - handling errors
@app.errorhandler(404)
def notFound(e):
    return render_template('pages/404.jinja'), 404