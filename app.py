from flask import Flask, render_template
from scrape import fetch_details, fetch_links, fetch_companynames


app = Flask(__name__)

@app.route("/")
def index():
    default = 'sort=modified-&q=&delta=75'
    jobs = fetch_details(default)
    if jobs == "error" or len(jobs) == 0:
        return render_template("error.html")
    else:
        # links = fetch_links(default)
        # names = fetch_companynames(default)
        names = [ sub['name'] for sub in jobs]
        links = [ sub['link'] for sub in jobs]
        salaries = [ sub['salary'] for sub in jobs]
        companies = [ sub['company'] for sub in jobs]
        return render_template("index.html", names=names, links=links, salaries=salaries, companies=companies)

if __name__ == '__main__':
    app.run() 