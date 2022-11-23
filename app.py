from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from scrape import pyJobnumberSearch, pyJobdetailsFetch


app = Flask(__name__)

@app.route("/")
def index():
    default = 'sort=modified-&q=&delta=75'
    number = pyJobnumberSearch(default)
    jobs = pyJobdetailsFetch(default)
    return render_template("index.html", number=number, jobs=jobs)

