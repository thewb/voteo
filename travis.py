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
		p = type(soup.find("div", {"class": "voterInfoDivider"}).findAll("br", limit=2))
		print(p)
		values_dict = {
			"lame": soup.find("div", {"class": "voterNameInfo"}).get_text(strip=True).split(nonBreakSpace)[1],
			"fname": soup.find("div", {"class": "voterNameInfo"}).get_text(strip=True).split(nonBreakSpace)[0],
			"vuid": soup.find("span", {"class": "voterVUID"}).get_text(strip=True),
			"rdate": "123",
			"raddress": soup.find("span", text="Residence Address:").next_sibling.get_text(strip=True),
			"precinct": soup.find("span", text="Precinct:").next_sibling.get_text(strip=True)
		}

		return json.dumps(values_dict, indent=0, sort_keys=False, default=None)	
