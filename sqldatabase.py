#!/usr/bin/python3
import pymysql

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
	vs = list(data.values())
	sql = "INSERT INTO `voter` (`vuid`, `fname`, `lname`, `regdate`, `bdate`, `maddress`, `raddress`, `precinct`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (vs[0], vs[1], vs[2], vs[3], vs[4], vs[5], vs[6], vs[7])
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





	