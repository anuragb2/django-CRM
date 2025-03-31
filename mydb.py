# install mysql
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='root123'

	)

#prepare the curson object
cursorObject = dataBase.cursor()

#create the database

cursorObject.execute("CREATE DATABASE elderco")

print("All done!") 
