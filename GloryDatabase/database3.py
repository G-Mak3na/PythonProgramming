# Deleting records from the database

# Connection
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='', database='MpesaTestDB')
print("Database connected successfully")

# Cursor
cursor = connection.cursor()

emp_id = 5

SQL = "Delete from Employees where emp-id = %s"

cursor.execute(SQL, emp_id)
connection.commit()

# Notify the user
print(f"Record {emp_id} deleted successfully")