# Read data from the users table
# Read Operation(SELECT) - retrieving data from the database

# Step 1 - Database connection
import pymysql

connection = pymysql.connect (host='localhost', user='root', password='', database='MpesaTestDB')
print("Database connected successfully")

# Step 2 - Create a connection cursor
cursor = connection.cursor()

# Step 3
SQL = "select * from users"

# Execute
cursor.execute(SQL)

# Step 4 - check whether it's empty (rowcount)
count = cursor.rowcount

if count == 0:
    print("No records found")

else:
    data = cursor.fetchall
    print(data)
