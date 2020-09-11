#!/usr/bin/python3
import db_config
import pymysql
import json
import pandas as pd


cnx = None

def connect():
	global cnx
	if not cnx:
		cnx = pymysql.connect('localhost', 'web', 'Thisisthebestpasswordever!', 'voteo', use_unicode=True, cursorclass=pymysql.cursors.DictCursor)
	return cnx
	
def insert(data):
	cnx = connect()
	cursor = cnx.cursor()
	qdata = json.loads(data)
	fields = (list(qdata.keys()))[1:-1]
	values = list(map(str.strip, list(qdata.values())))
	values[3] = pd.to_datetime(values[3]).date()
	values[4] = pd.to_datetime(values[4]).date()
	sql = "INSERT INTO `voter` (`vuid`, `fname`, `lname`, `regdate`, `bdate`, `maddress`, `raddress`, `precinct`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
	cursor.execute(sql, (values[0], values[1], values[2], values[3], values[4], values[5], values[5], values[7]))
	cnx.commit()
	cursorq.close()
	return 0

def check_name(bdate, fname, lname):
	cnx = connect()
	cursor = cnx.cursor()
	queryb = 'SELECT * from voter where fname = "%s" and lname = "%s" and bdate = "%s"' % (fname, lname, bdate)
	cursor.execute(queryb)
	result = ""
	qb_data = cursor.fetchone()

	if qb_data == None:
		info = "notexist"
	else:
		info = qb_data 
	cursor.close()
	return info

def tobeornot(data, bdate, fname, lname):
	if check_name(bdate. fname, lname) == notexist:
		insert(data)
		return "inserted"
	else:
		return "notinserted"




	