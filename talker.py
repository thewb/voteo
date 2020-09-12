#!/usr/bin/python
import requests
import pandas as pd
from urllib.parse import urlparse, parse_qs
import sqldatabase

class voteobj():
	def __init__(self):
		self.data = ""
		self.bdate = ""

class talker():
	#Base Class for counties
	def __init__(self):
		self.raw = " "

	def pdata(self, fname, lname, day, month, year):
		pass

	def jsonify(self,html):
		pass

	def soupit(self,html):
		pass
	#Function looks up voters. It looks in the MySQL database first, then makes a request to the county website
	#It loops until it finds a voter, and returns the information. If the information is class talker it returns
	#a talker object, if it's in the database it returns a record from the database.
	def request(self, fname, lname, sdate, edate):
		self.raw.replace(self.name_string, self.fname_separator + fname + self.lname_separator + lname)         
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
			year = str(i.year)
			bdate = pd.to_datetime(i).date()
			#record = sqldatabase.check_name(bdate, fname, lname) 
			record = "notexist"
			if record == "notexist":
				data = self.pdata(fname, lname, day, month, year)
				r = requests.post(self.url, data = data)
				print(data)
				print(self.url)
				print(r.content)
				if self.bad in r.content:
					continue
				else:
					v = voteobj()
					v.bdate = pd.to_datetime(str(i.month) + "/" + str(i.day) + "/" + str(i.year)).date()
					v.data = r.content
					jdata = self.jsonify(v)
					sqldatabase.insert(jdata)
					return jdata
			else:
				return record 

	#Abstract functions becasue the data from each county is different. These will remove HTML and convert to json.
	#We usually just call soupit from jsonify because we just want json in the view.


