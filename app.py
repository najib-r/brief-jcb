from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from scrape import pyJobnumberSearch


app = Flask(__name__)

@app.route("/")
def index():
    default = 'sort=modified-&start=1&q='
    number = pyJobnumberSearch(default)
    return render_template("index.html", number=number)

