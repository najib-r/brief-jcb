from flask import Flask, render_template
from scrape import fetch_details, fetch_links, fetch_companynames
import time


app = Flask(__name__)

@app.route("/")
def index():
    default = 'sort=modified-&q=&delta=75'
    jobs = fetch_details(default)
    if jobs == "error":
        return render_template("error.html")
    else:
        links = fetch_links(default)
        time.sleep(1)
        names = fetch_companynames(default)
        return render_template("index.html", jobs=jobs, links=links, names=names)
        
# @app.route('/sw.js', methods=['GET'])
# def sw():
#     return app.send_static_file('sw.js')

if __name__ == '__main__':
    app.run() 