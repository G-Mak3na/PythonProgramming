# For Loop in a Sequence (Collection)
# Collection - string, list, tuples, dictionaries

# String
language="Python"
for letter in language:
    print(letter)

print("===========")

# List Sequence
programminglanguages= ["Python", "C", "Java", "JavaScript", "C#"]
for language in programminglanguages:
    if language == "Java":
        print("Java exists")
        
# Assumption
# 1. Create a list of 8 counties in Kenya
# 2. Create 2 empty lists namely; single and double

# Task
# Iterate through the list of 8 counties checking whether it has either single name or double name. If it has a single name append to single empty list  otherwise append to the double empty list


counties= ["Nairobi","Taita Taveta","Garissa","Nakuru","Uasin Gishu","Homa Bay","Murang'a","Kakamega"]

single = []
double =[]

for county in counties:
    if " " in county:
        double.append(county)

    else:
        single.append(county)

        print(single)
        print(double)