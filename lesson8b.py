# Functions with Parameters/Arguments

def subtract():
    num1 = 50
    num2 = 20
    diff = num1 - num2
    print(diff)

# subtract()
# subtract()
# subtract()

# Parameters - variables that are passed when creating a function
# Arguments - values passed while calling a function

def multiply(num1, num2):
    product = num1 * num2
    print(product)
# multiply(5,6)
# multiply(7,8)
multiply(int(input("Enter the 1st value"))), int(input("Enter the 2nd value"))

def greet(name):
    print(f"Hello {name} !")
greet("Martin")
