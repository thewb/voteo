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
	pass
	
#def insert(data):
#	db = DB()
#	vs = data
#	sql = "INSERT INTO voter (vuid, fname, lname, regdate, bdate, maddress, raddress, precinct) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" % (vs['vuid'], vs['fname'], vs['lname'], vs['regdate'], vs['bdate'], vs['maddress'], vs['raddress'], vs['precinct'])
#	cursor = db.query(sql)
#	return 0

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





	