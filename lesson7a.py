# Iterations/Loops - used to repeat a line of code a number of times based on a condition

# print("Hello")
# print("Hello")

# In python the conditions used are - for, while
# In Kotlin - for, while, do-while
# In JS - for, while, for each

# For Loop
# Syntax: for variables in sequence (collection)
#                       in statements

# For Loop in range() - check the condition
print("==========")
for message in range (10):
    print(f"Hello {message}")
print("==========")
for index in range (21):
    print(index)

# Range function with a starting point
print("============")
for index in range (5,10):
    print(index)

# Range function with increment/decrement
print("==========")
for index in range (10,110,10):
    print(index)

# Summary
# Default - range(starting 0, limit,increment 1)
# Modified - range(start, limit, interval)

# print numbers from 100 to 60 with an interval of 10
print("===========")
for numbers in range (100,60,-10):
    print(numbers)
