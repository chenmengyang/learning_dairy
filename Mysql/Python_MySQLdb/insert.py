import MySQLdb

db = MySQLdb.connect("localhost","cmy","","test")

cur = db.cursor()

# 2 ways of passing parameters to sql

# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

sql = "INSERT INTO EMPLOYEE(FIRST_NAME,\
         LAST_NAME, AGE, SEX, INCOME) \
         VALUES('%s', '%s', '%d', '%c', '%d') " %('Menyoung', 'Chan', 29, 'M', 20099)

try:
	cur.execute(sql)
	db.commit()
except:
	print "Error: unable to execute this insert sql!"
	db.rollback()

db.close()