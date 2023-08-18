# Electricity Bill Calculator
print("===Welcome to Kenya Power===")
units=int(input("Enter The Number of Units: "))

if units<= 100:
    print("No Charges")

elif units >= 100 and units <= 200:
    price=(units)*5
    print(price)
elif units > 200:
    price=(units)*10
    print(price)