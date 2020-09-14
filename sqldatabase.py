#!/usr/bin/python3
import pymysql
import pandas as pd

class DB:
	cnx = None

	def connect(self):
		self.cnx = pymysql.connect('localhost', 'web', 'Thisisthebestpasswordever!', 'voteo', use_unicode=True, cursorclass=pymysql.cursors.DictCursor)
	
	def query(self, sql):
		try:
			cursor = self.cnx.cursor()
			cursor.execute(sql)
			
		except:
			self.connect()
			cursor = self.cnx.cursor()
			cursor.execute(sql)
			return cursor

	def commit(self):
			self.cnx.commit()

def insert(data):
	db = DB()
	sql = "INSERT INTO `voter` (`vuid`, `fname`, `lname`, `regdate`, `bdate`, `maddress`, `raddress`, `precinct`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (data['vuid'], data['fname'], data['lname'], pd.to_datetime(data['regdate']).date(), data['bdate'], data['maddress'], data['raddress'], data['precinct'], data['party'])
	db.query(sql)
	db.commit()
	return 0

def check_name(bdate, fname, lname):
	db = DB()
	queryb = 'SELECT * from voter where fname = "%s" and lname = "%s" and bdate = "%s"' % (fname, lname, bdate)
	cur = db.query(queryb)
	qb_data = cur.fetchone()

	if qb_data == None:
		info = "notexist"
	else:
		info = qb_data 
	return info





	