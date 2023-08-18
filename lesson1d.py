# Create a program to perform Simple Interest taking inputs from the user
# Algorith/Pseudo code - step by step procedure to perform a task

# Get and understand the formula eg (P*R*T/100)
# Principle - amount deposited
# Rate - 
# Time -
 
# Apply the formula
# Output your result

principle=int(input("Enter The Amount Deposited?:"))
rate=int(input("Enter The Rate?:"))
time=int(input("Enter The Time?:"))

interest=(principle * rate * time )/100
print(f"Your interest is{interest}")

# Body Mass Index
# Create a program to calculate BMI
# Given the formula (weight/(height*height))
# Weight - in kg
# Height - in metres
 
weight=int(input("Enter Your Weight:"))
height=float(input("Enter Your Height:"))

bodymassindex=(weight/(height*height))
print(f"Your Body Mass Index is {bodymassindex}")