# Simple Login System

user={
    "username":"user123",
    "password": "12345",
    "timeline1":{
        "username":"BigBuzz",
        "posted":"Live in Monaco"
    },
    "timeline2":{
        "username": "Coders",
        "posted":"Working on my project"
    } 
}

# User Authentication
username=input("Enter Your Username: ")
password=input("Enter Your Password: ")
if username != user["username"] or password== user["password"]:
    print("=====Welcome To Facebook======")
    print(user["timeline1"])
    print("==========")
    print(user["timeline2"])

else:
    print("=====Access Denied=====")
    print("=====Try Again=====")

# Task 1 - Attack(Hack) the system to grant access with only your username (or) password..
# Task 2 - Grant access with wrong credentials for both (!=) if username !=
# Mpesa Application - deposit, withdrawal, check balance, 
