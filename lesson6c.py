# Nested if Conditions
# Money Withdrawal Application

account = {
    "PIN": "1234",
    "name": "Glory",
    "balance": 10000
}

print("===Welcome To ABC Bank===")
pin = input("Enter Your PIN: ")
if pin == account["PIN"]:
    print(f"===Karibu {account['name']} ===")
    amount = int(input("Enter Your Amount: "))
    if amount <=account ["balance"]:
        print(f"Confirmed. Withdrawn Ksh {amount}")
        newbalance= account ["balance"] - amount
        print(f"Your Current balance is {newbalance}")

# Insufficient Funds  
    else:
        print("Failed!Insufficient Funds...")
        print(f"Your Balance is {account['balance']} ")

# Input Wrong PIN
else:
    print("Wrong PIN! Try Again!")

#
