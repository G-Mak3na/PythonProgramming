# Data Types - used to define the type of data stored in a variable eg a number, a letter, a collection etc
# Allows us to specify the operation(s) done on that variable

# In Python we have the following data types;

# 1.Integers(int) - numeric values without decimal places eg age,month

# 2. Floating Points (floats) - numbers with decimal places eg distance, height, speed etc

# 3. String (str) - sequence of characters enclosed inside a double or single quote eg name

# 4. A Boolean (bool) - a value having only 2 instances eg true or false

# Strings
# Escape Sequence - used to introduce special characters inside a string. We use(\)
message="I Love Programming"
print(type(message))

weather='It\'s a chilly Tuesday Morning'
print(weather)

paragraph='This is the first line,\n This is the second line'
print(paragraph)

# Concatenation - used to merge strings. We use(+)
firstmessage='I love'
secondmessage='Programming'
wholemessage=firstmessage+secondmessage
print(wholemessage)

# Len function - len() - return the number of characters in a string
password=input("Enter Your Password: ")
print(len(password))