# Dictionaries - collection{}
# Properties - unordered, no duplicates, mutable(changeable)*use of keys
# Key - value pair

student= ['Joseph',20,'Male',False,['Programming','SQL']]
# With lists data is accessed using indexing
student= {
    "name":"Joseph",
    "age": 34,
    "gender":"Male",
    "present": False,
    "subjects":["Programming","SQL"],
    "scores":{
        "programming":100,
        "SQL": 85
    }
}
print(type(student))

# Dictionary Operations
# 1. Printing dictionary
print(student)

# 2. Accessing items on a dictionary - we use the key to access a value
print(student["gender"])
print(student["subjects"])


# 3. Updating values - we use the key
student["age"]=40
print(student)
student["subjects"][0]="Programming in Python"
print(student)

# 4. Adding new items on a dictionary
student["email"]= "josephm@gmail.com"
print(student)

# 5. Nested Dictionary
# Access the SQL score
print(student ["scores"]["SQL"])

# Methods - its function
print(student.keys())
print(student.values())

student.clear