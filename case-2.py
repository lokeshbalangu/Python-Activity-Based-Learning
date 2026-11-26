balance = float(input())
n = int(input())

if balance < 0 or n < 0:
    print("Invalid details")
else:
    for i in range(n):
        choice = input().upper()
        amount = float(input())

        if amount <= 0:
            print("Invalid amount")

        elif choice == "D":
            balance += amount
            print("Deposit successful")

        elif choice == "W":
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful")
            else:
                print("Not enough balance")

        else:
            print("Invalid choice")

    print("Final balance:", round(balance, 2))