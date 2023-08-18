# Create a database connection
# Confirm the connection
# Create 3 variables to hold username, password, phone
# Create a cursor to your connection
# Write SQL to save username, password and phone on User's table
# Execute your SQL
# Commit your connection
# Notify that record has been saved

import pymysql
connection = pymysql.connect (host='', user='root', password='', database='MpesaTestDB')
print("Database connected successfully")

username = "Brown Mark"
password = '2019'
phone = +254712345678
cursor = connection.cursor()
SQL = "insert into users (username, password, phone) values(%s, %s, %s)"
data = (username, password, phone)



cursor.execute(SQL,data)

connection.commit()



username = "James"
password = '9012'
phone = +254714784655
cursor = connection.cursor()
SQL = "insert into users (username, password, phone) values(%s, %s, %s)"
data = (username, password, phone)



cursor.execute(SQL,data)

connection.commit()
print("Records updated successfully")