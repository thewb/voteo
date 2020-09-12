#!/usr/bin/python
import json
from bs4 import BeautifulSoup as bs
import talker
from urllib.parse import urlparse, parse_qs, urlencode

class king(talker.talker):
	def __init__(self):
		self.raw = "https://info.kingcounty.gov/kcelections/vote/myvoterinfo.aspx?mode=BBDEDACBFBAAEA/__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKMTk2ODY3MTEwNWRkjBlwTKM%2BtVtTJVBUu8TnqXjx%2Fgo%3D&__VIEWSTATEGENERATOR=50044A0F&__EVENTTARGET=&__EVENTARGUMENT=&__EVENTVALIDATION=%2FwEdAAYqIbCOYpBRoC5cyVMaV1UJfXpRWHcFD3xcLLL8GEDQecqhKm6XNq2qvCsXIfChktWtnqJgHjbcnqdE2lemm9J5FYn6O78xAbZqtTP8hIE7jpbTm5MhD69V6cvciyfPqhjOWYTm9SoQo8jBWAlCgue3B59%2Fwg%3D%3D&ctl00%24kcMasterPagePlaceHolder%24voterlogin%24firstname=FeiFei&ctl00%24kcMasterPagePlaceHolder%24voterlogin%24lastname=Zhang&ctl00%24kcMasterPagePlaceHolder%24voterlogin%24dateofbirth=03%2F27%2F1978&ctl00%24kcMasterPagePlaceHolder%24voterlogin%24housenumber=&ctl00%24kcMasterPagePlaceHolder%24voterlogin%24mvpbtnlogin=Submit"
		self.bad = b"unable"
		self.url = "https://info.kingcounty.gov/kcelections/vote/myvoterinfo.aspx?mode=BBDEDACBFBAAEA/"

	def pdata(self, fname, lname, day, month, year):
		cache = parse_qs(urlparse(self.raw).query)
		cache["dateofbirth"] = month + "/" + day + "/" + year
		cache["firstname"] = fname
		cache["lastname"] = lname
		return cache

	def jsonify(self,html):
		soup = bs(html, "lxml")
		print(soup)
		rstreet = soup.find("span", {"id": "currentelectiondata21_voterewsreginfo_mvpreginfohousestreet"}).split(">")[1].split("<")[0]
		rcsz = soup.find("span", {"id": "currentelectiondata21_voterewsreginfo_mvpreginfocitystatezip"}).split(">")[1].split("<")[0]
		raddress = rstreet + rcsz
		
		mstreet = soup.find("span", {"id": "currentelectiondata21_voterewsreginfo_mvpreginfomailinghousestreet"}).split(">")[1].split("<")[0]
		mcst = soup.find("span", {"id": "currentelectiondata21_voterewsreginfo_mvpreginfomailingcitystatezip"}).split(">")[1].split("<")[0]
		maddress = mstreet + mcst
		not_available = "N/A in kingcounty"
	
		values_dict = {
			"vuid": not_available,
			"fname": soup.find("span", {"class": "mvi-my-name-first"}).split(">")[1].split("<")[0],
			"lname": soup.find("span", {"class": "mvi-my-name-last"}).split(">")[1].split("<")[0],
			"rdate": not_available,
			"bdate": "",
			"raddress": raddress,
			"maddress": maddress,
			"precinct": soup.find("span", {"id": "voterreginfo_mvpreginfoprecinct"}).split(">")[1].split("<")[0]
		} 
	
		return json.dumps(values_dict, indent=0, sort_keys=False, default=None)	