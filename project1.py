# USSD - accessible by short codes eg *544#

# Withdraw Function

customer = {
    "PIN":2023,
    "name":"Elisa Marie",
    "balance":15000,
    "status":"active",
    "phone":"+254712464453"
}

# Withdraw Option   
def withdraw(PIN, amount, agent_no):
    print("=== Welcome ===")
    if PIN == customer ["PIN"]:
        print("=== Access Granted ===")
        if amount <= customer["balance"]:
            print(f"Confirmed. Successfully withdrawn Ksh {amount} from Agent No {agent_no}")
            balance = customer["balance"] - amount
            print(f"Your Balance is {balance}")
            print("Thank You")
        else:
            print("Insufficient Account Balance")
            print("Try Again")
    else:
        print("=== Access Denied ===")
        print("Wrong PIN")

# Deposit Option
def deposit(PIN,amount, agent_no):
    print("=== Deposit === ")
    if customer ["status"] == "active":
        if PIN == customer ["PIN"]:
            print("=== Access Granted ===")
            print("Kindly Wait...")
            current_balance = amount + customer["balance"]
            print(f"Well Received. Thank Your For Depositing At Agent No {agent_no} ")
            print(f"Your Current Balance is {current_balance}")
        else:
            print("=== Access Denied === ")
            print("Wrong PIN!!!")
    else:
        print("=== Sorry! === Please Activate Your Account ===")

# Check Balance Option
def check_balance(PIN):
    if customer["status"] == "active":
        if PIN == customer["PIN"]:
            print(f"Confirmed Your Current Balance is {customer['balance']}")
        else:
            print("=== Access Denied === ")
            print("Wrong PIN")

    else:
        print("=== Sorry! === Please Activate Your Account ===")
    
# Change PIN Option
def check_pin (current, new, confirm):
    if customer["status"] == "active":
        if current == customer["PIN"]:
            if new == confirm:
                customer["PIN"] = new
                print("PIN Updated Successfully")
                print(f"Your New PIN is {customer['PIN']}")

            else:
                print("Failed to update PIN")

        else:
            print("Wrong PIN")

    else:
        print("Please Activate Your Account!")

           




# Menu
while True:
    def menu():
        print("Simple Mpesa USSD App")
        print("===== Welcome =====")
        print("\n")

    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Change PIN")
    print("5. Loans and Savings")
    print("6. Fuliza")
    print("0. Exit")
    print("")

    option = int(input("Enter Your Choice: "))
    if option == 1:
        withdraw( int(input("Enter Your PIN: ")),int(input("Enter The Amount: ")), int(input("Enter Agent No: ")))
    elif option == 2:
         deposit( int(input("Enter Your PIN: ")),int(input("Enter The Amount: ")), int(input("Enter Agent No: ")))
    elif option == 3:
        check_balance(int(input("Enter Your PIN: ")))
    elif option == 4:
        check_pin( int(input("Enter Your Current PIN: ")), int(input("Enter Your New PIN:  ")), int(input("Confirm Your New PIN: ")))
    elif option == 0:
        break 
    else:
        print("Other options under development")
        
menu()
