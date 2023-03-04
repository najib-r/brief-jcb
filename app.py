from flask import Flask, render_template
from scrape import fetch_details


app = Flask(__name__)

@app.route("/")
def index():
    default = 'sort=modified-&q=&delta=75'
    jobs = fetch_details(default)
    if jobs == "error" or len(jobs) == 0:
        return render_template("error.html")
    else:
        return render_template("index.html", jobs=jobs)

@app.route('/sw.js')
def sw():
    return app.send_static_file('sw.js')

@app.route('/briefjcb.webmanifest')
def manifest():
    return app.send_static_file('briefjcb.webmanifest')

if __name__ == '__main__':
    app.run()