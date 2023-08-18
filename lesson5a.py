# Control Flow - a way to control program execution
# 3 categories
# 1. Sequential Control Flow - default codes executed line by line (no indentation)
# 2. Conditional Control Flow - codes are executed based on some conditions
# 3. Iterative Control Flow - codes are executed a number of times based on some conditions

# Conditional Control Flow - codes are executed based on some conditions
# We have 4 conditions - if, if else, if else if (elif), nested if

# if(condition/expression)- checked return boolean(True,False).
# For statements - code that is executed when condition is either true or false
age=20
if age >18:
    print("ISSUED WITH AN ID")

else:
    print("Please Try Next Time!")
#if else - one condition is checked. The condition returns true if statement is executed otherwise else statement is executed

# By requesting the number from the user first,apply the idea of modulus(%) and conditions write a program to test whether a number is even or odd 
number=int(input("Enter The Number Here: "))
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
