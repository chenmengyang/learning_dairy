# fetchone(): It fetches the next row of a query result set. A result set is an object that is returned when a cursor object is used to query a table.

# fetchall(): It fetches all the rows in a result set. If some rows have already been extracted from the result set, then it retrieves the remaining rows from the result set.

# rowcount: This is a read-only attribute and returns the number of rows that were affected by an execute() method.

import MySQLdb

db = MySQLdb.connect("localhost","cmy","","test")

cur = db.cursor()

sql = "select * from employee;"

try:
	cur.execute(sql)
	print "There are " + str(cur.rowcount) + " records!"
	results = cur.fetchall()
	# results is a set of tuples
	for r in results:
		print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (r[0],r[1],r[2],r[3],r[4])
except:
	print "Error:unable to fetch data"

db.close()