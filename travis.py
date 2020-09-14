#!/usr/bin/python
import json
from bs4 import BeautifulSoup as bs
import talker
from urllib.parse import urlparse, parse_qs, urlencode

class travis(talker.talker):
	def __init__(self):
		self.raw = "https://www.votetravis.com/vexpress/submit.do?action=display&searchType=N&electionCode=&electionDateStr=&criteria.firstName=DEREK&maxPollingLocationsDisplay=3&criteria.lastName=HINCH&criteria.vuid=&criteria.month=01&criteria.day=01&criteria.year=1980&earlyVoting=true&address.fullAddress=TX+&address.partialAddress=&address.city=&address.state=TX&address.zipcode="
		self.bad = b"Voter Information Cannot be Found"
		self.url = "https://www.votetravis.com/vexpress/submit.do"

	def pdata(self, fname, lname, day, month, year):
		cache = parse_qs(urlparse(self.raw).query)
		cache['criteria.firstName'] = fname
		cache['criteria.lastName'] = lname
		cache['criteria.month'] = month
		cache['criteria.day'] = day
		cache['criteria.year'] = year
		return cache

	def jsonify(self,html):
		soup = bs(html, "lxml")
		nonBreakSpace = u'\xa0'
		values_dict = {
			"vuid": soup.find("span", {"class": "voterVUID"}).getText(strip=True),
			"fname": soup.find("input", {"id": "queryBlock"}).get('value'),
			"lname": soup.find("input", {"id": "query"}).get('value'),
			"regdate": soup.find("td", {"valign": "top"}).text.split()[4],
			"maddress": soup.find("input", {"name": "address.fullAddress"}).get('value').strip(),
			"raddress": soup.find("input", {"name": "address.fullAddress"}).get('value').strip(),
			"precinct": soup.find_all("td", {"valign": "top"}, limit=5)[4].text.split()[1]
		}

		return values_dict	
