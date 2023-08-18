# Write a program to check whether a year is leap or not
# Should be divisible by 4
# Not divisible by 100 (2016,2020)
# Divisible by 400 (2000)

year = int(input("Enter the Year"))
if year % 4 == 0:
    if year % 100 != 0:
        print("Leap Year")

    else:
        if year % 400 == 0:
            print("Leap Year...")
        else:
            print("Not a Leap Year")
else:
     print("Not a Leap Year")

# Other Methods
if year % 4 == 0 and year % 100 != 0:
    print("Leap Year")

else:
    if year % 400 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
    
    
