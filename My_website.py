# A simple web application.
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')
@app.route("/hello/<name>")
def greet(name='Stranger'):
    return render_template("greeting.html", name=name)
@app.route("/slash")
def slash():
    return render_template("slash.html")




