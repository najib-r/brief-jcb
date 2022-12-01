from flask import Flask, render_template
from scrape import pyJobdetailsFetch, pyJoblinksFetch, pyJobcompanyNames


app = Flask(__name__)

@app.route("/")
def index():
    default = 'sort=modified-&q=&delta=75'
    jobs = pyJobdetailsFetch(default)
    links = pyJoblinksFetch(default)
    names = pyJobcompanyNames(default)
    return render_template("index.html", jobs=jobs, links=links, names=names)

if __name__ == '__main__':
    app.run() 