# Triangle

side1= int(input("Enter the 1st side in centimetres:  "))
side2= int(input("Enter the 2nd side in centimetres:  "))
side3= int(input("Enter the 3rd side in centimetres:  "))

# For an Equilateral triangle - all sides are equal
if side1 == side2 and side2 == side3:
    print("Equilateral")

# For an Isoceles triangle - 2 sides should be equal
elif (side1 == side2 and side2 != side3) or (side2 == side3 and side3 != side1 )or (side3 == side1 and side1!= side2):
    print("Isoceles")

# For a Scalene triangle - no side is equal to the other
elif(side1 != side2) and (side2 != side3) and (side3 != side1):
    print("Scalene")

else:
    print("Invalid Inputs")