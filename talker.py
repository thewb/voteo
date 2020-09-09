#!/usr/bin/python
import requests
import pandas as pd
from urllib.parse import urlparse, parse_qs
import sqldatabase

raw = "https://www.votetravis.com/vexpress/submit.do?action=display&searchType=N&electionCode=&electionDateStr=&criteria.firstName=DEREK&maxPollingLocationsDisplay=3&criteria.lastName=HINCH&criteria.vuid=&criteria.month=01&criteria.day=01&criteria.year=1980&earlyVoting=true&address.fullAddress=TX+&address.partialAddress=&address.city=&address.state=TX&address.zipcode="

bad = b"Voter Information Cannot be Found"

result = ""

class voter_data:
    def __init__(self):
        self.data = ""
        self.bdate = ""

def request(fname, lname, sdate, edate):
    daterange = pd.date_range(sdate, edate)
    req = raw.replace("firstName=DEREK&maxPollingLocationsDisplay=3&criteria.lastName=HINCH", "firstName=" + fname + "&maxPollingLocationsDisplay=3&criteria.lastName=" + lname)
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
            rep_str = "criteria.month=" + month + "&criteria.day=" + day + "&criteria.year=" + str(i.year)
            new_req = req.replace("criteria.month=01&criteria.day=01&criteria.year=1980", rep_str)
            post_data = urlparse(new_req)
            data = parse_qs(urlparse(new_req).query)
            r = requests.post("https://www.votetravis.com/vexpress/submit.do", data = data)
            if bad in r.content:
                continue
            else:
                v = voter_data
                v.bdate = pd.to_datetime(str(i.month) + "/" + str(i.day) + "/" + str(i.year)).date()
                v.data = r.content
                return v
        else:
            return record 