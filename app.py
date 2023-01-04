from flask import Flask, render_template
from scrape import fetch_details, fetch_links, fetch_companynames


app = Flask(__name__)

@app.route("/")
def index():
    default = 'sort=modified-&q=&delta=75'
    jobs = fetch_details(default)
    links = fetch_links(default)
    names = fetch_companynames(default)
    return render_template("index.html", jobs=jobs, links=links, names=names)

if __name__ == '__main__':
    app.run() 