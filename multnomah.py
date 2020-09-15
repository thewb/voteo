#!/usr/bin/python3
import talker
import requests
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup as bs
import pandas as pd

class multnomah(talker.talker):
	def __init__(self):
		self.raw = "https://secure.sos.state.or.us/orestar/vr/voterSearch.do?OWASP_CSRFTOKEN=6ITQ-1E59-6TL4-BPUA-2Q0J-TGGR-VGWK-TXCX"
		self.url = "https://secure.sos.state.or.us/orestar/vr/voterSearch.do"
		self.data = "buttonName=&dmvNumber=0&citizen=false&oldEnough=false&identifier2=Chris&identifier3=Smith&identifier8=07%2F27%2F1981&identifier12=&submitSearch=Submit&page=20"
		self.bad = b"No voter records were found"

	def pdata(self, fname, lname, day, month, year):
		S = requests.Session()
		cache = parse_qs(urlparse(self.raw).query)
		html = S.get("https://secure.sos.state.or.us/orestar/vr/voterSearch.do").content
		soup = bs(html, "lxml")
		csrf = soup.find("form", {"name": "VoterRegistrationForm"}).get('action').split("?")[1]
		self.cookies = S.cookies
		cache['OWASP_CSRFTOKEN'] = csrf.split("=")[1]
		cache['identifier2'] = fname
		cache['identifier3'] = lname
		cache['identifier8'] = month + "/" + day + "/" + year
		return cache
	
	def jsonify(self,html):
		soup = bs(html, "lxml")
		full_name = soup.find("span", {"class": "value"}).get_text(strip=True)
		name_list = full_name.split()
		values_dict = {
			"vuid": 'NULL',
			"fname": name_list[1],
			"mname": name_list[2],
			"lname": name_list[0][:-1],
			"regdate": pd.to_datetime("1900-01-01").date(),
			"bdate": "",
			"maddress": soup.findAll("div", {"class": "col-12 col-md-8 text-md-left mt-md-2"})[4].get_text(strip=True),
			"raddress": soup.findAll("div", {"class": "col-12 col-md-8 text-md-left mt-md-2"})[4].get_text(strip=True),
			"precinct": 'NULL',
			"party": soup.findAll("div", {"class": "col-12 col-md-8 text-md-left mt-md-2"})[3].get_text(strip=True)
		}

		return values_dict

