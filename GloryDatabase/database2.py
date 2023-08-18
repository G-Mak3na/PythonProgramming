# Updating records - modifying an already existing record

# Step 1 - Database connection
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='', database='MpesaTestDB')
print("Database connected successfully")

# Step 2 - Create a connection cursor
cursor = connection.cursor()

# Data
salary = 150000
emp_id = 5


# Step 3
SQL = "Update Employees set salary = %s where emp_id = %s"

# Execute
data = (salary, emp_id)
cursor.execute(SQL,data)
connection.commit()

# Notify the user
print(f"Employee ID {emp_id} salary updated successfully with {salary}")
