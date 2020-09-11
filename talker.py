#!/usr/bin/python
import requests
import pandas as pd
from urllib.parse import urlparse, parse_qs
import sqldatabase

class talker():
    #Base Class for counties
    def __init__(self):
    
    class voter_data:
        def __init__(self):
            self.data = ""
            self.bdate = ""

    #Function looks up voters. It looks in the MySQL database first, then makes a request to the county website
    #It loops until it finds a voter, and returns the information. If the information is class talker it returns
    #a talker object, if it's in the database it returns a record from the database.
    def request(fname, lname, sdate, edate, county):
        r_data = place[county]
        raw.replace(r_data.name_string, r_data.fname_separator + fname + r_data.lname_separator + lname)         
        daterange = pd.date_range(sdate, edate)
        for i in daterange:
            if i.month < 10:
                month = "0" + str(i.month)
            else:
                month = str(i.month)
            if i.day < 10:
                day = "0" + str(i.day)
            else:
                day = str(i.day)
            bdate = pd.to_datetime(i).date()
            record = sqldatabase.check_name(bdate, fname, lname) 
            if record == "notexist":
                rep_str = r_data.date_url_header + month + r_data.month_separator + day + r_data.day_separator + str(i.year)
                new_req = req.replace(r_data.dobstr, rep_str)
                data = parse_qs(urlparse(new_req).query)
                r = requests.post(r_data.url, data = data)
                if bad in r.content:
                    continue
                else:
                    v = voter_data
                    v.bdate = pd.to_datetime(str(i.month) + "/" + str(i.day) + "/" + str(i.year)).date()
                    v.data = r.content
                    jdata = jsonify(v)
                    sqldatabase.insert(jdata)
                    return jdata
            else:
                return record 

    #Abstract functions becasue the data from each county is different. These will remove HTML and convert to json.
    #We usually just call soupit from jsonify because we just want json in the view.
    def jsonify():
        pass

    def soupit():
        pass