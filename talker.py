#!/usr/bin/python
import requests
import pandas as pd
import sqldatabase

class talker():
	def __init__(self):
		self.raw = " "

	def pdata(self, fname, lname, day, month, year):
		pass

	def jsonify(self,html):
		pass

	def request(self, fname, lname, sdate, edate): 
		S = requests.Session()      
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
			record = sqldatabase.check_name(bdate, fname, lname) 
			if record == "notexist":
				data = self.pdata(fname, lname, day, month, year)
				try:
					r = S.post(self.url, data = data, cookies=self.cookies)
				except:
					r = S.post(self.url, data = data)
				if self.bad in r.content:
					continue
				else:
					jdata = self.jsonify(r.content)
					jdata['bdate'] = bdate
					sqldatabase.insert(jdata)
					record = sqldatabase.check_name(bdate, fname, lname)
					return record
			else:
				return record 



