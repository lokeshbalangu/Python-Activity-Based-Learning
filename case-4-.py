n = int(input("Enter number of transactions: "))

ids = []
amounts = []

for i in range(n):
    transaction_id = input("Enter transaction ID: ")
    amount = float(input("Enter amount: "))
    ids.append(transaction_id)
    amounts.append(amount)

threshold = float(input("Enter suspicious amount threshold: "))

print("\nDuplicate transactions:")

found_duplicate = False

for i in range(n):
    if ids.count(ids[i]) > 1:
        print(ids[i], "Amount:", amounts[i])
        found_duplicate = True

if not found_duplicate:
    print("No duplicate transactions")

print("\nHigh-value transactions:")

found_high = False

for i in range(n):
    if amounts[i] > threshold:
        print(ids[i], "Amount:", amounts[i])
        found_high = True

if not found_high:
    print("No high-value transactions")