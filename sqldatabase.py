#!/usr/bin/python3
import pymysql
import json
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
	
def insert(data):
	db = DB()
	qdata = data
	fields = (list(qdata.keys()))[1:-1]
	values = list(map(str, list(qdata.values())))
	#values[3] = pd.to_datetime(values[3]).date()
	#values[4] = pd.to_datetime(values[4]).date()
	sql = "INSERT INTO `voter` (`vuid`, `fname`, `lname`, `regdate`, `bdate`, `maddress`, `raddress`, `precinct`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" % (values[0], values[1], values[2], values[3], values[4], values[5], values[5], values[7])
	cursor = db.query(sql)
	return 0

def check_name(bdate, fname, lname):
	db = DB()
	queryb = 'SELECT * from voter where fname = "%s" and lname = "%s" and bdate = "%s"' % (fname, lname, bdate)
	cur = db.query(queryb)
	result = ""
	qb_data = cur.fetchone()

	if qb_data == None:
		info = "notexist"
	else:
		info = qb_data 
	return info





	