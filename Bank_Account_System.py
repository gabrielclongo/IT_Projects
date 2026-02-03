balance = 1000

while True:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Select an option, please: ")

    if choice == "1":
        amount = float(input("Choose the amount you want to deposit, please: "))
        balance += amount
        print(f"New balance: {balance}")
    
    elif choice == "2":
        amount = float(input("Choose the amount you want to withdraw, please: "))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print(f"New balance: {balance}")

    elif choice == "3":
        print("See you another time!")
        break
    else:
        print("Invalid option!")      
        
        
    


