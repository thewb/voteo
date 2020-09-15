#!/usr/bin/python
from bs4 import BeautifulSoup as bs
import talker
from urllib.parse import urlparse, parse_qs
import pandas as pd

class king(talker.talker):
	def __init__(self):
		self.raw = "https://info.kingcounty.gov/kcelections/vote/myvoterinfo.aspx?mode=BBDEDACBFBAAEA/__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKMTk2ODY3MTEwNWRkjBlwTKM%2BtVtTJVBUu8TnqXjx%2Fgo%3D&__VIEWSTATEGENERATOR=50044A0F&__EVENTTARGET=&__EVENTARGUMENT=&__EVENTVALIDATION=%2FwEdAAYqIbCOYpBRoC5cyVMaV1UJfXpRWHcFD3xcLLL8GEDQecqhKm6XNq2qvCsXIfChktWtnqJgHjbcnqdE2lemm9J5FYn6O78xAbZqtTP8hIE7jpbTm5MhD69V6cvciyfPqhjOWYTm9SoQo8jBWAlCgue3B59%2Fwg%3D%3D&ctl00%24kcMasterPagePlaceHolder%24voterlogin%24firstname=FeiFei&ctl00%24kcMasterPagePlaceHolder%24voterlogin%24lastname=Zhang&ctl00%24kcMasterPagePlaceHolder%24voterlogin%24dateofbirth=03%2F27%2F1978&ctl00%24kcMasterPagePlaceHolder%24voterlogin%24housenumber=&ctl00%24kcMasterPagePlaceHolder%24voterlogin%24mvpbtnlogin=Submit"
		self.bad = b"We are unable to find a registered voter"
		self.url = "https://info.kingcounty.gov/kcelections/vote/myvoterinfo.aspx?mode=BBDEDACBFBAAEA/"

	def pdata(self, fname, lname, day, month, year):
		cache = parse_qs(urlparse(self.raw).query)
		cache["dateofbirth"] = month + "/" + day + "/" + year
		cache["firstname"] = fname
		cache["lastname"] = lname
		return cache

	def jsonify(self,html):
		soup = bs(html, "lxml")

		rstreet = soup.find("span", {"id": "currentelectiondata21_voterewsreginfo_mvpreginfohousestreet"}).get_text(strip=True)
		rcsz = soup.find("span", {"id": "currentelectiondata21_voterewsreginfo_mvpreginfocitystatezip"}).get_text(strip=True)
		raddress = rstreet + " " + rcsz
		
		mstreet = soup.find("span", {"id": "currentelectiondata21_voterewsreginfo_mvpreginfomailinghousestreet"}).get_text(strip=True)
		mcst = soup.find("span", {"id": "currentelectiondata21_voterewsreginfo_mvpreginfomailingcitystatezip"}).get_text(strip=True)
		maddress = mstreet + " " + mcst

		values_dict = {
			"vuid": 'NULL',
			"fname": soup.find("span", {"class": "mvi-my-name-first"}).get_text(strip=True),
			"mname": self.not_available,
			"lname": soup.find("span", {"class": "mvi-my-name-last"}).get_text(strip=True),
			"regdate": pd.to_datetime("1900-01-01").date(),
			"bdate": "",
			"raddress": raddress,
			"maddress": maddress,
			"precinct": soup.find("span", {"id": "voterreginfo_mvpreginfoprecinct"}).get_text(strip=True),
			"party": 'NULL'
		}

		return values_dict
