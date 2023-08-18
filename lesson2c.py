# Booleans (bool)

approved=False
print(type(approved))

absent=True
print(type(absent))

# Booleans with Comparison Operators eg >,<,==,>=,<=,!=
print(10>5)

savedpassword='12345678'
requestedpassword=input("Enter Your Password: ")

print(savedpassword== requestedpassword)

# Logical Operators - compares the relationship between one condition and another
# and - returns to true when BOTH conditions are true
# or - return to when at least ONE condition is true
# not - it negates a condition

username = 'admin'
password = '123456789'
requestusername = input("Enter Your Username: ")
requestpassword = input("Enter Your Password: ")

print(username == requestusername and password == requestpassword)