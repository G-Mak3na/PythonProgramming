# Functions - a block of code that performs a specific task on the system that only executes it when it's called (referenced)
# Mpesa USSD Appliations - Send Money, Deposit, Withdraw, Check Balance, Change PIN

# Types of Functions
# Inbuilt - already existing on the project eg print(), input(), range()
# User-specific (Defined) - created by a developer then called when needed eg Send_SMS(), Encrypt(), Mpesa()

# Defining a function
# def function_name():
#     code block

def greet():
    print("Hello! Welcome to Functions!")
# Calling a function
# function_name(): - exit the function and call

# greet()

def add():
    number1 = int(input("Enter the 1st number: "))
    number2 = int(input("Enter the 2nd number: "))
    sum = number1 + number2
    print(sum)
# add()

# Create a function to perform simple interest and call the function
def simple_interest():
    principal = int(input("Enter the amounnt: "))
    rate = int(input("Enter the rate: "))
    time = int(input("Enter the duration: "))
    interest = (principal*rate*time) / 100
    print(f" Your Interest Is.... ")
simple_interest()

