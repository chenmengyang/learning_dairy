# this note is about how to operate on Mysql using python library Mysqldb

# First you should install this library of course, omit here
import MySQLdb

# 1. Database Connection
# Argument1: server host
# Argument2: username
# Argument3: password
# Argument4: database name
db = MySQLdb.connect("localhost","cmy","","test")

# 2. This will create a cursor object
cur = db.cursor()

# we can use it to execute sql query
cur.execute("select version()");

# fetch the return data of the sql query on the cursor
data = cur.fetchone()

print "database version: %s" % data

# 3. Disconnect from server
db.close()
