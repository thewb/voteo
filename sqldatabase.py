#!/usr/bin/python3
import pymysql
import pandas as pd

class DB:
    def __init__(self):
        self.cnx = None

    def connect(self):
        if not self.cnx or not self.cnx.open:
            self.cnx = pymysql.connect(host='localhost',
                                       user='web',
                                       password='Thisisthebestpasswordever!',
                                       database='voteo',
                                       use_unicode=True,
                                       cursorclass=pymysql.cursors.DictCursor)
    
    def query(self, sql, values=None):
        try:
            self.connect()  # Ensure connection is established
            cursor = self.cnx.cursor()
            if values:
                cursor.execute(sql, values)
            else:
                cursor.execute(sql)
            return cursor

        except Exception as e:
            print("Error executing query:", e)

    def commit(self):
        try:
            if self.cnx and self.cnx.open:
                self.cnx.commit()
        except Exception as e:
            print("Error committing transaction:", e)

# Create a single DB instance
db = DB()

def insert(data):
    data['regdate'] = pd.to_datetime(data['regdate']).date()
    sql = "INSERT INTO `voter` (`vuid`, `fname`, `mname`, `lname`, `regdate`, `bdate`, `maddress`, `raddress`, `precinct`, `party`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (data['vuid'], data['fname'], data['mname'], data['lname'], data['regdate'], data['bdate'], data['maddress'], data['raddress'], data['precinct'], data['party'])
    db.query(sql, values)
    db.commit()
    return 0

def check_name(bdate, fname, lname):
    queryb = 'SELECT * FROM voter WHERE fname = %s AND lname = %s AND bdate = %s'
    cur = db.query(queryb, (fname, lname, bdate))
    qb_data = cur.fetchone()

    if qb_data is None:
        info = "notexist"
    else:
        info = qb_data 
    return info
