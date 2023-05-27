from flask import Flask, render_template
from scrape import fetch_details


app = Flask(__name__)

@app.route("/")
def index():
    default = 'q=&delta=200'
    jobs, page = fetch_details(default)
    if jobs == "error" or len(jobs) == 0:
        return render_template("error.html")
    else:
        return render_template("index.html", jobs=jobs, page=page, index=1)
    
@app.route("/<pageno>")
def show_page(pageno):
    default = 'q=&delta=200'
    jobs, page = fetch_details(default+'&start='+pageno)
    if jobs == "error" or len(jobs) == 0:
        return render_template("error.html")
    else:
        return render_template("index.html", jobs=jobs, page=page, index=int(pageno))
    
@app.route('/sw.js')
def sw():
    return app.send_static_file('sw.js')

@app.route('/briefjcb.webmanifest')
def manifest():
    return app.send_static_file('briefjcb.webmanifest')

if __name__ == '__main__':
    app.run()