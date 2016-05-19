import MySQLdb

db = MySQLdb.connect("localhost","cmy","","test")

cur = db.cursor()

# Drop table if exists table_name, got it now...
cur.execute("drop table if exists employee")

create_sql = "create table employee(\
	FIRST_NAME  CHAR(20) NOT NULL,\
         LAST_NAME  CHAR(20),\
         AGE INT,  \
         SEX CHAR(1),\
         INCOME FLOAT)"

cur.execute(create_sql)

# 3. Disconnect from server
db.close()
