#!/usr/bin/python
import db_config
import mysql.connector
import json

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

DB_NAME = "voteo"

def insert(data):
	qdata = json.loads(data)
	fields = (str(list(qdata.keys()))[1:-1])
	values = (str(list(qdata.values()))[1:-1])
	sql = 'INSERT INTO voter (' + fields + ') VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
	cursor.execute(sql, values)


def check_name(bdate, fname, lname):
	cursor.execute('SELECT * from voters where fname = %s and lname = %s', (fname, lname))
	info = cursor.fetchone()
	if "Empty" not in info:
		return info
	else:
		return "notexist" 

def tobeornot(data, bdate, fname, lname):
	if check_name(bdate. fname, lname) == notexist:
		insert(data)
		return "inserted"
	else:
		return "notinserted"


connection.commit()
connection.close()