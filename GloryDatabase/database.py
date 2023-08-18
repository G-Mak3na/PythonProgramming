# Integrating MySQL database with Python

# Module - pymysql
import pymysql

# 1. Create a database connection
# connect(host = '', user = '', password = '', database = '')
connection = pymysql.connect(host='localhost', user='root', password='', database='MpesaTestDB')
print("Database connected successfully")

# 2. Inserting Data to the table
emp_name = "Kelly Anne"
date_hired = '2023-07-04'
salary = 170000
dept_id = 2 

# Cursor - a cursor is a property(state) used to execute SQL codes on Python files
# Prepared Statements(%s) - they indicate that values will be passed during SQL execution

cursor = connection.cursor()

SQL = "insert into Employees (emp_name, date_hired, salary, dept_id) values(%s, %s, %s, %s)"

# 3. SQL Execution
data = (emp_name, date_hired, salary, dept_id)
cursor.execute(SQL, data)

# Commit - saving changes to the database
connection.commit()
print("Records updated successfully")