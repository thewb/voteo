#!/usr/bin/python3
from flask import Flask, request, render_template
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
import json
import travis
import king
import json

app = Flask(__name__, template_folder='/home/wb/voteo')

locale = {"travis": travis.travis(),
          "king": king.king()  
         }

@app.route("/")
def index():
    return render_template('menu_template.html')

@app.route("/find")
def lookup():
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    sdate = request.args.get("sdate")
    edate = request.args.get("edate")
    fmat = request.args.get("fmat") if request.args.get("fmat") else "html"
    county = request.args.get("county")  

    t = locale[county]
    
    raw = t.request(fname, lname, sdate, edate)

    if raw is None:
        return render_template('fourofour.html', fname=fname, lname=lname)

    if fmat == "html":
        return render_template('template.html', raw=raw, fname=fname, lname=lname)

    if fmat == "json":
        jdata = json.dumps(raw, indent=0, default=str)
        return app.response_class(response=jdata, mimetype="application/json")

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=5000)  
