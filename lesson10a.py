# Error/Exception Handling - handling errors created by the user to avoid systems from crushing
# We use try, except block
# Try - houses a code that might generate an error from the user
# Except/Catch - the error is handled before the system crashes

# while True:
#     try:
#         number = int(input("Enter a digit: "))
#         print(f"You have entered {number} ")

#     except:
#         print("Please enter a valid input...")

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

division = num1 / num2
print(division)
