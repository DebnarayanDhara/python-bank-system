Welcomesc = "Welcome To Python Bank"
print(Welcomesc.center(50, "-"))

accounts = {
    "547288": {"name": "Dwijendranath Dhara", "password": "dwi1948", "balance": 445872},
    "547229": {"name": "Vaskar Das", "password": "va@kar", "balance": 260000},
    "547230": {"name": "Goutam Dhara", "password": "goutam.gd", "balance": 530000},
    "547231": {"name": "Debnarayan Dhara", "password": "deb@2011", "balance": 1200000},
    "58487": {"name": "Tuhin Manna", "password": "tuhin@5768", "balance": 230000},
    "58488": {"name": "Uttam Dhara", "password": "uttam1", "balance": 330000}
}

acc_number = input("\nEnter Your Account Number: ")

if acc_number in accounts:
    password = input("Enter Your Account Password: ")
    
    if password == accounts[acc_number]["password"]:
        print(f"\nLogin Successful, {accounts[acc_number]['name']}\n")
        
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")

        choice = input("\nEnter Your Choice (1/2/3): ")

        if choice == "1":
            print("\nYour Bank Balance is:", accounts[acc_number]["balance"], "\n")

        elif choice == "2":
            try:
                amount = int(input("\nEnter Amount to Deposit: "))
            except ValueError:
                print("Invalid Input! Please enter a number.")
            else:
                if amount > 0:
                    accounts[acc_number]["balance"] += amount
                    print("Deposit Successful!")
                    print("Money Remaining:", accounts[acc_number]["balance"])
                else:
                    print("Invalid Amount!")

        elif choice == "3":
            amount = int(input("\nEnter Amount to Withdraw: "))
            
            if amount > 0:
                if amount <= accounts[acc_number]["balance"]:
                    accounts[acc_number]["balance"] -= amount
                    print("Withdrawal Successful!")
                    print("Money Remaining:", accounts[acc_number]["balance"])
                    
                    if accounts[acc_number]["balance"] == 0:
                        print("⚠ Account Empty!")
                else:
                    print("Insufficient Balance")
            else:
                print("Invalid Amount ❌")

        else:
            print("Invalid Option")

    else:
        print("Wrong Password")

else:
    print("Account Not Found")

print("\nThank You For Banking With Us!\n")