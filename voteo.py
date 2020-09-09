#!/usr/bin/python3
from flask import Flask, request, render_template
import warnings
import utils
import talker
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
import sqldatabase
import json
import pandas as pd
import os

app = Flask(__name__, template_folder='/home/wb/voteo')

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
    raw = talker.request(fname, lname, sdate, edate)

    if raw is None:
        return render_template('fourofour.html', fname=fname, lname=lname)

    #if voter is not in db
    if type(raw) is not dict:
        jdata = utils.jsonify(raw)
        t = json.loads(jdata)
        sqldatabase.insert(jdata)

    #if voter is in db
    elif type(raw) is dict:
        jdata = json.dumps(raw, indent=4, sort_keys=False, default=str)
        t = json.loads(jdata)

    if fmat == "html":    
        return render_template('template.html', raw=t, fname=fname, lname=lname)

    if fmat == "json":
        return jdata

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=5000)  
