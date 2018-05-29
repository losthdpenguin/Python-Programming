import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","python" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE Login_and_Registration (
         Username  CHAR(20) NOT NULL,
         Password  CHAR(20) )"""

cursor.execute(sql)

# disconnect from server
db.close()